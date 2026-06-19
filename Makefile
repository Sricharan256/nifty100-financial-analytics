# Makefile for Nifty100 Financial Analytics Project

.PHONY: load ratios test report dashboard api clean

load:
	@echo "Running ETL Loader..."
	python src/etl/loader.py

ratios:
	@echo "Calculating Financial Ratios..."
	python src/analytics/calculate_ratios.py

test:
	@echo "Running Unit Tests..."
	pytest tests/

report:
	@echo "Generating Reports..."
	python src/report/generate_report.py

dashboard:
	@echo "Launching Dashboard..."

api:
	@echo "Starting API..."

clean:
	@echo "Cleaning Project..."