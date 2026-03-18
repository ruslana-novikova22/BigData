import time

start = time.time()

n = int(input("Введіть n: "))

for i in range(n):
    for j in range(n):
        if j % 2 == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()

end = time.time()

print (end - start)