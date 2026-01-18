from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MainWindowConfig:
    title: str = "3D Editor"
    width: int = 1280
    height: int = 720


class MainWindow:
    def __init__(self, config: MainWindowConfig) -> None:
        self.config = config

    def show(self) -> None:
        """Placeholder for Qt main window display."""
