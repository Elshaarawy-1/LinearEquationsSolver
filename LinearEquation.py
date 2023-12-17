from parser.Parser_NoLetter import Parser
from parser.Parser_Letter import Parser_Letter
from solvers.jacobi_solver import JacobiSolver
from solvers.lu_solver import *
from parser.EquationSystem import *
import numpy as np
from mpmath import mp
from GaussSeidelSolver import *
equations = input() # get from GUI

list_equation = equations.split(",")
noLetter=True
####
lu_decomposition = False
crout = False
doolittle=False
cholesky=False
###
gauss_elimination=False
gauss_jordan=False
gauss_seidel=False
jacobi=False
if (noLetter): # True if no_letter mode
    parser=Parser()
    system_of_equations = parser.parseEquations(list_equation)
    if (jacobi):
        jacobi_solver = JacobiSolver(system_of_equations.A,system_of_equations.B,itr=50,tolerance=1e-10,x=[1,1,1],Sf=5)
        print(jacobi_solver.solve())
    if (lu_decomposition):
        LU_Solver = LUSolverBase(system_of_equations.A,system_of_equations.B)
        if (doolittle):
            doolittle_solver=LUDoolittleSolver(LU_Solver)
            steps=doolittle_solver.solve()
            solution = doolittle_solver.b
        if (cholesky):
            cholesky_solver=LUCholeskySolver(LU_Solver)
            steps=cholesky_solver.solve()
            solution=cholesky_solver.b
        if(crout):
            crout_solver=LUCroutSolver(LU_Solver)
            steps = crout_solver.solve()
            solution=crout_solver.b
    # if (gauss_seidel):
    #     gauss_seidel_solver = GaussSeidelSolver()

else: # if letter_mode
    parser = Parser_Letter()
    #  copy same code

# for item in system_of_equations.variables:
#     print(f"Item: {item}, Type: {type(item)}")
# print (type(system_of_equations))
# print(system_of_equations.A)
# print(system_of_equations.B)
# print(system_of_equations.variables)
# print(type(system_of_equations.A))
# print(type(system_of_equations.B))
# print(type(system_of_equations.variables))