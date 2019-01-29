import numpy as np

np.random.seed(101)
array1 = np.random.randint(0, 100, 10)
print(array1)
print(array1.shape)

array2 = array1.reshape((2, 5))
print(array2)
print(array2.shape)
