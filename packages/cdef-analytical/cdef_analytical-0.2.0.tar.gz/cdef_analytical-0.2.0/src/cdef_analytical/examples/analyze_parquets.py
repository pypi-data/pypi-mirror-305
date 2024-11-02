from pathlib import Path

from cdef_analytical.logging_config import create_logger
from cdef_analytical.parquet_analyzer import ParquetAnalyzer

logger = create_logger("parquet_analyzer_example")


def analyze_data_directory(data_dir: Path, output_dir: Path) -> None:
    try:
        # Initialize analyzer
        analyzer = ParquetAnalyzer(str(data_dir))

        # Scan directory
        analyzer.scan_directory()

        # Generate and save report
        output_dir.mkdir(parents=True, exist_ok=True)
        report_path = output_dir / "parquet_structure_report.txt"
        analyzer.save_report(str(report_path))

    except Exception as e:
        print(f"Analysis failed: {str(e)}")


def main() -> None:
    data_dir = Path("/Users/tobiaskragholm/dev/TEST/data")
    output_dir = Path("reports")
    analyze_data_directory(data_dir, output_dir)


if __name__ == "__main__":
    main()
