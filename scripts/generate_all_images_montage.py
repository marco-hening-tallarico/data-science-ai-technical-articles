"""Build a single PNG contact sheet of every raster image in the portfolio tree.

Writes ``docs/assets/all_images_montage.png``: thumbnails of all ``*.png`` files
under ``articles/`` and ``docs/assets/`` (excluding the montage file itself so
regeneration stays stable).

Requires matplotlib + scipy (already in repository dependencies).
"""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import zoom

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "docs" / "assets" / "all_images_montage.png"

SCAN_ROOTS = (
    PROJECT_ROOT / "articles",
    PROJECT_ROOT / "docs" / "assets",
)

THUMB_MAX = 320
NCOLS = 4


def _resize_thumb(image_array: np.ndarray, max_px: int = THUMB_MAX) -> np.ndarray:
    """Downsample RGBA/RGB float or uint8 array for thumbnail grid."""
    if image_array.ndim == 2:
        image_array = np.stack([image_array] * 3, axis=-1)
    height, width = image_array.shape[:2]
    longest = max(height, width)
    if longest <= max_px:
        return image_array
    scale = max_px / float(longest)
    factors = (scale, scale) + tuple(1 for _ in range(image_array.ndim - 2))
    resized = zoom(image_array, factors, order=1)
    return np.clip(resized, 0.0, 1.0)


def _collect_png_paths() -> list[Path]:
    paths: list[Path] = []
    for root in SCAN_ROOTS:
        if not root.is_dir():
            continue
        paths.extend(sorted(root.rglob("*.png")))
    resolved_out = OUTPUT_PATH.resolve()
    unique: list[Path] = []
    seen: set[Path] = set()
    for path in paths:
        resolved = path.resolve()
        if resolved == resolved_out:
            continue
        if resolved in seen:
            continue
        seen.add(resolved)
        unique.append(path)
    return sorted(unique, key=lambda p: str(p.relative_to(PROJECT_ROOT)).lower())


def main() -> None:
    png_paths = _collect_png_paths()
    if not png_paths:
        msg = "No PNG files found under articles/ or docs/assets/"
        raise RuntimeError(msg)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    n_images = len(png_paths)
    ncols = min(NCOLS, n_images)
    nrows = math.ceil(n_images / ncols)

    fig_w = ncols * 3.4
    fig_h = max(4.0, nrows * 3.0)
    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=(fig_w, fig_h),
        dpi=120,
        squeeze=False,
    )

    for idx, ax in enumerate(axes.flatten()):
        if idx >= n_images:
            ax.axis("off")
            continue
        path = png_paths[idx]
        relative = path.relative_to(PROJECT_ROOT).as_posix()
        try:
            raw = mpimg.imread(path)
            thumb = _resize_thumb(np.asarray(raw))
            ax.imshow(thumb)
        except OSError as exc:
            ax.text(
                0.5,
                0.5,
                f"[read error]\n{relative}\n{exc}",
                ha="center",
                va="center",
                fontsize=7,
                wrap=True,
            )
        ax.set_title(relative, fontsize=7, fontfamily="monospace")
        ax.axis("off")

    fig.suptitle(
        "Portfolio PNG inventory (articles/ + docs/assets/, excluding this file)",
        fontsize=11,
        y=1.002,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.98))
    fig.savefig(OUTPUT_PATH, bbox_inches="tight")
    plt.close(fig)

    print(f"Wrote {OUTPUT_PATH.relative_to(PROJECT_ROOT)} ({n_images} images)")


if __name__ == "__main__":
    main()
