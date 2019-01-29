import numpy as np

matrix = np.arange(0, 100).reshape(10, 10)
print(matrix)

matrix[0:3, 0:3] = 0
print(matrix)
