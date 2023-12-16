from solvers.gauss_elimination_solver import GaussEliminationSolver
from solvers.gauss_jordan_solver import GaussJordanSolver


class SolverFactory:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        
    def get_solver(self, method: str):
        if method == "Gauss Elimination":
            return GaussEliminationSolver(self.A,self.B)
        elif method == "Gauss-Jordan":
            return GaussJordanSolver(self.A,self.B)
        # elif method == "lu":
        #     return LU_Solver(self._coefficients)
        # elif method == "jacobi":
        #     return JacobiSolver(self._coefficients)
        # elif method == "gauss_seidel":
        #     return GaussSeidelSolver(self._coefficients)
        else:
            return None