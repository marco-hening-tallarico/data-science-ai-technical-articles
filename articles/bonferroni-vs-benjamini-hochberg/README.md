# Bonferroni vs. Benjamini-Hochberg: Choosing Your P-Value Correction

- **Published URL:** https://towardsdatascience.com/the-time-10-99-was-too-big-superheavy-elements-and-deceit/
- **Status:** runnable
- **Primary tools:** Python, NumPy, matplotlib

## Purpose
Show practical trade-offs between FWER and FDR control in reproducible,
notebook-driven examples.

## Key Methods
- Family-Wise Error Rate (FWER)
- Bonferroni correction
- False Discovery Rate (FDR)
- Benjamini-Hochberg procedure
- Monte Carlo illustration of false positive risk

## Data
Synthetic simulation only. No external dataset is required for core reproduction.

## Reproduce
1. Create environment from repository root (`environment.yml`).
2. Install article-specific dependencies from `requirements.txt`.
3. Launch Jupyter from repository root.
4. Open and run `notebooks/heavy-atom-p-val.ipynb` from top to bottom.
5. Regenerate charts into `figures/` and verify paths are relative.
6. (Optional) Use `src/multiple_testing.py` helpers in custom scripts.

## Contents
- `notebooks/heavy-atom-p-val.ipynb`: main article companion notebook migrated from source repo
- `src/multiple_testing.py`: reusable correction helpers and thresholds
- `figures/`: generated plots and visuals
- `data/README.md`: data provenance and availability note
- `requirements.txt`: article-specific dependency list

## Status
`runnable` (notebook appears in `docs/notebook_execution_report.json` with `ok`).

## Notes
Educational demonstration; not a validated production inference framework for
regulated scientific claims.
