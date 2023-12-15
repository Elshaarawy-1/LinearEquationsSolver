
from mpmath import mp

# Set the precision.
mp.dps = 3

num1 = mp.mpf(1/3)
num2 = mp.mpf('2.987654321')

result = num1 + num2

print(result)

# Create two matrices.
matrix1 = mp.matrix([[1.12356, 2.23456], [3.35454, 4.48754]])
matrix2 = mp.matrix([[5.597545, 6.645188], [7.75891, 8.8884554]])

# Multiply the two matrices.
result = matrix1 * matrix2
ss = matrix1[0,0]
print(matrix1[0,0] * matrix1[0,1])
print(result)

# Calculate the determinant.
det = mp.det(matrix1)

print(det)

# Divide matrix1 by 3
print(matrix1 * (1/3))