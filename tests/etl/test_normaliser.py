from src.etl.normaliser import normalize_year, normalize_ticker


def test_normalize_year_fy():
    assert normalize_year("FY24") == 2024


def test_normalize_year_range():
    assert normalize_year("2023-24") == 2024


def test_normalize_year_number():
    assert normalize_year("2024") == 2024


def test_normalize_ticker_lower():
    assert normalize_ticker("tcs") == "TCS"


def test_normalize_ticker_spaces():
    assert normalize_ticker(" reliance ") == "RELIANCE"