import math

def cone_surface_area(radius, height):
    # Calculate the slant height
    slant_height = math.sqrt(radius**2 + height**2)
    
    # Calculate the surface area
    surface_area = math.pi * radius * (radius + slant_height)
    return surface_area

# Example usage
radius = 5  # Replace with your desired radius
height = 10  # Replace with your desired height
area = cone_surface_area(radius, height)
print(f"The surface area of the cone with radius {radius} and height {height} is: {area}")
