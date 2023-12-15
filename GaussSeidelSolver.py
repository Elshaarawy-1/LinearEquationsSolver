import numpy as np
from sympy import symbols, pprint, Add, Mul, Eq
import mpmath
import Solver

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

        #Check diagonally dominant
        self.matrix, converge = self.diagonally_dominant(self.matrix, False)
        diagonal = np.diag(np.array(self.matrix.tolist()))
        
        print(f"convergence: {converge}")
        print(f"Initial Guess:\n{self.x}")
        i = 0
        while True:
            i += 1
            print(f"\n_________________ iteration {i} _________________\n")
            for j in range(row):
                x_symb = symbols('x_{}^{}'.format(j+1, i))
                x_expr = self.soln[j]
                self.x[j] = self.soln[j]
                for k in range(row):
                    if k != j:
                        self.x[j] -= (self.matrix[j,k] * self.x[k])
                        x_expr = x_expr - Mul(self.matrix[j,k],self.x[k])
                self.x[j] /= diagonal[j]
                x_expr = x_expr/diagonal[j]
                x_expr = Eq(x_symb, x_expr)
                pprint(x_expr)

            print(f"Solution for iteration {i}: \n{self.x}\n")
            err = np.absolute(self.x - x_prev)/self.x * 100
            print(f"Error for Iteration {i}: {err}")
            x_prev = self.x.copy()
            if np.all(err<self.tol):
                break
            if i >= self.itr:
                break
        return self.x


    def diagonally_dominant(self, array, parsed_bef):
        abs_matrix = np.absolute(array.tolist())
        diagonal = np.diag(abs_matrix)
        greater = False
        gr_eq = True
        for i in range(abs_matrix.shape[0]):
            if diagonal[i] > np.sum(abs_matrix,axis=1)[i] - diagonal[i]:
                greater = True
            elif diagonal[i] == np.sum(abs_matrix,axis=1)[i] - diagonal[i]:
                continue
            else:
                gr_eq = False
                break
        
        if greater and gr_eq:
            return array, True
        elif not parsed_bef:
            return self.convert_matrix(array)
        else:
            return array, False


    def convert_matrix(self, array):
        abs_matrix = np.absolute(array)
        max_indices = np.argmax(abs_matrix, axis=1)
        #Check if the matrix can be converted into diagonal diagonally dominant one
        if len(np.unique(max_indices)) != len(max_indices):
            return array, False
        
        for i in range(array.shape[0]):
            max_ind = np.argmax(abs_matrix[i])
            if i != max_ind:
                array[:,[i,max_ind]] = array[:, [max_ind,i]]
                abs_matrix[:, [i,max_ind]] = abs_matrix[:, [max_ind,i]]

        return self.diagonally_dominant(array,True)
    

if __name__ == '__main__':
    matrix = mpmath.matrix([[4,2,1],[-1,2,0],[2,1,4]])
    soln = mpmath.matrix([11,3,16])

    solver = GaussSeidelSolver(matrix, soln, itr=4,
                               x=mpmath.matrix([1,1,1]), sf = 5)
    solution = solver.solve()
    print("\nFinal Solution:\n",solution)