"""
database.py

Creates SQLite database using schema.sql
"""

import sqlite3
from pathlib import Path

DB_PATH = Path("db/nifty100.db")
SCHEMA_PATH = Path("db/schema.sql")


def create_database():

    conn = sqlite3.connect(DB_PATH)

    # Enable Foreign Keys
    conn.execute("PRAGMA foreign_keys = ON;")

    # Execute schema
    with open(SCHEMA_PATH, "r") as file:
        conn.executescript(file.read())

    conn.commit()
    conn.close()

    print("Database created successfully!")
    print(f"Database location: {DB_PATH}")


if __name__ == "__main__":
    create_database()