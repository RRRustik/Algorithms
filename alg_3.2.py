"""Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
(помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа."""
import random

random_numbers = random.sample(range(1, 21), 5)
print(random_numbers)

even = []
for num in range(len(random_numbers)):
    if random_numbers[num]%2 == 0:
        even.append(num)
print(even)