from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ContextMenuAction:
    label: str
    action_id: str


class ContextMenu:
    def __init__(self, actions: list[ContextMenuAction]) -> None:
        self.actions = actions
