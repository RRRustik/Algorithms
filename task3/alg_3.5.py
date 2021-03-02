"""5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения."""

import random

random_numbers = random.sample(range(-100, 0), 10)

print(random_numbers)

maxs_negative = 0

for el in range(len(random_numbers)):
    if random_numbers[el] < maxs_negative:
        maxs_negative = random_numbers[el]

print(maxs_negative)
        