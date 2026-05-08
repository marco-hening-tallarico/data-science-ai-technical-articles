# From a Point to L∞

- **Published URL:** https://towardsdatascience.com/from-a-point-to-l%e2%88%9e/

## Purpose
This project develops intuition for how different norm choices reshape geometry,
optimization behavior, and regularization assumptions in machine-learning
objectives.

## Contents
- `notebooks/code.ipynb`
- `src/norms.py`
- `data/README.md`
- `figures/`
- `requirements.txt`

## Methods and libraries
- Methods: Lp norm comparisons, limiting behavior toward L-infinity, synthetic
  demonstrations of optimization/regularization effects.
- Libraries declared/used: Python, NumPy, matplotlib, seaborn, scikit-learn,
  JupyterLab.

## Reproduce
1. From repo root, run `make install`.
2. Install dependencies: `pip install -r articles/point-to-l-infinity/requirements.txt`.
3. Execute `notebooks/code.ipynb`.
4. Use reusable functions in `src/norms.py` for script-level checks.

## Data
Synthetic generated examples only; no external dataset is required.

## Status
`runnable` (notebook listed as `ok` in `docs/notebook_execution_report.json`).

## Skills demonstrated
- mathematical exposition for ML
- numerical experimentation
- scientific visualization
- translating notebook logic into reusable modules
- reproducible notebook workflow

## Notes
Examples are didactic and prioritize interpretability over exhaustive empirical
benchmarking.
