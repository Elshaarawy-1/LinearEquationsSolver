import numpy as np
from sympy import symbols, pprint, Add, Mul, Eq
import mpmath
from solvers.solver import Solver
import solvers.dominant as dominant

class GaussSeidelSolver(Solver):
    def __init__(self, A, B, itr=50,tolerance=1e-10,x=None):
        self.matrix = A
        self.soln = B
        self.itr = itr
        self.tolerance = tolerance
        self.x = x
        self.steps = []


    def solve(self):
        mpmath.mp.pretty = True
        x_prev = mpmath.matrix(self.x)
        row = self.matrix.rows
        col = self.matrix.cols
        if row != col:
            raise ValueError("Matrix is not square")

        x_order = np.arange(row)
        #Check diagonally dominant
        array, converge = dominant.diagonally_dominant(np.array(self.matrix.copy().tolist()), x_order,False)
        print(self.matrix)
        print(x_order)
        self.matrix = mpmath.matrix(array)
        diagonal = np.diag(np.array(self.matrix.tolist()))
        if diagonal.any() == 0:
            raise ZeroDivisionError("Matrix has a zero diagonal element")
        print(self.matrix)
        self.steps.append(f"Initial Guess:\n{self.x.copy()}\n")
        i = 0
        while True:
            i += 1
            self.steps.append(f"\n_________________ iteration {i} _________________\n")
            for j in range(row):
                self.x[j] = self.soln[j]
                for k in range(row):
                    if k != j:
                        self.x[j] -= (self.matrix[j,k] * self.x[k])
                self.x[j] /= diagonal[j]

            self.steps.append(f"Solution for iteration {i}: \n{self.x.copy()}\n")
            err = np.absolute(self.x - x_prev)/self.x * 100
            self.steps.append(f"Error for Iteration {i}: {err}\n")
            x_prev = self.x.copy()
            if np.all(err<self.tolerance):
                self.steps.append(f"\nConverged after {i} iterations.")
                break
            if i >= self.itr:
                self.steps.append(f"\nFinished {i} iterations.")
                break
            
        return self.x
    

if __name__ == '__main__':
    matrix = mpmath.matrix([[12, 3, -5],
             [1,5, 3],
             [3, 7, 13]])
    soln = mpmath.matrix([1,28,76])

    solver = GaussSeidelSolver(matrix, soln, itr=7,
                               x=mpmath.matrix([1,0,1]), sf = 5)
    solution, step_by_step = solver.solve()
    print(f"\nFinal Solution:\n{solution}")
    print("\nStep by step soln\n", step_by_step)