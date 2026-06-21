"""
check_year_coverage.py

Checks companies with less than 5 years of financial data.
"""

import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

print("=" * 60)
print("YEAR COVERAGE CHECK")
print("=" * 60)

cursor.execute("""
SELECT
    company_id,
    COUNT(DISTINCT year) AS total_years
FROM profit_loss
GROUP BY company_id
HAVING COUNT(DISTINCT year) < 5
ORDER BY total_years;
""")

rows = cursor.fetchall()

if rows:
    print("\nCompanies with less than 5 years of data:\n")

    for company, years in rows:
        print(f"{company:15} {years} years")

else:
    print("\nAll companies have at least 5 years of financial data.")

conn.close()

print("\nYear coverage verification completed.")