# from dataclasses import dataclass
# from enum import Enum
# from pathlib import Path
# from typing import List, Optional

# import polars as pl
# import polars.selectors as cs
# from great_tables import GT, loc, md, style

# from cdef_analytical.loaders.data_loader import AnalyticalDataLoader


# @dataclass
# class TableConfig:
#     year: int
#     education_levels = {
#         "high_school_or_less": ["10", "20", "25"],
#         "college_degree": ["30", "35", "40"],
#         "graduate_degree": ["50", "60", "70"],
#     }
#     income_quantiles = [0.2, 0.4, 0.6, 0.8]
#     income_labels = ["Q1", "Q2", "Q3", "Q4", "Q5"]

#     def get_income_categories(self, df: pl.DataFrame) -> pl.DataFrame:
#         """Calculate income categories using quantile binning."""
#         return df.select(
#             pl.col("personal_income")
#             .qcut(
#                 self.income_quantiles,
#                 labels=self.income_labels,
#                 include_breaks=True,
#             )
#             .alias("income_category")
#         )


# class Role(str, Enum):
#     CHILD = "child"
#     MATERNAL = "maternal"
#     PATERNAL = "paternal"
#     FAMILY = "family"


# class DataPreparation:
#     def __init__(self, loader, config: TableConfig):
#         self.loader = loader
#         self.config = config
#         self.prepare_base_data()

#     def prepare_base_data(self):
#         static_data = self.loader.get_static_data()
#         self.role_data = {
#             role: static_data.filter(pl.col("role") == role.value)
#             for role in [Role.CHILD, Role.MATERNAL, Role.PATERNAL]
#         }

#         self.scd_data = self.loader.get_scd_status().select(
#             ["individual_id", "is_scd", "first_scd_date"]
#         )

#         self.demographic_data = (
#             self.loader.get_longitudinal_data("demographics")
#             .filter(pl.col("year") == self.config.year)
#             .select(
#                 [
#                     pl.col("PNR").alias("individual_id"),
#                     pl.col("FOED_DAG").alias("birth_date"),
#                     pl.col("KOEN").alias("gender"),
#                     pl.col("FM_MARK").alias("parental_marking"),
#                     pl.col("ANTBOERNF").alias("children_in_family"),
#                     pl.col("FAMILIE_TYPE").alias("family_type"),
#                     pl.col("FAMILIE_ID").alias("family_id"),
#                 ]
#             )
#         )

#         self.education_data = (
#             self.loader.get_longitudinal_data("education")
#             .filter(pl.col("year") == self.config.year)
#             .select(
#                 [
#                     pl.col("PNR").alias("individual_id"),
#                     pl.col("HFAUDD").alias("education_level"),
#                 ]
#             )
#         )

#         self.income_data = (
#             self.loader.get_longitudinal_data("income")
#             .filter(pl.col("year") == self.config.year)
#             .select(
#                 [
#                     pl.col("PNR").alias("individual_id"),
#                     pl.col("PERINDKIALT_13").alias("personal_income"),
#                     pl.col("LOENMV_13").alias("salary_income"),
#                 ]
#             )
#         )

#     def get_group_data(
#         self, role: Role, is_scd: bool, extra_joins: Optional[List] = None
#     ):
#         base_query = (
#             self.role_data[role]
#             .join(
#                 self.scd_data.filter(pl.col("is_scd") if is_scd else ~pl.col("is_scd")),
#                 on="individual_id",
#             )
#             .join(self.demographic_data, on="individual_id")
#         )

#         if extra_joins:
#             for df in extra_joins:
#                 base_query = base_query.join(df, on="individual_id")

#         return base_query.collect()


# class CharacteristicsCalculator:
#     def __init__(self, cases_data, controls_data, config: TableConfig):
#         self.cases = cases_data
#         self.controls = controls_data
#         self.config = config

#     def calculate_basic_stats(self, column: str):
#         return {
#             "cases_mean": self.cases.select(pl.col(column).mean()).item(),
#             "cases_sd": self.cases.select(pl.col(column).std()).item(),
#             "controls_mean": self.controls.select(pl.col(column).mean()).item(),
#             "controls_sd": self.controls.select(pl.col(column).std()).item(),
#         }

#     def calculate_proportion(self, column: str, value):
#         return {
#             "cases": self.cases.select(pl.col(column).eq(value).mean()).item(),
#             "controls": self.controls.select(pl.col(column).eq(value).mean()).item(),
#         }

#     def calculate_age_stats(self, birth_date_col: str, reference_year: int):
#         """Calculate age statistics from birth dates."""

#         def calc_ages(df: pl.DataFrame) -> pl.DataFrame:
#             return df.select(
#                 (
#                     (
#                         pl.date(self.config.year, 12, 31) - pl.col(birth_date_col)
#                     ).dt.total_days()
#                     / 365.25
#                 ).alias("age")
#             )

#         cases_ages = calc_ages(self.cases)
#         controls_ages = calc_ages(self.controls)

#         return {
#             "cases_mean": cases_ages.select(pl.col("age").mean()).item(),
#             "cases_sd": cases_ages.select(pl.col("age").std()).item(),
#             "controls_mean": controls_ages.select(pl.col("age").mean()).item(),
#             "controls_sd": controls_ages.select(pl.col("age").std()).item(),
#         }

#     def calculate_income_distribution(self, role: Role):
#         """Calculate income distribution for a given role."""
#         cases_income = self.config.get_income_categories(self.cases)
#         controls_income = self.config.get_income_categories(self.controls)

#         rows = []
#         for quintile in self.config.income_labels:
#             cases_count = (
#                 cases_income.filter(pl.col("income_category") == quintile)
#                 .select(pl.len())
#                 .item()
#             )
#             controls_count = (
#                 controls_income.filter(pl.col("income_category") == quintile)
#                 .select(pl.len())
#                 .item()
#             )

#             total_cases = cases_income.select(pl.len()).item()
#             total_controls = controls_income.select(pl.len()).item()

#             rows.append(
#                 {
#                     "role": role,
#                     "characteristic": f"- {quintile}",
#                     "cases": cases_count / total_cases if total_cases > 0 else 0,
#                     "controls": controls_count / total_controls
#                     if total_controls > 0
#                     else 0,
#                 }
#             )
#         return rows


# class TableBuilder:
#     def __init__(self, data_prep: DataPreparation, config: TableConfig):
#         self.data_prep = data_prep
#         self.config = config
#         self.calculator = None  # Initialize in build method
#         self.parent_extra_joins = [
#             self.data_prep.education_data,
#             self.data_prep.income_data,
#         ]

#     def build(self) -> pl.DataFrame:
#         # Get data for each group
#         cases_children = self.data_prep.get_group_data(Role.CHILD, True)
#         controls_children = self.data_prep.get_group_data(Role.CHILD, False)

#         cases_mothers = self.data_prep.get_group_data(
#             Role.MATERNAL, True, self.parent_extra_joins
#         )
#         controls_mothers = self.data_prep.get_group_data(
#             Role.MATERNAL, False, self.parent_extra_joins
#         )

#         cases_fathers = self.data_prep.get_group_data(
#             Role.PATERNAL, True, self.parent_extra_joins
#         )
#         controls_fathers = self.data_prep.get_group_data(
#             Role.PATERNAL, False, self.parent_extra_joins
#         )

#         # Initialize calculators with config
#         child_calc = CharacteristicsCalculator(
#             cases_children, controls_children, self.config
#         )
#         mother_calc = CharacteristicsCalculator(
#             cases_mothers, controls_mothers, self.config
#         )
#         father_calc = CharacteristicsCalculator(
#             cases_fathers, controls_fathers, self.config
#         )

#         table_rows = [
#             # Child characteristics
#             # self._create_header_row(Role.CHILD, "child_characteristics"),
#             self._create_count_row(Role.CHILD, cases_children, controls_children),
#             {
#                 "role": Role.CHILD,
#                 "characteristic": "age",
#                 **child_calc.calculate_age_stats("birth_date", self.config.year),
#             },
#             # Child sex distribution
#             self._create_header_row(Role.CHILD, "sex_distribution"),
#             {
#                 "role": Role.CHILD,
#                 "characteristic": "female",
#                 **child_calc.calculate_proportion("gender", "2"),
#             },
#             {
#                 "role": Role.CHILD,
#                 "characteristic": "male",
#                 **child_calc.calculate_proportion("gender", "1"),
#             },
#             # Maternal characteristics
#             # self._create_header_row(Role.MATERNAL, "maternal_characteristics"),
#             {
#                 "role": Role.MATERNAL,
#                 "characteristic": "age",
#                 **mother_calc.calculate_age_stats("birth_date", self.config.year),
#             },
#             # Maternal education
#             self._create_header_row(Role.MATERNAL, "education"),
#             *self._create_education_rows(Role.MATERNAL, mother_calc),
#             # Maternal income
#             self._create_header_row(Role.MATERNAL, "income_distribution"),
#             *mother_calc.calculate_income_distribution(Role.MATERNAL),
#             # Paternal characteristics
#             {
#                 "role": Role.PATERNAL,
#                 "characteristic": "age",
#                 **father_calc.calculate_age_stats("birth_date", self.config.year),
#             },
#             # Paternal education
#             self._create_header_row(Role.PATERNAL, "education"),
#             *self._create_education_rows(Role.PATERNAL, father_calc),
#             # Paternal income
#             self._create_header_row(Role.PATERNAL, "income_distribution"),
#             *father_calc.calculate_income_distribution(Role.PATERNAL),
#             # Family characteristics
#             # self._create_header_row(Role.FAMILY, "family_characteristics"),
#             self._create_stats_row(Role.FAMILY, "children_in_family", child_calc),
#             # Family structure
#             self._create_header_row(Role.FAMILY, "family_structure"),
#             {
#                 "role": Role.FAMILY,
#                 "characteristic": "two-parent_household",
#                 **child_calc.calculate_proportion("family_type", "21"),
#             },
#             {
#                 "role": Role.FAMILY,
#                 "characteristic": "single-parent_household",
#                 **child_calc.calculate_proportion("family_type", "22"),
#             },
#         ]

#         return pl.DataFrame(table_rows)

#     def _create_education_rows(self, role: Role, calculator: CharacteristicsCalculator):
#         """Helper method to create education rows for a given role."""
#         return [
#             {
#                 "role": role,
#                 "characteristic": level_name,
#                 **calculator.calculate_proportion(
#                     "education_level", pl.col("education_level").is_in(level_codes)
#                 ),
#             }
#             for level_name, level_codes in self.config.education_levels.items()
#         ]

#     def _create_header_row(self, role: Role, characteristic: str):
#         return {
#             "role": role,
#             "characteristic": characteristic,
#             "cases": "",
#             "controls": "",
#         }

#     def _create_count_row(self, role: Role, cases_df, controls_df):
#         return {
#             "role": role,
#             "characteristic": "number_of_individuals",
#             "cases": cases_df.select(pl.col("individual_id").n_unique()).item(),
#             "controls": controls_df.select(pl.col("individual_id").n_unique()).item(),
#         }

#     def _create_stats_row(
#         self, role: Role, characteristic: str, calculator: CharacteristicsCalculator
#     ):
#         stats = calculator.calculate_basic_stats(characteristic)
#         return {"role": role, "characteristic": characteristic, **stats}

#         return pl.DataFrame(self.table_rows)


# def create_formatted_table(df: pl.DataFrame, n_cases: int, n_controls: int) -> GT:
#     sel_cases = cs.starts_with("cases")
#     sel_controls = cs.starts_with("controls")
#     table = (
#         GT(df)
#         .tab_header(
#             title=md("**Table 1. Participant Characteristics**"),
#             subtitle="Reference Year: 2024",
#         )
#         # Add table stub
#         .tab_stub(rowname_col="characteristic", groupname_col="role")
#         # Add column spanners
#         .tab_spanner(
#             label=md(f"**Cases (n={n_cases})**"),
#             columns=sel_cases,
#         )
#         .tab_spanner(
#             label=md(f"**Controls (n={n_controls})**"),
#             columns=sel_controls,
#         )
#         # Define column headers
#         .cols_label(
#             characteristic=md("**Characteristic**"),
#             # cases="Cases",
#             cases_mean="Mean",
#             cases_sd="SD",
#             # controls="Controls",
#             controls_mean="Mean",
#             controls_sd="SD",
#         )
#         # Format numeric columns
#         .fmt_number(
#             columns=["cases_mean", "controls_mean", "cases_sd", "controls_sd"],
#             decimals=1,
#             # missing_text="—",
#         )
#         # Format percentages
#         # .fmt_percent(
#         #     columns=["cases", "controls"],
#         #     decimals=1,
#         #     scale_values=True,
#         # )
#         # Style title
#         .tab_style(
#             style=style.text(color="blue", size="large", weight="bold"),
#             locations=loc.title(),
#         )
#         # Style subtitle
#         .tab_style(style=style.fill(color="lightblue"), locations=loc.subtitle())
#         # Style section headers
#         .tab_style(
#             style=style.fill(color="aliceblue"),
#             locations=loc.body(columns=sel_cases),
#         )
#         .tab_style(
#             style=style.fill(color="papayawhip"),
#             locations=loc.body(columns=sel_controls),
#         )
#         # Add borders
#         .tab_style(
#             style=style.borders(sides=["top", "bottom"], color="gray80", weight="1px"),
#             locations=loc.body(),
#         )
#         # Align columns
#         .cols_align(align="left", columns="characteristic")
#         .cols_align(
#             align="center",
#             columns=[
#                 "cases",
#                 "cases_mean",
#                 "cases_sd",
#                 "controls",
#                 "controls_mean",
#                 "controls_sd",
#             ],
#         )
#         .tab_source_note(
#             source_note=md("**Source:** Statistics Denmark, Administrative Data")
#         )
#     )
#     return table


# def main():
#     data_path = Path("/Users/tobiaskragholm/dev/backup_data/data/analytical_data/")
#     loader = AnalyticalDataLoader(data_path)

#     config = TableConfig(year=max(loader.get_available_years("demographics")))
#     data_prep = DataPreparation(loader, config)
#     table_builder = TableBuilder(data_prep, config)

#     table_df = table_builder.build()
#     formatted_table = create_formatted_table(table_df, n_cases=100, n_controls=100)

#     # Export table
#     with open("table_one.html", "w", encoding="utf-8") as f:
#         html_content = (
#             "<!DOCTYPE html>\n"
#             "<html>\n"
#             "<head>\n"
#             '<meta charset="utf-8">\n'
#             "</head>\n"
#             "<body>\n"
#             f"{formatted_table.as_raw_html()}\n"
#             "</body>\n"
#             "</html>"
#         )
#         f.write(html_content)


# if __name__ == "__main__":
#     main()
