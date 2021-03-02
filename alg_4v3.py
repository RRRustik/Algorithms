import cProfile
import timeit
import random

my_list = random.sample(range(0, 1000000), 1000000)
#print(my_list)


def var1():
    max_num = max(my_list)
    min_num = min(my_list)

    i_max = 0
    i_min = 0
    for i in range(len(my_list)):
        if my_list[i] == max_num:
            i_max = i
        elif my_list[i] == min_num:
            i_min = i

    my_list[i_min], my_list[i_max] = my_list[i_max], my_list[i_min]

    new_list = my_list
    return new_list

#print(var1())
cProfile.run('var1()')
#print(timeit.timeit(var1))