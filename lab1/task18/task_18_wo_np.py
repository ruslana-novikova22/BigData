import time
import random

start = time.time()

n = int(input("Введіть n: "))
a = [random.randint(0, 99) for _ in range(n)]
print(a)

unique = list(set(a))
print(unique)

end = time.time()

print (end - start)