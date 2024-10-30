from dataclasses import dataclass
from pathlib import Path
from typing import Any

import polars as pl

from cdef_analytical.enums import DataCategories
from cdef_analytical.logging_config import logger


@dataclass
class DataZone:
    """Container for data zone paths and metadata."""

    path: Path
    description: str


@dataclass
class Domain:
    """Container for domain information."""

    name: str
    description: str
    temporal: bool
    sources: list[str]


class AnalyticalDataLoader:
    """Loader for analytical datasets created by AnalyticalDataService."""

    def __init__(self, base_path: Path):
        """Initialize the loader with the base path of the analytical dataset.

        Args:
            base_path: Path to the root directory of the analytical dataset
        """
        self.base_path = Path(base_path)
        self._zones: dict[str, DataZone] = {}
        self._domains: dict[str, Domain] = {}
        self._metadata: dict[str, Any] = {}

        self._initialize()

    def _initialize(self) -> None:
        """Initialize the loader by reading metadata and validating structure."""
        try:
            # Read metadata
            metadata_path = self.base_path / "metadata.json"
            if not metadata_path.exists():
                raise FileNotFoundError(f"Metadata file not found at {metadata_path}")

            import json

            with open(metadata_path) as f:
                self._metadata = json.load(f)

            # Initialize zones with DataZone objects
            for zone_name, description in self._metadata["structure"].items():
                zone_path = self.base_path / zone_name
                self._zones[zone_name] = DataZone(
                    path=zone_path, description=description
                )

            # Initialize domains with proper Domain objects
            self._domains = {
                name: Domain(
                    name=name,
                    description=desc,
                    temporal=name not in ["static"],
                    sources=self._get_domain_sources(name),
                )
                for name, desc in self._metadata["domains"].items()
            }

            # Validate structure
            self._validate_structure()

            logger.info(f"Initialized analytical data loader for {self.base_path}")
            logger.debug(f"Available zones: {list(self._zones.keys())}")
            logger.debug(f"Available domains: {list(self._domains.keys())}")

        except Exception as e:
            logger.error(f"Error initializing analytical data loader: {str(e)}")
            raise

    def _validate_structure(self) -> None:
        """Validate the data structure exists as expected."""
        for zone_name, zone in self._zones.items():
            if not zone.path.exists():
                logger.warning(f"Zone directory not found: {zone.path}")

        for domain in self._domains.values():
            if domain.temporal:
                domain_path = self.base_path / "longitudinal" / domain.name
                if not domain_path.exists():
                    logger.warning(f"Domain directory not found: {domain_path}")

    def _get_domain_sources(self, domain: str) -> list[str]:
        """Get data sources for a domain from the directory structure."""
        if domain == "static":
            return ["individual_attributes"]
        elif domain == "family":
            return ["family_relationships"]

        # For longitudinal domains, check actual files
        domain_path = self.base_path / "longitudinal" / domain
        if domain_path.exists():
            return [p.stem for p in domain_path.glob("*.parquet")]
        return []

    def get_domain_info(self, domain: str) -> Domain:
        """Get information about a specific domain.

        Args:
            domain: Name of the domain to get information for

        Returns:
            Domain object containing domain information

        Raises:
            ValueError: If the domain doesn't exist
        """
        if domain not in self._domains:
            raise ValueError(
                f"Unknown domain: {domain}. "
                f"Available domains: {list(self._domains.keys())}"
            )
        return self._domains[domain]

    def list_available_data(self) -> None:
        """Print a summary of available data."""
        print("\nAvailable Data Summary:")
        print("=" * 50)

        # Print zones
        print("\nData Zones:")
        for name, zone in self._zones.items():
            print(f"- {name}: {zone.description}")

        # Print domains
        print("\nDomains:")
        for domain in self._domains.values():
            years = self.get_available_years(domain.name) if domain.temporal else []
            sources = ", ".join(domain.sources)
            print(f"\n{domain.name}:")
            print(f"  Description: {domain.description}")
            print(f"  Temporal: {domain.temporal}")
            print(f"  Sources: {sources}")
            if years:
                print(f"  Years available: {years}")
            elif domain.temporal:
                print("  Non-partitioned temporal data")

    def get_health_sources(self) -> list[str]:
        """Get available health data sources."""
        health_path = self._zones["longitudinal"].path / "health" / "longitudinal"

        if not health_path.exists():
            logger.debug(f"Health path not found: {health_path}")
            return []

        # Look for Hive-partitioned directories that end in .parquet
        sources = [
            p.name.replace(".parquet", "")
            for p in health_path.glob("*.parquet")
            if p.is_dir()
        ]

        logger.debug(f"Found health sources: {sources}")
        return sorted(sources)

    def get_static_data(self) -> pl.LazyFrame:
        """Load static individual attributes with role as Enum."""
        try:
            df = self._load_parquet(
                self._zones["static"].path / "individual_attributes.parquet"
            )

            # df = df.with_columns(
            #     pl.col("role")
            #     .cast(
            #         pl.Categorical("physical")
            #     )  # Explicitly specify physical ordering
            #     .alias("role")
            # )

            logger.debug(f"Static data schema: {df.collect_schema()}")
            return df
        except Exception as e:
            logger.error(f"Error loading static data: {str(e)}")
            raise

    def get_family_data(self) -> pl.LazyFrame:
        """Load family relationships data."""
        return self._load_parquet(
            self._zones["family"].path / "family_relationships.parquet"
        )

    def get_family_statistics(self) -> pl.LazyFrame:
        """Load derived family statistics."""
        return self._load_parquet(
            self._zones["derived"].path / "family_statistics.parquet"
        )

    def get_longitudinal_data(
        self, domain: str, years: list[int] | None = None
    ) -> pl.LazyFrame:
        """Load longitudinal data for a specific domain.

        Args:
            domain: Name of the domain (e.g., "demographics", "health")
            years: Optional list of years to filter by. Only applied if data has a year column.
        """
        if domain not in self._domains:
            raise ValueError(f"Unknown domain: {domain}")

        domain_path = self._zones["longitudinal"].path / domain
        if not domain_path.exists():
            raise FileNotFoundError(f"No data found for domain: {domain}")

        # Load and combine all parquet files in the domain directory
        dfs = []
        for file in domain_path.glob("*.parquet"):
            df = self._load_parquet(file)

            # Check if the data has a year column before filtering
            if years and "year" in df.collect_schema():
                df = df.filter(pl.col("year").is_in(years))
            dfs.append(df)

        return pl.concat(dfs) if dfs else pl.LazyFrame()

    def get_health_data(
        self,
        data_type: str = "summary",  # or "diagnosis_groups"
        years: list[int] | None = None,
    ) -> pl.LazyFrame:
        """Load health data of specified type."""
        try:
            health_path = self._zones["longitudinal"].path / "health" / "longitudinal"

            # Correct file naming
            file_name = (
                "health_summary.parquet"
                if data_type == "summary"
                else "diagnosis_groups.parquet"
            )
            partition_dir = health_path / file_name

            logger.debug(f"Loading partitioned health data from: {partition_dir}")

            if not partition_dir.exists():
                available = list(health_path.glob("*.parquet"))
                raise FileNotFoundError(
                    f"Health data directory not found: {partition_dir}\n"
                    f"Available files: {available}"
                )

            # Use scan_parquet with Hive partitioning
            df = pl.scan_parquet(
                partition_dir,
                hive_partitioning=True,
                parallel="auto",
            )

            # Apply year filter if specified
            if years:
                df = df.filter(pl.col("year").is_in(years))

            # Ensure consistent column naming but keep original PNR if it exists
            if "PNR" in df.collect_schema():
                df = df.with_columns(pl.col("PNR").alias("individual_id"))

            logger.debug(f"Loaded health data schema: {df.collect_schema()}")
            return df

        except Exception as e:
            logger.error(f"Error loading health data: {str(e)}")
            raise

    def get_available_years(self, domain: str) -> list[int]:
        """Get available years for a specific domain."""
        try:
            if domain == "health":
                health_path = (
                    self._zones["longitudinal"].path / "health" / "longitudinal"
                )
                years = []

                # Updated file names
                files = {
                    "summary": "health_summary.parquet",
                    "diagnosis_groups": "diagnosis_groups.parquet",
                }

                for data_type, filename in files.items():
                    partition_dir = health_path / filename
                    if partition_dir.exists():
                        years.extend(
                            [
                                int(d.name.split("=")[1])
                                for d in partition_dir.glob("year=*")
                                if d.is_dir()
                            ]
                        )
                return sorted(set(years))

            # For other domains...
            df = self.get_longitudinal_data(domain)
            if "year" in df.collect_schema():
                return sorted(
                    df.select(pl.col("year").unique()).collect().to_series().to_list()
                )
            return []

        except Exception as e:
            logger.warning(f"Could not get years for domain {domain}: {str(e)}")
            return []

    def get_diagnosis_groups(self, years: list[int] | None = None) -> pl.LazyFrame:
        """Load diagnosis groups data with standardized category names."""
        df = self.get_health_data("diagnosis_groups", years)

        # Validate diagnosis group columns
        valid_groups = DataCategories.diagnosis_groups()
        for group in valid_groups:
            expected_col = f"num_{group}_diagnoses"
            if expected_col not in df.collect_schema():
                logger.warning(
                    f"Expected diagnosis group column missing: {expected_col}"
                )

        return df

    def get_health_summary(self, years: list[int] | None = None) -> pl.LazyFrame:
        """Convenience method to load health summary data."""
        return self.get_health_data("summary", years)

    def list_health_files(self) -> dict[str, list[str]]:
        """List available health data files and their structure."""
        health_path = self._zones["longitudinal"].path / "health" / "longitudinal"
        if not health_path.exists():
            return {}

        result = {}
        for data_type in ["summary", "diagnosis_groups"]:
            partition_dir = health_path / f"{data_type}.parquet"
            if partition_dir.exists():
                result[data_type] = [
                    str(d.relative_to(health_path))
                    for d in partition_dir.glob("**/*.parquet")
                ]

        return result

    def _load_parquet(self, path: Path) -> pl.LazyFrame:
        """Helper method to load parquet files with detailed logging."""
        try:
            logger.debug(f"Loading parquet file: {path}")
            df = pl.scan_parquet(path)
            logger.debug(f"Successfully loaded {path}")
            logger.debug(f"Schema: {df.collect_schema()}")
            return df
        except Exception as e:
            logger.error(f"Error loading parquet file {path}: {str(e)}")
            raise

    @property
    def available_zones(self) -> list[str]:
        """Get list of available data zones."""
        return list(self._zones.keys())

    @property
    def available_domains(self) -> list[str]:
        """Get list of available domains."""
        return list(self._domains.keys())

    def get_metadata(self) -> dict[str, Any]:
        """Get the full metadata dictionary."""
        return self._metadata.copy()
