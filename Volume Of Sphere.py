import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

# Example usage
radius = 5  # Replace with your desired radius
volume = sphere_volume(radius)
print(f"The volume of the sphere with radius {radius} is: {volume}")
