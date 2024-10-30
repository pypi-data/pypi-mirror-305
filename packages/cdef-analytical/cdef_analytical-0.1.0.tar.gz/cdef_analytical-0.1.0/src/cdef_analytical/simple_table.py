from pathlib import Path

import polars as pl
from great_tables import GT, loc, md, style

from cdef_analytical.loaders.data_loader import AnalyticalDataLoader
from cdef_analytical.utils import detect_and_load_json


def create_detailed_role_distribution(
    static_data: pl.LazyFrame,
    demographic_data: pl.LazyFrame,
    employment_data: pl.LazyFrame,
    education_data: pl.LazyFrame,
    income_data: pl.LazyFrame,
    health_data: pl.LazyFrame,  # Add health data parameter
    year: int,
    mappings_dir: Path,  # Add mappings directory parameter
) -> pl.DataFrame:
    """Create detailed role distribution with demographic breakdowns."""

    # Load mappings using the new utility
    def load_mapping(filename: str) -> dict[str, str]:
        return detect_and_load_json(mappings_dir / filename)

    mappings = {
        "SOCIO13": load_mapping("socio13.json"),
        "HFAUDD": load_mapping("isced.json"),
        "STATSB": load_mapping("statsb.json"),
        "CIVST": load_mapping("civst.json"),
        "FM_MARK": load_mapping("fm_mark.json"),
    }

    # Prepare data with mappings
    demographic_data = (
        demographic_data.filter(pl.col("year") == year)
        .with_columns(
            [
                pl.col("PNR").alias("individual_id"),
                pl.col("KOEN"),
                pl.col("CIVST").cast(pl.Utf8).replace(mappings["CIVST"]),
                pl.col("STATSB").cast(pl.Utf8).replace(mappings["STATSB"]),
                pl.col("FM_MARK").cast(pl.Utf8).replace(mappings["FM_MARK"]),
            ]
        )
        .select("individual_id", "KOEN", "CIVST", "STATSB", "FM_MARK")
    )

    employment_data = (
        employment_data.filter(pl.col("year") == year)
        .with_columns(
            [
                pl.col("PNR").alias("individual_id"),
                pl.col("SOCIO13").cast(pl.Utf8).replace(mappings["SOCIO13"]),
            ]
        )
        .select("individual_id", "SOCIO13")
    )

    education_data = (
        education_data.filter(pl.col("year") == year)
        .with_columns(
            [
                pl.col("PNR").alias("individual_id"),
                pl.col("HFAUDD").cast(pl.Utf8).replace(mappings["HFAUDD"]),
            ]
        )
        .select("individual_id", "HFAUDD")
    )

    # Add severe chronic disease data
    health_data = health_data.with_columns(pl.col("PNR").alias("individual_id")).select(
        "individual_id", "is_scd", "first_scd_date"
    )

    # Prepare income data
    income_data = (
        income_data.filter(pl.col("year") == year)
        .with_columns(
            [
                pl.col("PNR").alias("individual_id"),
                # Convert to thousands and round to 2 decimals
                (pl.col("LOENMV_13") / 1000).round(2).alias("salary"),
                (pl.col("PERINDKIALT_13") / 1000).round(2).alias("total_income"),
            ]
        )
        .select("individual_id", "salary", "total_income")
    )

    # Join all data sources including income
    combined_data = (
        static_data.join(demographic_data, on="individual_id", how="left")
        .join(employment_data, on="individual_id", how="left")
        .join(education_data, on="individual_id", how="left")
        .join(health_data, on="individual_id", how="left")
        .join(income_data, on="individual_id", how="left")
    ).collect()

    def calculate_distribution(
        df: pl.DataFrame, column: str, roles: list[str], is_numeric: bool = False
    ) -> pl.DataFrame:
        """Calculate distribution for a given column and roles."""
        # Ensure standard columns are consistent
        standard_columns = ["Category", "child", "mother", "father"]

        if is_numeric:
            # For numeric columns, calculate summary statistics
            stats = (
                df.filter(pl.col("role").is_in(roles))
                .group_by("role")
                .agg(
                    [
                        pl.col(column).mean().round(2).alias("mean"),
                        pl.col(column).median().round(2).alias("median"),
                        pl.col(column).std().round(2).alias("std"),
                        pl.col(column).quantile(0.25).round(2).alias("q25"),
                        pl.col(column).quantile(0.75).round(2).alias("q75"),
                    ]
                )
                .with_columns(
                    [
                        pl.lit(f"{column}_mean").alias("Category"),
                        pl.col("mean").round(2),
                    ]
                )
                .select(["Category", "role", "mean"])
                .pivot(
                    values="mean",
                    index="Category",
                    on="role",
                    aggregate_function="first",
                )
            )

            # Ensure all standard columns exist
            for col in standard_columns:
                if col not in stats.columns:
                    stats = stats.with_columns(pl.lit(None).alias(col))

            return stats.select(standard_columns)

        else:
            # Categorical distribution calculation
            distribution = (
                df.filter(pl.col("role").is_in(roles))
                .with_columns(
                    [
                        pl.col("role").cast(pl.Utf8),
                        pl.col(column).cast(pl.Utf8),
                    ]
                )
                .group_by("role", column)
                .agg(pl.len().alias("count"))
                .with_columns(pl.col("count") / pl.col("count").sum().over("role"))
                .pivot(
                    values="count", index=column, on="role", aggregate_function="first"
                )
                .rename({column: "Category"})
                .fill_null(0.0)
            )

            # Ensure all standard columns exist
            for col in standard_columns:
                if col not in distribution.columns:
                    distribution = distribution.with_columns(pl.lit(0.0).alias(col))

            return distribution.select(standard_columns)

    # Define metrics to calculate
    metrics = [
        ("KOEN", "Gender", ["child", "mother", "father"], False),
        ("FM_MARK", "Living Status", ["child", "mother", "father"], False),
        ("CIVST", "Civil Status", ["mother", "father"], False),
        ("STATSB", "Citizenship", ["mother", "father"], False),
        ("HFAUDD", "Education", ["mother", "father"], False),
        ("SOCIO13", "Socioeconomic Status", ["mother", "father"], False),
        ("salary", "Salary (1000 DKK)", ["mother", "father"], True),
        ("total_income", "Total Income (1000 DKK)", ["mother", "father"], True),
        ("is_scd", "Severe Chronic Disease", ["child"], False),
    ]

    # Calculate all distributions
    distributions = []
    for column, metric_name, roles, is_numeric in metrics:
        df = calculate_distribution(combined_data, column, roles, is_numeric)
        df = df.with_columns(pl.lit(metric_name).alias("Metric"))
        distributions.append(df)

    # Combine all results and format
    return (
        pl.concat(distributions)
        .select(["Metric", "Category", "child", "mother", "father"])
        .with_columns([pl.exclude(["Metric", "Category"]).round(4)])
    )


def create_display_table(stats: pl.DataFrame, year: int) -> GT:
    """Create a formatted display table from the statistics DataFrame."""

    # Identify different types of metrics for formatting
    income_metrics = ["Salary (1000 DKK)", "Total Income (1000 DKK)"]
    percent_metrics = [
        "Gender",
        "Civil Status",
        "Citizenship",
        "Socioeconomic Status",
        "Education",
        "Living Status",
        "Severe Chronic Disease",
    ]

    # Function to format category values
    def format_category(s: str) -> str:
        if s == "None":
            return "Not Available"
        elif s.endswith("_mean"):
            return "Average"
        return s

    # Clean up the stats DataFrame
    stats = stats.with_columns(
        [pl.col("Category").map_elements(format_category, return_dtype=pl.Utf8)]
    )

    # Get row indices for different metric types using row_idx
    income_rows = list(
        stats.with_row_index()
        .filter(pl.col("Metric").is_in(income_metrics))
        .get_column("index")
    )
    percent_rows = list(
        stats.with_row_index()
        .filter(pl.col("Metric").is_in(percent_metrics))
        .get_column("index")
    )

    # Color palette
    colors = {
        "header_bg": "#2C3E50",  # Dark blue-gray
        "header_fg": "#FFFFFF",  # White
        "income_bg": "#EBF5FB",  # Light blue
        "stripe_bg": "#F8F9FA",  # Light gray
        "border": "#BDC3C7",  # Gray
        "highlight": "#3498DB",  # Blue
    }

    # Create table
    table = (
        GT(stats)
        .tab_header(
            title=md(f"**Population Characteristics by Role ({year})**"),
            subtitle="Distribution of demographic and socioeconomic characteristics",
        )
        .tab_spanner(
            label=md("**Distribution (%)**"), columns=["child", "mother", "father"]
        )
        .cols_label(
            Metric=md("**Characteristic**"),
            Category=md("**Category**"),
            child=md("**Child**"),
            mother=md("**Mother**"),
            father=md("**Father**"),
        )
        # Format percentages and numbers
        .fmt_percent(
            columns=["child", "mother", "father"],
            decimals=1,
            rows=percent_rows,
            sep_mark=".",
            dec_mark=",",
        )
        .fmt_number(
            columns=["child", "mother", "father"],
            decimals=0,
            rows=income_rows,
            sep_mark=".",
            dec_mark=",",
        )
        # Style headers
        .tab_style(
            style=[
                style.fill(color=colors["header_bg"]),
                style.text(color=colors["header_fg"]),
                style.text(weight="bold"),
            ],
            locations=loc.column_labels(),
        )
        # Style column spanners
        .tab_style(
            style=[
                style.fill(color=colors["header_bg"]),
                style.text(color=colors["header_fg"]),
                style.text(weight="bold"),
            ],
            locations=loc.column_header(),
        )
        # Style metric names
        .tab_style(
            style=[style.text(weight="bold"), style.text(color=colors["header_bg"])],
            locations=loc.body(columns="Metric"),
        )
        # Style income rows
        .tab_style(
            style=style.fill(color=colors["income_bg"]),
            locations=loc.body(rows=income_rows),
        )
        # Add borders
        .tab_style(
            style=style.borders(sides="bottom", weight="1px", color=colors["border"]),
            locations=loc.body(),
        )
        # Add special bottom borders for section breaks
        .tab_style(
            style=style.borders(
                sides="bottom", weight="2px", color=colors["highlight"]
            ),
            locations=loc.body(rows=percent_rows[-1:] + income_rows[-1:]),
        )
        # Add footnotes
        .tab_source_note(
            source_note=md("**Source:** Statistics Denmark, Administrative Data")
        )
        .tab_source_note(
            source_note=md("**Note:** Income values are in thousands (DKK)")
        )
        .tab_source_note(source_note=f"Reference year: {year}")
        # Layout options
        .opt_row_striping(
            row_striping=True,
            # row_striping_background_color=colors["stripe_bg"]
        )
        .opt_vertical_padding(scale=0.85)
        .opt_horizontal_padding(scale=1.1)
        .opt_table_font(font=["Helvetica Neue", "Helvetica", "Arial", "sans-serif"])
    )

    return table


def main():
    # Initialize the data loader
    base_path = Path("/Users/tobiaskragholm/dev/backup_data/data")
    mappings_dir = Path(
        "/Users/tobiaskragholm/dev/cdef-cohort/src/cdef_cohort/mappings"
    )
    loader = AnalyticalDataLoader(base_path / "analytical_data")

    # Load all required data
    static_data = loader.get_static_data()
    demographic_data = loader.get_longitudinal_data(domain="demographics")
    employment_data = loader.get_longitudinal_data(domain="employment")
    education_data = loader.get_longitudinal_data(domain="education")
    # Load income data
    income_data = loader.get_longitudinal_data(domain="income")

    # Load health data
    health_data = pl.scan_parquet(base_path / "health.parquet")

    # Get available years
    available_years = sorted(
        set(loader.get_available_years("demographics"))
        & set(loader.get_available_years("employment"))
        & set(loader.get_available_years("education"))
    )

    if not available_years:
        raise ValueError("No common years available across all domains")

    # Create and print detailed statistics for the most recent year
    latest_year = max(available_years)
    # Create and print detailed statistics
    detailed_stats = create_detailed_role_distribution(
        static_data=static_data,
        demographic_data=demographic_data,
        employment_data=employment_data,
        education_data=education_data,
        income_data=income_data,  # Add income data
        health_data=health_data,
        year=latest_year,
        mappings_dir=mappings_dir,
    )
    # Create formatted table
    table = create_display_table(detailed_stats, latest_year)

    # Save to HTML
    html_content = table.as_raw_html()
    with open("role_distribution_table.html", "w", encoding="utf-8") as f:
        # Add UTF-8 meta tag to HTML header
        html_with_encoding = (
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            '<meta charset="utf-8">\n'
            "</head>\n"
            "<body>\n"
            f"{html_content}\n"
            "</body>\n"
            "</html>"
        )
        f.write(html_with_encoding)

    # Display the table
    # print(table)


if __name__ == "__main__":
    main()
