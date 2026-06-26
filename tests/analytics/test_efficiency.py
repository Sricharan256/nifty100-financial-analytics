"""
test_efficiency.py

Unit tests for efficiency ratios.
"""

import unittest

from src.analytics.efficiency import (
    asset_turnover
)


class TestEfficiencyRatios(unittest.TestCase):

    def test_asset_turnover_normal(self):
        self.assertEqual(
            asset_turnover(10000, 5000),
            2.00
        )

    def test_asset_turnover_zero_assets(self):
        self.assertIsNone(
            asset_turnover(10000, 0)
        )

    def test_asset_turnover_negative_assets(self):
        self.assertIsNone(
            asset_turnover(10000, -5000)
        )

    def test_asset_turnover_missing_values(self):
        self.assertIsNone(
            asset_turnover(None, 5000)
        )


if __name__ == "__main__":
    unittest.main()