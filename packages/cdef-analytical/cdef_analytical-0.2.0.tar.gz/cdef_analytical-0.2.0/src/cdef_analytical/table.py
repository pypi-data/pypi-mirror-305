from pathlib import Path

import polars as pl
import polars.selectors as cs
from great_tables import loc, style

from cdef_analytical.loaders.data_loader import AnalyticalDataLoader
from cdef_analytical.logging_config import create_logger
from cdef_analytical.utils import detect_and_load_json

# Create logger instance
logger = create_logger("table")

# Enable string cache for categorical operations
pl.enable_string_cache()


def prepare_analytical_data(
    loader: AnalyticalDataLoader,
    year: int | None = None,
    include_education: bool = True,
    include_employment: bool = True,
    include_income: bool = True,
    include_health: bool = True,
) -> dict[str, pl.LazyFrame]:
    """
    Prepare and combine analytical data from various sources.

    Args:
        loader: Instance of AnalyticalDataLoader
        year: Reference year for the data (optional)
        include_education: Whether to include education data
        include_income: Whether to include income data
        include_health: Whether to include health data

    Returns:
        Dictionary containing prepared DataFrames for different roles
    """
    logger.info("Starting analytical data preparation")
    logger.debug(
        f"Parameters: year={year}, include_education={include_education}, include_employment={include_employment}, include_income={include_income}, include_health={include_health}"
    )

    # Get base static data with roles
    logger.debug("Loading static data")
    static_data = loader.get_static_data()

    logger.debug("Loading demographic data")
    demographic_query = loader.get_longitudinal_data("demographics")
    if year is not None:
        logger.debug(f"Filtering demographic data for year {year}")
        demographic_query = demographic_query.filter(pl.col("year") == year)

    demographic_data = demographic_query.select(
        [
            pl.col("PNR").alias("individual_id"),
            pl.col("FOED_DAG").alias("birth_date"),
            pl.col("KOEN").alias("gender"),
            pl.col("FM_MARK").cast(pl.Utf8).alias("parental_marking"),
            pl.col("ANTBOERNF").alias("children_in_family"),
            pl.col("FAMILIE_TYPE").alias("family_type"),
            pl.col("FAMILIE_ID").alias("family_id"),
            pl.col("CIVST").cast(pl.Utf8).alias("martial_status"),
            pl.col("STATSB").cast(pl.Utf8).alias("citizenship"),
        ]
    )

    # Initialize data dictionary
    data_frames = {}

    # Optional data loading based on parameters
    logger.debug("Loading additional data sources")
    additional_data = {}

    if include_education:
        logger.debug("Loading education data")
        education_query = loader.get_longitudinal_data("education")
        if year is not None:
            education_query = education_query.filter(pl.col("year") == year)
        education_data = education_query.select(
            [
                pl.col("PNR").alias("individual_id"),
                pl.col("HFAUDD").alias("education_level"),
            ]
        )
        additional_data["education"] = education_data

    if include_employment:
        logger.debug("Loading employment data")
        employment_query = loader.get_longitudinal_data(domain="employment")
        if year is not None:
            employment_query = employment_query.filter(pl.col("year") == year)
        employment_data = employment_query.select(
            [
                pl.col("PNR").alias("individual_id"),
                pl.col("SOCIO13").alias("socio_classification"),
            ]
        )
        additional_data["employment"] = employment_data

    if include_income:
        logger.debug("Loading income data")
        income_query = loader.get_longitudinal_data("income")
        if year is not None:
            income_query = income_query.filter(pl.col("year") == year)
        income_data = income_query.select(
            [
                pl.col("PNR").alias("individual_id"),
                pl.col("PERINDKIALT_13").alias("personal_income"),
                pl.col("LOENMV_13").alias("salary_income"),
            ]
        )
        additional_data["income"] = income_data

    if include_health:
        logger.debug("Loading health data")
        scd_data = loader.get_scd_status().select(
            ["individual_id", "is_scd", "first_scd_date"]
        )
        additional_data["health"] = scd_data

    # Prepare data for each role
    logger.debug("Preparing data for each role")
    for role in ["child", "maternal", "paternal"]:
        logger.debug(f"Processing role: {role}")
        # Start with static data filtered by role
        role_data = static_data.filter(pl.col("role") == role)

        # Join with demographic data
        combined_data = role_data.join(demographic_data, on="individual_id", how="left")

        # Join with additional data sources
        for data_type, df in additional_data.items():
            logger.debug(f"Joining {data_type} data for role {role}")
            combined_data = combined_data.join(df, on="individual_id", how="left")

        data_frames[role] = combined_data

    logger.info("Analytical data preparation completed")
    return data_frames


def create_detailed_role_distribution(
    loader: AnalyticalDataLoader,
    mappings_dir: Path,
    year: int | None = None,
) -> pl.LazyFrame:
    """Create detailed role distribution with demographic breakdowns."""
    logger.info("Creating detailed role distribution")

    # Prepare all required data
    logger.debug("Preparing analytical data")
    prepared_data = prepare_analytical_data(
        loader=loader,
        year=year,
        include_education=True,
        include_income=True,
        include_health=True,
        include_employment=True,
    )

    # Load mappings
    logger.debug(f"Loading mappings from {mappings_dir}")
    mappings = {
        filename.stem: detect_and_load_json(mappings_dir / f"{filename.stem}.json")
        for filename in mappings_dir.glob("*.json")
    }
    logger.debug(f"Loaded mappings: {list(mappings.keys())}")

    # Apply mappings to the prepared data
    logger.debug("Applying mappings to prepared data")
    for role, data in prepared_data.items():
        logger.debug(f"Processing role: {role}")
        prepared_data[role] = data.with_columns(
            [
                pl.col("gender").cast(pl.Utf8).replace(mappings.get("KOEN", {})),
                pl.col("parental_marking")
                .cast(pl.Utf8)
                .replace(mappings.get("FM_MARK", {})),
                pl.col("martial_status")
                .cast(pl.Utf8)
                .replace(mappings.get("CIVST", {})),
                pl.col("citizenship").cast(pl.Utf8).replace(mappings.get("STATSB", {})),
                pl.col("socio_classification").replace(mappings.get("SOCIO13", {})),
                pl.col("education_level")
                .cast(pl.Utf8)
                .replace(mappings.get("HFAUDD", {})),
                pl.when(pl.col("education_level").is_in(["0", "1", "2"]))
                .then(pl.lit("basic_education"))
                .when(pl.col("education_level").is_in(["3", "4"]))
                .then(pl.lit("upper_secondary"))
                .when(pl.col("education_level").is_in(["5"]))
                .then(pl.lit("short-cycle_tertiary"))
                .when(pl.col("education_level").is_in(["6"]))
                .then(pl.lit("bachelors_equivalent"))
                .when(pl.col("education_level").is_in(["7"]))
                .then(pl.lit("masters_equivalent"))
                .when(pl.col("education_level").is_in(["8"]))
                .then(pl.lit("doctorals_equivalent"))
                .otherwise(pl.lit("Unknown/Not stated"))
                .alias("education_group"),
            ]
        )

    # Combine all role data into a single LazyFrame
    logger.debug("Combining role data into single LazyFrame")
    combined_data = pl.concat(
        [
            df.with_columns(pl.lit(role).alias("role"))
            for role, df in prepared_data.items()
        ]
    ).lazy()

    logger.info("Role distribution creation completed")
    return combined_data


def create_descriptive_table(df):
    logger.info("Creating descriptive table")

    # Define common quartile labels
    quartile_labels = ["Q1", "Q2", "Q3", "Q4"]

    logger.debug("Calculating income quartiles")
    # Calculate income quartiles for mothers and fathers separately
    mother_income = df.filter(pl.col("role") == "mother").with_columns(
        pl.col("salary_income")
        .qcut(quantiles=4, labels=quartile_labels, allow_duplicates=True)
        .alias("mother_income_category")
    )

    father_income = df.filter(pl.col("role") == "father").with_columns(
        pl.col("salary_income")
        .qcut(quantiles=4, labels=quartile_labels, allow_duplicates=True)
        .alias("father_income_category")
    )

    logger.debug("Calculating household income")
    # Calculate household income
    household_income = (
        df.group_by("family_id")
        .agg(pl.col("salary_income").sum().alias("total_household_income"))
        .with_columns(
            pl.col("total_household_income")
            .qcut(quantiles=4, labels=quartile_labels, allow_duplicates=True)
            .alias("household_income_category")
        )
    )

    logger.debug("Joining income categories")
    # Join all income categories back to original dataframe
    df_with_income = (
        df.join(household_income, on="family_id")
        .join(
            mother_income.select(["individual_id", "mother_income_category"]),
            on="individual_id",
            how="left",
        )
        .join(
            father_income.select(["individual_id", "father_income_category"]),
            on="individual_id",
            how="left",
        )
    )

    logger.debug("Calculating aggregate statistics")
    # Calculate statistics with separate columns for categorical variables
    stats = df_with_income.group_by("is_scd").agg(
        [
            # Child characteristics
            (pl.col("individual_id").filter(pl.col("role") == "child").count()).alias(
                "n_children"
            ),
            # Gender counts and percentages
            (
                pl.col("gender")
                .filter((pl.col("role") == "child") & (pl.col("gender") == "F"))
                .count()
            ).alias("n_female_children"),
            (
                pl.col("gender")
                .filter((pl.col("role") == "child") & (pl.col("gender") == "M"))
                .count()
            ).alias("n_male_children"),
            # Mother's characteristics
            (pl.col("salary_income").filter(pl.col("role") == "mother").mean()).alias(
                "mean_mother_income"
            ),
            (pl.col("salary_income").filter(pl.col("role") == "mother").std()).alias(
                "std_mother_income"
            ),
            # Mother's income distribution
            (
                pl.col("mother_income_category").filter(pl.col("role") == "mother")
                == "Q1 (<25%)"
            )
            .sum()
            .alias("mother_income_q1"),
            (
                pl.col("mother_income_category").filter(pl.col("role") == "mother")
                == "Q2 (25-50%)"
            )
            .sum()
            .alias("mother_income_q2"),
            (
                pl.col("mother_income_category").filter(pl.col("role") == "mother")
                == "Q3 (50-75%)"
            )
            .sum()
            .alias("mother_income_q3"),
            (
                pl.col("mother_income_category").filter(pl.col("role") == "mother")
                == "Q4 (>75%)"
            )
            .sum()
            .alias("mother_income_q4"),
            # Mother's education
            (
                pl.col("education_group")
                .filter(
                    (pl.col("role") == "mother")
                    & (pl.col("education_group") == "Basic Education")
                )
                .count()
            ).alias("mother_edu_basic"),
            (
                pl.col("education_group")
                .filter(
                    (pl.col("role") == "mother")
                    & (pl.col("education_group") == "Upper Secondary")
                )
                .count()
            ).alias("mother_edu_upper_sec"),
            (
                pl.col("education_group")
                .filter(
                    (pl.col("role") == "mother")
                    & (pl.col("education_group") == "Short-cycle Tertiary")
                )
                .count()
            ).alias("mother_edu_short_tert"),
            (
                pl.col("education_group")
                .filter(
                    (pl.col("role") == "mother")
                    & (pl.col("education_group").str.contains("Bachelor"))
                )
                .count()
            ).alias("mother_edu_bachelor"),
            (
                pl.col("education_group")
                .filter(
                    (pl.col("role") == "mother")
                    & (pl.col("education_group").str.contains("Master"))
                )
                .count()
            ).alias("mother_edu_master"),
            (
                pl.col("education_group")
                .filter(
                    (pl.col("role") == "mother")
                    & (pl.col("education_group").str.contains("Doctoral"))
                )
                .count()
            ).alias("mother_edu_doctoral"),
            # Father's characteristics
            (pl.col("salary_income").filter(pl.col("role") == "father").mean()).alias(
                "mean_father_income"
            ),
            (pl.col("salary_income").filter(pl.col("role") == "father").std()).alias(
                "std_father_income"
            ),
            # Father's income distribution
            (
                pl.col("father_income_category").filter(pl.col("role") == "father")
                == "Q1 (<25%)"
            )
            .sum()
            .alias("father_income_q1"),
            (
                pl.col("father_income_category").filter(pl.col("role") == "father")
                == "Q2 (25-50%)"
            )
            .sum()
            .alias("father_income_q2"),
            (
                pl.col("father_income_category").filter(pl.col("role") == "father")
                == "Q3 (50-75%)"
            )
            .sum()
            .alias("father_income_q3"),
            (
                pl.col("father_income_category").filter(pl.col("role") == "father")
                == "Q4 (>75%)"
            )
            .sum()
            .alias("father_income_q4"),
            # Father's education
            (
                pl.col("education_group")
                .filter(
                    (pl.col("role") == "father")
                    & (pl.col("education_group") == "Basic Education")
                )
                .count()
            ).alias("father_edu_basic"),
            (
                pl.col("education_group")
                .filter(
                    (pl.col("role") == "father")
                    & (pl.col("education_group") == "Upper Secondary")
                )
                .count()
            ).alias("father_edu_upper_sec"),
            (
                pl.col("education_group")
                .filter(
                    (pl.col("role") == "father")
                    & (pl.col("education_group") == "Short-cycle Tertiary")
                )
                .count()
            ).alias("father_edu_short_tert"),
            (
                pl.col("education_group")
                .filter(
                    (pl.col("role") == "father")
                    & (pl.col("education_group").str.contains("Bachelor"))
                )
                .count()
            ).alias("father_edu_bachelor"),
            (
                pl.col("education_group")
                .filter(
                    (pl.col("role") == "father")
                    & (pl.col("education_group").str.contains("Master"))
                )
                .count()
            ).alias("father_edu_master"),
            (
                pl.col("education_group")
                .filter(
                    (pl.col("role") == "father")
                    & (pl.col("education_group").str.contains("Doctoral"))
                )
                .count()
            ).alias("father_edu_doctoral"),
            # Household characteristics
            (pl.col("total_household_income").mean()).alias("mean_household_income"),
            (pl.col("total_household_income").std()).alias("std_household_income"),
            # Household income distribution
            (pl.col("household_income_category") == "Q1 (<25%)")
            .sum()
            .alias("household_income_q1"),
            (pl.col("household_income_category") == "Q2 (25-50%)")
            .sum()
            .alias("household_income_q2"),
            (pl.col("household_income_category") == "Q3 (50-75%)")
            .sum()
            .alias("household_income_q3"),
            (pl.col("household_income_category") == "Q4 (>75%)")
            .sum()
            .alias("household_income_q4"),
        ]
    )

    logger.info("Descriptive table creation completed")
    return stats, df_with_income


def format_descriptive_table(stats_lf: pl.LazyFrame):
    logger.info("Formatting descriptive table")

    # Calculate percentages for categorical variables
    def calc_percent(row, count_col, total_col="n_children"):
        return (
            f"{row[count_col]} ({row[count_col]/row[total_col]*100:.1f}%)"
            if row[total_col] > 0
            else "0 (0%)"
        )

    logger.debug("Converting LazyFrame to DataFrame")
    stats_df = stats_lf.collect()

    # Get actual columns from the DataFrame
    available_columns = set(stats_df.columns)
    logger.debug(f"Available columns: {available_columns}")

    # Define spanners and filter to only include existing columns
    child_spanners = [
        col
        for col in [
            "n_children",
            "n_female_children",
            "n_male_children",
        ]
        if col in available_columns
    ]
    maternal_spanners = [
        col
        for col in [
            "mean_mother_income",
            "mother_income_q1",
            "mother_income_q2",
            "mother_income_q3",
            "mother_income_q4",
            "mother_edu_basic",
            "mother_edu_upper_sec",
            "mother_edu_short_tert",
            "mother_edu_bachelor",
            "mother_edu_master",
            "mother_edu_doctoral",
        ]
        if col in available_columns
    ]

    paternal_spanners = [
        col
        for col in [
            "mean_father_income",
            "father_income_q1",
            "father_income_q2",
            "father_income_q3",
            "father_income_q4",
            "father_edu_basic",
            "father_edu_upper_sec",
            "father_edu_short_tert",
            "father_edu_bachelor",
            "father_edu_master",
            "father_edu_doctoral",
        ]
        if col in available_columns
    ]

    household_spanners = [
        col
        for col in [
            "mean_household_income",
            "household_income_q1",
            "household_income_q2",
            "household_income_q3",
            "household_income_q4",
        ]
        if col in available_columns
    ]

    # Get income columns with polars selectors
    logger.debug("Applying formatting")
    currency_columns = cs.ends_with("_income")
    quantile_columns = cs.contains("_q")

    formatted_table = (
        stats_df.style.tab_header(
            title="Table 1. Participant Characteristics",
            subtitle="Distribution of demographic and socioeconomic characteristics",
        )
        .fmt_currency(
            columns=currency_columns,
            decimals=0,
            currency="DKK",
        )
        .fmt_percent(columns=quantile_columns, decimals=1)
        .tab_style(style=style.text(weight="bold"), locations=loc.column_labels())
        .tab_style(
            style=style.text(weight="bold"), locations=loc.body(rows=pl.col("is_scd"))
        )
        .cols_label(
            is_scd="Group",
            n_children="Total, n",
            n_female_children="Female, n",
            n_male_children="Male, n",
            mean_mother_income="Income (mean)",
            mean_father_income="Income (mean)",
            mean_household_income="Income (mean)",
            mother_income_q1="Q1",
            mother_income_q2="Q2",
            mother_income_q3="Q3",
            mother_income_q4="Q4",
            mother_edu_basic="Basic Education",
            mother_edu_upper_sec="Upper Secondary",
            mother_edu_short_tert="Short-cycle Tertiary",
            mother_edu_bachelor="Bachelor's",
            mother_edu_master="Master's",
            mother_edu_doctoral="Doctoral",
        )
    )

    logger.info("Table formatting completed")
    return formatted_table


def save_table_as_html(table, output_path: str) -> tuple[str, str | None]:
    """
    Save a GT table as an HTML file with proper encoding.
    If a file with the same name exists, renames the existing file by adding a number.

    Args:
        table: The GT table object to save
        output_path: Path where the HTML file should be saved

    Returns:
        tuple[str, str | None]: Tuple containing:
            - Path where the new file was saved
            - Path where the old file was moved (None if no file existed)
    """
    logger.info(f"Saving table to HTML: {output_path}")

    import re
    from pathlib import Path

    # Convert to Path object
    path = Path(output_path)
    old_file_path = None

    if path.exists():
        logger.debug(f"Existing file found at {output_path}")
        # Split into stem and suffix
        stem = path.stem
        suffix = path.suffix
        parent = path.parent

        # Find next available number for the old file
        counter = 1
        while True:
            # Check if stem already ends with a number in parentheses
            match = re.match(r"(.*?)\s*\((\d+)\)$", stem)
            if match:
                # If it does, increment that number
                base_stem = match.group(1)
                new_old_path = parent / f"{base_stem} ({counter}){suffix}"
            else:
                # If it doesn't, add the number
                new_old_path = parent / f"{stem} ({counter}){suffix}"

            if not new_old_path.exists():
                # Rename the existing file
                path.rename(new_old_path)
                old_file_path = str(new_old_path)
                logger.debug(f"Renamed existing file to {old_file_path}")
                break

            counter += 1

    # Save the new file with the original name
    logger.debug("Writing HTML file")
    with open(path, "w", encoding="utf-8") as f:
        html_with_encoding = (
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            '<meta charset="utf-8">\n'
            "</head>\n"
            "<body>\n"
            f"{table.as_raw_html()}\n"
            "</body>\n"
            "</html>"
        )
        f.write(html_with_encoding)

    logger.info(f"Table saved successfully to {path}")
    return str(path), old_file_path


def main():
    logger.info("Starting table generation process")

    # Initialize the data loader
    logger.debug("Initializing data loader")
    base_path = Path("/Users/tobiaskragholm/dev/backup_data/data")
    mappings_dir = Path(
        "/Users/tobiaskragholm/dev/cdef-cohort/src/cdef_cohort/mappings"
    )
    loader = AnalyticalDataLoader(base_path / "analytical_data")

    # Create detailed statistics
    logger.info("Creating detailed statistics")
    detailed_stats = create_detailed_role_distribution(
        loader=loader, mappings_dir=mappings_dir
    )

    # Create and display the formatted table
    logger.info("Creating and formatting table")
    stats_table, df_with_income = create_descriptive_table(detailed_stats)
    logger.debug("Saving detailed data to TSV")
    df_with_income.collect().write_csv("df_with_income.tsv", separator="\t")
    formatted_table = format_descriptive_table(stats_table)
    save_table_as_html(formatted_table, "formatted_table.html")

    logger.info("Process completed successfully")


if __name__ == "__main__":
    main()
