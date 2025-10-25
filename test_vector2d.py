
from vector2d import Vector2D

# Creating two vectors
vector1 = Vector2D(2, 3)
vector2 = Vector2D(4, 1)

# Adding two vectors
vector_sum = vector1 + vector2
print(vector_sum)  # Output: Vector2D(x=6, y=4)

# Subtracting two vectors
vector_diff = vector1 - vector2
print(vector_diff)  # Output: Vector2D(x=-2, y=2)

# Scalar multiplication
vector_scaled = vector1 * 3
print(vector_scaled)  # Output: Vector2D(x=6, y=9)

