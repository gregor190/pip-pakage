# world_edit/block.py

class Block:
    def __init__(self, block_id, data=0):
        self.id = block_id
        self.data = data

    def __repr__(self):
        return f"Block({self.id}, {self.data})"

# Assets
STONE = Block(1)
RED_WOOL = Block(35, 14)
