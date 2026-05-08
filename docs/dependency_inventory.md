# Dependency Inventory

This inventory is a human-readable summary of primary, top-level dependencies
used across the portfolio. It is not a substitute for exact pinned environment
files such as `requirements-lock.txt` and article-level `requirements.txt`.

| Package | Used in | Purpose |
| --- | --- | --- |
| numpy | root lockfile; multiple article `requirements.txt`; `shared/stats`; article `src` modules and notebooks | numerical arrays, vectorized math, simulation support |
| pandas | root lockfile; NASA/data-leakage/trading/PINN article requirements; `shared/nasa`; article modules | tabular data wrangling and time-series tables |
| scipy | root lockfile; NASA Pt. 1, NASA Pt. 2, PINN requirements | scientific computation and modeling utilities |
| matplotlib | root lockfile and most article requirements/notebooks | static quantitative plotting |
| seaborn | root lockfile; data-leakage, NASA Pt. 1, point-to-l-infinity, trading requirements/notebooks | statistical visualization styles/plots |
| scikit-learn | root lockfile; point-to-l-infinity and PINN requirements | ML utilities and didactic modeling helpers |
| requests | NASA Pt. 1 requirements; `shared/nasa/data_access.py` | HTTP access to NASA POWER API |
| statsmodels | NASA Pt. 2 requirements | time-series/statistical modeling utilities |
| jupyterlab | root lockfile and all article requirements | notebook execution and exploration environment |
| nest_asyncio | data-leakage requirements; leakage notebook import | notebook event-loop compatibility |
| ipython | data-leakage, trading, NASA Pt. 2 requirements | interactive Python shell/notebook integration |
| gym / gymnasium | trading requirements; trading notebook import | RL environment interfaces |
| stable-baselines3 | trading requirements | PPO and RL algorithm implementations |
| torch | trading and PINN requirements | deep learning backend support |
| tensorflow | PINN requirements | deep learning backend used by DeepXDE workflows |
| deepxde | PINN requirements | physics-informed neural network framework |
| meteostat | trading requirements | weather data retrieval for trading experiment inputs |
| pybroker | trading requirements | trading backtesting utilities used by article workflow |
| pytest | root lockfile; repository test suite | automated unit testing |
| ruff | root lockfile; `Makefile` lint target | linting and formatting checks |
| black | root lockfile; `pyproject.toml` config | Python code formatting configuration |
| pre-commit | root lockfile; `.pre-commit-config.yaml` | local quality gate automation |
