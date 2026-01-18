from __future__ import annotations

from dataclasses import dataclass

from app.core.scene import Scene


@dataclass
class CameraState:
    distance: float = 10.0
    yaw: float = 45.0
    pitch: float = 30.0


class GLScene:
    def __init__(self, scene: Scene, camera: CameraState) -> None:
        self.scene = scene
        self.camera = camera

    def draw(self) -> None:
        """Placeholder for OpenGL rendering."""
