from __future__ import annotations

from dataclasses import dataclass

from .objects import ObjectId
from .selection import FaceSelection


@dataclass
class ObjectSelected:
    object_id: ObjectId


@dataclass
class FaceSelected:
    selection: FaceSelection


@dataclass
class LinkSelected:
    link_id: str
