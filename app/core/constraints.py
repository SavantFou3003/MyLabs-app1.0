from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Literal

from .transforms import Vec3


class Axis(str, Enum):
    X = "x"
    Y = "y"
    Z = "z"


ConstraintMode = Literal["locked", "free", "limited"]


@dataclass
class AxisConstraint:
    mode: ConstraintMode
    min_val: float | None = None
    max_val: float | None = None

    def clamp(self, value: float) -> float:
        if self.mode == "locked":
            return 0.0
        if self.mode == "limited":
            if self.min_val is not None:
                value = max(value, self.min_val)
            if self.max_val is not None:
                value = min(value, self.max_val)
        return value


@dataclass
class LinkConstraints:
    translation: dict[Axis, AxisConstraint]
    rotation: dict[Axis, AxisConstraint]

    @staticmethod
    def all_locked() -> "LinkConstraints":
        locked = AxisConstraint(mode="locked")
        return LinkConstraints(
            translation={Axis.X: locked, Axis.Y: locked, Axis.Z: locked},
            rotation={Axis.X: locked, Axis.Y: locked, Axis.Z: locked},
        )


@dataclass
class ConstraintResult:
    translation: Vec3
    rotation: Vec3
