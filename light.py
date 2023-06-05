from vector import Vector

class Light:
    __slots__ = ('direction', 'strength')
    
    def __init__(self, direction: Vector, strength: int | float):
        self.direction = direction.normalize()
        self.strength = strength
        
    def __repr__(self) -> str:
        return f"Light(direction: {self.direction})"

