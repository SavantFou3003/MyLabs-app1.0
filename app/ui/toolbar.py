from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ToolbarState:
    progress: float = 0.0
    mode: str = "select_object"


class Toolbar:
    def __init__(self, state: ToolbarState) -> None:
        self.state = state

    def set_mode(self, mode: str) -> None:
        self.state.mode = mode
