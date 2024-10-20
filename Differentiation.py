choice = input("Enter your choice (1-4): ")
    if choice == '1':
        # Calculus problem
        equation_input = input("Enter your calculus equation in terms of x (e.g., sin(x) + ln(x)): ")
        f = sp.sympify(equation_input)
        
        # Calculate derivative
        derivative_f = sp.diff(f, x)
        print("Derivative:", derivative_f)
        
