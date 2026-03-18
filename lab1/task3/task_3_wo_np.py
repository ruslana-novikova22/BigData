import time

n = int(input("Enter n:"))
m = int(input("Enter m:"))
r = int(input("Enter r:"))
c = int(input("Enter c:"))

start = time.time()

for i in range(n):
    for j in range(m):
        if i == r or j == c:
            print (0, end=' ')
        else:
            print (1, end=' ') 
    print()

end = time.time()

print("Час виконання:", end - start)