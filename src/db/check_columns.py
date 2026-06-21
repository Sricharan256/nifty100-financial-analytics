import sqlite3

conn = sqlite3.connect("db/nifty100.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(profit_loss);")

for column in cursor.fetchall():
    print(column)

conn.close()