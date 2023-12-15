from mpmath import mp, matrix

class GaussJordanSolver():
    def __init__(self, sf=5):
        self.sf = sf
        mp.dps = self.sf

    def gauss_jordan_elimination(self, A, B):
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

            pivot = augmented_matrix[i, i]
            augmented_matrix[i, :] /= pivot
            print(f"\nRow {i + 1} /= {pivot}:")
            print(augmented_matrix)

            for j in range(n):
                if i != j:
                    multiplier = augmented_matrix[j, i]
                    augmented_matrix[j, :] -= multiplier * augmented_matrix[i, :]
                    print(f"\nRow {j + 1} -= {multiplier} * Row {i + 1}:")
                    print(augmented_matrix)

        return augmented_matrix

    def back_substitution(self, augmented_matrix):
        n = augmented_matrix.rows
        solution = matrix([mp.mpf(0)] * n)  

        for i in range(n - 1, -1, -1):
            solution[i] = mp.mpf(augmented_matrix[i, n]) 

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


# a = GaussJordanSolver()
# solution = a.back_substitution(a.gauss_jordan_elimination(A,B))
# print("\nSolution:")
# print(solution)
