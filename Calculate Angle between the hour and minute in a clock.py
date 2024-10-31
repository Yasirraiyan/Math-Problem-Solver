def clock_angle(hours, minutes):
    # Ensure hours are within 1-12
    hours = hours % 12
    
    # Calculate positions of the hour and minute hands
    hour_angle = 30 * hours + 0.5 * minutes
    minute_angle = 6 * minutes
    
    # Calculate the difference and find the smaller angle
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)

# Example usage
print(clock_angle(3, 15))  # Output: 7.5
