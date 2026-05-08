"""Article-local tests for multiple-testing helpers."""

import importlib.util
from pathlib import Path

import numpy as np

MODULE_PATH = Path(__file__).resolve().parents[1] / "src" / "multiple_testing.py"
SPEC = importlib.util.spec_from_file_location("article_multiple_testing", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def test_bh_rejection_mask_identifies_small_p_values() -> None:
    p_values = [0.001, 0.02, 0.03, 0.4]
    rejection_mask = MODULE.benjamini_hochberg_rejection_mask(p_values, q_level=0.05)
    assert np.array_equal(rejection_mask, np.array([True, True, True, False]))


def test_bh_rejection_mask_no_discoveries_when_all_large() -> None:
    p_values = [0.2, 0.3, 0.4]
    rejection_mask = MODULE.benjamini_hochberg_rejection_mask(p_values, q_level=0.05)
    assert np.array_equal(rejection_mask, np.array([False, False, False]))
