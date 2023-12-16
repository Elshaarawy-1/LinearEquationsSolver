# from GaussEliminationSolver import GaussEliminationSolver
# from GaussJordanSolver import GaussJordanSolver
# from LU_Solver import LU_Solver
# from JacobiSolver import JacobiSolver
# from GaussSeidelSolver import GaussSeidelSolver

class Solver:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.steps=[]

    def solve(self):
        pass


    # # solver factory
    # def get_solver(self, method: str):
    #     if method == "gauss_elimination":
    #         return GaussEliminationSolver(self._coefficients)
    #     elif method == "gauss_jordan":
    #         return GaussJordanSolver(self._coefficients)
    #     elif method == "lu":
    #         return LU_Solver(self._coefficients)
    #     elif method == "jacobi":
    #         return JacobiSolver(self._coefficients)
    #     elif method == "gauss_seidel":
    #         return GaussSeidelSolver(self._coefficients)
    #     else:
    #         return None