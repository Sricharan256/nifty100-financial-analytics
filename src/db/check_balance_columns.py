"""
check_balance_columns.py

Displays the columns of the balance_sheet table.
"""

import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(balance_sheet);")

columns = cursor.fetchall()

print("\nBalance Sheet Table Columns:\n")

for column in columns:
    print(column)

conn.close()