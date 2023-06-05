from vector import Vector

class Ray:
    __slots__ = ('origin', 'direction')
    
    def __init__(self, origin: Vector, direction: Vector):
        self.origin    = origin
        self.direction = direction.normalize()
        
    def __repr__(self) -> str:
        return f"Ray(origin: {self.origin}, direction: {self.direction})"
    
    def cast(self, objects: list) -> tuple:
        for object in objects:
            intersect = object.intersection(self)
            if intersect:
                return intersect, object
        return False, False

