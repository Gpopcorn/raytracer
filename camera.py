from math import tan, radians

from vector import Vector
from ray import Ray

class Camera:
    __slots__ = ('position', 'screen_size', 'fov')
    
    def __init__(self, position: Vector, screen_size: Vector, fov: int | float = 60.0):
        self.position    = position
        self.screen_size = screen_size
        self.fov         = fov
        
    def __repr__(self) -> str:
        return f"Camera(position: {self.position}, screen_size: {self.screen_size}, fov: {self.fov})"
        
    def get_direction(self, x_y: Vector) -> Ray:
        xy = x_y - self.screen_size / 2
        z  = self.screen_size.y / tan(radians(self.fov) / 2)
        return Ray(self.position, Vector(xy.x, xy.y, -z).normalize())
