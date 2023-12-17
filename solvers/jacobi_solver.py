import Solver
import numpy as np
import mpmath as mp
from dominant import diagonally_dominant


class JacobiSolver:

    def __init__(self, A, b, itr=3, tolerance=1e-10, x=None, Sf=2):
        self.A = A
        self.AD = np.array(A)
        self.b = b
        self.itr = itr
        self.tolerance = tolerance
        self.x = mp.matrix(x)
        self.sf = Sf
        self.steps=[]
        
        pass
        
    
    
    def solve(self): # function to solve the system of equations
        mp.dps = self.sf # set the precision
        
        
        # if self.check_zero_diagonal(D):
        #     self.A,check= diagonally_dominant(self.A, False)
        #     self.A=mp.matrix(self.A)
        #     R,D = self.matrixwithoutDiagonal(self.A) # R is the matrix without the diagonal
        
        
        # iterate through the number of iterations
        
        R,D = self.matrixwithoutDiagonal(self.A) # R is the matrix without the diagonal 
        R=mp.matrix(R)
        D=mp.matrix(D)
        
        for i in range(self.itr):
            self.steps.append(f"Iteration {i+1}:")
            x_old = mp.matrix(self.x.copy())  # copy the old values of x
            for itr in range(len(self.x)):
                # dot_product = round_to_sf(sum(round_to_sf(R[itr, j] * x_old[j],sf) for j in range(len(x_old))),sf)
                dot_product = mp.mpf(self.matrixSumofProduct(R, x_old, itr)) # calculate the sum of the product of R and x_old
                self.x[itr] = mp.mpf(mp.mpf(self.b[itr] - dot_product) / D[itr, itr]) # calculate the new x
                abs_rel_error = mp.mpf(np.abs((self.x[itr] - x_old[itr]) / self.x[itr]))  # calculate the absolute relative error for each x
                self.steps.append(f"x{itr} = {self.x[itr]} and Absolute relative error: {abs_rel_error}") # print the new x and the absolute relative error
            if np.all(abs_rel_error < self.tolerance):
                self.steps.append(f"\nConverged after {i + 1} iterations.")
                break

        return self.x
        pass

        # function to get the matrix without the diagonal and the diagonal
    def matrixwithoutDiagonal(self, A): 
        Dia=mp.matrix(len(A))
        for i in range(len(A)):
            Dia[i, i] = A[i, i]
            A[i, i] = 0
        return A, Dia  
    
    # function to check if the diagonal has zeros
    def check_zero_diagonal(self, matrix): 
        for i in range(len(matrix)):
            if matrix[i, i] == 0:
                return True
        return False
        
    # function to calculate the sum of the product of two vectors
    def matrixSumofProduct(self, R, v2, itr):
        sum = mp.mpf(0)
        R = mp.matrix(R)
        v2 = mp.matrix(v2)
        for i in range(len(v2)): # iterate through the length of the vector
            sum += R[itr, i] * v2[i] 
        return sum
    
    
    
# # Example usage:

# A = mp.matrix([[5, -1, 1],
#             [2, 8, -1],
#             [-1, 1, 4]])
# B = mp.matrix([10, 11, 3])
    
# x = mp.matrix([[0],
#             [0],
#             [0]])
# x= (JacobiSolver(A, B, x=x).solve())


# print(x)   
