import numpy as np

matrix = np.arange(0, 100).reshape(10, 10)

print(matrix[1, :])  # whole row 1
print(matrix[:, 1])  # whole col 1
print(matrix[1, 1:4])  # row 1 from col 1 to 4
print(matrix[1:4, 1])  # col 1 from row 1 to 4

new_matrix: np.ndarray = matrix[1, :]
print(new_matrix.reshape(5, 2))
