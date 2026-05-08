# Storm or Signal: A Trading Agent Showdown

- **Published URL:** https://ai.gopubby.com/storm-or-signal-a-trading-agent-showdown-5f3d662b2cef

## Purpose
This project tests whether a weather-linked hypothesis can produce meaningful
signal in an RL-driven trading setup, and emphasizes careful experimental
comparison rather than claims of production alpha.

## Contents
- `notebooks/PPO_agent.ipynb`
- `src/evaluation.py`
- `data/README.md`
- `figures/`
- `requirements.txt`

## Methods and libraries
- Methods: PPO-based RL experimentation, comparative evaluation, return/risk
  metric inspection.
- Libraries declared/used: Python, gym, stable-baselines3, torch, pandas,
  NumPy, matplotlib, seaborn, meteostat, pybroker, JupyterLab.

## Reproduce
1. From repo root, run `make install`.
2. Install dependencies: `pip install -r articles/trading-agent-showdown/requirements.txt`.
3. Execute `notebooks/PPO_agent.ipynb`.
4. Reuse metrics in `src/evaluation.py` for deterministic analysis checks.

## Data
Uses market/weather inputs as documented in the notebook and `data/README.md`.

## Status
`runnable` (notebook listed as `ok` in `docs/notebook_execution_report.json`).

## Skills demonstrated
- reinforcement learning experimentation
- quantitative evaluation design
- data integration for applied ML
- reproducible notebook workflow
- translating exploratory metrics into reusable Python

## Notes
Results are exploratory and sensitive to assumptions, timeframe, and market
frictions.
