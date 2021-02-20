"""3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""

import random

random_numbers = random.sample(range(0, 100), 10)

print(f'Исходный массив: {random_numbers}')

maxs = 0
min_number = 0
max_number = 0
for num in range(len(random_numbers)):

    if random_numbers[num] >= maxs:
        maxs = random_numbers[num]
        max_number = num

mini = maxs

for num in range(len(random_numbers)):

    if random_numbers[num] <= mini:
        mini = random_numbers[num]
        min_number = num

print(f'Максимальное значение: {maxs}')
print(f'Минимальное значение: {mini}')

random_numbers[max_number], random_numbers[min_number] = random_numbers[min_number], random_numbers[max_number]
print(f'Новый массив: {random_numbers}')
