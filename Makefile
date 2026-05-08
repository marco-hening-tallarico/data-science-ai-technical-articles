PYTHON ?= python

.PHONY: help install install-articles lint format test check notebook-status

help:
	@echo "Targets:"
	@echo "  install           Install root dependencies"
	@echo "  install-articles  Install all article requirements"
	@echo "  lint              Run ruff checks"
	@echo "  format            Run ruff format"
	@echo "  test              Run pytest suite"
	@echo "  check             Run lint + tests"
	@echo "  notebook-status   Print notebook execution report"

install:
	pip install -r requirements-lock.txt

install-articles:
	for requirements_file in articles/*/requirements.txt; do \
		echo "Installing $$requirements_file"; \
		pip install -r "$$requirements_file"; \
	done

lint:
	ruff check .

format:
	ruff format .

test:
	pytest

check: lint test

notebook-status:
	$(PYTHON) -m json.tool docs/notebook_execution_report.json
