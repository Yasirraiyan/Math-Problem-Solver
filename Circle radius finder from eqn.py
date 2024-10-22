import math

# Function to find radius from the circle equation (x-h)^2 + (y-k)^2 = r^2
def find_radius(a, b, c):
    # a and b are the coordinates of the center (h, k)
    # c is the constant on the right-hand side of the equation (r^2)
    return math.sqrt(c)

# Input the values of the equation
h = float(input("Enter the x-coordinate of the center (h): "))
k = float(input("Enter the y-coordinate of the center (k): "))
c = float(input("Enter the value of the constant (r^2) in the equation: "))

# Calculate the radius
radius = find_radius(h, k, c)
print(f"The radius of the circle is {radius}")
