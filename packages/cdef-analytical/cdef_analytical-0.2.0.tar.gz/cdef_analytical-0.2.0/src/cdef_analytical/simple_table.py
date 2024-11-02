# from pathlib import Path

# import polars as pl
# import polars.selectors as cs
# from great_tables import GT, google_font, loc, md, style

# from cdef_analytical.loaders.data_loader import AnalyticalDataLoader
# from cdef_analytical.utils import detect_and_load_json


# def create_descriptive_table(df):
#     # Define common quartile labels
#     quartile_labels = ["Q1", "Q2", "Q3", "Q4"]

#     # Calculate income quartiles for mothers and fathers separately
#     mother_income = df.filter(pl.col("role") == "mother").with_columns(
#         pl.col("salary_income")
#         .qcut(quantiles=4, labels=quartile_labels)
#         .alias("mother_income_category")
#     )

#     father_income = df.filter(pl.col("role") == "father").with_columns(
#         pl.col("salary_income")
#         .qcut(quantiles=4, labels=quartile_labels)
#         .alias("father_income_category")
#     )

#     # Calculate household income
#     household_income = (
#         df.group_by("family_id")
#         .agg(pl.col("salary_income").sum().alias("total_household_income"))
#         .with_columns(
#             pl.col("total_household_income")
#             .qcut(
#                 quantiles=4,
#                 labels=quartile_labels,
#             )
#             .alias("household_income_category")
#         )
#     )

#     # Join all income categories back to original dataframe
#     df_with_income = (
#         df.join(household_income, on="family_id")
#         .join(
#             mother_income.select(["individual_id", "mother_income_category"]),
#             on="individual_id",
#             how="left",
#         )
#         .join(
#             father_income.select(["individual_id", "father_income_category"]),
#             on="individual_id",
#             how="left",
#         )
#     )

#     # Calculate statistics with separate columns for categorical variables
#     stats = df_with_income.group_by("is_scd").agg(
#         [
#             # Child characteristics
#             (pl.col("individual_id").filter(pl.col("role") == "child").count()).alias(
#                 "n_children"
#             ),
#             # Gender counts and percentages
#             (
#                 pl.col("gender")
#                 .filter((pl.col("role") == "child") & (pl.col("gender") == "F"))
#                 .count()
#             ).alias("n_female_children"),
#             (
#                 pl.col("gender")
#                 .filter((pl.col("role") == "child") & (pl.col("gender") == "M"))
#                 .count()
#             ).alias("n_male_children"),
#             # Mother's characteristics
#             (pl.col("salary_income").filter(pl.col("role") == "mother").mean()).alias(
#                 "mean_mother_income"
#             ),
#             (pl.col("salary_income").filter(pl.col("role") == "mother").std()).alias(
#                 "std_mother_income"
#             ),
#             # Mother's income distribution
#             (
#                 pl.col("mother_income_category").filter(pl.col("role") == "mother")
#                 == "Q1 (<25%)"
#             )
#             .sum()
#             .alias("mother_income_q1"),
#             (
#                 pl.col("mother_income_category").filter(pl.col("role") == "mother")
#                 == "Q2 (25-50%)"
#             )
#             .sum()
#             .alias("mother_income_q2"),
#             (
#                 pl.col("mother_income_category").filter(pl.col("role") == "mother")
#                 == "Q3 (50-75%)"
#             )
#             .sum()
#             .alias("mother_income_q3"),
#             (
#                 pl.col("mother_income_category").filter(pl.col("role") == "mother")
#                 == "Q4 (>75%)"
#             )
#             .sum()
#             .alias("mother_income_q4"),
#             # Mother's education
#             (
#                 pl.col("education_group")
#                 .filter(
#                     (pl.col("role") == "mother")
#                     & (pl.col("education_group") == "Basic Education")
#                 )
#                 .count()
#             ).alias("mother_edu_basic"),
#             (
#                 pl.col("education_group")
#                 .filter(
#                     (pl.col("role") == "mother")
#                     & (pl.col("education_group") == "Upper Secondary")
#                 )
#                 .count()
#             ).alias("mother_edu_upper_sec"),
#             (
#                 pl.col("education_group")
#                 .filter(
#                     (pl.col("role") == "mother")
#                     & (pl.col("education_group") == "Short-cycle Tertiary")
#                 )
#                 .count()
#             ).alias("mother_edu_short_tert"),
#             (
#                 pl.col("education_group")
#                 .filter(
#                     (pl.col("role") == "mother")
#                     & (pl.col("education_group").str.contains("Bachelor"))
#                 )
#                 .count()
#             ).alias("mother_edu_bachelor"),
#             (
#                 pl.col("education_group")
#                 .filter(
#                     (pl.col("role") == "mother")
#                     & (pl.col("education_group").str.contains("Master"))
#                 )
#                 .count()
#             ).alias("mother_edu_master"),
#             (
#                 pl.col("education_group")
#                 .filter(
#                     (pl.col("role") == "mother")
#                     & (pl.col("education_group").str.contains("Doctoral"))
#                 )
#                 .count()
#             ).alias("mother_edu_doctoral"),
#             # Father's characteristics
#             (pl.col("salary_income").filter(pl.col("role") == "father").mean()).alias(
#                 "mean_father_income"
#             ),
#             (pl.col("salary_income").filter(pl.col("role") == "father").std()).alias(
#                 "std_father_income"
#             ),
#             # Father's income distribution
#             (
#                 pl.col("father_income_category").filter(pl.col("role") == "father")
#                 == "Q1 (<25%)"
#             )
#             .sum()
#             .alias("father_income_q1"),
#             (
#                 pl.col("father_income_category").filter(pl.col("role") == "father")
#                 == "Q2 (25-50%)"
#             )
#             .sum()
#             .alias("father_income_q2"),
#             (
#                 pl.col("father_income_category").filter(pl.col("role") == "father")
#                 == "Q3 (50-75%)"
#             )
#             .sum()
#             .alias("father_income_q3"),
#             (
#                 pl.col("father_income_category").filter(pl.col("role") == "father")
#                 == "Q4 (>75%)"
#             )
#             .sum()
#             .alias("father_income_q4"),
#             # Father's education
#             (
#                 pl.col("education_group")
#                 .filter(
#                     (pl.col("role") == "father")
#                     & (pl.col("education_group") == "Basic Education")
#                 )
#                 .count()
#             ).alias("father_edu_basic"),
#             (
#                 pl.col("education_group")
#                 .filter(
#                     (pl.col("role") == "father")
#                     & (pl.col("education_group") == "Upper Secondary")
#                 )
#                 .count()
#             ).alias("father_edu_upper_sec"),
#             (
#                 pl.col("education_group")
#                 .filter(
#                     (pl.col("role") == "father")
#                     & (pl.col("education_group") == "Short-cycle Tertiary")
#                 )
#                 .count()
#             ).alias("father_edu_short_tert"),
#             (
#                 pl.col("education_group")
#                 .filter(
#                     (pl.col("role") == "father")
#                     & (pl.col("education_group").str.contains("Bachelor"))
#                 )
#                 .count()
#             ).alias("father_edu_bachelor"),
#             (
#                 pl.col("education_group")
#                 .filter(
#                     (pl.col("role") == "father")
#                     & (pl.col("education_group").str.contains("Master"))
#                 )
#                 .count()
#             ).alias("father_edu_master"),
#             (
#                 pl.col("education_group")
#                 .filter(
#                     (pl.col("role") == "father")
#                     & (pl.col("education_group").str.contains("Doctoral"))
#                 )
#                 .count()
#             ).alias("father_edu_doctoral"),
#             # Household characteristics
#             (pl.col("total_household_income").mean()).alias("mean_household_income"),
#             (pl.col("total_household_income").std()).alias("std_household_income"),
#             # Household income distribution
#             (pl.col("household_income_category") == "Q1 (<25%)")
#             .sum()
#             .alias("household_income_q1"),
#             (pl.col("household_income_category") == "Q2 (25-50%)")
#             .sum()
#             .alias("household_income_q2"),
#             (pl.col("household_income_category") == "Q3 (50-75%)")
#             .sum()
#             .alias("household_income_q3"),
#             (pl.col("household_income_category") == "Q4 (>75%)")
#             .sum()
#             .alias("household_income_q4"),
#         ]
#     )

#     return stats, df_with_income


# def format_descriptive_table(stats_lf: pl.LazyFrame):
#     # Calculate percentages for categorical variables
#     def calc_percent(row, count_col, total_col="n_children"):
#         return (
#             f"{row[count_col]} ({row[count_col]/row[total_col]*100:.1f}%)"
#             if row[total_col] > 0
#             else "0 (0%)"
#         )

#     stats_df = stats_lf.collect()
#     formatted_table = (
#         stats_df.style.tab_header(
#             title="Table 1. Participant Characteristics",
#             subtitle="Distribution of demographic and socioeconomic characteristics",
#         )
#         # Add spanners for main categories
#         .tab_spanner(
#             "Child Characteristics",
#             ["n_children", "n_female_children", "n_male_children"],
#         )
#         .tab_spanner(
#             "Maternal Characteristics",
#             [
#                 "mean_mother_income",
#                 "mother_income_q1",
#                 "mother_income_q2",
#                 "mother_income_q3",
#                 "mother_income_q4",
#                 "mother_edu_basic",
#                 "mother_edu_upper_sec",
#                 "mother_edu_short_tert",
#                 "mother_edu_bachelor",
#                 "mother_edu_master",
#                 "mother_edu_doctoral",
#             ],
#         )
#         .tab_spanner(
#             "Paternal Characteristics",
#             [
#                 "mean_father_income",
#                 "father_income_q1",
#                 "father_income_q2",
#                 "father_income_q3",
#                 "father_income_q4",
#                 "father_edu_basic",
#                 "father_edu_upper_sec",
#                 "father_edu_short_tert",
#                 "father_edu_bachelor",
#                 "father_edu_master",
#                 "father_edu_doctoral",
#             ],
#         )
#         .tab_spanner(
#             "Household Characteristics",
#             [
#                 "mean_household_income",
#                 "household_income_q1",
#                 "household_income_q2",
#                 "household_income_q3",
#                 "household_income_q4",
#             ],
#         )
#         # Format numbers
#         .fmt_currency(
#             ["mean_mother_income", "mean_father_income", "mean_household_income"],
#             decimals=0,
#             currency="DKK",
#         )
#         .fmt_percent(cs.contains("_q"), decimals=1)
#         # Add styles
#         .tab_style(style.text(weight="bold"), loc.column_labels())
#         .tab_style(style.text(weight="bold"), loc.body(rows=pl.col("is_scd")))
#         # Rename columns
#         .cols_label(
#             is_scd="Group",
#             n_children="Total, n",
#             n_female_children="Female, n (%)",
#             n_male_children="Male, n (%)",
#             mean_mother_income="Income (mean)",
#             mean_father_income="Income (mean)",
#             mean_household_income="Income (mean)",
#             mother_income_q1="Q1 (<25%)",
#             mother_income_q2="Q2 (25-50%)",
#             mother_income_q3="Q3 (50-75%)",
#             mother_income_q4="Q4 (>75%)",
#             mother_edu_basic="Basic Education",
#             mother_edu_upper_sec="Upper Secondary",
#             mother_edu_short_tert="Short-cycle Tertiary",
#             mother_edu_bachelor="Bachelor's",
#             mother_edu_master="Master's",
#             mother_edu_doctoral="Doctoral",
#         )
#     )

#     return formatted_table


# def create_readable_table(stats_df):
#     # Helper expressions
#     def format_percent(count_col, total_col):
#         return pl.format("{} ({:.1f}%)", count_col, (count_col / total_col * 100))

#     def format_currency(amount):
#         return pl.format("${:,.0f}", amount)

#     # Calculate cases and controls statistics
#     cases = (
#         stats_df.filter(pl.col("is_scd"))
#         .select(
#             [
#                 # Child statistics
#                 pl.col("n_children").alias("total_children"),
#                 format_percent(pl.col("n_female_children"), pl.col("n_children")).alias(
#                     "female_children"
#                 ),
#                 format_percent(pl.col("n_male_children"), pl.col("n_children")).alias(
#                     "male_children"
#                 ),
#                 # Mother education
#                 format_percent(pl.col("mother_edu_basic"), pl.lit(1)).alias(
#                     "mother_basic"
#                 ),
#                 format_percent(pl.col("mother_edu_upper_sec"), pl.lit(1)).alias(
#                     "mother_upper_sec"
#                 ),
#                 format_percent(pl.col("mother_edu_short_tert"), pl.lit(1)).alias(
#                     "mother_short_tert"
#                 ),
#                 format_percent(pl.col("mother_edu_bachelor"), pl.lit(1)).alias(
#                     "mother_bachelor"
#                 ),
#                 format_percent(pl.col("mother_edu_master"), pl.lit(1)).alias(
#                     "mother_master"
#                 ),
#                 format_percent(pl.col("mother_edu_doctoral"), pl.lit(1)).alias(
#                     "mother_doctoral"
#                 ),
#                 # Mother income
#                 format_percent(pl.col("mother_income_q1"), pl.lit(1)).alias(
#                     "mother_income_q1"
#                 ),
#                 format_percent(pl.col("mother_income_q2"), pl.lit(1)).alias(
#                     "mother_income_q2"
#                 ),
#                 format_percent(pl.col("mother_income_q3"), pl.lit(1)).alias(
#                     "mother_income_q3"
#                 ),
#                 format_percent(pl.col("mother_income_q4"), pl.lit(1)).alias(
#                     "mother_income_q4"
#                 ),
#                 format_currency(pl.col("mean_mother_income")).alias(
#                     "mother_mean_income"
#                 ),
#                 # Father education
#                 format_percent(pl.col("father_edu_basic"), pl.lit(1)).alias(
#                     "father_basic"
#                 ),
#                 format_percent(pl.col("father_edu_upper_sec"), pl.lit(1)).alias(
#                     "father_upper_sec"
#                 ),
#                 format_percent(pl.col("father_edu_short_tert"), pl.lit(1)).alias(
#                     "father_short_tert"
#                 ),
#                 format_percent(pl.col("father_edu_bachelor"), pl.lit(1)).alias(
#                     "father_bachelor"
#                 ),
#                 format_percent(pl.col("father_edu_master"), pl.lit(1)).alias(
#                     "father_master"
#                 ),
#                 format_percent(pl.col("father_edu_doctoral"), pl.lit(1)).alias(
#                     "father_doctoral"
#                 ),
#                 # Father income
#                 format_percent(pl.col("father_income_q1"), pl.lit(1)).alias(
#                     "father_income_q1"
#                 ),
#                 format_percent(pl.col("father_income_q2"), pl.lit(1)).alias(
#                     "father_income_q2"
#                 ),
#                 format_percent(pl.col("father_income_q3"), pl.lit(1)).alias(
#                     "father_income_q3"
#                 ),
#                 format_percent(pl.col("father_income_q4"), pl.lit(1)).alias(
#                     "father_income_q4"
#                 ),
#                 format_currency(pl.col("mean_father_income")).alias(
#                     "father_mean_income"
#                 ),
#             ]
#         )
#         .row(0)
#     )

#     controls = (
#         stats_df.filter(~pl.col("is_scd"))
#         .select(
#             [
#                 # Same selections as above
#             ]
#         )
#         .row(0)
#     )

#     # Create table structure
#     table_data = pl.DataFrame(
#         {
#             "Characteristic": [
#                 "Child Characteristics",
#                 "Number of children",
#                 "Sex distribution",
#                 "- Female",
#                 "- Male",
#                 "Maternal Characteristics",
#                 "Education",
#                 "- Basic Education",
#                 "- Upper Secondary",
#                 "- Short-cycle Tertiary",
#                 "- Bachelor's degree",
#                 "- Master's degree",
#                 "- Doctoral degree",
#                 "Income distribution",
#                 "- Q1 (<25th percentile)",
#                 "- Q2 (25-50th percentile)",
#                 "- Q3 (50-75th percentile)",
#                 "- Q4 (>75th percentile)",
#                 "Mean annual income",
#                 "Paternal Characteristics",
#                 "Education",
#                 "- Basic Education",
#                 "- Upper Secondary",
#                 "- Short-cycle Tertiary",
#                 "- Bachelor's degree",
#                 "- Master's degree",
#                 "- Doctoral degree",
#                 "Income distribution",
#                 "- Q1 (<25th percentile)",
#                 "- Q2 (25-50th percentile)",
#                 "- Q3 (50-75th percentile)",
#                 "- Q4 (>75th percentile)",
#                 "Mean annual income",
#             ],
#             "Cases": [
#                 "",  # Child Characteristics
#                 str(cases["total_children"]),
#                 "",
#                 cases["female_children"],
#                 cases["male_children"],
#                 "",  # Maternal Characteristics
#                 "",
#                 cases["mother_basic"],
#                 cases["mother_upper_sec"],
#                 cases["mother_short_tert"],
#                 cases["mother_bachelor"],
#                 cases["mother_master"],
#                 cases["mother_doctoral"],
#                 "",
#                 cases["mother_income_q1"],
#                 cases["mother_income_q2"],
#                 cases["mother_income_q3"],
#                 cases["mother_income_q4"],
#                 cases["mother_mean_income"],
#                 "",  # Paternal Characteristics
#                 "",
#                 cases["father_basic"],
#                 cases["father_upper_sec"],
#                 cases["father_short_tert"],
#                 cases["father_bachelor"],
#                 cases["father_master"],
#                 cases["father_doctoral"],
#                 "",
#                 cases["father_income_q1"],
#                 cases["father_income_q2"],
#                 cases["father_income_q3"],
#                 cases["father_income_q4"],
#                 cases["father_mean_income"],
#             ],
#             "Controls": [
#                 # Same pattern as Cases
#             ],
#         }
#     )

#     # Format table
#     formatted_table = (
#         table_data.style.tab_header(
#             title="Table 1. Participant Characteristics",
#             subtitle="Distribution of demographic and socioeconomic characteristics",
#         )
#         .tab_style(
#             style.text(weight="bold"),
#             loc.body(
#                 rows=lambda df: df["Characteristic"].isin(
#                     [
#                         "Child Characteristics",
#                         "Maternal Characteristics",
#                         "Paternal Characteristics",
#                     ]
#                 )
#             ),
#         )
#         .cols_label(
#             Characteristic="Characteristic",
#             Cases=f"Cases (n={cases['total_children']})",
#             Controls=f"Controls (n={controls['total_children']})",
#         )
#     )

#     return formatted_table


# def calculate_distribution(
#     df: pl.LazyFrame, column: str, roles: list[str], is_numeric: bool = False
# ) -> pl.LazyFrame:
#     """Calculate distribution for a given column and roles."""
#     # Ensure standard columns are consistent
#     standard_columns = ["Category", "child", "mother", "father"]

#     if is_numeric:
#         # For numeric columns, calculate summary statistics
#         stats = (
#             df.filter(pl.col("role").is_in(roles))
#             .group_by("role")
#             .agg(
#                 [
#                     pl.col(column).mean().round(2).alias("mean"),
#                     pl.col(column).median().round(2).alias("median"),
#                     pl.col(column).std().round(2).alias("std"),
#                     pl.col(column).quantile(0.25).round(2).alias("q25"),
#                     pl.col(column).quantile(0.75).round(2).alias("q75"),
#                 ]
#             )
#             .with_columns(
#                 [
#                     pl.lit(f"{column}_mean").alias("Category"),
#                     pl.col("mean").round(2),
#                 ]
#             )
#             .select(["Category", "role", "mean"])
#             .collect()  # Need to collect for pivot
#             .pivot(
#                 values="mean",
#                 index="Category",
#                 on="role",
#                 aggregate_function="first",
#             )
#         ).lazy()  # Convert back to LazyFrame

#         # Ensure all standard columns exist
#         for col in standard_columns:
#             if col not in stats.collect_schema().names():
#                 stats = stats.with_columns(pl.lit(None).alias(col))

#         return stats.select(standard_columns)

#     else:
#         # Categorical distribution calculation
#         distribution = (
#             df.filter(pl.col("role").is_in(roles))
#             .with_columns(
#                 [
#                     pl.col("role").cast(pl.Utf8),
#                     pl.col(column).cast(pl.Utf8),
#                 ]
#             )
#             .group_by("role", column)
#             .agg(pl.len().alias("count"))
#             .with_columns(pl.col("count") / pl.col("count").sum().over("role"))
#             .collect()  # Need to collect for pivot
#             .pivot(values="count", index=column, on="role", aggregate_function="first")
#             .rename({column: "Category"})
#             .fill_null(0.0)
#         ).lazy()  # Convert back to LazyFrame

#         # Ensure all standard columns exist
#         for col in standard_columns:
#             if col not in distribution.collect_schema().names():
#                 distribution = distribution.with_columns(pl.lit(0.0).alias(col))

#         return distribution.select(standard_columns)


# def prepare_analytical_data(
#     loader: AnalyticalDataLoader,
#     year: int,
#     include_education: bool = True,
#     include_income: bool = True,
#     include_health: bool = True,
# ) -> dict[str, pl.LazyFrame]:
#     """
#     Prepare and combine analytical data from various sources.

#     Args:
#         loader: Instance of AnalyticalDataLoader
#         year: Reference year for the data
#         include_education: Whether to include education data
#         include_income: Whether to include income data
#         include_health: Whether to include health data

#     Returns:
#         Dictionary containing prepared DataFrames for different roles:
#         {
#             'child': DataFrame,
#             'maternal': DataFrame,
#             'paternal': DataFrame
#         }
#     """

#     # Get base static data with roles
#     static_data = loader.get_static_data()

#     # Get demographic data
#     demographic_data = (
#         loader.get_longitudinal_data("demographics")
#         .filter(pl.col("year") == year)
#         .select(
#             [
#                 pl.col("PNR").alias("individual_id"),
#                 pl.col("FOED_DAG").alias("birth_date"),
#                 pl.col("KOEN").alias("gender"),
#                 pl.col("FM_MARK").cast(pl.Utf8).alias("parental_marking"),
#                 pl.col("ANTBOERNF").alias("children_in_family"),
#                 pl.col("FAMILIE_TYPE").alias("family_type"),
#                 pl.col("FAMILIE_ID").alias("family_id"),
#                 pl.col("CIVST").cast(pl.Utf8).alias("martial_status"),
#                 pl.col("STATSB").cast(pl.Utf8).alias("citizenship"),
#             ]
#         )
#     )

#     # Initialize data dictionary
#     data_frames = {}

#     # Optional data loading based on parameters
#     additional_data = {}

#     if include_education:
#         education_data = (
#             loader.get_longitudinal_data("education")
#             .filter(pl.col("year") == year)
#             .select(
#                 [
#                     pl.col("PNR").alias("individual_id"),
#                     pl.col("HFAUDD").alias("education_level"),
#                 ]
#             )
#         )
#         additional_data["education"] = education_data

#     if include_income:
#         income_data = (
#             loader.get_longitudinal_data("income")
#             .filter(pl.col("year") == year)
#             .select(
#                 [
#                     pl.col("PNR").alias("individual_id"),
#                     pl.col("PERINDKIALT_13").alias("personal_income"),
#                     pl.col("LOENMV_13").alias("salary_income"),
#                 ]
#             )
#         )
#         additional_data["income"] = income_data

#     if include_health:
#         scd_data = loader.get_scd_status().select(
#             ["individual_id", "is_scd", "first_scd_date"]
#         )
#         additional_data["health"] = scd_data

#     # Prepare data for each role
#     for role in ["child", "maternal", "paternal"]:
#         # Start with static data filtered by role
#         role_data = static_data.filter(pl.col("role") == role)

#         # Join with demographic data
#         combined_data = role_data.join(demographic_data, on="individual_id", how="left")

#         # Join with additional data sources
#         for data_type, df in additional_data.items():
#             combined_data = combined_data.join(df, on="individual_id", how="left")

#         data_frames[role] = combined_data

#     return data_frames


# def create_detailed_role_distribution(
#     loader: AnalyticalDataLoader,
#     year: int,
#     mappings_dir: Path,
# ) -> pl.LazyFrame:
#     """Create detailed role distribution with demographic breakdowns."""

#     # Prepare all required data
#     prepared_data = prepare_analytical_data(
#         loader=loader,
#         year=year,
#         include_education=True,
#         include_income=True,
#         include_health=True,
#     )

#     # Load mappings
#     mappings = {
#         filename.stem: detect_and_load_json(mappings_dir / f"{filename.stem}.json")
#         for filename in mappings_dir.glob("*.json")
#     }

#     # Apply mappings to the prepared data
#     for role, data in prepared_data.items():
#         prepared_data[role] = data.with_columns(
#             [
#                 pl.col("gender").cast(pl.Utf8).replace(mappings.get("KOEN", {})),
#                 pl.col("parental_marking")
#                 .cast(pl.Utf8)
#                 .replace(mappings.get("FM_MARK", {})),
#                 pl.col("martial_status")
#                 .cast(pl.Utf8)
#                 .replace(mappings.get("CIVST", {})),
#                 pl.col("citizenship").cast(pl.Utf8).replace(mappings.get("STATSB", {})),
#                 pl.col("education_level")
#                 .cast(pl.Utf8)
#                 .replace(mappings.get("HFAUDD", {})),
#                 pl.when(pl.col("education_level").is_in(["0", "1", "2"]))
#                 .then(pl.lit("Basic Education"))
#                 .when(pl.col("education_level").is_in(["3", "4"]))
#                 .then(pl.lit("Upper Secondary"))
#                 .when(pl.col("education_level").is_in(["5"]))
#                 .then(pl.lit("Short-cycle Tertiary"))
#                 .when(pl.col("education_level").is_in(["6"]))
#                 .then(pl.lit("Bachelor's or equivalent"))
#                 .when(pl.col("education_level").is_in(["7"]))
#                 .then(pl.lit("Master's or equivalent"))
#                 .when(pl.col("education_level").is_in(["8"]))
#                 .then(pl.lit("Doctoral or equivalent"))
#                 .otherwise(pl.lit("Unknown/Not stated"))
#                 .alias("education_group"),
#             ]
#         )  # Group ISCED levels

#     # Combine all role data into a single LazyFrame
#     combined_data = pl.concat(
#         [
#             df.with_columns(pl.lit(role).alias("role"))
#             for role, df in prepared_data.items()
#         ]
#     ).lazy()

#     return combined_data


# def calculate_role_distribution(combined_data: pl.LazyFrame) -> pl.DataFrame:
#     # Define metrics to calculate
#     metrics = [
#         # (column_name, display_name, roles_to_include, is_numeric)
#         # Categorical variables (is_numeric=False)
#         ("gender", "Gender", ["child", "mother", "father"], False),
#         ("parental_marking", "Living Status", ["child", "mother", "father"], False),
#         ("martial_status", "Civil Status", ["mother", "father"], False),
#         ("citizenship", "Citizenship", ["mother", "father"], False),
#         ("is_scd", "Severe Chronic Disease", ["child"], False),
#         ("education_level", "Education", ["mother", "father"], False),
#         # Numeric variables (is_numeric=True)
#         ("salary_income", "Salary", ["mother", "father"], True),
#         ("personal_income", "Total Income", ["mother", "father"], True),
#     ]

#     # Calculate all distributions
#     distributions = []
#     for column, metric_name, roles, is_numeric in metrics:
#         df = calculate_distribution(combined_data, column, roles, is_numeric)
#         df = df.with_columns(pl.lit(metric_name).alias("Metric"))
#         distributions.append(df)

#     # Combine all results and format
#     return (
#         pl.concat(distributions)
#         .select(["Metric", "Category", "child", "mother", "father"])
#         .with_columns([pl.exclude(["Metric", "Category"]).round(4)])
#         .collect()  # Collect at the very end
#     )


# def create_display_table(stats: pl.DataFrame, year: int) -> GT:
#     """Create a formatted display table from the statistics DataFrame."""

#     # Identify different types of metrics for formatting
#     income_metrics = ["Salary", "Total Income"]
#     parent_percent_metrics = [
#         "Gender",
#         "Civil Status",
#         "Citizenship",
#         "Socioeconomic Status",
#         "Education",
#         "Living Status",
#     ]
#     child_percent_metrics = ["Gender", "Living Status", "Severe Chronic Disease"]

#     # Function to format category values
#     def format_category(s: str) -> str:
#         if s == "None":
#             return "Not Available"
#         elif s.endswith("_mean"):
#             return "Average"
#         return s

#     # Clean up the stats DataFrame
#     stats = stats.with_columns(
#         [pl.col("Category").map_elements(format_category, return_dtype=pl.Utf8)]
#     )

#     # Get row indices for different metric types using row_idx
#     income_rows = list(
#         stats.with_row_index()
#         .filter(pl.col("Metric").is_in(income_metrics))
#         .get_column("index")
#     )

#     parent_percent_rows = list(
#         stats.with_row_index()
#         .filter(pl.col("Metric").is_in(parent_percent_metrics))
#         .get_column("index")
#     )

#     child_percent_rows = list(
#         stats.with_row_index()
#         .filter(pl.col("Metric").is_in(child_percent_metrics))
#         .get_column("index")
#     )

#     role_sel = cs.by_name("child", "mother", "father")
#     parent_sel = cs.by_name("mother", "father")
#     # case_sel = cs.boolean()

#     # Color palette
#     colors = {
#         "header_bg": "#2C3E50",  # Dark blue-gray
#         "header_fg": "#FFFFFF",  # White
#         "income_bg": "#EBF5FB",  # Light blue
#         "stripe_bg": "#F8F9FA",  # Light gray
#         "border": "#BDC3C7",  # Gray
#         "highlight": "#3498DB",  # Blue
#     }

#     # Create table
#     table = (
#         GT(stats)
#         .tab_header(
#             title=md(f"**Population Characteristics by Role ({year})**"),
#             subtitle="Distribution of demographic and socioeconomic characteristics",
#         )
#         .tab_spanner(
#             label=md("**Distribution (%)**"),
#             columns=role_sel,
#         )
#         .tab_stub(rowname_col="Category", groupname_col="Metric")
#         .tab_stubhead(label=md("**Characteristic**"))
#         .cols_label(
#             Metric=md("**Characteristic**"),
#             Category=md("**Category**"),
#             child=md("**Child**"),
#             mother=md("**Mother**"),
#             father=md("**Father**"),
#         )
#         # Format percentages and numbers
#         .fmt_percent(
#             columns=parent_sel,
#             decimals=1,
#             rows=parent_percent_rows,
#             sep_mark=".",
#             dec_mark=",",
#         )
#         .fmt_percent(
#             columns=["child"],
#             decimals=1,
#             rows=child_percent_rows,
#             sep_mark=".",
#             dec_mark=",",
#         )
#         .fmt_currency(
#             columns=["child", "mother", "father"],
#             decimals=0,
#             rows=income_rows,
#             # sep_mark=".",
#             # dec_mark=",",
#             currency="DKK",
#         )
#         # Style headers
#         .tab_style(
#             style=[
#                 style.fill(color=colors["header_bg"]),
#                 style.text(color=colors["header_fg"]),
#                 style.text(weight="bold"),
#             ],
#             locations=loc.column_labels(),
#         )
#         # Style column spanners
#         .tab_style(
#             style=[
#                 style.fill(color=colors["header_bg"]),
#                 style.text(color=colors["header_fg"]),
#                 style.text(weight="bold"),
#             ],
#             locations=loc.column_header(),
#         )
#         # Style metric names
#         .tab_style(
#             style=[style.text(weight="bold"), style.text(color=colors["header_bg"])],
#             locations=loc.body(columns="Metric"),
#         )
#         # Style income rows
#         .tab_style(
#             style=style.fill(color=colors["income_bg"]),
#             locations=loc.body(rows=income_rows),
#         )
#         .sub_missing(missing_text="")
#         # Add borders
#         .tab_style(
#             style=style.borders(sides="bottom", weight="1px", color=colors["border"]),
#             locations=loc.body(),
#         )
#         # Add footnotes
#         .tab_source_note(
#             source_note=md("**Source:** Statistics Denmark, Administrative Data")
#         )
#         .tab_source_note(
#             source_note=md("**Note:** Income values are in thousands (DKK)")
#         )
#         .tab_source_note(source_note=f"Reference year: {year}")
#         # Layout options
#         .tab_options(
#             row_striping_background_color="lightblue",
#             row_striping_include_stub=True,
#             row_striping_include_table_body=True,
#         )
#         .opt_vertical_padding(scale=0.85)
#         .opt_horizontal_padding(scale=1.1)
#         .opt_table_font(font=["Helvetica Neue", "Helvetica", "Arial", "sans-serif"])
#     )

#     return table


# def calculate_comparison_distribution(
#     combined_data: pl.LazyFrame, reference_year: int
# ) -> pl.DataFrame:
#     """Calculate distributions for cases and controls in a comparison format."""
#     # First identify families with SCD (cases) and without (controls)
#     scd_families = (
#         combined_data.filter(pl.col("is_scd"))
#         .select(pl.col("family_id"))
#         .unique()
#         .collect()
#         .get_column("family_id")
#     )

#     cases = combined_data.filter(pl.col("family_id").is_in(scd_families))
#     controls = combined_data.filter(~pl.col("family_id").is_in(scd_families))

#     def calculate_stats(
#         data: pl.LazyFrame, column: str, role: str, reference_year: int
#     ) -> dict:
#         """Calculate statistics for a given column and role."""
#         filtered_data = data.filter(pl.col("role") == role)

#         if column == "birth_date":
#             # Convert birth_date to age in years
#             stats_df = (
#                 filtered_data.with_columns(
#                     [
#                         (
#                             (
#                                 pl.lit(f"{reference_year}-12-31").str.strptime(
#                                     pl.Date, "%Y-%m-%d"
#                                 )
#                                 - pl.col("birth_date")
#                             ).dt.total_days()
#                             / 365.25
#                         ).alias("age_years")
#                     ]
#                 )
#                 .select(
#                     [
#                         pl.col("age_years").mean().alias("mean"),
#                         pl.col("age_years").std().alias("sd"),
#                         pl.len().alias("n"),
#                     ]
#                 )
#                 .collect()
#             )
#         else:
#             stats_df = filtered_data.select(
#                 [
#                     pl.col(column).mean().alias("mean"),
#                     pl.col(column).std().alias("sd"),
#                     pl.len().alias("n"),
#                 ]
#             ).collect()

#         return {
#             "mean": stats_df["mean"][0],
#             "sd": stats_df["sd"][0],
#             "n": stats_df["n"][0],
#         }

#     # Helper function to calculate percentages
#     def calculate_percentage(
#         data: pl.LazyFrame, column: str, value: str, role: str
#     ) -> float:
#         filtered_data = data.filter(pl.col("role") == role)
#         total = filtered_data.select(pl.len()).collect().item()
#         count = (
#             filtered_data.filter(pl.col(column) == value)
#             .select(pl.len())
#             .collect()
#             .item()
#         )
#         return (count / total * 100) if total > 0 else 0

#     # Build comparison rows
#     rows = []

#     # Child Characteristics
#     child_age_cases = calculate_stats(cases, "birth_date", "child", reference_year)
#     child_age_controls = calculate_stats(
#         controls, "birth_date", "child", reference_year
#     )

#     rows.extend(
#         [
#             {
#                 "group": "Child Characteristics",
#                 "characteristic": "Age, years",
#                 "cases": f"{child_age_cases['mean']:.1f} ± {child_age_cases['sd']:.1f}",
#                 "controls": f"{child_age_controls['mean']:.1f} ± {child_age_controls['sd']:.1f}",
#             },
#             {
#                 "group": "Child Characteristics",
#                 "characteristic": "Sex",
#                 "cases": "",
#                 "controls": "",
#             },
#             {
#                 "group": "Child Characteristics",
#                 "characteristic": "- Female",
#                 "cases": f"{calculate_percentage(cases, 'gender', 'F', 'child'):.1f}",
#                 "controls": f"{calculate_percentage(controls, 'gender', 'F', 'child'):.1f}",
#             },
#             {
#                 "group": "Child Characteristics",
#                 "characteristic": "- Male",
#                 "cases": f"{calculate_percentage(cases, 'gender', 'M', 'child'):.1f}",
#                 "controls": f"{calculate_percentage(controls, 'gender', 'M', 'child'):.1f}",
#             },
#         ]
#     )

#     # Parent Characteristics
#     for parent_role in ["mother", "father"]:
#         parent_age_cases = calculate_stats(
#             cases, "birth_date", parent_role, reference_year
#         )
#         parent_age_controls = calculate_stats(
#             controls, "birth_date", parent_role, reference_year
#         )

#         rows.extend(
#             [
#                 {
#                     "group": "Parent Characteristics",
#                     "characteristic": f"{parent_role.title()} age, years",
#                     "cases": f"{parent_age_cases['mean']:.1f} ± {parent_age_cases['sd']:.1f}",
#                     "controls": f"{parent_age_controls['mean']:.1f} ± {parent_age_controls['sd']:.1f}",
#                 }
#             ]
#         )

#     # Education levels
#     for parent_role in ["mother", "father"]:
#         rows.extend(
#             [
#                 {
#                     "group": "Parent Characteristics",
#                     "characteristic": f"{parent_role.title()} education",
#                     "cases": "",
#                     "controls": "",
#                 }
#             ]
#         )
#         for level in ["Basic Education", "Upper Secondary", "Short-cycle Tertiary"]:
#             rows.append(
#                 {
#                     "group": "Parent Characteristics",
#                     "characteristic": f"- {level}",
#                     "cases": f"{calculate_percentage(cases, 'education_group', level, parent_role):.1f}",
#                     "controls": f"{calculate_percentage(controls, 'education_group', level, parent_role):.1f}",
#                 }
#             )

#     # Family Characteristics
#     family_size_cases = calculate_stats(
#         cases, "children_in_family", "child", reference_year
#     )
#     family_size_controls = calculate_stats(
#         controls, "children_in_family", "child", reference_year
#     )

#     rows.extend(
#         [
#             {
#                 "group": "Family Characteristics",
#                 "characteristic": "Number of children",
#                 "cases": f"{family_size_cases['mean']:.1f} ± {family_size_cases['sd']:.1f}",
#                 "controls": f"{family_size_controls['mean']:.1f} ± {family_size_controls['sd']:.1f}",
#             },
#             {
#                 "group": "Family Characteristics",
#                 "characteristic": "Family structure",
#                 "cases": "",
#                 "controls": "",
#             },
#             {
#                 "group": "Family Characteristics",
#                 "characteristic": "- Two-parent household",
#                 "cases": f"{calculate_percentage(cases, 'family_type', '21', 'child'):.1f}",
#                 "controls": f"{calculate_percentage(controls, 'family_type', '21', 'child'):.1f}",
#             },
#             {
#                 "group": "Family Characteristics",
#                 "characteristic": "- Single-parent household",
#                 "cases": f"{calculate_percentage(cases, 'family_type', '22', 'child'):.1f}",
#                 "controls": f"{calculate_percentage(controls, 'family_type', '22', 'child'):.1f}",
#             },
#         ]
#     )

#     return pl.DataFrame(rows)


# def create_comparison_table(stats: pl.DataFrame, year: int) -> GT:
#     """Create a formatted comparison table."""
#     # Get counts
#     n_cases = stats.filter(pl.col("characteristic") == "Number of children")[
#         "cases"
#     ].item()
#     n_controls = stats.filter(pl.col("characteristic") == "Number of children")[
#         "controls"
#     ].item()

#     table = (
#         GT(stats)
#         .tab_header(
#             title=md(f"**Table 1. Characteristics of Cases and Controls ({year})**"),
#             subtitle="Comparison between families with and without SCD",
#         )
#         .tab_spanner(label=md(f"**Cases (n={n_cases})**"), columns="cases")
#         .tab_spanner(label=md(f"**Controls (n={n_controls})**"), columns="controls")
#         .cols_label(
#             group=md("**Group**"),
#             characteristic=md("**Characteristic**"),
#             # cases="**Value**",
#             controls=md("**Value**"),
#         )
#         .tab_stub(groupname_col="group", rowname_col="characteristic")
#         .fmt_number(
#             columns=["cases", "controls"],
#             decimals=1,
#         )
#         .tab_style(style=style.text(weight="bold"), locations=loc.row_groups())
#         .tab_source_note(
#             source_note=md("**Source:** Statistics Denmark, Administrative Data")
#         )
#     )

#     return table


# def create_family_tables(stats: pl.DataFrame, year: int) -> dict[str, GT]:
#     """Create three themed tables from the statistics DataFrame."""

#     # Helper function to format category values
#     def format_category(s: str) -> str:
#         if s == "None":
#             return "Not Available"
#         elif s.endswith("_mean"):
#             return "Average"
#         return s

#     # Clean the stats DataFrame
#     stats = stats.with_columns(
#         [pl.col("Category").map_elements(format_category, return_dtype=pl.Utf8)]
#     )

#     # Split data into themes
#     demographic_metrics = ["Gender", "Living Status", "Civil Status", "Citizenship"]
#     socioeconomic_metrics = [
#         "Education",
#         "Socioeconomic Status",
#         "Salary",
#         "Total Income",
#     ]
#     health_metrics = ["Severe Chronic Disease"]

#     demographic_stats = stats.filter(pl.col("Metric").is_in(demographic_metrics))
#     socioeconomic_stats = stats.filter(pl.col("Metric").is_in(socioeconomic_metrics))
#     health_stats = stats.filter(pl.col("Metric").is_in(health_metrics))

#     # Create tables
#     tables = {
#         "demographics": create_demographic_table(demographic_stats, year),
#         "socioeconomic": create_socioeconomic_table(socioeconomic_stats, year),
#         "health": create_health_table(health_stats, year),
#     }

#     return tables


# def create_demographic_table(stats: pl.DataFrame, year: int) -> GT:
#     """Create table focusing on core demographics."""

#     # Get row indices for percentage formatting
#     percent_rows = list(range(len(stats)))

#     table = (
#         GT(stats)
#         .tab_header(
#             title=md(f"**Demographic Characteristics ({year})**"),
#             subtitle="Distribution of core demographic characteristics by family role",
#         )
#         .tab_spanner(
#             label=md("**Distribution (%)**"), columns=["child", "mother", "father"]
#         )
#         .cols_label(
#             Metric=md("**Characteristic**"),
#             Category=md("**Category**"),
#             child=md("**Child**"),
#             mother=md("**Mother**"),
#             father=md("**Father**"),
#         )
#         .fmt_percent(
#             columns=["child", "mother", "father"],
#             decimals=1,
#             rows=percent_rows,
#             sep_mark=".",
#             dec_mark=",",
#         )
#         # .apply_theme_minimal()
#         .tab_style(
#             style=[
#                 style.text(size="20px", font=google_font("IBM Plex Sans")),
#                 style.fill(color="#2E86C1"),
#                 style.text(color="white"),
#             ],
#             locations=loc.title(),
#         )
#         .tab_source_note(
#             source_note=md("**Source:** Statistics Denmark, Administrative Data")
#         )
#         .tab_source_note(source_note=f"Reference year: {year}")
#     )

#     return table


# def create_socioeconomic_table(stats: pl.DataFrame, year: int) -> GT:
#     """Create table focusing on socioeconomic status."""

#     # Identify income rows for currency formatting
#     income_rows = list(
#         stats.with_row_index()
#         .filter(pl.col("Metric").is_in(["Salary", "Total Income"]))
#         .get_column("index")
#     )

#     # Get other rows for percentage formatting
#     percent_rows = list(
#         stats.with_row_index()
#         .filter(pl.col("Metric").is_in(["Education", "Socioeconomic Status"]))
#         .get_column("index")
#     )

#     table = (
#         GT(stats)
#         .tab_header(
#             title=md(f"**Socioeconomic Status ({year})**"),
#             subtitle="Distribution of education, employment, and income by family role",
#         )
#         .tab_spanner(
#             label=md("**Distribution**"), columns=["child", "mother", "father"]
#         )
#         .cols_label(
#             Metric=md("**Characteristic**"),
#             Category=md("**Category**"),
#             child=md("**Child**"),
#             mother=md("**Mother**"),
#             father=md("**Father**"),
#         )
#         .fmt_percent(
#             columns=["mother", "father"],
#             decimals=1,
#             rows=percent_rows,
#             sep_mark=".",
#             dec_mark=",",
#         )
#         .fmt_currency(
#             columns=["child", "mother", "father"],
#             decimals=0,
#             rows=income_rows,
#             sep_mark=".",
#             dec_mark=",",
#             currency="DKK",
#         )
#         # .apply_theme_minimal()
#         .tab_style(
#             style=[
#                 style.text(size="20px", font=google_font("IBM Plex Sans")),
#                 style.fill(color="#27AE60"),
#                 style.text(color="white"),
#             ],
#             locations=loc.title(),
#         )
#         .tab_source_note(
#             source_note=md("**Source:** Statistics Denmark, Administrative Data")
#         )
#         .tab_source_note(
#             source_note=md("**Note:** Income values are in thousands (DKK)")
#         )
#         .tab_source_note(source_note=f"Reference year: {year}")
#     )

#     return table


# def create_health_table(stats: pl.DataFrame, year: int) -> GT:
#     """Create table focusing on health status."""

#     # Get row indices for percentage formatting
#     percent_rows = list(range(len(stats)))

#     table = (
#         GT(stats)
#         .tab_header(
#             title=md(f"**Health Status ({year})**"),
#             subtitle="Distribution of health indicators by family role",
#         )
#         .tab_spanner(
#             label=md("**Distribution (%)**"), columns=["child", "mother", "father"]
#         )
#         .cols_label(
#             Metric=md("**Characteristic**"),
#             Category=md("**Category**"),
#             child=md("**Child**"),
#             mother=md("**Mother**"),
#             father=md("**Father**"),
#         )
#         .fmt_percent(
#             columns=["child", "mother", "father"],
#             decimals=1,
#             rows=percent_rows,
#             sep_mark=".",
#             dec_mark=",",
#         )
#         # .apply_theme_minimal()
#         .tab_style(
#             style=[
#                 style.text(size="20px", font=google_font("IBM Plex Sans")),
#                 style.fill(color="#8E44AD"),
#                 style.text(color="white"),
#             ],
#             locations=loc.title(),
#         )
#         .tab_source_note(
#             source_note=md("**Source:** Statistics Denmark, Administrative Data")
#         )
#         .tab_source_note(source_note=f"Reference year: {year}")
#     )

#     return table


# def save_table_as_html(table, output_path: str) -> tuple[str, str | None]:
#     """
#     Save a GT table as an HTML file with proper encoding.
#     If a file with the same name exists, renames the existing file by adding a number.

#     Args:
#         table: The GT table object to save
#         output_path: Path where the HTML file should be saved

#     Returns:
#         tuple[str, str | None]: Tuple containing:
#             - Path where the new file was saved
#             - Path where the old file was moved (None if no file existed)
#     """
#     import re
#     from pathlib import Path

#     # Convert to Path object
#     path = Path(output_path)
#     old_file_path = None

#     if path.exists():
#         # Split into stem and suffix
#         stem = path.stem
#         suffix = path.suffix
#         parent = path.parent

#         # Find next available number for the old file
#         counter = 1
#         while True:
#             # Check if stem already ends with a number in parentheses
#             match = re.match(r"(.*?)\s*\((\d+)\)$", stem)
#             if match:
#                 # If it does, increment that number
#                 base_stem = match.group(1)
#                 new_old_path = parent / f"{base_stem} ({counter}){suffix}"
#             else:
#                 # If it doesn't, add the number
#                 new_old_path = parent / f"{stem} ({counter}){suffix}"

#             if not new_old_path.exists():
#                 # Rename the existing file
#                 path.rename(new_old_path)
#                 old_file_path = str(new_old_path)
#                 break

#             counter += 1

#     # Save the new file with the original name
#     with open(path, "w", encoding="utf-8") as f:
#         html_with_encoding = (
#             "<!DOCTYPE html>\n"
#             "<html>\n"
#             "<head>\n"
#             '<meta charset="utf-8">\n'
#             "</head>\n"
#             "<body>\n"
#             f"{table.as_raw_html()}\n"
#             "</body>\n"
#             "</html>"
#         )
#         f.write(html_with_encoding)

#     return str(path), old_file_path


# def main():
#     # Initialize the data loader
#     base_path = Path("/Users/tobiaskragholm/dev/backup_data/data")
#     mappings_dir = Path(
#         "/Users/tobiaskragholm/dev/cdef-cohort/src/cdef_cohort/mappings"
#     )
#     loader = AnalyticalDataLoader(base_path / "analytical_data")

#     # Get available years
#     latest_year = max(loader.get_available_years("demographics"))

#     # Create detailed statistics
#     detailed_stats = create_detailed_role_distribution(
#         loader=loader, year=latest_year, mappings_dir=mappings_dir
#     )

#     # Create and display the formatted table
#     # dummy_data = generate_dummy_data(1000).collect()
#     stats_table, df_with_income = create_descriptive_table(detailed_stats)
#     df_with_income.collect().write_csv("df_with_income.tsv", separator="\t")
#     formatted_table = format_descriptive_table(stats_table)
#     save_table_as_html(formatted_table, "formatted_table.html")

#     # comparison_stats = calculate_comparison_distribution(detailed_stats, latest_year)

#     # Create comparison table
#     # comparison_table = create_comparison_table(comparison_stats, latest_year)

#     # Save comparison table
#     # save_table_as_html(comparison_table, "comparison_table.html")


# if __name__ == "__main__":
#     main()
