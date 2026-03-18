#Розв’язати систему алгебраїчних рівнянь за допомогою
#формул Крамера і виконати перевірку за допомогою:

import numpy as np

a = np.array([
    [1, 5, 3, -4],
    [3, 1, -2, 0],
    [5, -7, 0, 10],
    [0, 3, -5, 0]
], dtype=float)

b = np.array([20, 9, -9, 1], dtype=float)

det_a = np.linalg.det(a)
print("det(a) =", det_a)

if det_a == 0:
    print("Система не має єдиного розв’язку")
else:
    n = a.shape[0]
    x = np.zeros(n)
    for i in range(n):
        ai = a.copy()
        ai[:, i] = b
        x[i] = np.linalg.det(ai) / det_a

print("Розв’язок за Крамером:", x)

#матричне множення
b_check = a @ x
print("Перевірка через множення a*x:", b_check)

#оберненої матриці
ob = np.linalg.inv(a)
x_ob = ob @ b
print("Перевірка через обернену матрицю:", x_ob)

#функції numpy.linalg.solve().
solve = np.linalg.solve(a,b)
print("Перевірка через функцією numpy.linalg.solve(): ",solve)

print("Крамер ≈ множення:", np.allclose(x, b_check))
print("Крамер ≈ обернена матриця:", np.allclose(x, x_ob))
print("Крамер ≈ solve():", np.allclose(x, solve))
