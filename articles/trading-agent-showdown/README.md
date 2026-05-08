# Storm or Signal: A Trading Agent Showdown

- **Published URL:** https://ai.gopubby.com/storm-or-signal-a-trading-agent-showdown-5f3d662b2cef
- **Status:** runnable
- **Primary tools:** Python, notebooks, NumPy, pandas, matplotlib

## Purpose
Reinforcement learning companion comparing trading-agent behavior under
weather-linked signal hypotheses.

## Key Methods
- RL environment setup
- Agent comparison
- Signal testing
- Experimental evaluation

## Data
Market/weather input sources as described in article materials and repo assets.

## Reproduce
1. Create environment from repository root (`environment.yml`).
2. Install article-specific dependencies from `requirements.txt`.
3. Launch Jupyter from repository root.
4. Open and run `notebooks/PPO_agent.ipynb`.
5. Save generated figures to `figures/` and tabular outputs to local `data/processed/`.
6. Use `src/evaluation.py` for reusable strategy metrics.

## Contents
- `notebooks/PPO_agent.ipynb`: main article companion notebook
- `src/evaluation.py`: reusable metrics for return/risk evaluation
- `figures/`: generated plots and visuals
- `data/README.md`: data source and provenance notes
- `requirements.txt`: article-specific dependency list

## Status
`runnable` (notebook appears in `docs/notebook_execution_report.json` with `ok`).

## Notes
Financial modeling assumptions and market frictions may limit external validity.
