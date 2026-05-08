# Portfolio report

This document summarizes repository metadata and **existing** generated artifacts (article READMEs, `docs/notebook_execution_report.json`). It does **not** execute notebooks, refresh plots, or run CI.

## Dependencies inventory

Pinned and declared dependency notes live in `docs/dependency_inventory.md`.

## Article summary

| Article | Status | Declared libraries | Data availability | Notebook status entries |
| --- | --- | --- | --- | --- |
| `articles/bonferroni-vs-benjamini-hochberg` | runnable | numpy, matplotlib, jupyterlab | synthetic/generated | heavy-atom-p-val.ipynb: ok |
| `articles/data-leakage-challenge` | runnable | ipython, nest_asyncio, numpy, pandas, matplotlib, seaborn, jupyterlab | synthetic/generated | Data_leaks.ipynb: ok |
| `articles/grammar-as-injectable-nlp` | pending migration | numpy, pandas, jupyterlab | pending migration | - |
| `articles/nasa-climate-data-pt1` | runnable | numpy, pandas, requests, scipy, matplotlib, seaborn, jupyterlab | public source (documented) | Climate_pt1.ipynb: ok |
| `articles/nasa-climate-data-pt2-sdes` | runnable | ipython, numpy, pandas, scipy, statsmodels, matplotlib, jupyterlab | public source (documented) | Climate_pt2.ipynb: ok |
| `articles/physics-informed-neural-networks` | runnable | numpy, pandas, scipy, matplotlib, scikit-learn, tensorflow, deepxde, torch, jupyterlab | synthetic/generated | Laplacian-example.ipynb: ok; PINN.ipynb: ok; hot_rod_4.ipynb: ok |
| `articles/point-to-l-infinity` | runnable | numpy, matplotlib, seaborn, scikit-learn, jupyterlab | synthetic/generated | code.ipynb: ok |
| `articles/trading-agent-showdown` | runnable | ipython, gym, matplotlib, meteostat, pandas, pybroker, seaborn, stable-baselines3, torch, jupyterlab | external providers (see notes) | PPO_agent.ipynb: ok |

## Notebook execution snapshot

- Source: `docs/notebook_execution_report.json`
- Notebook entries: 9
- `ok`: 9

## Lint, tests, and local validation

- Not captured automatically in this file.
- Run `make check` in your active virtual environment for current Ruff + pytest results.
