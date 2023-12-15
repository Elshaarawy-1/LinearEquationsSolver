from GaussEliminationSolver import GaussEliminationSolver
from GaussJordanSolver import GaussJordanSolver
from LU_Solver import LU_Solver
from JacobiSolver import JacobiSolver
from GaussSeidelSolver import GaussSeidelSolver

class Solver:
    def __init__(self, eqns):
        self._coefficients = eqns
        

    def solve(self, method):
        my_solver = self.get_solver(method)
        if my_solver is None:
            raise ValueError(f"Invalid solver method: {method}")
        return my_solver.solve()


    # solver factory
    def get_solver(self, method: str):
        if method == "gauss_elimination":
            return GaussEliminationSolver(self._coefficients)
        elif method == "gauss_jordan":
            return GaussJordanSolver(self._coefficients)
        elif method == "lu":
            return LU_Solver(self._coefficients)
        elif method == "jacobi":
            return JacobiSolver(self._coefficients)
        elif method == "gauss_seidel":
            return GaussSeidelSolver(self._coefficients)
        else:
            return None