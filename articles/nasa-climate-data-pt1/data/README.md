# Data Notes

- Primary source: NASA POWER API (public climate data service)
  - https://power.larc.nasa.gov/
- Local reproducibility artifact:
  - generate `data/processed/climate_data.csv` locally from notebook/API calls

## License and Use

NASA POWER data is public, but attribution and downstream use should follow NASA POWER guidance.
Do not assume third-party redistribution rights beyond original source terms.

## Reproduction Path

1. Pull fresh data using API logic in `shared/nasa/data_access.py`.
2. Save processed output to `data/processed/`.
3. Run `notebooks/Climate_pt1.ipynb` using relative local paths.
