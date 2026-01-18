from __future__ import annotations

import json

from app.core.scene import Scene


def serialize_scene(scene: Scene) -> str:
    payload = {
        "objects": {key: obj.name for key, obj in scene.objects.items()},
        "links": {key: link.object_a for key, link in scene.links.items()},
    }
    return json.dumps(payload, indent=2)
