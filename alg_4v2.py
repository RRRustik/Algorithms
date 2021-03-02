"""В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."""
import cProfile
import random
import timeit

my_list = random.sample(range(0, 1000000), 1000000)
#print(my_list)
def var1():

    max_el_index = 0
    min_el_index = 0
    for i in range(len(my_list)):
        if my_list[max_el_index] < my_list[i]:
            max_el_index = i
        elif my_list[min_el_index] > my_list[i]:
            min_el_index = i

    my_list[max_el_index], my_list[min_el_index] = my_list[min_el_index], my_list[max_el_index]
    new_list = my_list
    return new_list

#print(var1())
cProfile.run('var1()')
#print(timeit.timeit(var1))


