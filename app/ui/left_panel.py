from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LeftPanelState:
    visible: bool = False
    selection_kind: str | None = None


class LeftPanel:
    def __init__(self, state: LeftPanelState) -> None:
        self.state = state

    def show_for(self, selection_kind: str) -> None:
        self.state.visible = True
        self.state.selection_kind = selection_kind

    def hide(self) -> None:
        self.state.visible = False
        self.state.selection_kind = None
