# world_edit/region.py

def fill(mc, start, end, block):
    x1, y1, z1 = start
    x2, y2, z2 = end
    mc.setBlocks(x1, y1, z1, x2, y2, z2, block.id, block.data)
