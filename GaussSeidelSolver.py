import numpy as np
from sympy import symbols, pprint, Add, Mul, Eq
import mpmath
import dominant

class GaussSeidelSolver():
    def __init__(self, matrix, soln, itr=50,tol=1e-10,x=None, sf = 5):
        self.matrix = matrix
        self.soln = soln
        self.itr = itr
        self.tol = tol
        self.x = x
        self.sf = sf


    def solve(self):
        mpmath.mp.dps = self.sf
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
        steps = f"Initial Guess:\n{self.x}\n"
        i = 0
        while True:
            i += 1
            steps += f"\n_________________ iteration {i} _________________\n"
            for j in range(row):
                self.x[j] = self.soln[j]
                for k in range(row):
                    if k != j:
                        self.x[j] -= (self.matrix[j,k] * self.x[k])
                self.x[j] /= diagonal[j]

            steps += f"Solution for iteration {i}: \n{self.x}\n"
            err = np.absolute(self.x - x_prev)/self.x * 100
            steps += f"Error for Iteration {i}: {err}\n"
            x_prev = self.x.copy()
            if np.all(err<self.tol):
                break
            if i >= self.itr:
                break
        return self.x, steps
    

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