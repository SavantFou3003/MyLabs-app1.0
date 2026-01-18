# Architecture d'un éditeur 3D procédural (Python + Qt + OpenGL)

Ce document décrit une architecture complète pour un éditeur 3D desktop en Python, sans moteur de jeu externe, basé sur Qt (PyQt/PySide) et une vue 3D OpenGL (via `QOpenGLWidget` + OpenGL modern, ou `pyqtgraph.opengl`). L'objectif est de structurer clairement **données**, **calculs**, **affichage** et **flux d'événements** pour un éditeur modulaire et maintenable.

## 1. Objectifs clefs

- **Éditeur 3D interactif** (rotation caméra, zoom, déplacement).
- **Création et édition de pavés droits** (position, taille, rotation).
- **Sélection d'objets, de faces et de liaisons**.
- **Liaisons paramétrables** (contraintes de translation et rotation, référentiel local ou global).
- **Visualisation claire** (sol damier, gizmos, points de liaison).
- **Architecture modulaire** (données séparées des calculs et du rendu).

---

## 2. Vue d'ensemble des modules

```
app/
  main.py
  ui/
    main_window.py
    toolbar.py
    left_panel.py
    viewport.py
    context_menu.py
  core/
    scene.py
    objects.py
    links.py
    constraints.py
    transforms.py
    selection.py
    events.py
  render/
    gl_scene.py
    gl_meshes.py
    gl_gizmos.py
    gl_materials.py
    gl_picking.py
  services/
    command_stack.py
    presets.py
    serializer.py
    settings.py
```

### Rôles principaux
- **`core/`** : données + calculs (état, contraintes, résolution).
- **`render/`** : affichage OpenGL, picking, gizmos.
- **`ui/`** : composants Qt (toolbar, panneau latéral, vue 3D).
- **`services/`** : services transverses (undo/redo, presets, sauvegarde).

---

## 3. Modèle de données (Données pures)

### 3.1 `Scene`

```python
class Scene:
    objects: dict[ObjectId, BoxObject]
    links: dict[LinkId, Link]
    active_object: ObjectId | None
    active_face: FaceSelection | None
    active_link: LinkId | None
```

### 3.2 `BoxObject`

```python
class BoxObject:
    id: ObjectId
    name: str
    transform: Transform
    size: Vec3  # largeur, hauteur, profondeur
    mesh_ref: MeshHandle
```

### 3.3 `Link`

```python
class Link:
    id: LinkId
    object_a: ObjectId
    object_b: ObjectId
    face_a: FaceId
    constraints: LinkConstraints
    frame: LinkFrame  # local ou global
    pivot: Vec3  # point central de liaison
```

### 3.4 `LinkConstraints`

```python
class AxisConstraint:
    mode: Literal['locked', 'free', 'limited']
    min_val: float | None
    max_val: float | None

class LinkConstraints:
    translation: dict[Axis, AxisConstraint]
    rotation: dict[Axis, AxisConstraint]
```

### 3.5 `Transform`

```python
class Transform:
    position: Vec3
    rotation: Vec3  # Euler (deg)
    scale: Vec3
```

---

## 4. Calculs et contraintes (cinématique)

### 4.1 `ConstraintSolver`

Responsable de :
- appliquer les contraintes lors d'un déplacement/rotation
- calculer la pose finale d'un objet lié
- clamp ou bloquer des degrés de liberté

```python
class ConstraintSolver:
    def apply_constraints(
        self,
        link: Link,
        source: Transform,
        target: Transform,
        reference_frame: Frame
    ) -> Transform:
        # Clamp translation and rotation depending on constraints
        return constrained_transform
```

### 4.2 Résolution des mouvements

Flux général :
1. L'utilisateur déplace un objet (A).
2. Les liaisons impliquant A sont vérifiées.
3. Pour chaque liaison, on calcule la transformation autorisée pour l'objet B.
4. Les degrés de liberté interdits sont bloqués, les limités sont clampés.

---

## 5. Rendu OpenGL

### 5.1 `GLScene`

- gère la caméra
- dessine le sol damier
- affiche les meshes des objets
- dessine les sphères de liaison
- dessine les gizmos (axes, boîte de sélection)

### 5.2 Picking (sélection)

Deux méthodes possibles :
- **Color picking** : chaque objet/face a un ID unique encodé en couleur dans une passe hors écran.
- **Ray casting** : intersection ray/mesh (plus complexe, plus précis).

---

## 6. UI et flux d'événements

### 6.1 Barre supérieure

- bouton "Créer pavé droit"
- toggles de mode (sélection objet, sélection face, création liaison)

### 6.2 Panneau latéral

Affichage dynamique :
- paramètres d'objet (position/rotation/scale)
- paramètres d'une liaison (contraintes)

### 6.3 Événements principaux

```
MouseClick -> SelectionManager -> update Scene.active_*
Scene change -> UI refresh (left panel)
Transform edit -> ConstraintSolver -> apply
Render loop -> GLScene redraw
```

---

## 7. Presets de liaison

Dans `services/presets.py` :

```python
def fixed_joint():
    return LinkConstraints(
        translation=all_locked,
        rotation=all_locked
    )

def pivot(axis):
    return LinkConstraints(
        translation=all_locked,
        rotation={axis: free, others: locked}
    )

def slider(axis):
    return LinkConstraints(
        translation={axis: free, others: locked},
        rotation=all_locked
    )

def ball_socket():
    return LinkConstraints(
        translation=all_locked,
        rotation=all_free
    )
```

---

## 8. Séparation claire (Data / Logic / Render)

| Couche | Rôle | Exemple |
|-------|------|---------|
| Données | état brut | `Scene`, `BoxObject`, `Link` |
| Calculs | cinématique | `ConstraintSolver` |
| Affichage | OpenGL | `GLScene`, `GLMeshes` |
| UI | Qt widgets | `MainWindow`, `LeftPanel` |

---

## 9. Flux complet d'interaction

1. L'utilisateur crée un pavé → `Scene.objects.add()` → `GLScene` crée un mesh.
2. L'utilisateur clique → `SelectionManager` identifie l'objet/face.
3. UI met à jour panneau gauche avec paramètres.
4. L'utilisateur modifie un paramètre → `ConstraintSolver` applique → scène mise à jour.
5. Liaisons visibles en continu (sphère orange entre objets).

---

## 10. Extensibilité

- Ajouter d'autres primitives (sphère, cylindre) dans `core/objects.py`.
- Ajouter un export (JSON/GLTF) via `services/serializer.py`.
- Ajouter un système de gizmos plus complet (translation/rotation/scale).
- Ajouter un solveur plus avancé (IK chain, contraintes multi-axes).

---

## 11. Résumé

Cette architecture propose :
- une séparation stricte **données / calculs / rendu / UI**
- un système robuste de **liaisons paramétrables**
- un flux d'événements clair et maintenable
- une base extensible pour un éditeur 3D procédural complet en Python + Qt + OpenGL.
