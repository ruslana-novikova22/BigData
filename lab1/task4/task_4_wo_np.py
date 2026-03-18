import time

start = time.time()

n = int(input("Введіть n: "))
m = int(input("Введіть m: "))

for i in range(n):
    for j in range(m):
        if i == 0:
            print(j, end=' ')
        else:
            print(0,end=' ')
    print()

end = time.time()

print (end - start)