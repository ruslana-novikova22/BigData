import time

n = int(input("Введіть n: "))

start = time.time()

for i in range(n):
    for j in range(n):
        if i == j:
            print(i + 1, end=" ")
        else:
            print(0, end=" ")
    print()

end = time.time()

print("Час виконання:", end - start)