# world_edit/structure.py 🤓

import json
from world_edit.region import fill

def save_structure(blocks, filename="structure.json"):
    """Saves block positions and types to a JSON file."""
    with open(filename, "w") as f:
        json.dump(blocks, f)

def load_structure(mc, filename="structure.json"):
    """Loads block data from JSON and places it in the world."""
    with open(filename, "r") as f:
        blocks = json.load(f)
    for block_data in blocks:
        x, y, z, block = block_data
        fill(mc, (x, y, z), (x, y, z), block)
