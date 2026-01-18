from __future__ import annotations

from dataclasses import dataclass
from typing import NewType

from .transforms import Transform, Vec3

ObjectId = NewType("ObjectId", str)


@dataclass
class BoxObject:
    id: ObjectId
    name: str
    transform: Transform
    size: Vec3

    @staticmethod
    def default(object_id: ObjectId, name: str = "Box") -> "BoxObject":
        return BoxObject(
            id=object_id,
            name=name,
            transform=Transform.identity(),
            size=Vec3(1.0, 1.0, 1.0),
        )
