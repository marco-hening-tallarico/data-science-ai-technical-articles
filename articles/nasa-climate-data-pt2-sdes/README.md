# Stochastic Differential Equations and Temperature: NASA Climate Data pt. 2

- **Published URL:** https://towardsdatascience.com/stochastic-differential-equations-and-temperature-nasa-climate-data-pt-2/

## Purpose
This project investigates whether simple stochastic differential equation models
(especially Ornstein-Uhlenbeck dynamics) can capture meaningful structure in
temperature time series derived from the Pt. 1 climate pipeline.

## Contents
- `notebooks/Climate_pt2.ipynb`
- `src/sde_ou.py`
- `data/README.md`
- `data/processed/`
- `figures/`
- `requirements.txt`

## Methods and libraries
- Methods: Ornstein-Uhlenbeck process modeling, Euler-style simulation,
  parameter interpretation, time-series diagnostics.
- Libraries declared/used: Python, NumPy, pandas, SciPy, statsmodels,
  matplotlib, JupyterLab.

## Reproduce
1. From repo root, run `make install`.
2. Install dependencies: `pip install -r articles/nasa-climate-data-pt2-sdes/requirements.txt`.
3. Ensure prepared climate input exists (typically from Pt. 1 workflow).
4. Execute `notebooks/Climate_pt2.ipynb`.
5. Reuse helper functions in `src/sde_ou.py` where applicable.

## Data
Uses prepared NASA climate time series from the Pt. 1 data-access workflow.

## Status
`runnable` (notebook listed as `ok` in `docs/notebook_execution_report.json`).

## Skills demonstrated
- numerical simulation
- stochastic process modeling
- scientific visualization
- parameter interpretation under uncertainty
- reproducible notebook workflow

## Notes
The OU formulation is intentionally simplified and should be interpreted as a
didactic model, not a full climate dynamics model.
