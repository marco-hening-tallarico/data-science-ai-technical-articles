# Reproducibility Standards

- Set explicit seeds in scripts and notebooks (`random`, `numpy`, framework).
- Keep reusable logic in `src/` and reserve notebooks for narrative analysis.
- Use relative paths only (no machine-specific absolute paths).
- Document exact run steps and dependencies in each article README.
- Store generated figures in `figures/` with reproducible generation steps.
- If data is omitted, provide `data/README.md` with acquisition instructions.
