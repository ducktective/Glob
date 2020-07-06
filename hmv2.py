import numpy as np

b = np.diagflat([1, 2, 3, 4], -1)
print(b)
print('-------------')
b = np.zeros((8, 8), dtype=int)
b[1::2, ::2] = 1
b[::2, 1::2] = 1
print(b)
print('--------------')
a = np.array([[1, 5],
              [3, 0],
              [6, 5]])
b = np.array([[3, 8, 1],
              [0, 6, 5]])
print(np.dot(a, b))
print('--------------')
a = np.array([[6, 4, 1],
              [4, 1, 0],
              [1, 0, 8]])
b = np.array([[2, 3],
              [1, 6],
              [7, 2]])
print(np.dot(a, b))
print('--------------')
a = [[i for i in range(1, 5)], [i for i in range(1, 5)]]
a = np.array(a, dtype=int)
print(type(a))
print('--------------')
a = np.arange(4)
b = np.array([0, 1, 2, 3])
print(np.array_equal(a, b))
a = np.arange(4)
b = np.array([0, 0, 2, 3])
print(np.array_equal(a, b))
a = np.arange(4)
b = np.array([0, 1, 2, 3], dtype=float)
print(a)
print(np.array_equal(a, b))
