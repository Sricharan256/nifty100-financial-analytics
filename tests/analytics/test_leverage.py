"""
test_leverage.py

Unit tests for leverage ratios.
"""

import unittest

from src.analytics.leverage import (
    debt_to_equity,
    interest_coverage
)


class TestLeverageRatios(unittest.TestCase):

    # ----------------------------
    # Debt-to-Equity Tests
    # ----------------------------

    def test_debt_to_equity_normal(self):
        self.assertEqual(
            debt_to_equity(2500, 5000),
            0.50
        )

    def test_debt_to_equity_zero_equity(self):
        self.assertIsNone(
            debt_to_equity(1000, 0)
        )

    def test_debt_to_equity_negative_equity(self):
        self.assertIsNone(
            debt_to_equity(1000, -500)
        )

    def test_debt_to_equity_missing_values(self):
        self.assertIsNone(
            debt_to_equity(None, 500)
        )

    # ----------------------------
    # Interest Coverage Tests
    # ----------------------------

    def test_interest_coverage_normal(self):
        self.assertEqual(
            interest_coverage(1200, 200),
            7.00
        )

    def test_interest_coverage_zero_interest(self):
        self.assertIsNone(
            interest_coverage(1200, 0)
        )

    def test_interest_coverage_missing_values(self):
        self.assertIsNone(
            interest_coverage(None, 200)
        )


if __name__ == "__main__":
    unittest.main()