from math import sqrt

from vector import Vector
from ray import Ray

class Sphere:
    __slots__ = ('center', 'radius', 'color')

    def __init__(self, center: Vector, radius: int | float, color: Vector):
        self.center = center
        self.radius = radius
        self.color  = color

    def __repr__(self) -> str:
        return f"Sphere(center: {self.center}, radius: {self.radius}, color: {self.color})"

    def intersection(self, ray: Ray) -> bool | Vector:
        l = self.center - ray.origin
        adj = l.dot(ray.direction)
        d2 = l.dot(l) - (adj * adj)
        radius2 = self.radius * self.radius
        if d2 > radius2:
            return False
        thc = sqrt(radius2 - d2)
        t0 = adj - thc
        t1 = adj + thc
        if t0 < 0 and t1 < 0:
            return False
        distance = t0 if t0 < t1 else t1
        return ray.origin + ray.direction * distance
    
    def get_color(self, hit_position: Vector) -> Vector:
        return self.color
    
    def get_normal(self, hit_position: Vector) -> Vector:
        return (hit_position - self.center).normalize()

class Checkerboard:
    __slots__ = ('y', 'color1', 'color2')
    
    def __init__(self, y: int | float, color1: Vector, color2: Vector):
        self.y      = y
        self.color1 = color1
        self.color2 = color2
        
    def __repr__(self) -> str:
        return f"Checkerboard(y: {self.y}, color1: {self.color1}, color2: {self.color2})"
    
    def intersection(self, ray: Ray) -> bool | Vector:
        if ray.direction.y < 0:
            return False
        distance = self.y - ray.origin.y
        steps = distance / ray.direction.y
        return ray.origin + ray.direction * steps
    
    def get_color(self, hit_position: Vector) -> Vector:
        if round(hit_position.x) % 6 <= 2 and round(hit_position.z) % 6 <= 2 or \
           round(hit_position.x) % 6 >= 3 and round(hit_position.z) % 6 >= 3:
                return self.color2
        return self.color1
    
    def get_normal(self, hit_position: Vector) -> Vector:
        return Vector(0, -1, 0)
