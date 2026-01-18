from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EditorSettings:
    show_grid: bool = True
    grid_size: float = 1.0
