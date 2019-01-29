import numpy as np

np.random.seed(101)
array1 = np.random.randint(0, 100, 10)
print(array1.max())
print(array1.argmax()) # index of max value
print(array1.min())
print(array1.argmin()) # index of min value
print(array1.mean())