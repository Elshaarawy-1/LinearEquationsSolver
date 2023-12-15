from mpmath import mp, matrix, zeros

class Decomposition:
    def __init__(self,A,single_step) -> None:
        self.N = A.rows
        self.A = A
        self.single_step = single_step
        self.L = None
        self.U = None

    def decompose():
        pass

class CroutDecomposition(Decomposition):

    def decompose():
        pass

    def crout(self, single_step=False):
        # N = len(a[0])
        self.L = zeros(self.N, self.N)
        self.U = zeros(self.N, self.N)

        for i in range(self.N):
            self.L[i, 0] = self.A[i, 0]
            self.U[i, i] = 1

        if self.L[0,0] == 0:
            print("Can't Divide By Zero A[1][1]")
            raise ValueError("Can't divide by zero")
        
        for j in range(1, self.N):
            self.U[0, j] = self.A[0, j] / self.L[0, 0]

        for i in range(1, self.N):
            for j in range(1, i + 1):
                sum_val = sum(self.L[i, k] * self.U[k, j] for k in range(j))

                self.L[i, j] = self.A[i, j] - sum_val
                # self.L[i, j] = self.A[i, j] - np.dot(self.L[i, 0:j], self.U[0:j, j])


            if self.L[i,i] == 0:
                print(f"Can't Divide By Zero L[{i+1}][{i+1}]")
                raise ValueError("Can't divide by zero")
            for j in range(i + 1, self.N):
                sum_val = sum(self.L[i, k] * self.U[k, j] for k in range(i))
                self.U = (self.A[i, j] - sum_val) / self.L[i, i]
                # self.U[i, j] = (self.A[i, j] - np.dot(self.L[i, 0:i], self.U[0:i, j])) / self.L[i, i]

            print("Step:", i)
            print("L:")
            print(self.L)
            print("\nU:")
            print(self.U)
            print("\n-------------------------")

            if single_step and i < self.N - 1:
                input("Press Enter to go to the next step...")

        print("Final L:")
        print(self.L)
        print("\nFinal U:")
        print(self.U)
