from __future__ import annotations

from app.core.objects import BoxObject, ObjectId
from app.core.scene import Scene
from app.ui.main_window import MainWindow, MainWindowConfig


def build_default_scene() -> Scene:
    scene = Scene()
    scene.add_object(BoxObject.default(ObjectId("box-1")))
    return scene


def main() -> None:
    _scene = build_default_scene()
    window = MainWindow(MainWindowConfig())
    window.show()


if __name__ == "__main__":
    main()
