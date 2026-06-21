"""
run_queries.py

Executes exploratory SQL queries.
"""

import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

queries = [
    ("Total Companies", "SELECT COUNT(*) FROM companies;"),
    ("Top 5 Companies by ROE",
     "SELECT company_name, roe_percentage FROM companies ORDER BY roe_percentage DESC LIMIT 5;"),
    ("Top 5 Companies by ROCE",
     "SELECT company_name, roce_percentage FROM companies ORDER BY roce_percentage DESC LIMIT 5;"),
    ("Profit Loss Records", "SELECT COUNT(*) FROM profit_loss;"),
    ("Balance Sheet Records", "SELECT COUNT(*) FROM balance_sheet;"),
    ("Cash Flow Records", "SELECT COUNT(*) FROM cash_flow;")
]

for title, query in queries:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

conn.close()