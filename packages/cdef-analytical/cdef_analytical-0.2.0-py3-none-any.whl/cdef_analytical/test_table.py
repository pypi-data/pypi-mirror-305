import datetime
import math

import numpy as np
import polars as pl
from great_tables import GT, loc, style


def generate_dummy_data(n_families=1000):
    # Set random seed for reproducibility
    np.random.seed(42)

    # Generate family IDs
    family_ids = list(range(1, n_families + 1))

    # Helper function to generate random dates
    def random_date(start_year: int, end_year: int) -> datetime.date:
        """Generate a random date between start_year and end_year."""
        # Define start and end dates
        start = datetime.date(start_year, 1, 1)
        end = datetime.date(end_year, 12, 31)

        # Calculate the number of days between the start and end dates
        days_between = (end - start).days

        # Generate a random number of days to add to the start date
        random_days = np.random.randint(0, days_between)

        # Return start date plus random days
        return start + datetime.timedelta(days=random_days)

    # Lists to store data
    data = []

    for family_id in family_ids:
        # Generate parent data
        for role in ["mother", "father"]:
            birth_date = random_date(1960, 1990)

            record = {
                "individual_id": f"{family_id}_{role}",
                "birth_date": birth_date,
                "role": role,
                "gender": "F" if role == "mother" else "M",
                "parental_marking": np.random.choice(
                    ["1", "2", "3"], p=[0.8, 0.15, 0.05]
                ),
                "children_in_family": np.random.randint(1, 5),
                "family_type": str(np.random.randint(1, 5)),
                "family_id": family_id,
                "martial_status": np.random.choice(
                    ["G", "U", "F", "E"], p=[0.7, 0.15, 0.1, 0.05]
                ),
                "citizenship": np.random.choice(
                    ["5100", "5120", "5110"], p=[0.85, 0.1, 0.05]
                ),
                "education_level": str(np.random.randint(1, 8)),
                "personal_income": np.random.normal(400000, 100000),
                "salary_income": np.random.normal(350000, 80000),
                "education_group": np.random.choice(
                    [
                        "Basic Education",
                        "Upper Secondary",
                        "Short-cycle Tertiary",
                        "Bachelor's or equivalent",
                        "Master's or equivalent",
                        "Doctoral or equivalent",
                    ]
                ),
            }
            data.append(record)

        # Generate child data (1-3 children per family)
        n_children = np.random.randint(1, 4)
        for i in range(n_children):
            birth_date = random_date(2000, 2020)

            record = {
                "individual_id": f"{family_id}_child_{i}",
                "birth_date": birth_date,
                "role": "child",
                "gender": np.random.choice(["M", "F"]),
                "parental_marking": "1",
                "children_in_family": n_children,
                "family_type": str(np.random.randint(1, 5)),
                "family_id": family_id,
                "martial_status": "U",
                "citizenship": "5100",
                "personal_income": 0,
                "salary_income": 0,
                "is_scd": bool(np.random.choice([True, False], p=[0.05, 0.95])),
                "first_scd_date": random_date(2015, 2023)
                if np.random.random() < 0.05
                else None,
            }
            data.append(record)

    # Convert to Polars DataFrame with explicit schema
    df = pl.DataFrame(
        data,
        schema={
            "individual_id": pl.Utf8,
            "birth_date": pl.Date,
            "role": pl.Utf8,
            "gender": pl.Utf8,
            "parental_marking": pl.Utf8,
            "children_in_family": pl.Int32,
            "family_type": pl.Utf8,
            "family_id": pl.Int32,
            "martial_status": pl.Utf8,
            "citizenship": pl.Utf8,
            "education_level": pl.Utf8,
            "personal_income": pl.Float64,
            "salary_income": pl.Float64,
            "is_scd": pl.Boolean,
            "first_scd_date": pl.Date,
            "education_group": pl.Utf8,
        },
    )

    return df.lazy()


def create_descriptive_table(df):
    # Calculate income quartiles for mothers and fathers separately
    mother_income = df.filter(pl.col("role") == "mother").with_columns(
        pl.col("salary_income")
        .qcut(
            quantiles=4, labels=["Q1 (<25%)", "Q2 (25-50%)", "Q3 (50-75%)", "Q4 (>75%)"]
        )
        .alias("mother_income_category")
    )

    father_income = df.filter(pl.col("role") == "father").with_columns(
        pl.col("salary_income")
        .qcut(
            quantiles=4, labels=["Q1 (<25%)", "Q2 (25-50%)", "Q3 (50-75%)", "Q4 (>75%)"]
        )
        .alias("father_income_category")
    )

    # Calculate household income
    household_income = (
        df.group_by("family_id")
        .agg(pl.col("salary_income").sum().alias("total_household_income"))
        .with_columns(
            pl.col("total_household_income")
            .qcut(
                quantiles=4,
                labels=["Q1 (<25%)", "Q2 (25-50%)", "Q3 (50-75%)", "Q4 (>75%)"],
            )
            .alias("household_income_category")
        )
    )

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

    # print("Income Dataframe:")
    # print(df_with_income.collect_schema.names())
    # print(df_with_income.collect())

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

    return stats


def create_readable_table(stats_df):
    def format_value(value, type_="percent"):
        """Format values as percentage or currency."""
        if not isinstance(value, (int, float)) or (
            isinstance(value, float) and math.isnan(value)
        ):
            return ""
        if type_ == "percent":
            return f"{value * 100:.1f}%"
        if type_ == "currency":
            return f"{value:,.0f} DKK"
        if type_ == "count":
            return str(int(value))
        return str(value)

    def extract_stats(df, is_case: bool):
        """Extract statistics for either cases or controls."""
        data = df.filter(pl.col("is_scd") if is_case else ~pl.col("is_scd"))
        row = data.select(
            [
                # Child statistics
                pl.col("n_children").alias("total_children"),
                (pl.col("n_female_children") / pl.col("n_children")).alias(
                    "female_children_pct"
                ),
                (pl.col("n_male_children") / pl.col("n_children")).alias(
                    "male_children_pct"
                ),
                # Mother statistics
                (pl.col("mother_edu_basic") / pl.col("n_children")).alias(
                    "mother_basic_pct"
                ),
                (pl.col("mother_edu_upper_sec") / pl.col("n_children")).alias(
                    "mother_upper_sec_pct"
                ),
                (pl.col("mother_edu_short_tert") / pl.col("n_children")).alias(
                    "mother_short_tert_pct"
                ),
                (pl.col("mother_edu_bachelor") / pl.col("n_children")).alias(
                    "mother_bachelor_pct"
                ),
                (pl.col("mother_edu_master") / pl.col("n_children")).alias(
                    "mother_master_pct"
                ),
                (pl.col("mother_edu_doctoral") / pl.col("n_children")).alias(
                    "mother_doctoral_pct"
                ),
                (pl.col("mother_income_q1") / pl.col("n_children")).alias(
                    "mother_income_q1_pct"
                ),
                (pl.col("mother_income_q2") / pl.col("n_children")).alias(
                    "mother_income_q2_pct"
                ),
                (pl.col("mother_income_q3") / pl.col("n_children")).alias(
                    "mother_income_q3_pct"
                ),
                (pl.col("mother_income_q4") / pl.col("n_children")).alias(
                    "mother_income_q4_pct"
                ),
                pl.col("mean_mother_income"),
                # Father statistics
                (pl.col("father_edu_basic") / pl.col("n_children")).alias(
                    "father_basic_pct"
                ),
                (pl.col("father_edu_upper_sec") / pl.col("n_children")).alias(
                    "father_upper_sec_pct"
                ),
                (pl.col("father_edu_short_tert") / pl.col("n_children")).alias(
                    "father_short_tert_pct"
                ),
                (pl.col("father_edu_bachelor") / pl.col("n_children")).alias(
                    "father_bachelor_pct"
                ),
                (pl.col("father_edu_master") / pl.col("n_children")).alias(
                    "father_master_pct"
                ),
                (pl.col("father_edu_doctoral") / pl.col("n_children")).alias(
                    "father_doctoral_pct"
                ),
                (pl.col("father_income_q1") / pl.col("n_children")).alias(
                    "father_income_q1_pct"
                ),
                (pl.col("father_income_q2") / pl.col("n_children")).alias(
                    "father_income_q2_pct"
                ),
                (pl.col("father_income_q3") / pl.col("n_children")).alias(
                    "father_income_q3_pct"
                ),
                (pl.col("father_income_q4") / pl.col("n_children")).alias(
                    "father_income_q4_pct"
                ),
                pl.col("mean_father_income"),
            ]
        ).row(0)
        # Create dictionary with correct keys
        return {
            "n_children": row[0],
            "female_children_pct": row[1],
            "male_children_pct": row[2],
            "mother_basic_pct": row[3],
            "mother_upper_sec_pct": row[4],
            "mother_short_tert_pct": row[5],
            "mother_bachelor_pct": row[6],
            "mother_master_pct": row[7],
            "mother_doctoral_pct": row[8],
            "mother_income_q1_pct": row[9],
            "mother_income_q2_pct": row[10],
            "mother_income_q3_pct": row[11],
            "mother_income_q4_pct": row[12],
            "mean_mother_income": row[13],
            "father_basic_pct": row[14],
            "father_upper_sec_pct": row[15],
            "father_short_tert_pct": row[16],
            "father_bachelor_pct": row[17],
            "father_master_pct": row[18],
            "father_doctoral_pct": row[19],
            "father_income_q1_pct": row[20],
            "father_income_q2_pct": row[21],
            "father_income_q3_pct": row[22],
            "father_income_q4_pct": row[23],
            "mean_father_income": row[24],
        }

    # Extract statistics
    cases = extract_stats(stats_df, True)
    controls = extract_stats(stats_df, False)

    # Define table structure with (label, data_key, format_type, row_type)
    table_structure = [
        # Child Characteristics
        ("Child Characteristics", None, None, "header"),
        ("Number of children", "n_children", "count", None),
        ("Sex distribution", None, None, "subheader"),
        ("- Female", "female_children_pct", "percent", None),
        ("- Male", "male_children_pct", "percent", None),
        # Maternal Characteristics
        ("Maternal Characteristics", None, None, "header"),
        ("Education", None, None, "subheader"),
        ("- Basic Education", "mother_basic_pct", "percent", None),
        ("- Upper Secondary", "mother_upper_sec_pct", "percent", None),
        ("- Short-cycle Tertiary", "mother_short_tert_pct", "percent", None),
        ("- Bachelor's degree", "mother_bachelor_pct", "percent", None),
        ("- Master's degree", "mother_master_pct", "percent", None),
        ("- Doctoral degree", "mother_doctoral_pct", "percent", None),
        ("Income distribution", None, None, "subheader"),
        ("- Q1 (<25th percentile)", "mother_income_q1_pct", "percent", None),
        ("- Q2 (25-50th percentile)", "mother_income_q2_pct", "percent", None),
        ("- Q3 (50-75th percentile)", "mother_income_q3_pct", "percent", None),
        ("- Q4 (>75th percentile)", "mother_income_q4_pct", "percent", None),
        ("Mean annual income", "mean_mother_income", "currency", None),
        # Paternal Characteristics
        ("Paternal Characteristics", None, None, "header"),
        ("Education", None, None, "subheader"),
        ("- Basic Education", "father_basic_pct", "percent", None),
        ("- Upper Secondary", "father_upper_sec_pct", "percent", None),
        ("- Short-cycle Tertiary", "father_short_tert_pct", "percent", None),
        ("- Bachelor's degree", "father_bachelor_pct", "percent", None),
        ("- Master's degree", "father_master_pct", "percent", None),
        ("- Doctoral degree", "father_doctoral_pct", "percent", None),
        ("Income distribution", None, None, "subheader"),
        ("- Q1 (<25th percentile)", "father_income_q1_pct", "percent", None),
        ("- Q2 (25-50th percentile)", "father_income_q2_pct", "percent", None),
        ("- Q3 (50-75th percentile)", "father_income_q3_pct", "percent", None),
        ("- Q4 (>75th percentile)", "father_income_q4_pct", "percent", None),
        ("Mean annual income", "mean_father_income", "currency", None),
    ]

    # Create table data
    table_data = {"Characteristic": [], "Cases": [], "Controls": []}

    # Fill in values
    for label, data_key, format_type, row_type in table_structure:
        table_data["Characteristic"].append(label)

        if row_type in ("header", "subheader"):
            table_data["Cases"].append("")
            table_data["Controls"].append("")
        else:
            table_data["Cases"].append(format_value(cases[data_key], format_type))
            table_data["Controls"].append(format_value(controls[data_key], format_type))

    print(table_data)
    # Create and format table
    header_rows = [i for i, (_, _, _, t) in enumerate(table_structure) if t == "header"]

    return (
        GT(pl.DataFrame(table_data))
        .tab_header(
            title="Table 1. Participant Characteristics",
            subtitle="Distribution of demographic and socioeconomic characteristics",
        )
        .tab_style(style.text(weight="bold"), loc.body(rows=header_rows))
        .cols_label(
            Characteristic="Characteristic",
            Cases=f"Cases (n={format_value(cases['n_children'], 'count')})",
            Controls=f"Controls (n={format_value(controls['n_children'], 'count')})",
        )
    )


dummy_data = generate_dummy_data(n_families=100000)
stats_table = create_descriptive_table(dummy_data)

formatted_table = create_readable_table(stats_table.collect())
formatted_table.show("browser")
formatted_table.save("formatted_table.pdf", scale=4)
