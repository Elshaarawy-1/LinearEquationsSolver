from Round_SF import round_to_sf
import Solver
import numpy as np
import mpmath as mp


class JacobiSolver(Solver):

    def __init__(self, A, b, itr=50, tolerance=1e-10, x=None, Sf=5):
        self.A = mp.nmatrix(A)
        self.b = mp.matrix(b)
        self.itr = itr
        self.tolerance = tolerance
        self.x = mp.matrix(x)
        self.sf = Sf
        pass

    def solve(self):
        mp.dps = self.sf # set the precision to the number of significant figures
        D = np.diag(self.A)  # D is the diagonal of A
        D = mp.matrix(D)
        # R is the matrix A with the diagonal elements removed
        R = self.A - np.diagflat(D)
        R = mp.matrix(R)
        
        if D.any() == 0:
            
            # implement diagnol dominance from gauss seidel and update selef.x
            
            raise ValueError("A has a zero diagonal element.")
    
        # iterate through the number of iterations
        for i in range(self.itr):
            print(f"Iteration {i+1}:")
            x_old = self.x.copy()  # copy the old values of x
            for itr in range(len(self.x)):
                # dot_product = round_to_sf(sum(round_to_sf(R[itr, j] * x_old[j],sf) for j in range(len(x_old))),sf)
                dot_product = self.matrixSumofProduct(R, x_old, itr)
                self.x[itr] = ([itr] - dot_product) / D[itr] # calculate the new x
                abs_rel_error = np.abs((self.x[itr] - x_old[itr]) / self.x[itr])  # calculate the absolute relative error for each x
                print(
                    f"x{itr} = {self.x[itr]} and Absolute relative error: {abs_rel_error}") # print the new x and the absolute relative error
            if np.all(abs_rel_error < self.tolerance):
                print(f"\nConverged after {i + 1} iterations.")
                break

        return self.x
        pass

    # function to calculate the sum of the product of two vectors
    def matrixSumofProduct(self, R, v2, itr):
        sum = mp.mpf(0)
        for i in range(len(v2)): # iterate through the length of the vector
            sum += R[itr, i] * v2[i] 
        return sum
