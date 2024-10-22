import sympy as sp

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
        f = sp.sympify(equation_input)
        
        # Calculate derivative
        derivative_f = sp.diff(f, x)
        
        # Calculate integral
        integral_f = sp.integrate(f, x)
        
        # Calculate limit as x approaches infinity
        limit_f = sp.limit(f, x, sp.oo)
        
        # Print results
        print("\nCalculus Problem Results:")
        print("Function:", f)
        print("Derivative:", derivative_f)
        print("Integral:", integral_f)
        print("Limit as x approaches infinity:", limit_f)
    elif choice == '2':
        # Trigonometry problem
        trig_input = input("Enter your trigonometric equation (e.g., sin(x) = 0.5): ")
        
        # Parsing the equation
        equation = sp.sympify(trig_input)
        
        # Solve the equation
        solutions = sp.solve(equation, x)
        
        # Print results
        print("\nTrigonometry Problem Results:")
        print("Solutions:", solutions)
        
        # Evaluate specific trigonometric functions if needed
        trig_func_input = input("Enter a trigonometric function to evaluate (e.g., sin(pi/6)): ")
        trig_value = sp.sympify(trig_func_input)
        evaluated_value = trig_value.evalf()
        print("Evaluated value:", evaluated_value)
    elif choice == '3':
        # Algebraic equation problem
        algebra_input = input("Enter your algebraic equation (e.g., x**2 - 4 = 0): ")
        
        # Parsing the equation
        equation = sp.sympify(algebra_input)
        
        # Solve the algebraic equation
        solutions = sp.solve(equation, x)
        
        # Print results
        print("\nAlgebraic Equation Results:")
        print("Solutions:", solutions)
    elif choice == '4':
        # Evaluate an expression
        expression_input = input("Enter the expression to evaluate (e.g., 3*x**2 + 2*x + 1): ")
        
        # Parsing the expression
        expression = sp.sympify(expression_input)
        
        # Evaluate the expression at a specific value
        value_input = input("Enter the value of x to evaluate the expression: ")
        value = float(value_input)
        evaluated_result = expression.evalf(subs={x: value})
        print("\nExpression Evaluation Result:")
        print("Expression:", expression)
        print("Evaluated result at x =", value, "is:", evaluated_result)
    else:
        print("Invalid choice! Please choose a number between 1 and 4.")
number =float(input("Enter a number to find cube root");
cube_root_result=cube_root(number);
print(" Cube root is{cube_root_result}")
calculation
area = float(input("Enter the area of the circle to find its radius: "))
radius_result = radius_from_area(area)
print(f"The radius of the circle with area {area} is {radius_result}")


# Take input from user
num = float(input("Enter a number: "))

# Calculate the square root
sqrt_num = math.sqrt(num)

# Print the result
print(f"The square root of {num} is {sqrt_num}")
