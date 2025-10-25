
import math

class Vector2D:
    """A class to represent a 2D vector."""

    def __init__(self, x: float, y: float):
        """Initializes a new Vector2D object."""
        self.x = x
        self.y = y

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        """Adds two vectors."""
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        """Subtracts two vectors."""
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> 'Vector2D':
        """Multiplies a vector by a scalar."""
        return Vector2D(self.x * scalar, self.y * scalar)

    def __str__(self) -> str:
        """Returns a string representation of the Vector2D object."""
        return f"Vector2D(x={self.x}, y={self.y})"

