# Stochastic Differential Equations and Temperature — NASA Climate Data pt. 2

- **Published URL:** https://towardsdatascience.com/stochastic-differential-equations-and-temperature-nasa-climate-data-pt-2/
- **Status:** runnable
- **Primary tools:** Python, NumPy, pandas, scipy, matplotlib

## Purpose
Scientific computing companion implementing SDE-based temperature modeling with
reproducible simulation.

## Key Methods
- Ornstein-Uhlenbeck process
- SDE simulation
- Parameter interpretation
- Time-series diagnostics

## Data
NASA climate time series prepared from Pt. 1 pipeline and documented sources.

## Reproduce
1. Create environment from repository root (`environment.yml`).
2. Install article-specific dependencies from `requirements.txt`.
3. Ensure local input data exists at `../data/processed/climate_data.csv`.
4. Launch Jupyter from repository root and run `notebooks/Climate_pt2.ipynb`.
5. Notebook outputs and diagnostics are written to `../figures/`.
6. Reusable SDE logic is available in `src/sde_ou.py`.

## Contents
- `notebooks/Climate_pt2.ipynb`: main SDE analysis notebook
- `src/sde_ou.py`: OU simulation and estimation helpers
- `figures/`: migrated diagnostics and generated plots
- `data/README.md`: data provenance and preparation notes
- `requirements.txt`: article-specific dependency list

## Status
`runnable` (notebook appears in `docs/notebook_execution_report.json` with `ok`).

## Notes
Model assumptions simplify real climate dynamics and should be interpreted
cautiously.
