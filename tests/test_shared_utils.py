"""Shared utility tests."""

from pathlib import Path

from shared.utils.slugs import article_slug_from_title


def test_article_slug_from_title() -> None:
    slug = article_slug_from_title("From a Point to L∞")
    assert slug.startswith("from-a-point-to")
    assert Path(slug).name == slug
