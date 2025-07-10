# world_edit/utils.py 🤓

import math
import random

class Vec3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vec3(self.x * scalar, self.y * scalar, self.z * scalar)

    def distance_to(self, other):
        return math.sqrt(
            (self.x - other.x)**2 +
            (self.y - other.y)**2 +
            (self.z - other.z)**2
        )

    def as_tuple(self):
        return (self.x, self.y, self.z)

    def jitter(self, amount=1):
        """Adds random offset to each axis."""
        return Vec3(
            self.x + random.randint(-amount, amount),
            self.y + random.randint(-amount, amount),
            self.z + random.randint(-amount, amount)
        )

    def __repr__(self):
        return f"Vec3({self.x}, {self.y}, {self.z})"
