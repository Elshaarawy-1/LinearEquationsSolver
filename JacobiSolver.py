import Solver
import numpy as np


class JacobiSolver(Solver):

    def __init__(self, A, b, itr=50, tolerance=1e-10, x=None, Sf=5):
        self.A = A.astype(float)
        self.b = b.astype(float)
        self.itr = itr
        self.tolerance = tolerance
        self.x = x.astype(float)
        self.sf = Sf
        pass




    def solve(self):

        b = b.astype(float)
        D = np.diag(self.A)  # D is the diagonal of A
        # R is the matrix A with the diagonal elements removed
        R = self.A - np.diagflat(D)
        R = R.astype(float)
        R = self.round_matrix_to_sf(R, self.sf)
        if D.any() == 0:
            
            # implement diagnol dominance from gauss seidel and update selef.x
            
            raise ValueError("A has a zero diagonal element.")
        

        for i in range(self.itr):
            print(f"Iteration {i+1}:")
            x_old = self.x.copy()  # copy the old values of x
            for itr in range(len(self.x)):
                # dot_product = round_to_sf(sum(round_to_sf(R[itr, j] * x_old[j],sf) for j in range(len(x_old))),sf)
                dot_product = self.matrixSumofProduct(R, x_old, itr)
                self.x[itr] = self.round_to_sf((self.round_to_sf((b[itr] - dot_product), self.sf) / D[itr]), self.sf) # calculate the new x
                abs_rel_error = np.abs((self.x[itr] - x_old[itr]) / self.x[itr])  # calculate the absolute relative error for each x
                print(
                    f"x{itr} = {self.x[itr]} and Absolute relative error: {abs_rel_error}") # print the new x and the absolute relative error
            if np.all(abs_rel_error < self.tolerance):
                print(f"\nConverged after {i + 1} iterations.")
                break

        return self.x
        pass

    def round_to_sf(self, number, sf):
        if number == 0:
            return 0
        order_of_magnitude = 10 ** (sf -
                                    int(np.floor(np.log10(abs(number)))) - 1)
        rounded_number = round(
            number * order_of_magnitude) / order_of_magnitude
        return rounded_number

    def round_matrix_to_sf(self, matrix, sf):
        """
        Round a NumPy matrix to a specified number of significant figures.

        Parameters:
        - matrix: The input matrix to be rounded.
        - sf: The desired number of significant figures.

        Returns:
        - rounded_matrix: The matrix rounded to the specified significant figures.
        """
        rounded_matrix = np.vectorize(
            lambda x: self.round_to_sf(x, sf))(matrix)
        return rounded_matrix

    def matrixSumofProduct(self, v1, v2, itr):
        sum = 0
        for i in range(len(v1)):
            sum += self.round_to_sf(v1[itr, i] * v2[i], 5)
        return sum
