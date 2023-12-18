#ahmed ya aymannnn  erbotha bl gui
#ahmed ya aymannnn  erbotha bl gui
#ahmed ya aymannnn  erbotha bl gui


from mpmath import mp, matrix
import numpy as np
from solvers.solver import Solver

class GaussEliminationWithScalingSolver(Solver):
    def __init__(self,A,B):
        super().__init__(A,B)
        self.n= self.A.rows
        
    def solve(self):
        augmented_matrix = self.gaussian_elimination()
        solution = self.back_substitution(augmented_matrix)
        return solution

    def scaling(self):
        scaling_factors = mp.matrix([0] * self.n)
        for i in range(self.n):
            scaling_factors[i, 0] = max([abs(self.A[i, j]) for j in range(i + 1)])
        return scaling_factors

    def gaussian_elimination(self):
        augmented_matrix = matrix(
            [[self.A[i, j] for j in range(self.A.cols)] + [self.B[i, 0]] for i in range(self.A.rows)])
        n = augmented_matrix.rows

        self.steps.append("Initial Augmented Matrix:")
        self.steps.append(augmented_matrix.copy())

        scaling_factors = self.scaling()

        for i in range(n):
            max_index = max(range(i, n), key=lambda x: abs(
                augmented_matrix[x, i] / scaling_factors[x]))

            if i != max_index:
                self.steps.append(f"\nSwapping rows {i + 1} and {max_index + 1}:")
                augmented_matrix[i, :], augmented_matrix[max_index,
                                                         :] = augmented_matrix[max_index, :], augmented_matrix[i, :]
                self.steps.append(augmented_matrix.copy())

            for j in range(i + 1, n):
                factor = augmented_matrix[j, i] / augmented_matrix[i, i]
                self.steps.append(
                    f"\nRow {j + 1} = Row {j + 1} - ({factor}) * Row {i + 1}:")
                augmented_matrix[j, :] -= factor * augmented_matrix[i, :]
                self.steps.append(augmented_matrix.copy())

        return augmented_matrix

    def back_substitution(self, augmented_matrix):
        n = len(augmented_matrix)
        solution = matrix([mp.mpf(0)] * n)

        for i in range(n - 1, -1, -1):
            # Fetch the constant from the augmented matrix
            solution[i] = mp.mpf(augmented_matrix[i, n])

            for j in range(i + 1, n):
                solution[i] -= mp.mpf(augmented_matrix[i, j]) * solution[j]

            solution[i] /= mp.mpf(augmented_matrix[i, i])

        return solution


