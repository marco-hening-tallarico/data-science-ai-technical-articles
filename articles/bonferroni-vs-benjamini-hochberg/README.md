# Bonferroni vs. Benjamini-Hochberg: Choosing Your P-Value Correction

- **Published URL:** https://towardsdatascience.com/the-time-10-99-was-too-big-superheavy-elements-and-deceit/

## Purpose
This companion asks when strict family-wise error control is worth the loss of
power, and when false-discovery-rate control is a better fit for exploratory
scientific workflows with many simultaneous hypotheses.

## Contents
- `notebooks/heavy-atom-p-val.ipynb`
- `src/multiple_testing.py`
- `data/README.md`
- `figures/`
- `requirements.txt`

## Methods and libraries
- Methods: Bonferroni correction, Benjamini-Hochberg thresholding, Monte Carlo
  style simulation framing for false-positive risk.
- Libraries declared/used: Python, NumPy, matplotlib, JupyterLab.

## Reproduce
1. From repo root, install tooling with `make install`.
2. Install article dependencies: `pip install -r articles/bonferroni-vs-benjamini-hochberg/requirements.txt`.
3. Run `notebooks/heavy-atom-p-val.ipynb` from top to bottom.
4. Optionally reuse logic from `src/multiple_testing.py` in scripts/tests.

## Data
Synthetic data only; no external dataset is required for the core workflow.

## Status
`runnable` (notebook listed as `ok` in `docs/notebook_execution_report.json`).

## Skills demonstrated
- multiple hypothesis testing
- statistical simulation
- quantitative trade-off analysis (FWER vs FDR)
- reproducible notebook workflow
- extraction of reusable statistical helpers

## Notes
Educational notebook companion, not a standalone inference library intended for
new domains without review.
