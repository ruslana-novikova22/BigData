#Заповнити парні стовпчикі матриці розміром n×n
#одиницями, а непарні – нулями.

import numpy as np
import time

start = time.time()

n = int(input("Введіть n: "))
a = np.ones((n,n), dtype=int)

a[:, ::2] = 0

print(a)
end = time.time()

print ('Час виконання:', end - start)