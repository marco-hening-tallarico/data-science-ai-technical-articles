"""Evaluation helpers for trading-agent experiments."""

from __future__ import annotations

import numpy as np
import pandas as pd


def compute_max_drawdown(equity_curve: pd.Series) -> float:
    """Return maximum drawdown from an equity curve."""
    running_peak = equity_curve.cummax()
    drawdowns = (equity_curve - running_peak) / running_peak
    return float(drawdowns.min())


def compute_sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    """Return annualized Sharpe ratio from daily returns."""
    excess_returns = returns - risk_free_rate / 252.0
    volatility = excess_returns.std(ddof=1)
    if volatility == 0 or np.isnan(volatility):
        return 0.0
    return float(np.sqrt(252.0) * excess_returns.mean() / volatility)


def summarize_strategy(returns: pd.Series, equity_curve: pd.Series) -> dict[str, float]:
    """Return compact strategy summary metrics."""
    return {
        "total_return": float((equity_curve.iloc[-1] / equity_curve.iloc[0]) - 1.0),
        "sharpe_ratio": compute_sharpe_ratio(returns),
        "max_drawdown": compute_max_drawdown(equity_curve),
    }
