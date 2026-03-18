import time
import random

start = time.time()

n = int(input("Введіть n: "))
a = [random.randint(0, 20) for _ in range(n)]

for i in range(n):
    if a[i] < n/2 or a[i] > 3*n/4:
        a[i] = - a[i]

print(a)

end = time.time()

print (end - start)