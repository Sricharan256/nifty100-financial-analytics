from src.etl.normaliser import normalize_year, normalize_ticker


def test_normalize_year():
    assert normalize_year("FY24") == 2024


def test_normalize_ticker():
    assert normalize_ticker(" tcs ") == "TCS"