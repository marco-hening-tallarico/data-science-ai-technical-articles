# How to Access NASA's Climate Data, Pt. 1

- **Published URL:** https://towardsdatascience.com/how-to-access-nasas-climate-data-and-how-its-powering-the-fight-against-climate-change-pt-1/

## Purpose
This project addresses the practical question of how to transform raw NASA POWER
API responses into clean, analysis-ready climate tables that can be reused
across notebooks and downstream statistical workflows.

## Contents
- `notebooks/Climate_pt1.ipynb`
- `src/nasa_pt1_pipeline.py`
- `data/README.md`
- `data/processed/`
- `figures/`
- `requirements.txt`

## Methods and libraries
- Methods: API retrieval, JSON-to-table conversion, date normalization, export
  to processed CSV for downstream analyses.
- Libraries declared/used: Python, requests, pandas, NumPy, SciPy, matplotlib,
  seaborn, JupyterLab.

## Reproduce
1. From repo root, run `make install`.
2. Install article dependencies: `pip install -r articles/nasa-climate-data-pt1/requirements.txt`.
3. Execute `notebooks/Climate_pt1.ipynb`.
4. Generated outputs are typically written under `data/processed/`.
5. Reuse helper logic from `src/nasa_pt1_pipeline.py` and `shared/nasa/data_access.py`.

## Data
Public NASA POWER climate data. See `data/README.md` for source details and
handling notes.

## Status
`runnable` (notebook listed as `ok` in `docs/notebook_execution_report.json`).

## Skills demonstrated
- API-driven data collection
- data cleaning and transformation
- scientific Python time-series preparation
- reusable pipeline helper design
- reproducible notebook workflow

## Design notes

- Reproducibility depends on stable NASA POWER access patterns and documented
  parameter choices; URL/query drift can change payloads even when code is fixed.
- Date normalization and missing-value coercion are analytical decisions:
  `normalize_date_column` encodes how ambiguous inputs become comparable rows.
- Plots and summaries assume the preprocessing described here; changing cleaning
  steps changes what the charts mean.
- Pipeline helpers (`src/nasa_pt1_pipeline.py`, shared NASA accessors) separate
  retrieval/normalization from narrative notebook cells so EDA can stay focused.

## Notes
Upstream API availability and evolving endpoints can affect reproducibility
timing and exact payload details.
