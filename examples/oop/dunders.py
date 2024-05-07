class Vector:
    def __init__(self, x, y):
        """Initialize a vector with x and y coordinates."""
        self.x = x
        self.y = y

    def __add__(self, other):
        """Override + operator to add two vectors."""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __eq__(self, other):
        """Override == operator to compare two vectors."""
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __str__(self):
        """Override str() function to provide a custom string representation."""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Override repr() function for an unambiguous representation."""
        return f"Vector({self.x!r}, {self.y!r})"

# Example usage of the Vector class
vector1 = Vector(2, 3)
vector2 = Vector(4, 5)

# Demonstrate addition
result_add = vector1 + vector2
print("vector1 + vector2 =", result_add)

# Demonstrate equality comparison
print("vector1 == vector2:", vector1 == vector2)
print("vector1 == Vector(2, 3):", vector1 == Vector(2, 3))

# Demonstrate string representation
print("String representation of vector1:", str(vector1))
print("Repr representation of vector1:", repr(vector1))
