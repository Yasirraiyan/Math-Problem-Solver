import math

def sphere_surface_area(radius):
    surface_area = 4 * math.pi * (radius ** 2)
    return surface_area

# Example usage
radius = 5  # Replace with your desired radius
area = sphere_surface_area(radius)
print(f"The surface area of the sphere with radius {radius} is: {area}")
