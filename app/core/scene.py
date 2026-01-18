from __future__ import annotations

from dataclasses import dataclass, field

from .links import Link, LinkId
from .objects import BoxObject, ObjectId
from .selection import FaceSelection


@dataclass
class Scene:
    objects: dict[ObjectId, BoxObject] = field(default_factory=dict)
    links: dict[LinkId, Link] = field(default_factory=dict)
    active_object: ObjectId | None = None
    active_face: FaceSelection | None = None
    active_link: LinkId | None = None

    def add_object(self, obj: BoxObject) -> None:
        self.objects[obj.id] = obj

    def add_link(self, link: Link) -> None:
        self.links[link.id] = link
