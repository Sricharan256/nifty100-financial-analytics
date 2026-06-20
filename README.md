# Nifty 100 Financial Analytics Platform

## Project Overview

The **Nifty 100 Financial Analytics Platform** is an end-to-end data engineering project that processes financial data of Nifty 100 companies. The project builds a robust ETL pipeline to extract, transform, validate, and load financial datasets into a SQLite database. The validated data serves as the foundation for financial analytics, reporting, and Power BI dashboards.

---

# Project Objectives

* Build a scalable ETL pipeline for financial datasets.
* Standardize financial year and stock ticker formats.
* Validate data using Data Quality (DQ) rules.
* Store validated data in a SQLite database.
* Prepare data for financial analytics and dashboard development.
* Generate reports for data validation and auditing.

---

# Sprint 1 – Data Foundation

## Day 1 – Environment Setup ✅

* Created the project directory structure.
* Configured the Python virtual environment.
* Installed required Python libraries.
* Added `.env`, `.gitignore`, `requirements.txt`, and `Makefile`.
* Initialized the Git repository.
* Created the initial project documentation.

---

## Day 2 – Excel Loader & Normaliser ✅

* Developed `loader.py` to load Excel datasets using Pandas.
* Implemented `normalize_year()` to standardize financial year formats.
* Implemented `normalize_ticker()` to standardize stock ticker symbols.
* Successfully loaded sample datasets from the `data/raw` directory.
* Added unit tests for loader and normaliser modules.

---

## Day 3 – Schema Validator & Data Quality Checks ✅

* Developed `validator.py`.
* Implemented Required Columns validation.
* Implemented Missing Values validation.
* Implemented Duplicate Rows validation.
* Implemented Year validation.
* Implemented Ticker validation.
* Generated `validation_report.csv`.
* Successfully passed all ETL unit tests.

Validation Summary

* ✅ Required Columns – Passed
* ✅ Missing Values – Passed
* ✅ Duplicate Rows – Passed

---

## Day 4 – SQLite Database Schema ✅

* Created `schema.sql`.
* Created SQLite database (`nifty100.db`).
* Developed `database.py`.
* Enabled SQLite Foreign Key support.
* Created the Companies table.
* Verified database creation.
* Added database unit tests.

---

# Project Structure

```text
nifty100_financial_analytics/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── supplementary/
│
├── db/
│   ├── schema.sql
│   └── nifty100.db
│
├── docs/
│
├── notebooks/
│
├── output/
│   └── validation_report.csv
│
├── src/
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── check_database.py
│   │
│   ├── etl/
│   │   ├── __init__.py
│   │   ├── loader.py
│   │   ├── normaliser.py
│   │   └── validator.py
│   │
│   └── utils/
│
├── tests/
│   ├── db/
│   │   ├── __init__.py
│   │   └── test_database.py
│   │
│   └── etl/
│       ├── __init__.py
│       ├── test_loader.py
│       ├── test_normaliser.py
│       └── test_validator.py
│
├── README.md
├── requirements.txt
├── Makefile
├── .env
└── .gitignore
```

---

# ETL Workflow

```text
Excel Files
      │
      ▼
Loader Module
      │
      ▼
Data Normalisation
      │
      ▼
Schema Validation
      │
      ▼
SQLite Database
      │
      ▼
Financial Analytics
      │
      ▼
Power BI Dashboard
```

---

# Technologies Used

* Python 3.12
* Pandas
* NumPy
* OpenPyXL
* SQLite
* Pytest
* Git & GitHub
* Power BI

---

# Modules

## Loader Module (`loader.py`)

* Reads Excel datasets.
* Loads Excel files into Pandas DataFrames.
* Handles file loading errors.
* Displays dataset statistics.

---

## Normaliser Module (`normaliser.py`)

* Standardizes financial year values.
* Standardizes stock ticker symbols.
* Removes extra whitespace.
* Converts ticker values to uppercase.

---

## Validator Module (`validator.py`)

Implements Data Quality (DQ) validation before data is loaded into SQLite.

### Validation Rules

* Required Columns Validation
* Missing Values Validation
* Duplicate Rows Validation
* Year Validation
* Ticker Validation

### Validation Output

The validator generates:

```text
output/
└── validation_report.csv
```

The report contains:

* Validation Rule
* Validation Status
* Issue Description
* Rows Affected

---

## Database Module (`database.py`)

Responsible for:

* Creating SQLite database
* Executing `schema.sql`
* Creating database tables
* Enabling foreign keys
* Preparing the database for ETL loading

---

# Current Progress

* ✅ Environment Setup Completed
* ✅ Excel Loader Completed
* ✅ Data Normalisation Completed
* ✅ Schema Validator Completed
* ✅ Validation Report Generated
* ✅ SQLite Database Schema Completed
* ✅ Unit Tests Passed
* ⏳ Full Data Loading (Day 5)
* ⏳ Data Quality Review (Day 6)
* ⏳ Sprint Review & Documentation (Day 7)

---

# How to Run

## Activate Virtual Environment

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Loader

```bash
python src/etl/loader.py
```

---

## Run Normaliser

```bash
python src/etl/normaliser.py
```

---

## Run Validator

```bash
python src/etl/validator.py
```

---

## Create Database

```bash
python src/db/database.py
```

---

## Verify Database

```bash
python src/db/check_database.py
```

---

## Run All Unit Tests

```bash
python -m pytest
```

---

# Deliverables Completed

* Project Structure
* Excel Loader
* Data Normaliser
* Schema Validator
* Validation Report
* SQLite Database
* Database Schema
* Unit Tests
* Project Documentation

---
# Author

**Sricharan Medaboina**

**Nifty 100 Financial Analytics Platform**

Sprint 1 – Data Foundation
