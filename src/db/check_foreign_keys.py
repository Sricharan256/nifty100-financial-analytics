"""
check_foreign_keys.py

Checks foreign key integrity in the SQLite database.
"""

import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

print("=" * 60)
print("FOREIGN KEY CHECK")
print("=" * 60)

cursor.execute("PRAGMA foreign_key_check;")
rows = cursor.fetchall()

if rows:
    print("\nForeign key issues found:\n")
    for row in rows:
        print(row)
else:
    print("\nNo foreign key issues found.")

conn.close()

print("\nForeign key verification completed.")