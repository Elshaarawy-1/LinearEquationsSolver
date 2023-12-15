from sympy import symbols, Eq, solve, sympify, linear_eq_to_matrix
import numpy as np

def get_equations(num_equations):
    equations = []
    for i in range(num_equations):
        while True:
            try:
                equation_str = input(f"Enter equation {i + 1}: ")
                equation = Eq(*map(sympify, equation_str.split("=")))
                equations.append(equation)
                break
            except (ValueError, TypeError, SyntaxError):
                print("Invalid equation. Please enter a valid equation.")

    return equations

while True:
    try:
        # Get the number of equations from the user
        num_equations = int(input("Enter the number of equations: "))
        if num_equations <= 0:
            raise ValueError("Number of equations must be a positive integer.")

        # Get equations as string inputs from the terminal
        equations = get_equations(num_equations)

        # Get the symbols dynamically from the equations
        symbols_used = list(set().union(*(eq.free_symbols for eq in equations)))

        # Convert equations to matrix form AX = B
        A, B = linear_eq_to_matrix(equations, symbols_used)

        # Solve the system of equations
        solution = solve(equations, symbols_used)

        # Display the coefficient matrix (A)
        print("Coefficient Matrix (A):")
        print(A)

        # Display the variable matrix (X)
        print("Variable Matrix (X):")
        print(symbols_used)

        # Display the constant matrix (B)
        print("Constant Matrix (B):")
        print(B)

        # Display the solution
        # print("Solution:")
        # for symbol in symbols_used:
        #     print(f"{symbol} = {solution[symbol]}")

        break
    except (ValueError, TypeError):
        print("Invalid input. Please enter a valid positive integer for the number of equations.")
    except Exception as e:
        print(f"An error occurred: {e}")