from __future__ import annotations

from dataclasses import dataclass

from .links import FaceId
from .objects import ObjectId


@dataclass
class FaceSelection:
    object_id: ObjectId
    face_id: FaceId
