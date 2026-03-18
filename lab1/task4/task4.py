#Вводяться числа n і m. Вивести масив розміру n×m, в
#якому у першому рядку (рядок з нулевим індексом) йдуть числа від 0
#до m–1, а всі інші елементи матриці дорівнюють 0.
import numpy as np
import time

start = time.time()

n = int(input("Введіть n: "))
m = int(input("Введіть m: "))

a = np.zeros((n,m), dtype=int)
a[0] = np.arange(m)

end = time.time()

print(a)
print (end - start)