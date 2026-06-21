"""
check_missing_values.py

Checks for missing values in important columns.
"""

import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

print("=" * 60)
print("MISSING VALUE CHECK")
print("=" * 60)

cursor.execute("""
SELECT id, company_name
FROM companies
WHERE
company_name IS NULL
OR website IS NULL
OR face_value IS NULL
OR book_value IS NULL
OR roce_percentage IS NULL
OR roe_percentage IS NULL;
""")

rows = cursor.fetchall()

if rows:
    print("\nCompanies with missing values:\n")

    for row in rows:
        print(row)

else:
    print("\nNo missing values found.")

conn.close()

print("\nMissing value verification completed.")