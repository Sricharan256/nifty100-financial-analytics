"""
check_duplicates.py

Checks for duplicate company IDs in the companies table.
"""

import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

print("=" * 60)
print("DUPLICATE RECORD CHECK")
print("=" * 60)

cursor.execute("""
SELECT
    id,
    COUNT(*)
FROM companies
GROUP BY id
HAVING COUNT(*) > 1;
""")

rows = cursor.fetchall()

if rows:
    print("\nDuplicate records found:\n")
    for row in rows:
        print(row)
else:
    print("\nNo duplicate records found.")

conn.close()

print("\nDuplicate verification completed.")