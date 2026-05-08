# Will You Spot the Leaks? A Data Science Challenge

- **Published URL:** https://towardsdatascience.com/will-you-spot-the-leaks-a-data-science-challenge/
- **Status:** runnable
- **Primary tools:** Python, pandas, NumPy, matplotlib, seaborn

## Purpose
Practical leakage-detection companion emphasizing split strategy, preprocessing
boundaries, and entity-aware validation.

## Key Methods
- Target leakage identification
- Temporal split hygiene
- Entity leakage controls
- Pipeline-safe preprocessing
- Evaluation discipline

## Data
Challenge-style tabular examples modeled after airline safety scenarios, generated and manipulated within the notebook.

## Reproduce
1. Create environment from repository root (`environment.yml`).
2. Install article-specific dependencies from `requirements.txt`.
3. Launch Jupyter from repository root.
4. Open and run `notebooks/Data_leaks.ipynb` from top to bottom.
5. Use `src/leakage_guards.py` for reusable leakage checks in scripts/tests.
6. Regenerate visuals into `figures/` with relative paths only.

## Contents
- `notebooks/Data_leaks.ipynb`: primary article companion notebook
- `src/leakage_guards.py`: reusable checks for entity overlap and date-order validation
- `figures/`: generated plots and visuals
- `data/README.md`: data provenance and usage notes
- `requirements.txt`: article-specific dependency list

## Status
`runnable` (notebook appears in `docs/notebook_execution_report.json` with `ok`).

## Notes
Synthetic/scaffolded challenge framing; real enterprise leakage controls may
require broader governance checks.
