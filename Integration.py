def main():
    # Define the variable
    x = sp.symbols('x')
    print("Choose an option:")
    print("1. Solve a calculus problem")
 choice = input("Enter your choice (1-4): ")
    if choice == '1':
equation_input = input("Enter your calculus equation in terms of x (e.g., sin(x) + ln(x)): ")
        f = sp.sympify(equation_input)
integral_f = sp.integrate(f, x)
print("Integral:", integral_f)
