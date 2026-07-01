"""
populate_financial_ratios.py

Sprint 2 - Day 12

Reads financial tables from SQLite,
calculates all financial ratios,
stores results into financial_ratios table.
"""

import sqlite3
import pandas as pd

from src.analytics.profitability import *
from src.analytics.leverage import *
from src.analytics.efficiency import *
from src.analytics.cashflow_kpis import *
from src.analytics.cagr import *

DB_PATH = "db/nifty100.db"


def main():

    conn = sqlite3.connect(DB_PATH)

    print("=" * 60)
    print("POPULATING FINANCIAL RATIOS")
    print("=" * 60)

    # -------------------------------
    # Read Tables
    # -------------------------------

    profit_loss = pd.read_sql(
        "SELECT * FROM profit_loss",
        conn
    )

    balance_sheet = pd.read_sql(
        "SELECT * FROM balance_sheet",
        conn
    )

    cash_flow = pd.read_sql(
        "SELECT * FROM cash_flow",
        conn
    )

    print(f"Profit & Loss Rows : {len(profit_loss)}")
    print(f"Balance Sheet Rows : {len(balance_sheet)}")
    print(f"Cash Flow Rows     : {len(cash_flow)}")

    # -------------------------------
    # Merge Tables
    # -------------------------------

    print("\nMerging tables...")

    merged_df = pd.merge(
        profit_loss,
        balance_sheet,
        on=["company_id", "year"],
        how="inner"
    )

    merged_df = pd.merge(
        merged_df,
        cash_flow,
        on=["company_id", "year"],
        how="inner"
    )

    print("Merge completed successfully.")

    print(f"Merged Rows    : {len(merged_df)}")
    print(f"Merged Columns : {len(merged_df.columns)}")

    print("\nCalculating Financial Ratios...")
        # ---------------------------------------
    # Profitability Ratios
    # ---------------------------------------

    merged_df = calculate_npm(merged_df)
    merged_df = calculate_opm(merged_df)
    merged_df = calculate_roe(merged_df)

    merged_df.rename(
        columns={
            "npm": "net_profit_margin_pct",
            "calculated_opm": "operating_profit_margin_pct",
            "roe": "return_on_equity_pct"
        },
        inplace=True
    )

    # ---------------------------------------
    # Leverage Ratios
    # ---------------------------------------

    merged_df["debt_to_equity"] = merged_df.apply(
        lambda row: debt_to_equity(
            row["borrowings"],
            row["equity_capital"] + row["reserves"]
        ),
        axis=1
    )

    merged_df["interest_coverage"] = merged_df.apply(
        lambda row: interest_coverage(
            row["profit_before_tax"],
            row["interest"]
        ),
        axis=1
    )

    # ---------------------------------------
    # Efficiency Ratios
    # ---------------------------------------

    merged_df["asset_turnover"] = merged_df.apply(
        lambda row: asset_turnover(
            row["sales"],
            row["total_assets"]
        ),
        axis=1
    )

    # ---------------------------------------
    # Cash Flow KPIs
    # ---------------------------------------

    merged_df["free_cash_flow_cr"] = merged_df.apply(
        lambda row: free_cash_flow(
            row["operating_activity"],
            row["investing_activity"]
        ),
        axis=1
    )

    def get_capex(row):

        result = capex_intensity(
            row["investing_activity"],
            row["sales"]
        )

        if result is None:
            return None

        return result[0]

    merged_df["capex_cr"] = merged_df.apply(
        get_capex,
        axis=1
    )

    merged_df["earnings_per_share"] = merged_df["eps"]

    merged_df["book_value_per_share"] = merged_df.apply(
        lambda row:
        (
            (row["equity_capital"] + row["reserves"])
            /
            row["equity_capital"]
        )
        if row["equity_capital"] != 0
        else None,
        axis=1
    )

    merged_df["dividend_payout_ratio_pct"] = merged_df["dividend_payout"]

    merged_df["total_debt_cr"] = merged_df["borrowings"]

    merged_df["cash_from_operations_cr"] = merged_df["operating_activity"]

    # ---------------------------------------
    # CAGR
    # ---------------------------------------

    merged_df["revenue_cagr_5yr"] = None
    merged_df["pat_cagr_5yr"] = None
    merged_df["eps_cagr_5yr"] = None

    # ---------------------------------------
    # Composite Score
    # ---------------------------------------

    merged_df["composite_quality_score"] = (
        merged_df["net_profit_margin_pct"] +
        merged_df["return_on_equity_pct"]
    ) / 2

    print("Financial Ratios Calculated Successfully.")
        # ---------------------------------------
    # Final DataFrame
    # ---------------------------------------

    final_df = merged_df[
        [
            "company_id",
            "year",
            "net_profit_margin_pct",
            "operating_profit_margin_pct",
            "return_on_equity_pct",
            "debt_to_equity",
            "interest_coverage",
            "asset_turnover",
            "free_cash_flow_cr",
            "capex_cr",
            "earnings_per_share",
            "book_value_per_share",
            "dividend_payout_ratio_pct",
            "total_debt_cr",
            "cash_from_operations_cr",
            "revenue_cagr_5yr",
            "pat_cagr_5yr",
            "eps_cagr_5yr",
            "composite_quality_score"
        ]
    ]

    print("\nPreview\n")

    print(final_df.head())

    # ---------------------------------------
    # Save into SQLite
    # ---------------------------------------

    final_df.to_sql(
        "financial_ratios",
        conn,
        if_exists="replace",
        index=False
    )

    print("\nfinancial_ratios table populated successfully!")

    # ---------------------------------------
    # Save Validation Report
    # ---------------------------------------

    final_df.to_csv(
        "output/financial_ratios_validation.csv",
        index=False
    )

    print(
        "Validation report saved to output/financial_ratios_validation.csv"
    )

    conn.close()

    print("\nDay 12 Completed Successfully.")


if __name__ == "__main__":
    main()