import numpy as np
from sympy import symbols, pprint, Add, Mul, Eq
import Solver

class GaussSeidelSolver():
    def __init__(self, matrix, soln, itr=50,tol=1e-10,x=None, sf = 5):
        self.matrix = matrix.astype(float)
        self.soln = soln.astype(float)
        self.itr = itr
        self.tol = tol
        self.x = x.astype(float)
        self.sf = sf

    def solve(self):
        x_prev = self.x.copy()
        row, col = self.matrix.shape
        if row != col:
            raise ValueError("Matrix is not square")

        #Check diagonally dominant
        self.matrix, converge = self.diagonally_dominant(self.matrix, False)
        diagonal = np.diag(self.matrix)
        
        print(f"convergence: {converge}")
        print(f"Initial Guess: {self.x}")
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
                        self.x[j] -= (self.matrix[j,k]*self.x[k])
                        x_expr = x_expr - Mul(self.matrix[j,k],self.x[k])
                self.x[j] /= diagonal[j]
                x_expr = x_expr/diagonal[j]
                x_expr = Eq(x_symb, x_expr)
                pprint(x_expr)

            print(f"Solution for iteration {i}: {self.x}\n")
            err = np.absolute(self.x - x_prev)/self.x * 100
            print(f"Error for Iteration {i}: {err}")
            x_prev = self.x.copy()
            if np.all(err<self.tol):
                break
            if i >= self.itr:
                break
        return self.x


    def diagonally_dominant(self, array, parsed_bef):
        abs_matrix = np.absolute(array)
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
    matrix = np.array([[12,3,-5],[1,5,3],[3,7,13]])
    soln = np.array([1,28,76])

    solver = GaussSeidelSolver(matrix, soln, itr=6,
                               x=np.array([1,0,1]))
    solution = solver.solve()
    print("Final Solution: ", solution)