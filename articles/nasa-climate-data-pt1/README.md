# How to Access NASA's Climate Data — Pt. 1

- **Published URL:** https://towardsdatascience.com/how-to-access-nasas-climate-data-and-how-its-powering-the-fight-against-climate-change-pt-1/
- **Status:** runnable
- **Primary tools:** Python, requests, pandas, numpy, matplotlib

## Purpose
Data-access companion focused on obtaining, validating, and organizing NASA
climate data for downstream analysis.

## Key Methods
- API retrieval
- Tabular cleaning
- Schema normalization
- Time-series preparation
- Exploratory validation

## Data
NASA POWER climate data (public). See data/README.md for acquisition details and terms.

## Reproduce
1. Create environment from repository root (`environment.yml`).
2. Install article-specific dependencies from `requirements.txt`.
3. Launch Jupyter from repository root.
4. Open and run `notebooks/Climate_pt1.ipynb` from top to bottom.
5. Use local dataset path `../data/processed/climate_data.csv` when prompted by notebook cells.
6. For reusable API access logic, use `shared/nasa/data_access.py`.
7. Regenerate plots into `figures/` and keep all paths relative.

## Contents
- `notebooks/Climate_pt1.ipynb`: main article companion notebook
- `data/processed/`: local output directory for generated climate tables (not committed by default)
- `data/README.md`: data source, licensing, and acquisition guidance
- `src/`: article-specific utilities (reserved for follow-up extraction)
- `requirements.txt`: article-specific dependency list

## Status
`runnable` (notebook appears in `docs/notebook_execution_report.json` with `ok`).

## Notes
API availability and parameter choices may affect reproducibility over time.
