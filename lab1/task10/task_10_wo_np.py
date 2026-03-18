import time

start = time.time()

arr = list(map(int, input("Введи числа через пробіл: ").split()))

for i in range(len(arr)):
    if arr[i] != 0:
        arr[i] = -1

print(arr)

end = time.time()

print (end - start)