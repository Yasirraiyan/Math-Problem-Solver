import math

def cylinder_volume(radius, height):
    volume = math.pi * (radius ** 2) * height
    return volume

# Example usage
radius = 5  # Replace with your desired radius
height = 10  # Replace with your desired height
volume = cylinder_volume(radius, height)
print(f"The volume of the cylinder with radius {radius} and height {height} is: {volume}")
