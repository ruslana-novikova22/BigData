#Згенерувати вектор з n випадкових чисел в діапазоні
#від 0 до 99. Визначити кількість унікальних чисел в послідовності.

import numpy as np
import time

start = time.time()

n = int(input("Введіть n: "))
a = np.random.randint(0, 99, n)
print(a)

unique = np.unique(a)
print(unique)

end = time.time()

print ('Час виконання:', end - start)