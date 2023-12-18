from sympy import symbols, Eq, solve, sympify, linear_eq_to_matrix
import mpmath
from parser.EquationSystem import EquationSystem
from parser.parser_letter import Parser_Letter
import numpy as np
from mpmath import mp, matrix
from solvers.gauss_with_letter_solver import GaussianLetter

if __name__ == '__main__':
    print("enter equations: ")
    while True:
        equations = input()
        list_equation = equations.split(',')
        parser = Parser_Letter()
        system=parser.parseEquations(list_equation)
        print(system.A)
        print(system.B)
        print(system.variables)
        letter_solver=GaussianLetter(np.array(system.A),np.array(system.B))
        letter_solver.solve()