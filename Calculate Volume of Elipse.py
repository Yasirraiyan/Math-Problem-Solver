import math

def calculate_volume_of_elipse(a, b, c):
    volume = (4/3) * math.pi * a * b * c
    return volume

volume = ellipsoid_volume(a, b, c)
print(f"The volume of the ellipsoid with axes {a}, {b}, and {c} is: {volume}")
