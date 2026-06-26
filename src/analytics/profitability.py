"""
profitability.py

Sprint 2 - Day 8

Loads Profit & Loss and Balance Sheet data
from the SQLite database.
"""

import sqlite3
from pathlib import Path

import pandas as pd


# Database Path
DB_PATH = Path("db/nifty100.db")


def get_connection():
    """
    Create SQLite database connection.
    """

    conn = sqlite3.connect(DB_PATH)

    return conn


def load_profit_loss():
    """
    Load Profit & Loss table.
    """

    conn = get_connection()

    query = """
    SELECT
        company_id,
        year,
        sales,
        operating_profit,
        net_profit
    FROM profit_loss;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    print(f"\nProfit & Loss Records : {len(df)}")

    return df


def load_balance_sheet():
    """
    Load Balance Sheet table.
    """

    conn = get_connection()

    query = """
    SELECT
        company_id,
        year,
        equity_capital,
        reserves,
        borrowings,
        total_liabilities,
        total_assets
    FROM balance_sheet;
    """

    df = pd.read_sql(query, conn)

    conn.close()

    print(f"Balance Sheet Records : {len(df)}")

    return df
def merge_data(profit_loss_df, balance_sheet_df):
    """
    Merge Profit & Loss and Balance Sheet tables.
    """

    merged_df = pd.merge(
        profit_loss_df,
        balance_sheet_df,
        on=["company_id", "year"],
        how="inner"
    )

    print(f"\nMerged Records : {len(merged_df)}")

    return merged_df


def calculate_npm(df):
    """
    Net Profit Margin
    """

    df["npm"] = (
        df["net_profit"] / df["sales"]
    ) * 100

    return df


def calculate_opm(df):
    """
    Operating Profit Margin
    """

    df["calculated_opm"] = (
        df["operating_profit"] / df["sales"]
    ) * 100

    return df
def calculate_roe(df):
    """
    Calculate Return on Equity (ROE).
    """

    # Shareholders' Equity
    df["shareholders_equity"] = (
        df["equity_capital"] +
        df["reserves"]
    )

    # Avoid division by zero
    df["roe"] = (
        df["net_profit"] /
        df["shareholders_equity"]
    ) * 100

    return df


def calculate_roce(df):
    """
    Calculate Return on Capital Employed (ROCE).
    """

    # Capital Employed
    df["capital_employed"] = (
        df["equity_capital"] +
        df["reserves"] +
        df["borrowings"]
    )

    df["roce"] = (
        df["operating_profit"] /
        df["capital_employed"]
    ) * 100

    return df
def save_validation_report(df):
    """
    Save calculated profitability ratios to CSV.
    """

    output_file = "output/profitability_validation.csv"

    report = df[
        [
            "company_id",
            "year",
            "sales",
            "net_profit",
            "operating_profit",
            "npm",
            "calculated_opm",
            "roe",
            "roce"
        ]
    ]

    report.to_csv(output_file, index=False)

    print("\nValidation report generated successfully.")
    print(f"Location : {output_file}")

if __name__ == "__main__":

    print("=" * 60)
    print("PROFITABILITY RATIO ENGINE")
    print("=" * 60)

    profit_loss_df = load_profit_loss()

    balance_sheet_df = load_balance_sheet()

    merged_df = merge_data(
        profit_loss_df,
        balance_sheet_df
    )

    merged_df = calculate_npm(merged_df)

    merged_df = calculate_opm(merged_df)

    merged_df = calculate_roe(merged_df)

    merged_df = calculate_roce(merged_df)
    save_validation_report(merged_df) 

    print("\nCalculated Ratios")

    print(
    merged_df[
        [
            "company_id",
            "year",
            "npm",
            "calculated_opm",
            "roe",
            "roce"
        ]
    ].head()
)