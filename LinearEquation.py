# from Parser_NoLetter import Parser
from Parser_Letter import Parser

from EquationSystem import *
import numpy as np
from mpmath import mp

parser = Parser()
equations = input() # get from GUI

list_equation = equations.split(",")

A,B,variables=parser.parseEquations(list_equation)
system_of_equations = EquationSystem(A,B,variables)

# for item in system_of_equations.variables:
#     print(f"Item: {item}, Type: {type(item)}")
# print (type(system_of_equations))
# print(system_of_equations.A)
# print(system_of_equations.B)
# print(system_of_equations.variables)
# print(type(system_of_equations.A))
# print(type(system_of_equations.B))
# print(type(system_of_equations.variables))