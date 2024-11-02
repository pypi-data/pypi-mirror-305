import datetime

import numpy as np
import polars as pl


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
