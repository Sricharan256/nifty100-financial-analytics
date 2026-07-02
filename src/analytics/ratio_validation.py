"""
ratio_validation.py

Sprint 2 - Day 13

Validates calculated ROE against source ROE
and generates ratio_edge_cases.log.
"""

import sqlite3
import pandas as pd

DB_PATH = "db/nifty100.db"

# ---------------------------------------
# Connect to Database
# ---------------------------------------

conn = sqlite3.connect(DB_PATH)

# ---------------------------------------
# Read Companies Table
# ---------------------------------------

companies = pd.read_sql(
    """
    SELECT
        id,
        company_name,
        roce_percentage,
        roe_percentage
    FROM companies
    """,
    conn
)

# Rename id -> company_id for merging
companies.rename(
    columns={"id": "company_id"},
    inplace=True
)

# ---------------------------------------
# Read Financial Ratios Table
# ---------------------------------------

ratios = pd.read_sql(
    """
    SELECT
        company_id,
        year,
        return_on_equity_pct
    FROM financial_ratios
    """,
    conn
)

# ---------------------------------------
# Merge Data
# ---------------------------------------

merged = pd.merge(
    companies,
    ratios,
    on="company_id",
    how="inner"
)

print("=" * 60)
print("DAY 13 - RATIO VALIDATION")
print("=" * 60)

edge_cases = []

# ---------------------------------------
# Compare ROE Values
# ---------------------------------------

for _, row in merged.iterrows():

    source_roe = row["roe_percentage"]
    calculated_roe = row["return_on_equity_pct"]

    if pd.isna(source_roe) or pd.isna(calculated_roe):
        continue

    difference = abs(source_roe - calculated_roe)

    if difference > 5:

        edge_cases.append([
            row["company_id"],
            row["company_name"],
            source_roe,
            calculated_roe,
            round(difference, 2),
            "Formula Difference"
        ])

conn.close()

# ---------------------------------------
# Generate Log File
# ---------------------------------------

with open("output/ratio_edge_cases.log", "w") as file:

    file.write("=" * 60 + "\n")
    file.write("RATIO EDGE CASE LOG\n")
    file.write("=" * 60 + "\n\n")

    if len(edge_cases) == 0:

        file.write("No anomalies found.\n")

    else:

        for case in edge_cases:

            file.write(
                f"""Company ID : {case[0]}
Company    : {case[1]}
Source ROE : {case[2]}
Calculated : {case[3]}
Difference : {case[4]}
Category   : {case[5]}
------------------------------------------------------------
"""
            )

print(f"\nTotal Edge Cases Found : {len(edge_cases)}")
print("Edge Case Log Generated Successfully.")
print("Location : output/ratio_edge_cases.log")