from mpmath import mp, matrix

class GaussEliminationSolver():
    def __init__(self,sf=5):
        self.sf = sf
        mp.dps = self.sf
        pass

    def gaussian_elimination(self, A, B):
        augmented_matrix = matrix([[A[i, j] for j in range(A.cols)] + [B[i, 0]] for i in range(A.rows)])
        n = augmented_matrix.rows

        print("Initial Augmented Matrix:")
        print(augmented_matrix)

        for i in range(n):
            max_index = max(range(i, n), key=lambda x: abs(augmented_matrix[x, i]))

            if i != max_index:
                print(f"\nSwapping rows {i + 1} and {max_index + 1}:")
                augmented_matrix[i, :], augmented_matrix[max_index, :] = augmented_matrix[max_index, :], augmented_matrix[i, :]
                print(augmented_matrix)


            for j in range(i + 1, n):
                factor = augmented_matrix[j, i] / augmented_matrix[i, i]
                print(f"\nRow {j + 1} = Row {j + 1} - ({factor}) * Row {i + 1}:")
                augmented_matrix[j, :] -= factor * augmented_matrix[i, :]
                print(augmented_matrix)

        return augmented_matrix

    def back_substitution(self, augmented_matrix):
        n = len(augmented_matrix)
        solution = matrix([mp.mpf(0)] * n)  

        for i in range(n - 1, -1, -1):
            solution[i] = mp.mpf(augmented_matrix[i, n])  # Fetch the constant from the augmented matrix

            for j in range(i + 1, n):
                solution[i] -= mp.mpf(augmented_matrix[i, j]) * solution[j]

            solution[i] /= mp.mpf(augmented_matrix[i, i])

        return solution


    

# Example 
# A = matrix([[-8, 1, -2],
#             [-3, -1, 7],
#             [2, -6, 1]])

# B = matrix([[106.8],
#             [177.2],
#             [279.2]])

# a = GaussEliminationSolver()
# solution = a.back_substitution(a.gaussian_elimination(A, B))
# print("\nSolution:")
# print(solution)