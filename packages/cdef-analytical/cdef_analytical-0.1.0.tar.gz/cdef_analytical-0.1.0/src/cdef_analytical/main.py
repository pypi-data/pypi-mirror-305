from pathlib import Path

import polars as pl

from cdef_analytical.enums import DataCategories
from cdef_analytical.loaders.data_loader import AnalyticalDataLoader


def print_data_summary(df: pl.LazyFrame, name: str) -> None:
    """Print summary information about a DataFrame."""
    print(f"\n{name} Summary:")
    print("-" * 50)
    print(f"Schema: {df.collect_schema()}")
    try:
        count = df.select(pl.len()).collect().item()
        print(f"Number of records: {count:,}")
        if "year" in df.collect_schema():
            # Modified to handle multiple years
            years = (
                df.select(pl.col("year").unique().sort())
                .collect()
                .to_series()
                .to_list()
            )
            print(f"Years covered: {years}")
    except Exception as e:
        print(f"Error getting summary: {e}")


# Initialize loader
analytical_data_dir = Path("/Users/tobiaskragholm/dev/backup_data/data/analytical_data")
loader = AnalyticalDataLoader(analytical_data_dir)

# Print available data summary
loader.list_available_data()

try:
    # Load static data
    static_data = loader.get_static_data()

    # Filter using enum values
    children_data = static_data.filter(
        pl.col("role") == DataCategories.ROLE_CHILD.value
    )

    # Get diagnosis groups
    diagnosis_data = loader.get_diagnosis_groups(years=[2015, 2016, 2017])

    # You can use the enum methods to get lists of categories
    diagnosis_columns = [
        f"num_{group}_diagnoses" for group in DataCategories.diagnosis_groups()
    ]

    # Calculate statistics using standardized category names
    yearly_stats = (
        diagnosis_data.group_by("year")
        .agg(
            [
                pl.sum(f"num_{group}_diagnoses").alias(group)
                for group in DataCategories.diagnosis_groups()
            ]
        )
        .sort("year")
        .collect()
    )

except Exception as e:
    print(f"Error: {e}")

try:
    # Load static data
    static_data = loader.get_static_data()
    print_data_summary(static_data, "Static Data")
    # Get unique values in the 'role' column
    role_categories = (
        static_data.select(pl.col("role").unique().sort())
        .collect()
        .to_series()
        .to_list()
    )

    # Convert to categorical and get value counts
    role_distribution = (
        static_data.select(pl.col("role").cast(pl.Categorical))
        .group_by("role")
        .len()
        .sort("len", descending=True)
        .collect()
    )

    print("\nRole Categories:", role_categories)
    print("\nRole Distribution:")
    print(role_distribution)

    # Load diagnosis groups data
    diagnosis_data = loader.get_diagnosis_groups(years=[2015, 2016, 2017])

    # Get unique years
    years = (
        diagnosis_data.select(pl.col("year").unique().sort())
        .collect()
        .to_series()
        .to_list()
    )

    # Get diagnosis columns (excluding admissions)
    diagnosis_columns = [
        col
        for col in diagnosis_data.collect_schema().keys()
        if col.startswith("num_") and col.endswith("_diagnoses")
    ]

    # Calculate summary statistics per year
    yearly_stats = (
        diagnosis_data.group_by("year")
        .agg(
            [
                pl.sum(col).alias(col.replace("num_", "").replace("_diagnoses", ""))
                for col in diagnosis_columns
            ]
        )
        .sort("year")
        .collect()
    )

    print("\nYears covered:", years)
    print("\nDiagnosis Categories:")
    for col in diagnosis_columns:
        category = col.replace("num_", "").replace("_diagnoses", "")
        print(f"- {category}")

    print("\nYearly Statistics:")
    print(yearly_stats)

    # Combine data
    combined_data = static_data.filter(
        pl.col("role") == "child"
    ).join(  # Only include children
        diagnosis_data, on="individual_id", how="left"
    )

    print_data_summary(combined_data, "Combined Data")

    # Show some statistics
    stats = (
        combined_data.group_by("year")
        .agg(
            [
                pl.count("individual_id").alias("total_individuals"),
                pl.col("^num.*_diagnoses$").sum().name.map(lambda x: f"total_{x}"),
            ]
        )
        .sort("year")
        .collect()
    )

    print("\nYearly Statistics:")
    print(stats)

except Exception as e:
    print(f"Error: {e}")

# Working with the data
try:
    # Get static data
    static_data = loader.get_static_data()

    # Get health data for specific years
    health_data = loader.get_health_data(years=[2015, 2016, 2017])

    # Combine data
    combined_data = static_data.join(health_data, on="individual_id")

    # Show schema
    print("\nCombined data schema:")
    print(combined_data.collect_schema())

except Exception as e:
    print(f"Error working with data: {e}")


# Load all health data
health_data = loader.get_health_data()

# Load specific health source
# lpr3_data = loader.get_health_data(source="lpr3")

# Check available health sources
sources = loader.get_health_sources()
print("Available health sources:", sources)

# Load yearly data (if available)
try:
    yearly_data = loader.get_health_data(years=[2015, 2016, 2017])
except Exception:
    print("Note: Health data does not have yearly partitioning")
    yearly_data = loader.get_health_data()
