# Physics-Informed Neural Networks for Inverse PDE Problems

- **Published URL:** https://towardsdatascience.com/physics-informed-neural-networks-for-inverse-pde-problems/
- **Status:** runnable
- **Primary tools:** Python, DeepXDE, TensorFlow, NumPy, pandas, matplotlib

## Purpose
Scientific ML companion solving inverse PDE parameter estimation with PINNs and
DeepXDE.

## Key Methods
- PINNs
- Inverse PDE setup
- Heat equation parameter inference
- Automatic differentiation constraints

## Data
Simulated/structured temperature data as described in notebook pipeline.  
Included sample: `data/simulated-heat-equation.csv`.

## Reproduce
1. Create environment from repository root (`environment.yml`).
2. Install article-specific dependencies from `requirements.txt`.
3. Launch Jupyter from repository root.
4. Run notebooks in this recommended order:
   - `notebooks/hot_rod_4.ipynb`
   - `notebooks/PINN.ipynb`
   - `notebooks/Laplacian-example.ipynb`
5. Keep all I/O paths relative to the article folder.
6. Reuse helper functions from `src/pinn_heat.py` for deterministic synthetic data generation.

## Contents
- `notebooks/PINN.ipynb`: main PINN inverse-problem workflow
- `notebooks/hot_rod_4.ipynb`: heat-equation simulation support notebook
- `notebooks/Laplacian-example.ipynb`: Laplacian intuition notebook
- `src/pinn_heat.py`: reusable seed and synthetic heat-grid helpers
- `data/simulated-heat-equation.csv`: local sample data artifact
- `requirements.txt`: article-specific dependency list

## Status
`runnable` (notebook appears in `docs/notebook_execution_report.json` with `ok`).

## Notes
Compute-heavy and sensitive to architecture/hyperparameters.
