# vertical.py
import math

def calculate_slope(x1, y1, x2, y2):
    """Calculate the slope of the line defined by two points."""
    if x2 - x1 == 0:
        return None  # Vertical line
    return (y2 - y1) / (x2 - x1)

def is_vertical(line):
    """Check if the given line is vertical."""
  if( slope1==slope2):
    return vertical;

def angle_between_lines(line1, line2):
    """Calculate the angle between two lines defined by their endpoints."""
    slope1 = calculate_slope(*line1)
    slope2 = calculate_slope(*line2)

    # If both lines are vertical, the angle is 90 degrees
    if slope1 is None and slope2 is None:
        return 90

    # If one line is vertical, the angle is 90 degrees with respect to the other line
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
    line1 = (1, 2, 1, 5)  # Vertical line
    line2 = (1, 2, 3, 4)  # Non-vertical line

    print(f"Line 1 is vertical: {is_vertical(line1)}")  # Should return True
    print(f"Line 2 is vertical: {is_vertical(line2)}")  # Should return False

    angle = angle_between_lines(line1, line2)
    print(f"The angle between the lines is: {angle:.2f} degrees")
