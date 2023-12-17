from solvers.gauss_elimination_solver import GaussEliminationSolver
from solvers.gauss_jordan_solver import GaussJordanSolver
from solvers.gauss_elimination_with_scaling_solver import GaussEliminationWithScalingSolver
from solvers.lu_solver import LUCholeskySolver,LUDoolittleSolver,LUCroutSolver

class SolverFactory:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        
    def get_solver(self, method: str):
        if method == "Gauss Elimination":
            return GaussEliminationSolver(self.A,self.B)
        elif method == "Gauss Elimination With Scaling":
            return GaussEliminationWithScalingSolver(self.A,self.B)
        elif method == "Gauss-Jordan":
            return GaussJordanSolver(self.A,self.B)
        elif method == "LU Decomposition Doolittle":
            return LUDoolittleSolver(self.A,self.B)
        elif method == "LU Decomposition Crout":
            return LUCroutSolver(self.A,self.B)
        elif method == "LU Decomposition Cholesky":
            return LUCholeskySolver(self.A,self.B)
        else:
            return None