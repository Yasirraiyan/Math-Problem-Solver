import math

def cylinder_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (height + radius)
    return surface_area

# Example usage
radius = 5  # Replace with your desired radius
height = 10  # Replace with your desired height
area = cylinder_surface_area(radius, height)
print(f"The surface area of the cylinder with radius {radius} and height {height} is: {area}")
