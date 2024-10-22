import math

def calculate_angle(x1, y1, x2, y2):
    # Calculate the change in coordinates
    delta_y = y2 - y1
    delta_x = x2 - x1

    # Calculate the angle in radians
    angle_radians = math.atan2(delta_y, delta_x)

    # Convert radians to degrees
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees

# Example usage
x1, y1 = 1, 2
x2, y2 = 4, 6
angle = calculate_angle(x1, y1, x2, y2)
print(f"The angle of the line with respect to the x-axis is: {angle} degrees")
