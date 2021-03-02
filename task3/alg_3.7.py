"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться
"""
import random

list1 = [10, 2, 3, 1, 5, 6, 2, 5]
print(list1)
mini_1 = random.choice(list1)

min_number = 0
for num in range(len(list1)):
    if list1[num] <= mini_1:
        mini_1 = list1[num]
        min_number = num

print(f'Два наименьших числа в массиве: {mini_1}')
del list1[min_number]


mini_2 = random.choice(list1)
min_number_2 = 0
for num_2 in range(len(list1)):
    if list1[num_2] <= mini_2:
        mini_2 = list1[num_2]
        min_number_2 = num_2

print(f'Два наименьших числа в массиве:{mini_2}')