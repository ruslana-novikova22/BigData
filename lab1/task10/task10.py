#Вводиться числа n i m. Створити масив випадкових
#значень n×m і обчислити мінімальне, максимальне значення, середнє та
#середньо квадратичне відхилення, округлене до 3 знаків після коми.
import numpy as np
import time

start = time.time()

n = int(input("Введіть n: "))
m = int(input("Введіть m: "))

a = np.random.randint(-100, 100, (n,m))

min = np.min(a)
max = np.max(a)
av = np.mean(a)
std = round(np.std(a), 3)

#print(a)
print(min)
print(max)
print(av)
print(std)

end = time.time()

print ('Час виконання:', end - start)