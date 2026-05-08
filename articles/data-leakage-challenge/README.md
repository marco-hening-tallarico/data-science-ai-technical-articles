# Will You Spot the Leaks? A Data Science Challenge

- **Published URL:** https://towardsdatascience.com/will-you-spot-the-leaks-a-data-science-challenge/

## Purpose
This project explores a central ML reliability question: how seemingly good
model performance can be caused by leakage from time, entities, or target-proxy
features rather than genuine predictive signal.

## Contents
- `notebooks/Data_leaks.ipynb`
- `src/leakage_guards.py`
- `data/README.md`
- `figures/`
- `requirements.txt`

## Methods and libraries
- Methods: leakage detection, entity overlap checks, chronological validation,
  split hygiene, challenge-style diagnostic framing.
- Libraries declared/used: Python, pandas, NumPy, seaborn, matplotlib,
  nest_asyncio, JupyterLab.

## Reproduce
1. From repo root, run `make install`.
2. Install article dependencies: `pip install -r articles/data-leakage-challenge/requirements.txt`.
3. Run `notebooks/Data_leaks.ipynb` end to end.
4. Reuse utility functions in `src/leakage_guards.py` for deterministic checks.

## Data
Synthetic/scaffolded challenge-style tabular examples generated and transformed
within the notebook workflow.

## Status
`runnable` (notebook listed as `ok` in `docs/notebook_execution_report.json`).

## Skills demonstrated
- leakage-aware model validation
- data cleaning and transformation
- split design under temporal and entity constraints
- exploratory analysis translated into reusable Python checks
- reproducible notebook workflow

## Notes
Real production leakage prevention usually also requires feature-store and
serving-time governance beyond this companion scope.
