import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

query = """
SELECT
company_id,
year,
return_on_equity_pct,
revenue_cagr_5yr
FROM financial_ratios
WHERE company_id IN ('ABB','INFY','TCS');
"""

df = pd.read_sql(query, conn)

print(df)

conn.close()