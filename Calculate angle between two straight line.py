import math

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return None  # Vertical line
    return (y2 - y1) / (x2 - x1)

def angle_between_lines(line1, line2):
    # Unpack line coordinates
    (x1, y1, x2, y2) = line1
    (x3, y3, x4, y4) = line2
    
    # Calculate slopes
    slope1 = calculate_slope(x1, y1, x2, y2)
    slope2 = calculate_slope(x3, y3, x4, y4)
    
    # If both lines are vertical, angle is 90 degrees
    if slope1 is None and slope2 is None:
        return 90
    
    # If one line is vertical, angle depends on the other line
    if slope1 is None:
        return 90 - math.degrees(math.atan(slope2))
    if slope2 is None:
        return 90 - math.degrees(math.atan(slope1))

    # Calculate the angle between the two lines
    angle_radians = math.atan(abs((slope1 - slope2) / (1 + slope1 * slope2)))
    
    # Convert radians to degrees
    angle_degrees = math.degrees(angle_radians)
    
    return angle_degrees

# Example usage
line1 = (1, 2, 4, 5)  # Line 1 defined by points (1, 2) and (4, 5)
line2 = (1, 1, 4, 3)  # Line 2 defined by points (1, 1) and (4, 3)

angle = angle_between_lines(line1, line2)
print(f"The angle between the two lines is: {angle:.2f} degrees")
