PYTHON ?= python3
PIP ?= $(PYTHON) -m pip

.PHONY: help install install-articles lint format test check notebook-status portfolio-report

help:
	@echo "Targets:"
	@echo "  install           Install root dependencies"
	@echo "  install-articles  Install all article requirements"
	@echo "  lint              Run ruff checks"
	@echo "  format            Run ruff format"
	@echo "  test              Run pytest suite"
	@echo "  check             Run lint + tests"
	@echo "  notebook-status   Print notebook execution report"
	@echo "  portfolio-report  Generate docs/portfolio_report.md"

install:
	$(PIP) install -r requirements-lock.txt

install-articles:
	for requirements_file in articles/*/requirements.txt; do \
		echo "Installing $$requirements_file"; \
		$(PIP) install -r "$$requirements_file"; \
	done

lint:
	$(PYTHON) -m ruff check .

format:
	$(PYTHON) -m ruff format .

test:
	$(PYTHON) -m pytest

check: lint test

notebook-status:
	$(PYTHON) -m json.tool docs/notebook_execution_report.json

portfolio-report:
	$(PYTHON) scripts/generate_portfolio_report.py
