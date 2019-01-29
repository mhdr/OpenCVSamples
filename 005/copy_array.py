import numpy as np

matrix: np.ndarray = np.arange(0, 100).reshape(10, 10)
print(matrix)

matrix2 = matrix.copy()
matrix2[0:3, 0:3] = 0
print(matrix2)
