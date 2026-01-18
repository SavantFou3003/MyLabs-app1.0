from __future__ import annotations

from dataclasses import replace

from .constraints import Axis, ConstraintResult, LinkConstraints
from .links import Link
from .transforms import Transform, Vec3


class ConstraintSolver:
    def apply_constraints(
        self,
        link: Link,
        source: Transform,
        target: Transform,
    ) -> Transform:
        constrained = self._apply_axis_constraints(link.constraints, target)
        return replace(target, position=constrained.translation, rotation=constrained.rotation)

    def _apply_axis_constraints(
        self,
        constraints: LinkConstraints,
        target: Transform,
    ) -> ConstraintResult:
        translation = Vec3(
            x=constraints.translation[Axis.X].clamp(target.position.x),
            y=constraints.translation[Axis.Y].clamp(target.position.y),
            z=constraints.translation[Axis.Z].clamp(target.position.z),
        )
        rotation = Vec3(
            x=constraints.rotation[Axis.X].clamp(target.rotation.x),
            y=constraints.rotation[Axis.Y].clamp(target.rotation.y),
            z=constraints.rotation[Axis.Z].clamp(target.rotation.z),
        )
        return ConstraintResult(translation=translation, rotation=rotation)
