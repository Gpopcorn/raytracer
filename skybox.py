from math import atan2, asin, pi
from numpy import asarray
from PIL import Image

from vector import Vector

class Skybox:
    __slots__ = ('path', 'array', 'size')
    
    def __init__(self, path: str):
        self.path  = path
        image      = Image.open(self.path)
        self.array = asarray(image)
        self.size  = image.size

    def get_image_coords(self, normal: Vector) -> Vector:
        u = 0.5 + atan2(normal.z, normal.x) / (2 * pi)
        v = 0.5 + asin(normal.y) / pi
        image_position = (int(u * self.size[0]), int(v * self.size[1]))
        color = self.array[image_position[1]][image_position[0]]
        return Vector(color[0], color[1], color[2]) / 255
