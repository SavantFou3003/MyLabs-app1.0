from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable


@dataclass
class Command:
    name: str
    execute: Callable[[], None]
    undo: Callable[[], None]


@dataclass
class CommandStack:
    stack: list[Command] = field(default_factory=list)
    index: int = -1

    def do(self, command: Command) -> None:
        self.stack = self.stack[: self.index + 1]
        self.stack.append(command)
        self.index += 1
        command.execute()

    def undo(self) -> None:
        if self.index < 0:
            return
        command = self.stack[self.index]
        command.undo()
        self.index -= 1

    def redo(self) -> None:
        if self.index + 1 >= len(self.stack):
            return
        self.index += 1
        command = self.stack[self.index]
        command.execute()
