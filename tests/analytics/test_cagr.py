import unittest

from src.analytics.cagr import (
    calculate_cagr,
    revenue_cagr,
    pat_cagr,
    eps_cagr
)


class TestCAGR(unittest.TestCase):

    def test_revenue_cagr(self):
        self.assertEqual(
            revenue_cagr(1000, 1800, 5),
            12.47
        )

    def test_pat_cagr(self):
        self.assertEqual(
            pat_cagr(250, 500, 5),
            14.87
        )

    def test_eps_cagr(self):
        self.assertEqual(
            eps_cagr(20, 40, 5),
            14.87
        )

    def test_zero_beginning(self):
        self.assertIsNone(
            calculate_cagr(0, 100, 5)
        )

    def test_negative_value(self):
        self.assertIsNone(
            calculate_cagr(-100, 200, 5)
        )

    def test_none_value(self):
        self.assertIsNone(
            calculate_cagr(None, 200, 5)
        )

    def test_invalid_years(self):
        self.assertIsNone(
            calculate_cagr(100, 200, 0)
        )


if __name__ == "__main__":
    unittest.main()