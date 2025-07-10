# world_edit/random_world_generation.py 🤓

import random
from world_edit.block import GRASS, STONE, DIRT
from world_edit.region import fill

def generate_world(mc, width, depth, max_height=6):
    """Generates a randomized terrain world."""
    for x in range(width):
        for z in range(depth):
            height = random.randint(1, max_height)
            for y in range(height):
                block = STONE if y < height - 1 else GRASS
                fill(mc, (x, y, z), (x, y, z), block)
