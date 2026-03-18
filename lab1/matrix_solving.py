import time

start = time.time()

A = [
    [5, 2, 0], 
    [10, 4, 1], 
    [7, 3, 2]
]

B = [
    [3, 6, -1], 
    [-1, -2, 0], 
    [2, 1, 3]
]

B2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):          
    for j in range(3):      
        sum = 0
        for k in range(3):  
            sum += B[i][k] * B[k][j]
        B2[i][j] = sum

part1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        part1[i][j] = A[i][j] - B2[i][j]

part2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        part2[i][j] = 2 * A[i][j] + B[i][j]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(3):
    for j in range(3):
        sum = 0
        for k in range(3):
            sum += part1[i][k] * part2[k][j]
        result[i][j] = sum

print("Результат обчислення:")
for row in result:
    print(row)

end = time.time()
print(end - start)