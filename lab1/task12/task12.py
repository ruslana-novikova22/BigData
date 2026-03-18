#Створити масив одиниць розміром n×n та створити в
#ньому «рамку», що утворюється з 0.

import numpy as np
import time

start = time.time()

n = int(input("Введіть n: "))
a = np.ones((n,n), dtype=int)

a[0, :] = 0        
a[-1, :] = 0       
a[:, 0] = 0       
a[:, -1] = 0 

print(a)

end = time.time()

print ('Час виконання:', end - start)