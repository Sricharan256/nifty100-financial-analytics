"""
test_database.py

Unit tests for SQLite database.
"""

import sqlite3
import unittest
from pathlib import Path


DB_PATH = Path("db/nifty100.db")


class TestDatabase(unittest.TestCase):

    def test_database_exists(self):
        """Check database file exists."""

        self.assertTrue(DB_PATH.exists())

    def test_database_connection(self):
        """Check database connection."""

        conn = sqlite3.connect(DB_PATH)

        self.assertIsNotNone(conn)

        conn.close()

    def test_companies_table_exists(self):
        """Check companies table exists."""

        conn = sqlite3.connect(DB_PATH)

        cursor = conn.cursor()

        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name='companies';
        """)

        table = cursor.fetchone()

        conn.close()

        self.assertIsNotNone(table)


if __name__ == "__main__":
    unittest.main()