# Nifty 100 Financial Analytics Platform

## Project Overview

The Nifty 100 Financial Analytics Platform is a data engineering project focused on building a robust ETL pipeline for processing financial datasets of Nifty 100 companies. The project extracts data from multiple Excel files, standardizes and validates the data, and prepares it for storage in a SQLite database. This data foundation supports future modules such as financial analytics, dashboards, and reporting.

---

## Sprint 1 – Data Foundation

### Day 1 – Environment Setup

* Created the project directory structure.
* Configured the Python virtual environment.
* Installed required Python libraries.
* Added `.env`, `.gitignore`, `Makefile`, and `requirements.txt`.
* Initialized the Git repository.

### Day 2 – Excel Loader & Normaliser

* Developed the `loader.py` module to load Excel datasets using Pandas.
* Implemented `normalize_year()` to standardize financial year formats.
* Implemented `normalize_ticker()` to standardize stock ticker symbols.
* Added basic unit tests for loader and normalisation functions.
* Validated successful loading and preprocessing of sample datasets.

---

## Project Structure

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
│   │   ├── normaliser.py
│   │   └── validator.py
│   │
│   └── utils/
│
├── tests/
│   └── etl/
│
├── notebooks/
├── output/
├── docs/
│
├── README.md
├── requirements.txt
├── Makefile
├── .env
└── .gitignore
```

---

## ETL Workflow

```
Excel Files
      │
      ▼
Loader Module
      │
      ▼
Data Normalisation
      │
      ▼
Data Validation
      │
      ▼
SQLite Database
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* OpenPyXL
* SQLite
* Pytest
* Git & GitHub

---

## Modules

### Loader Module (`loader.py`)

* Reads Excel datasets from the `data/raw` directory.
* Loads data into Pandas DataFrames.
* Handles missing files and loading errors.
* Displays dataset statistics.

### Normaliser Module (`normaliser.py`)

* Standardizes financial year formats.
* Standardizes stock ticker symbols.
* Removes unwanted whitespace.
* Converts ticker values to uppercase.

---
## Day 3 - Schema Validator — 16 DQ Rules

## Schema Validator

The `validator.py` module validates the integrity and consistency of financial datasets before they are loaded into the SQLite database. It applies a series of Data Quality (DQ) rules to detect missing values, duplicate records, invalid formats, and schema inconsistencies.

### Validation Features

- Required column validation
- Missing value detection
- Duplicate record identification
- Year format validation
- Ticker format validation
- Validation report generation

### Validation Output

The validator generates a CSV report containing validation results, including the validation rule, status, affected rows, and issue description. This report helps identify and resolve data quality issues before database loading.

Output File:

```text
output/validation_report.csv

## Current Progress

* ✅ Project setup completed
* ✅ Virtual environment configured
* ✅ Excel loader implemented
* ✅ Data normalisation implemented
* ✅ Initial unit tests created
* ⏳ Data Quality Validator (Day 3)
* ⏳ SQLite Database (Day 4)
* ⏳ Full ETL Pipeline (Day 5–7)

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the loader:

```bash
python src/etl/loader.py
```

Run the normaliser test:

```bash
python src/etl/normaliser.py
```

Run unit tests:

```bash
pytest
```

---

## Future Enhancements

* Implement 16 Data Quality (DQ) rules.
* Build the SQLite database schema.
* Automate the ETL pipeline.
* Generate validation and load audit reports.
* Develop financial analytics and dashboards.

---

## Author

**Sricharan Medaboina**

Nifty 100 Financial Analytics Platform – Sprint 1
