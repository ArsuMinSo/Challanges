# vector2.py
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.xy = self.x, self.y

    def __add__(self, other):
        if isinstance(self, other):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            raise TypeError ("Operands must be an instance of Vector2")
    
    def __subtract__(self, other):
        if isinstance(self, other):
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            raise TypeError ("Operands must be an instance of Vector2")
    
    def __multiply__(self, other):
        """scalar multipication"""
        return Vector2(self.x * other.x, self.y * other.y)
    

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"