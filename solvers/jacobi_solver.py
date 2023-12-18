from solvers.solver import Solver
import numpy as np
import mpmath as mp
from solvers.dominant import diagonally_dominant


class JacobiSolver(Solver):

    def __init__(self, A, B, itr=3, tolerance=1e-10, x=None):
        self.A = A
        self.AD = np.array(A)
        self.b = B
        self.itr = itr
        self.tolerance = tolerance
        self.x = x
        self.steps=[]
        
        pass
        
    
    
    def solve(self): # function to solve the system of equations
        
        
        
        R,D = self.matrixwithoutDiagonal(self.A) # R is the matrix without the diagonal 
        R=mp.matrix(R)
        D=mp.matrix(D)
        
        for i in range(self.itr):
            self.steps.append(f"Iteration {i+1}:")
            x_old = mp.matrix(self.x.copy())  # copy the old values of x
            for itr in range(len(self.x)):
                # dot_product = round_to_sf(sum(round_to_sf(R[itr, j] * x_old[j],sf) for j in range(len(x_old))),sf)
                dot_product = mp.fdot(R[itr, :], x_old)
                self.x[itr] = mp.mpf(mp.mpf(self.b[itr] - dot_product) / D[itr, itr]) # calculate the new x
                abs_rel_error = mp.mpf(np.abs((self.x[itr] - x_old[itr]) / self.x[itr]))  # calculate the absolute relative error for each x
                self.steps.append(f"x{itr} = {self.x[itr]} and Absolute relative error: {abs_rel_error}") # print the new x and the absolute relative error
            err = np.absolute((np.array(self.x.tolist()) - np.array(x_old.tolist())) / np.array(self.x.tolist()))
            if np.all(err < self.tolerance):
                self.steps.append(f"\nConverged after {i + 1} iterations.")
                break
            if i == self.itr - 1:
                self.steps.append(f"\nDid not converge after {i + 1} iterations.")

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

    