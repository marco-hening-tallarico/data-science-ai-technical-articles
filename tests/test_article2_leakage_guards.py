"""Tests for Article 2 reusable leakage guard helpers."""

import importlib.util
from pathlib import Path

import pandas as pd

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "articles"
    / "data-leakage-challenge"
    / "src"
    / "leakage_guards.py"
)
SPEC = importlib.util.spec_from_file_location("leakage_guards", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_article2_detects_entity_overlap() -> None:
    training_frame = pd.DataFrame({"tail_id": ["N1", "N2", "N3"]})
    testing_frame = pd.DataFrame({"tail_id": ["N3", "N4"]})
    assert MODULE.has_entity_overlap(training_frame, testing_frame, "tail_id")


def test_article2_detects_chronological_sort() -> None:
    sorted_frame = pd.DataFrame({"date": ["2025-01-01", "2025-01-02"]})
    unsorted_frame = pd.DataFrame({"date": ["2025-01-02", "2025-01-01"]})
    assert MODULE.is_sorted_chronologically(sorted_frame, "date")
    assert not MODULE.is_sorted_chronologically(unsorted_frame, "date")
