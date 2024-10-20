equation = sp.sympify(trig_input)
     print("\nTrigonometry Problem Results:")
        print("Solutions:", solutions)
 trig_func_input = input("Enter a trigonometric function to evaluate (e.g., sin(pi/6)): ")
        trig_value = sp.sympify(trig_func_input)
        evaluated_value = trig_value.evalf()
        print("Evaluated value:", evaluated_value)
        
