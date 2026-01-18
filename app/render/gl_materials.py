from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Material:
    name: str
    color: tuple[float, float, float]
