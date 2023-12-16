from sympy import symbols, Eq, solve, sympify, linear_eq_to_matrix
import mpmath
from EquationSystem import EquationSystem
import numpy as np
class Parser:
    def get_equations(self, list_equation):
        equations = []
        for eqn in list_equation:
            try:
                equation = Eq(*map(sympify, eqn.split("=")))
                equations.append(equation)
            except (ValueError, TypeError, SyntaxError):
                print("Invalid equation. Please enter a valid equation.")

        return equations
    def matrix2numpy(self,m):
        a = np.empty(m.shape)
        for i in range(m.rows):
            for j in range(m.cols):
                a[i, j] = m[i, j]
        return a
    
    def parseEquations(self, list_equation):
        try:
            # Get equations as string inputs from the terminal
            equations = self.get_equations(list_equation)

            # Get the symbols dynamically from the equations
            symbols_used = list(set().union(*(eq.free_symbols for eq in equations)))

            # Convert equations to matrix form AX = B
            A, B = linear_eq_to_matrix(equations, symbols_used)
            a=mpmath.matrix(A.tolist())
            b=mpmath.matrix(B.tolist())
            variables=symbols_used # convert to np array
            if (len(variables) != len(list_equation)):
                raise Exception("Number of equations not equal number of variables")
            return EquationSystem(a,b,variables)
            # Solve the system of equations
            # solution = solve(equations, symbols_used)

            # # Display the coefficient matrix (A)
            # print("Coefficient Matrix (A):")
            # print(A)

            # # Display the variable matrix (X)
            # print("Variable Matrix (X):")
            # print(symbols_used)

            # # Display the constant matrix (B)
            # print("Constant Matrix (B):")
            # print(B)

            # # Display the solution
            # print("Solution:")
            # for symbol in symbols_used:
            #     print(f"{symbol} = {solution[symbol]}")

        except Exception as e:
            print(f"An error occurred: {e}")
            
