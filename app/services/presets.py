from __future__ import annotations

from app.core.constraints import Axis, AxisConstraint, LinkConstraints


def fixed_joint() -> LinkConstraints:
    return LinkConstraints.all_locked()


def pivot(axis: Axis) -> LinkConstraints:
    locked = AxisConstraint(mode="locked")
    free = AxisConstraint(mode="free")
    rotation = {Axis.X: locked, Axis.Y: locked, Axis.Z: locked}
    rotation[axis] = free
    return LinkConstraints(
        translation={Axis.X: locked, Axis.Y: locked, Axis.Z: locked},
        rotation=rotation,
    )


def slider(axis: Axis) -> LinkConstraints:
    locked = AxisConstraint(mode="locked")
    free = AxisConstraint(mode="free")
    translation = {Axis.X: locked, Axis.Y: locked, Axis.Z: locked}
    translation[axis] = free
    return LinkConstraints(
        translation=translation,
        rotation={Axis.X: locked, Axis.Y: locked, Axis.Z: locked},
    )


def ball_socket() -> LinkConstraints:
    locked = AxisConstraint(mode="locked")
    free = AxisConstraint(mode="free")
    return LinkConstraints(
        translation={Axis.X: locked, Axis.Y: locked, Axis.Z: locked},
        rotation={Axis.X: free, Axis.Y: free, Axis.Z: free},
    )
