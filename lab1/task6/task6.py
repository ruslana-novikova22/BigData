#З клавіатури вводиться масив. Замінити всі ненульові елементи на –1.
import numpy as np
import time

start = time.time()

arr = np.array(list(map(int, input("Введи числа через пробіл: ").split())))

arr[arr != 0] = -1

end = time.time()

print(arr)
print (end - start)