"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
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


summ = 0

if max_number >= min_number:
    summ_list = random_numbers[min_number+1:max_number]
    for el in summ_list:
        summ += el
    print(f'Сумма элементов равна: {summ}')
else:
    summ_list = random_numbers[max_number+1:min_number]
    for el in summ_list:
        summ += el
    print(f'Сумма элементов равна: {summ}')


