#Заповнити вектор значеннями від 0 до n. Замінити
#знаки для всіх значень, що менші за n/2 та більші за 3n/4 на
#протилежні.

import numpy as np
import time

start = time.time()

n = int(input("Введіть n: "))
a = np.random.randint(0, 21, n)

a = np.where((a < n/2) | (a > 3*n/4), -a, a)

print(a)
end = time.time()

print ('Час виконання:', end - start)