# vector2.py

from math import sqrt

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.xyz = (x, y, z)

    def __add__(self, other):
        if isinstance(self, type(other)):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Operands must be an instance of Vector3")
    
    def __subtract__(self, other):
        if isinstance(self, type(other)):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("Operands must be an instance of Vector3")
    
    def dotProduct(self, other):
        if isinstance(self, type(other)):
            return Vector2(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            raise TypeError("Operands must be an instance of Vector3")
        
    def crossProuct(self, other): #normal vector to the plane created by 2 vectors
        if isinstance(self, type(other)):
            x, y, z = self.xyz
            ox, oy, oz = other.xyz
            return Vector3(y * oz - 
                           self.x * other.y - self.y * self.x)
        else:
            raise TypeError("Operands must be an instance of Vector3")

    def multyplyByScalar(self, operand):
        if type(operand) == int:
            return Vector2(self.x * operand, self.y * operand)
        else:
            raise TypeError("Operand must be a number")

    def magnitude(self) -> int:
        return sqrt(self.x**2 + self.y**2)

    def mormalize(self):
        magnitude = self.magnitude
        return Vector2(self.x / self.magnitude, self.y / self.magnitude)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xy = self.x, self.y

    def __add__(self, other):
        if isinstance(self, type(other)):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Operands must be an instance of Vector2")
    
    def __subtract__(self, other):
        if isinstance(self, type(other)):
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Operands must be an instance of Vector2")
    
    def dotProduct(self, other):
        if isinstance(self, type(other)):
            return Vector2(self.x * other.x, self.y * other.y)
        else:
            raise TypeError("Operands must be an instance of Vector2")
        
    def crossProuct(self, other): #normal vector to the plane created by 2 vectors
        return Vector3(0, 0, self.x * other.y - self.y * self.x)

    def multyplyByScalar(self, operand):
        if type(operand) == int:
            return Vector2(self.x * operand, self.y * operand)
        else:
            raise TypeError("Operand must be a number")

    def magnitude(self) -> int:
        return sqrt(self.x**2 + self.y**2)

    def mormalize(self):
        magnitude = self.magnitude
        return Vector2(self.x / self.magnitude, self.y / self.magnitude)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"