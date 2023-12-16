from sympy import symbols, Eq, solve, sympify, linear_eq_to_matrix,Symbol,Mul
import numpy as np
from EquationSystem import EquationSystem
from mpmath import mp, matrix

class Parser_Letter:
    def get_equations(self, list_equation):
        equations = []
        for eqn in list_equation:
            try:
                equation = Eq(*map(sympify, eqn.split("=")))
                equations.append(equation)
            except (ValueError, TypeError, SyntaxError):
                print("Invalid equation. Please enter a valid equation.")

        return equations
    
    def getSymbols(self, equations, list_equation):
        symbols_used = list(set().union(*(eq.free_symbols for eq in equations)))
        symbols_to_remove = []  # Create a list to store symbols to be removed

        for equation in list_equation:
            for symbol in symbols_used:
                if symbol in symbols_to_remove:
                    continue
                equation = equation.replace(" ", "")  # remove spaces
                if str(symbol.name[0]) + '*' in equation or '=' + str(symbol) in equation:
                    symbols_to_remove.append(symbol)


        # Remove symbols found in the loop
        for symbol in symbols_to_remove:
            symbols_used.remove(symbol)
        
        ret_symbols=[]
        for symbol in symbols_used:
            ret_symbols.append(symbol.name)

        return symbols_used, ret_symbols
    def matrix2list(self,m):
        a = []
        for i in range(m.rows):
            row = []
            for j in range(m.cols):
                if isinstance(m[i, j], Symbol):
                    row.append(m[i, j].name)
                elif isinstance(m[i,j], Mul):
                    row.append(f'{m[i,j]}')
                else:
                    row.append(m[i, j])
            if(len(row)==1):
                a.append(row[0])
            else:
                a.append(row)
        return a
    def parseEquations(self, list_equation):
        try:
            # Get equations as string inputs from the terminal
            equations = self.get_equations(list_equation)

            # Get the symbols dynamically from the equations
            symbols_used, variables = self.getSymbols(equations, list_equation)

            # Convert equations to matrix form AX = B
            A, B = linear_eq_to_matrix(equations, symbols_used)
        
            a=self.matrix2list(A)
            b=self.matrix2list(B)
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
            
