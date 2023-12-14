import sympy as sp
import numpy as np

class GaussianLetter:
    def __init__(self, matrix, soln):
        self.matrix = matrix
        self.soln = soln
        

    def solve(self):
        # Get the dimensions of the array
        num_rows, num_cols = self.matrix.shape

        # Create symbols for the matrix in row-wise order
        symbolic_matrix = sp.Matrix([sp.symbols(f'a_{i}_{j}') for i in range(num_rows) for j in range(num_cols)])

        # Reshape the flat symbols into the shape of the NumPy array
        symbolic_matrix = symbolic_matrix.reshape(num_rows, num_cols)

        # Substitute values from the NumPy array into the symbolic matrix
        substitution_dict = {(symbolic_matrix[i, j]): self.matrix[i, j] for i in range(num_rows) for j in range(num_cols)}
        symbolic_matrix_with_values = symbolic_matrix.subs(substitution_dict)

        # Get the echelon form of the matrix
        reduced_matrix = symbolic_matrix_with_values.echelon_form()

        # Display the SymPy matrix with symbols in row-wise order
        print("\nSymPy Matrix with Symbols:\n")
        sp.pprint(reduced_matrix)

        self.back_substitution(reduced_matrix, self.soln)


    def back_substitution(self, matrix, soln):
        n = matrix.shape[0]
        x = [sp.symbols(f'x_{i}') for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i-1, -1):
                summation = sum(matrix[i, j] * x[j] for j in range(i + 1, n))
                x[i] = sp.simplify((soln[i] - summation) / matrix[i, i])
        print("\nSolution\n")
        sp.pprint(x)
        return x

if __name__ == '__main__':
    solver = GaussianLetter(matrix = np.array([[1, 'a', 'x'],['b', 2, 4],['c', 1, -1]]), soln = np.array([1, 2, 3]))
    solution = solver.solve()