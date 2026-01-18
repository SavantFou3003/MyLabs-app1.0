from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ViewportState:
    camera_distance: float = 10.0
    camera_pitch: float = 30.0
    camera_yaw: float = 45.0


class Viewport:
    def __init__(self, state: ViewportState) -> None:
        self.state = state

    def orbit(self, delta_yaw: float, delta_pitch: float) -> None:
        self.state.camera_yaw += delta_yaw
        self.state.camera_pitch += delta_pitch

    def zoom(self, delta: float) -> None:
        self.state.camera_distance = max(0.1, self.state.camera_distance + delta)
