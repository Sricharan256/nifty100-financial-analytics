"""
test_profitability.py

Unit tests for profitability ratios.
"""

from src.analytics.profitability import (
    calculate_npm,
    calculate_opm,
    calculate_roe,
    calculate_roce
)

import pandas as pd


def test_calculate_npm():

    df = pd.DataFrame({
        "sales": [1000],
        "net_profit": [200]
    })

    df = calculate_npm(df)

    assert round(df["npm"][0], 2) == 20.00


def test_calculate_opm():

    df = pd.DataFrame({
        "sales": [1000],
        "operating_profit": [250]
    })

    df = calculate_opm(df)

    assert round(df["calculated_opm"][0], 2) == 25.00


def test_calculate_roe():

    df = pd.DataFrame({
        "net_profit": [200],
        "equity_capital": [100],
        "reserves": [900]
    })

    df = calculate_roe(df)

    assert round(df["roe"][0], 2) == 20.00


def test_calculate_roce():

    df = pd.DataFrame({
        "operating_profit": [250],
        "equity_capital": [100],
        "reserves": [900],
        "borrowings": [500]
    })

    df = calculate_roce(df)

    assert round(df["roce"][0], 2) == 16.67