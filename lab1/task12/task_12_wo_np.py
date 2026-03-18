import time

start = time.time()

n = int(input("Введіть n: "))

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()

end = time.time()

print (end - start)