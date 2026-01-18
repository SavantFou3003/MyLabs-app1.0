from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import NewType

from .constraints import LinkConstraints
from .objects import ObjectId
from .transforms import Vec3

LinkId = NewType("LinkId", str)
FaceId = NewType("FaceId", str)


class LinkFrame(str, Enum):
    LOCAL = "local"
    GLOBAL = "global"


@dataclass
class Link:
    id: LinkId
    object_a: ObjectId
    object_b: ObjectId
    face_a: FaceId
    constraints: LinkConstraints
    frame: LinkFrame
    pivot: Vec3
