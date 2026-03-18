#Обчислити значення матричного виразу
import numpy as np
import time

start = time.time()

A = np.array([
    [5, 2, 0],
    [10, 4, 1],
    [7, 3, 2]
], dtype=float)

B = np.array([
    [3, 6, -1],
    [-1, -2, 0],
    [2, 1, 3]
], dtype=float)

b_sq = B @ B
#print(b_sq)

first = np.subtract(A, b_sq)
#print(first)

double_a = 2*A
#print(double_a)

second = np.add(double_a, B)
#print(second)

result = first @ second
print("Result = \n", result)

end = time.time()
print(end - start)