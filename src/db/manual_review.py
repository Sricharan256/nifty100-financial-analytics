"""
manual_review.py

Displays details of selected companies for manual verification.
"""

import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

companies = [
    "ABB",
    "ADANIENT",
    "INFY",
    "RELIANCE",
    "TCS"
]

print("=" * 60)
print("MANUAL REVIEW OF RANDOM COMPANIES")
print("=" * 60)

for company in companies:

    cursor.execute(
        "SELECT * FROM companies WHERE id = ?",
        (company,)
    )

    row = cursor.fetchone()

    print("\n" + "=" * 50)

    if row:
        print(f"Company ID : {row[0]}")
        print(f"Company Name : {row[2]}")
        print(f"Website : {row[5]}")
        print(f"ROCE : {row[10]}")
        print(f"ROE : {row[11]}")
    else:
        print(f"{company} not found.")

conn.close()

print("\nManual review completed successfully.")