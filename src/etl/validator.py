"""
validator.py

Validates loaded Excel datasets and generates a validation report.
"""

from pathlib import Path
import pandas as pd

from loader import load_excel


OUTPUT_DIR = Path("output")
OUTPUT_DIR.mkdir(exist_ok=True)

validation_results = []


def add_result(rule, status, issue, rows):
    validation_results.append({
        "Rule": rule,
        "Status": status,
        "Issue": issue,
        "Rows Affected": rows
    })


def check_required_columns(df, required_columns):

    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        add_result(
            "Required Columns",
            "Failed",
            f"Missing columns: {missing}",
            0
        )
    else:
        add_result(
            "Required Columns",
            "Passed",
            "All required columns present",
            0
        )


def check_missing_values(df):

    missing = df.isnull().sum()

    print("\nMissing Values by Column:")
    print(missing)

    total_missing = missing.sum()

    if total_missing > 0:
        add_result(
            "Missing Values",
            "Failed",
            "Missing values found",
            int(total_missing)
        )
    else:
        add_result(
            "Missing Values",
            "Passed",
            "No missing values",
            0
        )


def check_duplicate_rows(df):

    duplicates = df.duplicated().sum()

    if duplicates > 0:
        add_result(
            "Duplicate Rows",
            "Failed",
            "Duplicate rows detected",
            int(duplicates)
        )
    else:
        add_result(
            "Duplicate Rows",
            "Passed",
            "No duplicate rows",
            0
        )


def check_year_column(df):

    if "Year" not in df.columns:
        return

    invalid = df["Year"].isnull().sum()

    if invalid > 0:
        add_result(
            "Year Validation",
            "Failed",
            "Invalid year values",
            int(invalid)
        )
    else:
        add_result(
            "Year Validation",
            "Passed",
            "Year values are valid",
            0
        )


def check_ticker_column(df):

    if "Ticker" not in df.columns:
        return

    invalid = df["Ticker"].str.contains(" ").sum()

    if invalid > 0:
        add_result(
            "Ticker Validation",
            "Failed",
            "Ticker contains spaces",
            int(invalid)
        )
    else:
        add_result(
            "Ticker Validation",
            "Passed",
            "Ticker format valid",
            0
        )


def save_report():

    report = pd.DataFrame(validation_results)

    report.to_csv(
        OUTPUT_DIR / "validation_report.csv",
        index=False
    )

    print("\nValidation report saved:")
    print("output/validation_report.csv")


def validate_dataset(file_name):

    print(f"\nLoading {file_name}")

    df = load_excel(file_name)
    # Fill missing text values
    for col in ["company_logo", "website", "nse_profile", "bse_profile"]:
        if col in df.columns:
            df[col] = df[col].fillna("Not Available")
    for col in ["face_value", "book_value", "roce_percentage", "roe_percentage"]:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    if df is None:
        return

    required_columns = list(df.columns)
    check_required_columns(df, required_columns)
    check_missing_values(df)
    check_duplicate_rows(df)
    check_year_column(df)
    check_ticker_column(df)
    save_report()
    print("\nValidation Summary")
    print(pd.DataFrame(validation_results))

if __name__ == "__main__":

    validate_dataset("companies.xlsx")