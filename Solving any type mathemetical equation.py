import sympy as sp

def solve_equation(equation_str, variable_str):
    # Define the variable symbol
    variable = sp.Symbol(variable_str)
    
    # Parse the equation string and create a sympy equation
    equation = sp.sympify(equation_str)
    
    # Solve the equation for the given variable
    solutions = sp.solve(equation, variable)
    
    return solutions

# Example usage
equation_str = input("Enter the equation (e.g., x**2 - 4): ")
variable_str = input("Enter the variable to solve for (e.g., x): ")

# Solve the equation
solutions = solve_equation(equation_str, variable_str)

print(f"Solutions for the equation {equation_str} = 0: {solutions}")
