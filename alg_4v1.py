"""4. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
"""

Для замера времени выполнения я использовал функцию cProfile.
По времени выполнения alg_4v2 является наиболее оптимальным вариантом, поскольку алгоритм alg_4.2 и alg_4.3 
перебирают элементы 2 и 4 раза соответственно. 

"""
import cProfile
import timeit
import random

random_numbers = random.sample(range(0, 1000000), 1000000)

#print(f'{random_numbers}')

def var1():
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

    random_numbers[max_number], random_numbers[min_number] = random_numbers[min_number], random_numbers[max_number]

    new_list = random_numbers

    return new_list


#print(var1())
cProfile.run('var1()')
#print(timeit.timeit(var1))



