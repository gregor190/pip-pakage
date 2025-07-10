# world_edit/brush.py 🤓

import random
from world_edit.region import fill
from world_edit.block import STONE, RED_WOOL, GRASS

def solid_brush(mc, center, size, block=STONE):
    """Paints a solid cube of blocks centered at 'center'."""
    x, y, z = center
    for dx in range(-size, size + 1):
        for dy in range(-size, size + 1):
            for dz in range(-size, size + 1):
                fill(mc, (x + dx, y + dy, z + dz), (x + dx, y + dy, z + dz), block)

def chaos_brush(mc, center, size, palette=[STONE, RED_WOOL, GRASS]):
    """Paints a cube with random blocks from a palette."""
    x, y, z = center
    for dx in range(-size, size + 1):
        for dy in range(-size, size + 1):
            for dz in range(-size, size + 1):
                block = random.choice(palette)
                fill(mc, (x + dx, y + dy, z + dz), (x + dx, y + dy, z + dz), block)
