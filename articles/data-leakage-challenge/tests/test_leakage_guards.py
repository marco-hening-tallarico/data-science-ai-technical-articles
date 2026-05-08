"""Article-local tests for leakage guard utilities."""

import importlib.util
from pathlib import Path

import pandas as pd

MODULE_PATH = Path(__file__).resolve().parents[1] / "src" / "leakage_guards.py"
SPEC = importlib.util.spec_from_file_location("article_leakage_guards", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_entity_overlap_ratio_for_partial_overlap() -> None:
    training_frame = pd.DataFrame({"tail_id": ["A", "B", "C"]})
    testing_frame = pd.DataFrame({"tail_id": ["C", "D"]})
    assert MODULE.entity_overlap_ratio(training_frame, testing_frame, "tail_id") == 0.5


def test_entity_overlap_ratio_for_empty_test_entities() -> None:
    training_frame = pd.DataFrame({"tail_id": ["A"]})
    testing_frame = pd.DataFrame({"tail_id": []})
    assert MODULE.entity_overlap_ratio(training_frame, testing_frame, "tail_id") == 0.0
