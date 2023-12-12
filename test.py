import numpy as np

def crout(a, single_step=False):
    N = len(a[0])
    l = np.zeros((N, N))
    u = np.zeros((N, N))

    for i in range(N):
        l[i, 0] = a[i, 0]
        u[i, i] = 1

    if l[0,0] == 0:
        print("Can't Divide By Zero A[1][1]")
        raise ValueError("Can't divide by zero")
    
    for j in range(1, N):
        u[0, j] = a[0, j] / l[0, 0]

    for i in range(1, N):
        for j in range(1, i + 1):
            l[i, j] = a[i, j] - np.dot(l[i, 0:j], u[0:j, j])


        if l[i,i] == 0:
            print(f"Can't Divide By Zero L[{i+1}][{i+1}]")
            raise ValueError("Can't divide by zero")
        for j in range(i + 1, N):
            u[i, j] = (a[i, j] - np.dot(l[i, 0:i], u[0:i, j])) / l[i, i]

        print("Step:", i)
        print("L:")
        print(l)
        print("\nU:")
        print(u)
        print("\n-------------------------")

        if single_step and i < N - 1:
            input("Press Enter to go to the next step...")

    print("Final L:")
    print(l)
    print("\nFinal U:")
    print(u)

# Example usage with single-step mode
crout(
    np.array([
        [2, 3, -1],
        [3, 2, 1],
        [1, -5, 3]
    ]),
    single_step=True
)