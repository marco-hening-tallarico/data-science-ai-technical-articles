# Physics-Informed Neural Networks for Inverse PDE Problems

- **Published URL:** https://towardsdatascience.com/physics-informed-neural-networks-for-inverse-pde-problems/

## Purpose
This companion examines how physics-informed neural networks can infer PDE
parameters from sparse observations while preserving physical constraints during
optimization.

## Contents
- `notebooks/hot_rod_4.ipynb`
- `notebooks/PINN.ipynb`
- `notebooks/Laplacian-example.ipynb`
- `src/pinn_heat.py`
- `data/simulated-heat-equation.csv`
- `requirements.txt`

## Methods and libraries
- Methods: PINN formulation, inverse PDE parameter estimation, heat-equation
  constraints, simulation-backed diagnostics.
- Libraries declared/used: Python, DeepXDE, TensorFlow, torch, NumPy, pandas,
  SciPy, scikit-learn, matplotlib, JupyterLab.

## Reproduce
1. From repo root, run `make install`.
2. Install dependencies: `pip install -r articles/physics-informed-neural-networks/requirements.txt`.
3. Execute notebooks in order: `hot_rod_4.ipynb`, `PINN.ipynb`,
   `Laplacian-example.ipynb`.
4. Reuse helper logic in `src/pinn_heat.py` where applicable.

## Data
Uses simulated/structured data in the notebook workflow; includes sample
artifact `data/simulated-heat-equation.csv`.

## Status
`runnable` (all three notebooks listed as `ok` in
`docs/notebook_execution_report.json`).

## Skills demonstrated
- scientific machine learning
- inverse problem formulation
- numerical simulation
- model constraint design from governing equations
- technical writing about physics-informed network setups and failure modes

## Notes
This workflow is compute-sensitive and hyperparameter-sensitive; numerical
stability and convergence can vary across environments.
