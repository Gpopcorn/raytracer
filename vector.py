from __future__ import annotations
from math import sqrt

class Vector:
    __slots__ = ('x', 'y', 'z')
    
    def __init__(self, x: int | float = 0.0, y: int | float = 0.0, z: int | float = 0.0):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self) -> str:
        return f"Vector(x: {self.x}, y: {self.y}, z: {self.z})"
    
    def __add__(self, addend: Vector | int | float) -> Vector:
        if type(addend) == int or type(addend) == float:
            return Vector(self.x + addend, self.y + addend, self.z + addend)
        elif type(addend) == Vector:
            return Vector(self.x + addend.x, self.y + addend.y, self.z + addend.z)
        print("WARNING! You are adding a vector with an unsupported variable type!")
        return Vector(self.x, self.y, self.z)
    
    def __sub__(self, subtrahend: Vector | int | float) -> Vector:
        if type(subtrahend) == int or type(subtrahend) == float:
            return Vector(self.x - subtrahend, self.y - subtrahend, self.z - subtrahend)
        elif type(subtrahend) == Vector:
            return Vector(self.x - subtrahend.x, self.y - subtrahend.y, self.z - subtrahend.z)
        print("WARNING! You are subtracting a vector with an unsupported variable type!")
        return Vector(self.x, self.y, self.z)
    
    def __mul__(self, factor: Vector | int | float) -> Vector:
        if type(factor) == int or type(factor) == float:
            return Vector(self.x * factor, self.y * factor, self.z * factor)
        elif type(factor) == Vector:
            return Vector(self.x * factor.x, self.y * factor.y, self.z * factor.z)
        print("WARNING! You are multiplying a vector with an unsupported variable type!")
        return Vector(self.x, self.y, self.z)
    
    def __truediv__(self, divisor: Vector | int | float) -> Vector:
        if type(divisor) == int or type(divisor) == float:
            return Vector(self.x / (divisor + 0.00000001), self.y / (divisor + 0.00000001), self.z / (divisor + 0.00000001))
        elif type(divisor) == Vector:
            return Vector(self.x / (divisor.x + 0.00000001), self.y / (divisor.y + 0.00000001), self.z / (divisor.z + 0.00000001))
        print("WARNING! You are dividing a vector with an unsupported variable type!")
        return Vector(self.x, self.y, self.z)
    
    def __pow__(self, exponent: Vector | int | float) -> Vector:
        if type(exponent) == int or type(exponent) == float:
            return Vector(self.x ** exponent, self.y ** exponent, self.z ** exponent)
        elif type(exponent) == Vector:
            return Vector(self.x ** exponent.x, self.y ** exponent.y, self.z ** exponent.z)
        print("WARNING! You are powering a vector with an unsupported variable type!")
        return Vector(self.x, self.y, self.z)
    
    def __gt__(self, other: Vector | int | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() > other
        if type(other) == Vector:
            return self.magnitude() > other.magnitude()
        print("WARNING! You are comparing a vector with an unsupported variable type!")
        return False
    
    def __lt__(self, other: Vector | int | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() < other
        if type(other) == Vector:
            return self.magnitude() < other.magnitude()
        print("WARNING! You are comparing a vector with an unsupported variable type!")
        return False
    
    def __gte__(self, other: Vector | int | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() >= other
        if type(other) == Vector:
            return self.magnitude() >= other.magnitude()
        print("WARNING! You are comparing a vector with an unsupported variable type!")
        return False
    
    def __lte__(self, other: Vector | int | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() <= other
        if type(other) == Vector:
            return self.magnitude() <= other.magnitude()
        print("WARNING! You are comparing a vector with an unsupported variable type!")
        return False
    
    def __eq__(self, other: Vector | int | float) -> bool:
        if type(other) == int or type(other) == float:
            return self.magnitude() == other
        if type(other) == Vector:
            return self.magnitude() == other.magnitude()
        print("WARNING! You are comparing a vector with an unsupported variable type!")
        return False
    
    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y, -self.z)
    
    def __pos__(self) -> Vector:
        return Vector(+self.x, +self.y, +self.z)
    
    def __float__(self) -> float:
        return float(self.magnitude())
    
    def __int__(self) -> int:
        return int(self.magnitude())
    
    def dot(self, factor: Vector | int | float) -> int | float:
        if type(factor) == int or type(factor) == float:
            return self.x * factor + self.y * factor + self.z * factor
        elif type(factor) == Vector:
            return self.x * factor.x + self.y * factor.y + self.z * factor.z
        print("WARNING! You are multiplying a vector with an unsupported variable type!")
        return self.x + self.y + self.z
    
    def cross(self, factor: Vector) -> Vector:
        return Vector((self.y * factor.z) - (self.z * factor.y), (self.z * factor.x) - (self.x * factor.z), (self.x * factor.y) - (self.y * factor.x))

    def magnitude(self) -> int | float:
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)
    
    def normalize(self) -> Vector:
        return self / self.magnitude()
    
    def reflect(self, normal: Vector) -> Vector:
        return self - normal * (self.dot(normal)) * 2
    
    def to_rgb(self) -> tuple:
        r, g, b = self.x, self.y, self.z
        if   r < 0: r = 0
        elif r > 1: r = 1
        if   g < 0: g = 0
        elif g > 1: g = 1
        if   b < 0: b = 0
        elif b > 1: b = 1
        return (r * 255, g * 255, b * 255)
