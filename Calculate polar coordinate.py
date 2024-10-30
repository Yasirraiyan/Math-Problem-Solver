import math

def cartesian_to_polar(x, y):
    r = math.sqrt(x**2 + y**2)          # Radius
    theta = math.atan2(y, x)             # Angle in radians
    return (r, theta)

# Example usage:
x, y = 3, 4
polar_coordinates = cartesian_to_polar(x, y)
print(f"Radius: {polar_coordinates[0]}, Angle (radians): {polar_coordinates[1]}")
