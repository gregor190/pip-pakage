# world_edit/__init__.py 🤓

__version__ = "0.2.0"
__author__ = "Gregor the Terrain Bender"

from .block import Block, STONE, RED_WOOL
from .region import fill
from .brush import solid_brush, chaos_brush
from .structure import save_structure, load_structure
from .utils import Vec3
from .random_world_generation import generate_world

__all__ = [
    "Block", "STONE", "RED_WOOL",
    "fill",
    "solid_brush", "chaos_brush",
    "save_structure", "load_structure",
    "Vec3",
    "generate_world"
]

print(f"world_edit v{__version__} loaded 🤓 — ready to terraform like a boss.")
