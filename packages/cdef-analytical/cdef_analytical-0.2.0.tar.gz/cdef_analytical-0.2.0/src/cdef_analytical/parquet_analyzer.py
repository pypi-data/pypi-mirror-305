import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import polars as pl

from cdef_analytical.logging_config import ServiceLogger, create_logger

# Create logger instance
logger = create_logger("parquet_analyzer")


class ParquetAnalyzer:
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.file_summaries: list[Dict[str, Any]] = []
        self.logger: ServiceLogger = logger

    def _aggregate_directory_summaries(
        self, directory_structure: Dict[str, List[Dict[str, Any]]]
    ) -> Dict[str, Dict[str, Any]]:
        """Create aggregated summaries for similar directory structures."""
        # Group directories by their schema structure
        schema_groups: Dict[str, List[str]] = {}

        for dir_path, summaries in directory_structure.items():
            # Skip empty directories or summaries with errors
            if not summaries or "columns" not in summaries[0]:
                continue

            # Create a schema fingerprint as a string instead of tuple
            schema_key = json.dumps(
                [
                    (col["name"], col["dtype"])
                    for col in sorted(summaries[0]["columns"], key=lambda x: x["name"])
                ],
                sort_keys=True,
            )

            if schema_key not in schema_groups:
                schema_groups[schema_key] = []
            schema_groups[schema_key].append(dir_path)

        # Create aggregated summaries
        aggregated_summaries: Dict[str, Dict[str, Any]] = {}
        for schema_key, dirs in schema_groups.items():
            # Collect all valid summaries for these directories
            all_summaries = [
                summary
                for dir_path in dirs
                for summary in directory_structure[dir_path]
                if "columns" in summary
            ]

            if not all_summaries:
                continue

            # Get column names from first summary
            column_names = [col["name"] for col in all_summaries[0]["columns"]]

            # Create common schema by matching columns by name
            common_schema = []
            for col_name in column_names:
                # Find this column in all summaries
                col_stats = {
                    "name": col_name,
                    "dtype": next(
                        col["dtype"]
                        for summary in all_summaries
                        for col in summary["columns"]
                        if col["name"] == col_name
                    ),
                }

                # Collect unique counts if available
                unique_counts = [
                    col["unique_count"]
                    for summary in all_summaries
                    for col in summary["columns"]
                    if col["name"] == col_name and "unique_count" in col
                ]
                if unique_counts:
                    col_stats["unique_values_range"] = (
                        min(unique_counts),
                        max(unique_counts),
                    )

                # Collect null counts
                null_counts = [
                    col["null_count"]
                    for summary in all_summaries
                    for col in summary["columns"]
                    if col["name"] == col_name and "null_count" in col
                ]
                if null_counts:
                    col_stats["null_count_range"] = (min(null_counts), max(null_counts))

                common_schema.append(col_stats)

            # Create summary
            try:
                aggregated_summaries[schema_key] = {
                    "directories": sorted(dirs),
                    "file_count": len(all_summaries),
                    "size_range": (
                        min(
                            s["file_size_mb"]
                            for s in all_summaries
                            if "file_size_mb" in s
                        ),
                        max(
                            s["file_size_mb"]
                            for s in all_summaries
                            if "file_size_mb" in s
                        ),
                    ),
                    "row_count_range": (
                        min(s["row_count"] for s in all_summaries if "row_count" in s),
                        max(s["row_count"] for s in all_summaries if "row_count" in s),
                    ),
                    "common_schema": common_schema,
                    "partition_keys": sorted(
                        set(
                            key
                            for s in all_summaries
                            if "partitions" in s
                            for key in s["partitions"].keys()
                        )
                    ),
                }
            except Exception as e:
                self.logger.error(f"Error creating summary for schema pattern: {e}")
                continue

        return aggregated_summaries

    def _get_directory_structure(self) -> Dict[str, List[Dict[str, Any]]]:
        """Organize file summaries by directory structure."""
        directory_structure: Dict[str, List[Dict[str, Any]]] = {}

        for summary in self.file_summaries:
            file_path = Path(summary["file_path"])
            dir_path = str(file_path.parent)

            if dir_path not in directory_structure:
                directory_structure[dir_path] = []

            directory_structure[dir_path].append(summary)

        return directory_structure

    def _analyze_directory(self, summaries: List[Dict[str, Any]]) -> str:
        """Analyze a group of files in a directory."""
        total_size = sum(
            summary["file_size_mb"]
            for summary in summaries
            if "file_size_mb" in summary
        )
        total_rows = sum(
            summary["row_count"] for summary in summaries if "row_count" in summary
        )

        # Collect all column names across files
        column_sets = {
            tuple(sorted(col["name"] for col in summary["columns"]))
            for summary in summaries
            if "columns" in summary
        }

        # Analyze schema consistency
        schema_consistent = len(column_sets) == 1
        if schema_consistent:
            columns = list(next(iter(column_sets)))
        else:
            columns = sorted(set.union(*[set(cols) for cols in column_sets]))

        # Partition analysis
        partition_keys = set()
        for summary in summaries:
            if "partitions" in summary:
                partition_keys.update(summary["partitions"].keys())

        analysis = [
            f"Files in directory: {len(summaries)}",
            f"Total size: {self._format_float(total_size)} MB",
            f"Total rows: {total_rows:,}",
            f"Schema consistent across files: {'Yes' if schema_consistent else 'No'}",
            f"Number of columns: {len(columns)}",
        ]

        if partition_keys:
            analysis.append(f"Partition keys: {', '.join(sorted(partition_keys))}")

        return "\n".join(analysis)

    def _format_float(self, value: Optional[float], precision: int = 2) -> str:
        """Safely format a float value with given precision."""
        if value is None:
            return "N/A"
        return f"{value:.{precision}f}"

    def _format_numeric_stats(self, stats: Dict[str, Optional[float]]) -> List[str]:
        """Format numeric statistics into readable strings."""
        formatted = []
        if "mean" in stats:
            formatted.append(f"- Mean: {self._format_float(stats['mean'])}")
        if "median" in stats:
            formatted.append(f"- Median: {self._format_float(stats['median'])}")
        if "std" in stats:
            formatted.append(f"- Std Dev: {self._format_float(stats['std'])}")
        if "min" in stats:
            formatted.append(f"- Min: {self._format_float(stats['min'])}")
        if "max" in stats:
            formatted.append(f"- Max: {self._format_float(stats['max'])}")
        return formatted

    def _safe_float_cast(self, value: Any) -> Optional[float]:
        """Safely cast a value to float, returning None if not possible."""
        if value is None:
            return None
        try:
            return float(value)
        except (ValueError, TypeError):
            return None

    def _safe_n_unique(self, series: pl.Series) -> int:
        """Safely compute number of unique values for a series."""
        try:
            return series.n_unique()
        except Exception as e:
            self.logger.debug(
                f"Could not compute unique count for {series.name}: {str(e)}"
            )
            return -1  # or another sentinel value

    def _safe_numeric_stats(self, series: pl.Series) -> Dict[str, Optional[float]]:
        """Safely compute numeric statistics for a series."""
        try:
            if series.dtype in [pl.Int64, pl.Float64]:
                return {
                    "min": self._safe_float_cast(series.min()),
                    "max": self._safe_float_cast(series.max()),
                    "mean": self._safe_float_cast(series.mean()),
                    "median": self._safe_float_cast(series.median()),
                    "std": self._safe_float_cast(series.std()),
                }
            return {}
        except Exception as e:
            self.logger.debug(
                f"Could not compute numeric stats for {series.name}: {str(e)}"
            )
            return {}

    def _get_column_type_summary(self, series: pl.Series) -> str:
        """Get a human-readable summary of the column type."""
        dtype = series.dtype
        if isinstance(dtype, pl.List):
            return f"list[{dtype.inner}]"
        return str(dtype)

    def _extract_partition_info(self, file_path: Path) -> Dict[str, str]:
        """Extract Hive partition information from file path."""
        partition_info = {}

        # Get relative path from root directory
        rel_path = file_path.relative_to(self.root_dir)
        path_parts = rel_path.parts

        # Look for key=value pairs in path
        for part in path_parts:
            if "=" in part:
                key, value = part.split("=", 1)
                partition_info[key] = value

        return partition_info

    def analyze_parquet_file(self, file_path: Path) -> Dict[str, Any]:
        """Analyze a single parquet file and return its metadata."""
        try:
            self.logger.info(f"Analyzing file: {file_path}")

            # Extract partition information
            partition_info = self._extract_partition_info(file_path)

            # Read just the metadata first
            df = pl.scan_parquet(file_path)
            schema = df.collect_schema()

            # Get file stats
            file_stat = file_path.stat()
            file_size = file_stat.st_size
            modified_time = datetime.fromtimestamp(file_stat.st_mtime)

            # Get basic dataframe info
            df_computed = df.collect()
            row_count = len(df_computed)
            column_count = len(df_computed.columns)

            # Get column details
            column_info = []
            for col_name, dtype in schema.items():
                if col_name in partition_info:
                    continue

                series = df_computed[col_name]

                # Basic stats that work for all types
                stats: Dict[str, Any] = {
                    "name": col_name,
                    "dtype": self._get_column_type_summary(series),
                    "null_count": series.null_count(),
                }

                # Type-specific statistics
                if dtype in [pl.Int64, pl.Float64]:
                    numeric_stats = self._safe_numeric_stats(series)
                    stats.update(numeric_stats)
                elif dtype == pl.Utf8:
                    # For string columns, just count uniques if possible
                    unique_count = self._safe_n_unique(series)
                    if unique_count >= 0:
                        stats["unique_count"] = unique_count
                elif isinstance(dtype, pl.List):
                    # For list columns, provide list-specific information
                    stats["inner_type"] = str(dtype.inner)
                    # Can add more list-specific analysis here
                else:
                    # For other types, try unique count but don't fail if not possible
                    unique_count = self._safe_n_unique(series)
                    if unique_count >= 0:
                        stats["unique_count"] = unique_count

                column_info.append(stats)

            summary = {
                "file_path": str(file_path.relative_to(self.root_dir)),
                "partitions": partition_info,
                "file_size_mb": file_size / (1024 * 1024),
                "last_modified": modified_time.isoformat(),
                "row_count": row_count,
                "column_count": column_count,
                "columns": column_info,
            }

            self.logger.debug(f"File analysis complete: {summary}")
            return summary

        except Exception as e:
            self.logger.error(f"Error analyzing file {file_path}: {str(e)}")
            return {
                "file_path": str(file_path.relative_to(self.root_dir)),
                "error": str(e),
            }

    def analyze_partition_structure(self) -> str:
        """Analyze the Hive partition structure of the dataset."""
        partition_analysis = []
        partition_keys = set()
        partition_values: Dict[str, set] = {}

        # Collect all partition information
        for summary in self.file_summaries:
            if "partitions" in summary:
                partitions = summary["partitions"]
                partition_keys.update(partitions.keys())

                for key, value in partitions.items():
                    if key not in partition_values:
                        partition_values[key] = set()
                    partition_values[key].add(value)

        if not partition_keys:
            return "No Hive partitions found"

        # Generate partition analysis report
        partition_analysis.append("\nHive Partition Analysis:")
        partition_analysis.append(f"Number of partition keys: {len(partition_keys)}")

        for key in sorted(partition_keys):
            values = partition_values[key]
            partition_analysis.append(f"\nPartition key: {key}")
            partition_analysis.append(f"- Unique values: {len(values)}")
            partition_analysis.append(f"- Values: {', '.join(sorted(values))}")

        return "\n".join(partition_analysis)

    def scan_directory(self) -> None:
        """Recursively scan directory for parquet files and analyze them."""
        self.logger.info(f"Scanning directory: {self.root_dir}")
        for file_path in self.root_dir.rglob("*.parquet"):
            summary = self.analyze_parquet_file(file_path)
            self.file_summaries.append(summary)
        self.logger.info(f"Scan complete. Found {len(self.file_summaries)} files.")

    def analyze_file_size_distribution(self) -> str:
        """Analyze the distribution of file sizes."""
        self.logger.info("Analyzing file size distribution")
        sizes = [
            summary["file_size_mb"]
            for summary in self.file_summaries
            if "file_size_mb" in summary
        ]

        if not sizes:
            return "No valid file sizes found"

        df = pl.DataFrame({"file_sizes_mb": sizes})

        # Safely get statistics
        stats = {
            "min_size": self._safe_float_cast(df["file_sizes_mb"].min()),
            "max_size": self._safe_float_cast(df["file_sizes_mb"].max()),
            "mean_size": self._safe_float_cast(df["file_sizes_mb"].mean()),
            "median_size": self._safe_float_cast(df["file_sizes_mb"].median()),
            "total_size": self._safe_float_cast(df["file_sizes_mb"].sum()),
            "q25": self._safe_float_cast(df["file_sizes_mb"].quantile(0.25)),
            "q75": self._safe_float_cast(df["file_sizes_mb"].quantile(0.75)),
        }

        return f"""
    File Size Distribution (MB):
    - Minimum: {self._format_float(stats['min_size'])}
    - 25th percentile: {self._format_float(stats['q25'])}
    - Median: {self._format_float(stats['median_size'])}
    - 75th percentile: {self._format_float(stats['q75'])}
    - Maximum: {self._format_float(stats['max_size'])}
    - Mean: {self._format_float(stats['mean_size'])}
    - Total: {self._format_float(stats['total_size'])}
            """

    def analyze_schema_compatibility(self) -> str:
        """Analyze schema compatibility across files."""
        schema_registry: dict[str, dict[str, set[str]]] = {}

        for summary in self.file_summaries:
            if "columns" not in summary:
                continue

            file_path = summary["file_path"]

            for col in summary["columns"]:
                col_name = col["name"]
                col_type = col["dtype"]

                if col_name not in schema_registry:
                    schema_registry[col_name] = {"types": set(), "files": set()}

                schema_registry[col_name]["types"].add(col_type)
                schema_registry[col_name]["files"].add(file_path)

        # Analyze inconsistencies
        report = []
        report.append("\nSchema Compatibility Analysis:")

        for col_name, info in schema_registry.items():
            if len(info["types"]) > 1:
                report.append(f"\nColumn '{col_name}' has inconsistent types:")
                report.append(f"- Found types: {', '.join(info['types'])}")
                report.append(f"- Appears in {len(info['files'])} files")

        # Find columns that don't appear in all files
        total_files = len(self.file_summaries)
        partial_columns = {
            col: info
            for col, info in schema_registry.items()
            if len(info["files"]) < total_files
        }

        if partial_columns:
            report.append("\nPartially Present Columns:")
            for col, info in partial_columns.items():
                report.append(
                    f"- '{col}' appears in {len(info['files'])} out of {total_files} files"
                )

        return "\n".join(report)

    def analyze_time_series(self) -> str:
        """Analyze temporal aspects of the data if timestamp columns exist."""
        time_analysis = []

        for summary in self.file_summaries:
            if "columns" not in summary:
                continue

            # Look for timestamp/datetime columns
            timestamp_cols = [
                col
                for col in summary["columns"]
                if "datetime" in col["dtype"].lower()
                or "timestamp" in col["dtype"].lower()
            ]

            if timestamp_cols:
                time_analysis.append(f"\nFile: {summary['file_path']}")

                for col in timestamp_cols:
                    df = pl.scan_parquet(
                        os.path.join(self.root_dir, summary["file_path"])
                    )
                    time_stats = df.select(
                        [
                            pl.col(col["name"]).min().alias("min_time"),
                            pl.col(col["name"]).max().alias("max_time"),
                        ]
                    ).collect()

                    time_analysis.append(f"Column: {col['name']}")
                    time_analysis.append(
                        f"- Time range: {time_stats['min_time'][0]} to {time_stats['max_time'][0]}"
                    )

        return "\n".join(time_analysis)

    def analyze_column_distribution(self, max_unique_values: int = 20) -> str:
        """Analyze value distribution for columns."""
        distribution_analysis = []

        for summary in self.file_summaries:
            if "columns" not in summary:
                continue

            file_path = summary["file_path"]
            distribution_analysis.append(f"\nFile: {file_path}")

            df = pl.scan_parquet(os.path.join(self.root_dir, summary["file_path"]))

            for col in summary["columns"]:
                col_name = col["name"]
                col_type = col["dtype"]

                # Skip list columns and handle different types appropriately
                if "list" in col_type.lower():
                    distribution_analysis.append(
                        f"\nColumn: {col_name} (List type - distribution analysis skipped)"
                    )
                    continue

                distribution_analysis.append(f"\nColumn: {col_name}")
                distribution_analysis.append(f"Type: {col_type}")

                try:
                    if (
                        "unique_count" in col
                        and col["unique_count"] <= max_unique_values
                    ):
                        # For columns with few unique values, show value counts
                        value_counts = (
                            df.select(pl.col(col_name))
                            .group_by(col_name)
                            .count()
                            .sort("count", descending=True)
                            .collect()
                        )

                        distribution_analysis.append("Value distribution:")
                        for row in value_counts.iter_rows():
                            value, count = row
                            distribution_analysis.append(
                                f"- {value if value is not None else 'NULL'}: {count}"
                            )

                    # For numeric columns with statistics
                    numeric_stats = {}
                    for stat in ["mean", "median", "std", "min", "max"]:
                        if stat in col:
                            numeric_stats[stat] = col[stat]

                    if numeric_stats:
                        distribution_analysis.append("Statistical summary:")
                        distribution_analysis.extend(
                            self._format_numeric_stats(numeric_stats)
                        )

                except Exception as e:
                    self.logger.error(
                        f"Error analyzing distribution for column {col_name}: {str(e)}"
                    )
                    distribution_analysis.append(f"Analysis failed: {str(e)}")

        return "\n".join(distribution_analysis)

    def generate_comprehensive_report(self) -> str:
        """Generate a comprehensive report with aggregated summaries."""
        try:
            directory_structure = self._get_directory_structure()
            aggregated_summaries = self._aggregate_directory_summaries(
                directory_structure
            )

            if not aggregated_summaries:
                return "No valid data patterns found to analyze"

            report_sections = [
                "=== Comprehensive Parquet Files Analysis Report ===\n",
                f"Analysis Date: {datetime.now().isoformat()}",
                f"Root Directory: {self.root_dir}",
                f"Total Files Analyzed: {len(self.file_summaries)}",
                f"Total Directories: {len(directory_structure)}",
                f"Distinct Schema Patterns: {len(aggregated_summaries)}",
                "\n=== Data Organization Summary ===",
            ]

            # Add aggregated summaries
            for i, (schema_key, summary) in enumerate(aggregated_summaries.items(), 1):
                report_sections.extend(
                    [
                        f"\nSchema Pattern {i}:",
                        "-" * 50,
                        f"Found in {len(summary['directories'])} directories:",
                        *[f"  - {d}" for d in summary["directories"]],
                        "\nCommon Characteristics:",
                        f"  Files per directory: {summary['file_count'] // len(summary['directories'])}",
                        f"  Size range: {self._format_float(summary['size_range'][0])} - {self._format_float(summary['size_range'][1])} MB",
                        f"  Row count range: {summary['row_count_range'][0]:,} - {summary['row_count_range'][1]:,}",
                        f"  Partition keys: {', '.join(summary['partition_keys'])}",
                        "\nSchema:",
                    ]
                )

                # Add column details
                for col in summary["common_schema"]:
                    col_info = [f"  * {col['name']} ({col['dtype']})"]

                    if "unique_values_range" in col:
                        min_unique, max_unique = col["unique_values_range"]
                        if min_unique == max_unique:
                            col_info.append(f"    Unique values: {min_unique}")
                        else:
                            col_info.append(
                                f"    Unique values range: {min_unique:,} - {max_unique:,}"
                            )

                    if "null_count_range" in col:
                        min_null, max_null = col["null_count_range"]
                        if min_null == max_null:
                            col_info.append(f"    Null count: {min_null}")
                        else:
                            col_info.append(
                                f"    Null count range: {min_null:,} - {max_null:,}"
                            )

                    report_sections.extend(col_info)

            # Add aggregate statistics
            report_sections.extend(
                [
                    "\n=== Aggregate Statistics ===",
                    self.analyze_file_size_distribution(),
                    "\n=== Schema Compatibility ===",
                    self.analyze_schema_compatibility(),
                    "\n=== Time Series Analysis ===",
                    self.analyze_time_series(),
                ]
            )

            return "\n".join(
                section for section in report_sections if section is not None
            )

        except Exception as e:
            self.logger.error(f"Error generating comprehensive report: {str(e)}")
            return f"Error generating report: {str(e)}"

    def save_report(self, output_file: str) -> None:
        """Save the comprehensive analysis report to a file."""
        self.logger.info(f"Saving report to {output_file}")
        try:
            report = self.generate_comprehensive_report()
            if not report:
                raise ValueError("Generated report is empty")

            output_path = Path(output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_file, "w") as f:
                f.write(report)
            self.logger.info("Report saved successfully")
        except Exception as e:
            self.logger.error(f"Error saving report: {str(e)}")
            raise

    def save_json(self, output_file: str) -> None:
        """Save the raw analysis data as JSON."""
        self.logger.info(f"Saving JSON data to {output_file}")
        try:
            with open(output_file, "w") as f:
                json.dump(self.file_summaries, f, indent=2)
            self.logger.info("JSON data saved successfully")
        except Exception as e:
            self.logger.error(f"Error saving JSON data: {str(e)}")


# Sample usage
if __name__ == "__main__":
    # Initialize the analyzer with your directory
    analyzer = ParquetAnalyzer("/path/to/your/parquet/files")

    # Scan all parquet files
    print("Scanning parquet files...")
    analyzer.scan_directory()

    # Generate and save comprehensive report
    print("Generating comprehensive report...")
    analyzer.save_report("parquet_analysis_report.txt")

    # Save raw data as JSON
    print("Saving raw data...")
    analyzer.save_json("parquet_analysis_data.json")

    # Print specific analyses if needed
    print("\nFile Size Distribution:")
    print(analyzer.analyze_file_size_distribution())

    print("\nSchema Compatibility:")
    print(analyzer.analyze_schema_compatibility())

    print("\nTime Series Analysis:")
    print(analyzer.analyze_time_series())

    print("\nColumn Distribution Analysis:")
    print(analyzer.analyze_column_distribution(max_unique_values=10))
