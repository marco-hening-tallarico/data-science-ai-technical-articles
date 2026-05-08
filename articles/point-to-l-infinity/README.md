# From a Point to L∞

- **Published URL:** https://towardsdatascience.com/from-a-point-to-l%e2%88%9e/
- **Status:** runnable
- **Primary tools:** Python, NumPy, matplotlib, seaborn, scikit-learn

## Purpose
Math-for-ML companion examining norm behavior, loss tradeoffs, and
regularization implications.

## Key Methods
- Lp norms
- L1/L2 loss behavior
- Regularization comparison
- Convergence to L-infinity norm

## Data
Synthetic numeric examples and generated demonstrations.

## Reproduce
1. Create environment from repository root (`environment.yml`).
2. Install article-specific dependencies from `requirements.txt`.
3. Launch Jupyter from repository root.
4. Open and run `notebooks/code.ipynb` from top to bottom.
5. Use reusable functions in `src/norms.py` for scripts and tests.
6. Save generated plots to `figures/` when exporting visuals.

## Contents
- `notebooks/code.ipynb`: main article companion notebook
- `src/norms.py`: reusable Lp, L-infinity, and regularization helpers
- `figures/`: generated plots and visuals
- `data/README.md`: data and provenance notes
- `requirements.txt`: article-specific dependency list

## Status
`runnable` (notebook appears in `docs/notebook_execution_report.json` with `ok`).

## Notes
Didactic focus; benchmarks are illustrative rather than exhaustive.
