def main():
    # Define the variable
    x = sp.symbols('x')
    print("Choose an option:")
    print("1. Solve a calculus problem")
    print("2. Solve a trigonometry problem")
    print("3. Solve an algebraic equation")
    print("4. Evaluate an expression")
    
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        # Calculus problem
        equation_input = input("Enter your calculus equation in terms of x (e.g., sin(x) + ln(x)): ")
