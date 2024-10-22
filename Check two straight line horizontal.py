import math

def calculate_slope(x1, y1, x2, y2):
    """Calculate the slope of the line defined by two points."""
    if x2 - x1 == 0:
        return None  # Vertical line
    return (y2 - y1) / (x2 - x1)

def are_lines_horizontal(line1, line2):
    """Check if both lines are horizontal."""
    slope1 = calculate_slope(*line1)
    slope2 = calculate_slope(*line2)

    # Check if both slopes are zero (indicating horizontal lines)
    if slope1 == 0 and slope2 == 0:
        return True
    return False

def angle_between_lines(line1, line2):
    """Calculate the angle between two lines defined by their endpoints."""
    slope1 = calculate_slope(*line1)
    slope2 = calculate_slope(*line2)

    # Handle cases where slopes are None (vertical lines)
    if slope1 is None and slope2 is None:
        return 90
    if slope1 is None:
        return 90 - math.degrees(math.atan(slope2))
    if slope2 is None:
        return 90 - math.degrees(math.atan(slope1))

    # Calculate the angle between the two lines
    angle_radians = math.atan(abs((slope1 - slope2) / (1 + slope1 * slope2)))
    angle_degrees = math.degrees(angle_radians)
    
    return angle_degrees

# Example usage
if __name__ == "__main__":
    line1 = (1, 2, 3, 2)  # Horizontal line (y = 2)
    line2 = (4, 2, 5, 2)  # Horizontal line (y = 2)
    line3 = (1, 3, 4, 1)  # Not horizontal line

    print(f"Are both lines horizontal? {are_lines_horizontal(line1, line2)}")  # True
    print(f"Are line1 and line3 horizontal? {are_lines_horizontal(line1, line3)}")  # False

    angle = angle_between_lines(line1, line2)
    print(f"The angle between line1 and line2 is: {angle:.2f} degrees")  # Should be 0 degrees
