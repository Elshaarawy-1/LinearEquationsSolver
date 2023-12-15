import Solver
import numpy as np
from mpmath import mp, matrix

class LU_Solver(Solver):

    def __init__(self, A):
        mp.dps = 6
        self.N = A.rows
        self.A = A
        self.b = None
        self.L = None
        self.U = None

    def solve(self, b):
        self.b = b
        self.doolittle_decomposition()
        self.solveForLower()
        self.solveForUpper()
        return self.b

    def crout(a, single_step=False):
        N = len(a[0])
        l = np.zeros((N, N))
        u = np.zeros((N, N))

        for i in range(N):
            l[i, 0] = a[i, 0]
            u[i, i] = 1

        if l[0,0] == 0:
            print("Can't Divide By Zero A[1][1]")
            raise ValueError("Can't divide by zero")
        
        for j in range(1, N):
            u[0, j] = a[0, j] / l[0, 0]

        for i in range(1, N):
            for j in range(1, i + 1):
                l[i, j] = a[i, j] - np.dot(l[i, 0:j], u[0:j, j])


            if l[i,i] == 0:
                print(f"Can't Divide By Zero L[{i+1}][{i+1}]")
                raise ValueError("Can't divide by zero")
            for j in range(i + 1, N):
                u[i, j] = (a[i, j] - np.dot(l[i, 0:i], u[0:i, j])) / l[i, i]

            print("Step:", i)
            print("L:")
            print(l)
            print("\nU:")
            print(u)
            print("\n-------------------------")

            if single_step and i < N - 1:
                input("Press Enter to go to the next step...")

        print("Final L:")
        print(l)
        print("\nFinal U:")
        print(u)


    
    
    def solveForUpper(self):
        for i in range(self.N-1, -1, -1):
            self.b[i] = (self.b[i] - sum(self.U[i, k] * self.b[k] for k in range(i + 1, self.N))) / self.U[i, i]


    def solveForLower(self):
        for i in range(self.N):
            self.b[i] = (self.b[i] - sum(self.L[i, k] * self.b[k] for k in range(i))) / self.L[i, i]

    def partial_pivot(self, k):
        pivot_row = max(range(k, self.N), key=lambda i: abs(self.U[i, k]))
        if pivot_row == k:
            self.row_swap(self.U, k, pivot_row)
            self.row_swap(self.b, k, pivot_row)


    def row_swap(self, matrix, row1, row2):
        temp = matrix[row1, :].copy()
        matrix[row1, :] = matrix[row2, :] 
        matrix[row2, :] = temp
    
    def doolittle_decomposition(self):
        self.U = self.A.copy()
        self.L = matrix(self.N, self.N)
        for i in range(self.N):
            self.partial_pivot(i)
            print("L matrix:")
            print(self.L)
            print("U matrix:")
            print(self.U)
            # U matrix
            for j in range(0, self.N):
                sum_val = sum(self.L[i, k] * self.U[k, j] for k in range(i))
                self.U[i, j] = self.A[i, j] - sum_val
            # L matrix
            for j in range(i, self.N):
                if i == j:
                    self.L[i, j] = 1
                else:
                    sum_val = sum(self.L[j, k] * self.U[k, i] for k in range(i))
                    self.L[j, i] = (self.A[j, i] - sum_val) / self.U[i, i]
        print("L matrix:")
        print(self.L)
        print("U matrix:")
        print(self.U)

    def cholesky_decomposition(self):
        if (self.is_symmetric()):
            self.L = matrix(self.N, self.N)
            for i in range(self.N):
                for j in range(i, self.N):
                    sum_val = sum(self.L[i, k] * self.L[j, k] for k in range(i))
                    if i == j:
                        self.L[i, i] = (self.A[i, i] - sum_val) ** 0.5
                    else:
                        self.L[j, i] = (self.A[j, i] - sum_val) / self.L[i, i]
            self.U = self.L.copy()
        else:
            print("Matrix A is not symmetric, and therefore, the Cholesky decomposition cannot be applied to it.")
            raise ValueError("Cholesky Work in symmetric matrix only")

    def is_symmetric(self):
        for i in range(self.N):
            for j in range(self.N):
                if(self.A[i, j] != self.A[j, i]):
                    return False;            
        return True



# Example usage:
    
# A = matrix([[2, -1, 1], [-3, -1, 2], [-2, 1, 2]])
# A = matrix([[3, -0.1, -0.2],
#             [0.1, 7, -0.3],
#             [0.3, -0.2, 10]])
A = matrix([[-8, 1, -2],
            [-3, -1, 7],
            [2, -6, 1]])


b = matrix([106.8, 177.2, 279.2])
lu_solver = LU_Solver(A)
result = lu_solver.solve(b)
print(result)
