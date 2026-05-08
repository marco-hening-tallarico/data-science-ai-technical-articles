# Applied AI and Data Science Portfolio

This repository is a reproducible portfolio of technical article companions
across statistics, applied machine learning, scientific computing, NLP,
reinforcement learning, and scientific ML.

Website: [marcoheningtallarico.com](https://marcoheningtallarico.com/)  
LinkedIn: [Marco Hening Tallarico](https://www.linkedin.com/in/marco-hening-tallarico/)  
Towards Data Science: [Author Page](https://towardsdatascience.com/author/marco-heningtallarico/)

## What This Repository Is

Each article is organized as a mini-project with:

- an article-level `README.md`
- reproducible notebook and/or helper module paths
- dependency pins in article `requirements.txt`
- data provenance notes in `data/README.md`
- lightweight tests in `tests/` for reusable logic

## Project Index

Status labels are evidence-based:

- `runnable`: notebook(s) appear in `docs/notebook_execution_report.json` with `"status": "ok"`
- `partial`: only part of the companion is currently represented (for example, docs without full code parity)
- `in progress`: active migration/buildout
- `pending migration`: article is listed but executable companion assets are not yet present

| article folder | topic | key methods | article link | status |
| --- | --- | --- | --- | --- |
| `bonferroni-vs-benjamini-hochberg` | Statistics | FWER/FDR, Bonferroni, BH | [Bonferroni vs Benjamini-Hochberg](https://towardsdatascience.com/the-time-10-99-was-too-big-superheavy-elements-and-deceit/) | runnable |
| `data-leakage-challenge` | Applied ML | Leakage detection, split hygiene | [Will You Spot the Leaks](https://towardsdatascience.com/will-you-spot-the-leaks-a-data-science-challenge/) | runnable |
| `nasa-climate-data-pt1` | Data engineering | API access, cleaning, tabular preparation | [NASA Climate Data Pt. 1](https://towardsdatascience.com/how-to-access-nasas-climate-data-and-how-its-powering-the-fight-against-climate-change-pt-1/) | runnable |
| `nasa-climate-data-pt2-sdes` | Scientific computing | Ornstein-Uhlenbeck process, simulation | [NASA Climate Data Pt. 2](https://towardsdatascience.com/stochastic-differential-equations-and-temperature-nasa-climate-data-pt-2/) | runnable |
| `grammar-as-injectable-nlp` | NLP theory | CCG, compositional grammar framing | [Grammar as an Injectable](https://towardsdatascience.com/grammar-as-a-trojan-horse-to-nlp-and-computer-science/) | pending migration |
| `point-to-l-infinity` | Math for ML | Lp norms, L-infinity behavior | [From a Point to L-infinity](https://towardsdatascience.com/from-a-point-to-l%e2%88%9e/) | runnable |
| `trading-agent-showdown` | Reinforcement learning | PPO experimentation and evaluation | [Storm or Signal](https://ai.gopubby.com/storm-or-signal-a-trading-agent-showdown-5f3d662b2cef) | runnable |
| `physics-informed-neural-networks` | Scientific ML | PINNs, inverse PDE setup | [PINNs for Inverse PDE Problems](https://towardsdatascience.com/physics-informed-neural-networks-for-inverse-pde-problems/) | runnable |

## Suggested Reading Paths

- Statistics and evaluation rigor:
  `bonferroni-vs-benjamini-hochberg` -> `data-leakage-challenge` -> `point-to-l-infinity`
- Scientific data and modeling:
  `nasa-climate-data-pt1` -> `nasa-climate-data-pt2-sdes` -> `physics-informed-neural-networks`
- RL and experimental framing:
  `trading-agent-showdown` -> shared tests in `tests/`

## Reproducibility

1. Create the base environment:
   `conda env create -f environment.yml`
2. Activate it:
   `conda activate tds-ai-data-science`
3. Install root tooling (if needed):
   `pip install -r requirements-lock.txt`
4. Install an article's requirements:
   `pip install -r articles/<slug>/requirements.txt`
5. Follow the article `README.md` to run notebook(s) and helpers.

See also:

- `docs/REPRODUCIBILITY.md`
- `docs/DATA_POLICY.md`
- `docs/LICENSE_NOTES.md`

## Notebook Execution Snapshot

Based on `docs/notebook_execution_report.json`:

- 9 notebooks listed
- 9/9 with status `ok`
- slowest notebook in report:
  `articles/nasa-climate-data-pt1/notebooks/Climate_pt1.ipynb` (~84.55s)
- no grammar notebook is listed in the execution report

## Skills Demonstrated

- Multiple-testing statistics and error-rate control
- Applied ML leakage prevention and validation design
- Public API data retrieval and cleaning pipelines
- Stochastic process modeling (OU/SDE)
- PINN-based inverse-problem setup
- RL experiment setup and evaluation
- Reproducibility discipline and data provenance documentation

## Repository Structure

```text
articles/    article-specific companions
shared/      reusable modules (nasa, stats, plotting, utils)
data/        optional shared data notes/artifacts
tests/       lightweight validation tests
docs/        reproducibility, policy, licensing, templates
```

## Author Spotlight

Featured by Towards Data Science:  
[Bridging the Gap Between Research and Readability with Marco Hening Tallarico](https://towardsdatascience.com/bridging-the-gap-between-research-and-readability-with-marco-hening-tallarico/)
