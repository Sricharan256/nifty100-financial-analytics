## ETL Overview

The ETL (Extract, Transform, Load) pipeline is responsible for reading financial datasets from Excel files, standardizing data formats, validating input values, and preparing the data for loading into a SQLite database. This modular design improves data quality, consistency, and maintainability.

---

## Loader Module

The `loader.py` module loads Excel datasets from the `data/raw/` directory using Pandas. It validates file availability, reads worksheets into DataFrames, handles file-related exceptions, and prepares the data for preprocessing.

**Key Features:**

* Reads Excel files using Pandas
* Handles missing or invalid files
* Displays dataset row and column counts
* Passes data to the normalisation module

---

## Normaliser Module

The `normaliser.py` module standardizes important fields before validation and database loading.

**Implemented Functions:**

* `normalize_year()` – Converts financial year formats such as `FY24` and `2023-24` into the standard format `2024`.
* `normalize_ticker()` – Removes extra spaces and converts stock ticker symbols to uppercase for consistency.

---

## Folder Structure

```text
nifty100_financial_analytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── supplementary/
│
├── db/
│
├── src/
│   ├── etl/
│   │   ├── loader.py
│   │   └── normaliser.py
│   └── utils/
│
├── tests/
│   └── etl/
│       ├── test_loader.py
│       └── test_normaliser.py
│
├── output/
├── notebooks/
├── docs/
│
├── README.md
├── requirements.txt
├── Makefile
└── .env
```
