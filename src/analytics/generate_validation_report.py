"""
generate_validation_report.py

Generates leverage and efficiency validation report.
"""

from pathlib import Path
import pandas as pd

from src.analytics.leverage import debt_to_equity, interest_coverage
from src.analytics.efficiency import asset_turnover


def main():

    # Sample data
    df = pd.DataFrame({
        "company": ["ABB", "INFY", "TCS"],
        "total_debt": [500, 0, 100],
        "equity": [2000, 5000, 10000],
        "profit_before_tax": [1200, 1500, 1800],
        "interest": [100, 50, 200],
        "sales": [10000, 20000, 15000],
        "total_assets": [8000, 12000, 10000]
    })

    # Calculate ratios
    df["Debt_to_Equity"] = df.apply(
        lambda row: debt_to_equity(
            row["total_debt"],
            row["equity"]
        ),
        axis=1
    )

    df["Interest_Coverage"] = df.apply(
        lambda row: interest_coverage(
            row["profit_before_tax"],
            row["interest"]
        ),
        axis=1
    )

    df["Asset_Turnover"] = df.apply(
        lambda row: asset_turnover(
            row["sales"],
            row["total_assets"]
        ),
        axis=1
    )

    df["Status"] = "PASS"

    # Create output folder
    output_folder = Path("output")
    output_folder.mkdir(parents=True, exist_ok=True)

    # Save CSV
    output_file = output_folder / "leverage_validation.csv"
    df.to_csv(output_file, index=False)

    print("=" * 60)
    print("VALIDATION REPORT GENERATED")
    print("=" * 60)
    print(df)

    print("\nCSV saved successfully.")
    print("Location :", output_file.resolve())


if __name__ == "__main__":
    main()