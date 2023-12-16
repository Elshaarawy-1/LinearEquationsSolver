from mpmath import mp, matrix, zeros

class LUSolverBase:
    def __init__(self, A):
        mp.dps = 6
        self.N = A.rows
        self.A = A
        self.b = None
        self.L = zeros(self.N, self.N)
        self.U = zeros(self.N, self.N)

    def solve(self, b):
        self.b = b
        self.initialize_A_pivot()
        self.decomposition()
        self.solve_for_lower()
        self.solve_for_upper()
        return self.b

    def initialize_A_pivot(self):
        for i in range(self.N):
            self.partial_pivot(i)

    def partial_pivot(self, k):
        pivot_row = max(range(k, self.N), key=lambda i: abs(self.A[i, k]))
        if pivot_row != k:
            self.row_swap(self.A, k, pivot_row)
            self.row_swap(self.b, k, pivot_row)

    def row_swap(self, matrix, row1, row2):
        temp = matrix[row1, :].copy()
        matrix[row1, :] = matrix[row2, :] 
        matrix[row2, :] = temp

    def solve_for_upper(self):
        for i in range(self.N-1, -1, -1):
            self.b[i] = (self.b[i] - sum(self.U[i, k] * self.b[k] for k in range(i + 1, self.N))) / self.U[i, i]


    def solve_for_lower(self):
        for i in range(self.N):
            self.b[i] = (self.b[i] - sum(self.L[i, k] * self.b[k] for k in range(i))) / self.L[i, i]

    def decomposition(self):
        raise NotImplementedError
    

class LUCholeskySolver(LUSolverBase):
    def decomposition(self):
        if self.is_symmetric():
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
                if self.A[i, j] != self.A[j, i]:
                    return False
        return True

class LUDoolittleSolver(LUSolverBase):
    def decomposition(self):
        for i in range(self.N):
            for j in range(i, self.N):
                sum_val = sum(self.L[i, k] * self.U[k, j] for k in range(i))
                self.U[i, j] = self.A[i, j] - sum_val
                if i == j:
                    self.L[i, j] = 1
                else:
                    sum_val = sum(self.L[j, k] * self.U[k, i] for k in range(i))
                    self.L[j, i] = (self.A[j, i] - sum_val) / self.U[i, i]

class LUCroutSolver(LUSolverBase):
    def decomposition(self):
        for i in range(self.N):
            for j in range(i, self.N):
                if i == j:
                    self.U[i, j] = 1
                else:
                    sum_val = sum(self.L[i, k] * self.U[k, j] for k in range(i))
                    self.U[i, j] = (self.A[i, j] - sum_val) / self.L[i, i]
                sum_val = sum(self.L[j, k] * self.U[k, i] for k in range(i))
                self.L[j, i] = (self.A[j, i] - sum_val) / self.U[i, i]



## Example Test
A = matrix([[2, 0, 4],
            [1, 0, -8],
            [0, 1, 0]])
b = matrix([5, 15.5, 15])

lu_solver = LUDoolittleSolver(A.copy())
result = lu_solver.solve(b.copy())
print("Solution:")
print(result)

crout_solver = LUCroutSolver(A.copy())
result = crout_solver.solve(b.copy())
print("Solution:")
print(result)
cholesky_solver = LUCholeskySolver(A.copy())
result = cholesky_solver.solve(b.copy())
print("Solution:")
print(result)