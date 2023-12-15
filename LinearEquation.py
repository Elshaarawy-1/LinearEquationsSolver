from Parser_NoLetter import Parser
from EquationSystem import *
import numpy as np

parser = Parser()
equations = input() # get from GUI

list_equation = equations.split(",")

A,B,variables=parser.parseEquations(list_equation)
system_of_equations = EquationSystem(A,B,variables)

print (type(system_of_equations))