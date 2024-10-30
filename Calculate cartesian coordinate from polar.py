import math

def polar_to_cartesian(r, theta):
    x = r * math.cos(theta)     # x-coordinate
    y = r * math.sin(theta)     # y-coordinate
    return (x, y)

# Example usage:
r, theta = 5, math.radians(30)  # Radius and angle in radians
cartesian_coordinates = polar_to_cartesian(r, theta)
print(f"x: {cartesian_coordinates[0]}, y: {cartesian_coordinates[1]}")
