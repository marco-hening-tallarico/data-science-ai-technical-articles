"""Tests for Article 7 strategy evaluation helpers."""

import importlib.util
from pathlib import Path

import pandas as pd

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "articles"
    / "trading-agent-showdown"
    / "src"
    / "evaluation.py"
)
SPEC = importlib.util.spec_from_file_location("evaluation", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_compute_max_drawdown_is_negative_or_zero() -> None:
    equity_curve = pd.Series([100.0, 110.0, 90.0, 95.0])
    max_drawdown = MODULE.compute_max_drawdown(equity_curve)
    assert max_drawdown <= 0.0


def test_summarize_strategy_contains_expected_keys() -> None:
    returns = pd.Series([0.01, -0.02, 0.015, 0.0])
    equity_curve = pd.Series([100.0, 101.0, 99.0, 100.5, 100.5])
    summary = MODULE.summarize_strategy(returns, equity_curve)
    assert "total_return" in summary
    assert "sharpe_ratio" in summary
    assert "max_drawdown" in summary
