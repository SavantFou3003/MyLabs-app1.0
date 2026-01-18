from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Vec3:
    x: float
    y: float
    z: float

    def to_tuple(self) -> tuple[float, float, float]:
        return (self.x, self.y, self.z)


@dataclass
class Transform:
    position: Vec3
    rotation: Vec3
    scale: Vec3

    @staticmethod
    def identity() -> "Transform":
        return Transform(
            position=Vec3(0.0, 0.0, 0.0),
            rotation=Vec3(0.0, 0.0, 0.0),
            scale=Vec3(1.0, 1.0, 1.0),
        )
