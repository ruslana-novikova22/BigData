#Вводяться 4 числа n, m, r, c. Вивести масив розміру
#n×m, в якому в кожному рядку з номером r і в кожному стовпчику з
#номером c стоять 0, а інші елементи дорівнюють 1.
import numpy as np
import time

start = time.time()

n = int(input("Введіть n: "))
m = int(input("Введіть m: "))
r = int(input("Введіть номер рядка r: "))
c = int(input("Введіть номер стовпця c: "))

A = np.ones((n, m), dtype=int)

A[r, :] = 0
A[:, c] = 0

end = time.time()

print(A)
print (end - start)