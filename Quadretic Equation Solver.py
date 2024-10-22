import cmath  # To handle complex number

# Coefficients
a = 1
b = -3
c = 2

# Calculate the discriminant
D = b**2 - 4*a*c

# Calculate the roots
if D > 0:
    root1 = (-b + cmath.sqrt(D)) / (2 * a)
    root2 = (-b - cmath.sqrt(D)) / (2 * a)
    print(f"The roots are real and different: {root1} and {root2}")
elif D == 0:
    root = -b / (2 * a)
    print(f"The root is real and the same: {root}")
else:
    real_part = -b / (2 * a)
    imaginary_part = cmath.sqrt(-D) / (2 * a)
    root1 = real_part + imaginary_part * 1j
    root2 = real_part - imaginary_part * 1j
    print(f"The roots are complex: {root1} and {root2}")
