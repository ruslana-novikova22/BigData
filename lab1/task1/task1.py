#Вводиться число n. Вивести масив розміру n×n, в
#якому по діагоналі йдуть числа від 1 до n, а інші числа дорівнюють 0.
import numpy as np
import time

n = int(input("Введіть n: "))

start = time.time()

A = np.diag(np.arange(1, n + 1))
print(A)

end = time.time()

print("Час виконання:", end - start)