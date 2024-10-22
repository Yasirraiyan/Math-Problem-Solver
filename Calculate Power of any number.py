
def power(a, x):
    return a ** x


a = float(input("Enter the base (a != 0): "))
x = float(input("Enter the exponent (x is a real number): "))


result = power(a, x)
print(f"The result of {a}^{x} is: {result}")
