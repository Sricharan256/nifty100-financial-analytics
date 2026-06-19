"""
normaliser.py

Utility functions to normalize year and stock ticker values.
"""

import re


def normalize_year(year):

    if year is None:
        return None

    year = str(year).strip().upper()

    if year.startswith("FY"):
        yy = int(year.replace("FY", ""))
        return 2000 + yy

    if "-" in year:
        return int("20" + year.split("-")[-1])

    if year.isdigit():
        return int(year)

    return None


def normalize_ticker(ticker):

    if ticker is None:
        return None

    ticker = str(ticker).strip().upper()

    ticker = re.sub(r"\s+", "", ticker)

    return ticker


if __name__ == "__main__":
    print("Testing normalize_year()")
    print(normalize_year("FY24"))
    print(normalize_year("2023-24"))
    print(normalize_year("2024"))

    print("\nTesting normalize_ticker()")
    print(normalize_ticker("tcs"))
    print(normalize_ticker(" Reliance "))
    print(normalize_ticker("infy"))