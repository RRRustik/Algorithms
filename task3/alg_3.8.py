
import random

list1 = [10, 2, 3, 1, 5, 6, 7, 5]

mini_1 = random.choice(list1)


for num in range(len(list1)):
    if list1[num] <= mini_1:
        mini_1 = list1[num]
        min_number = num

del list1[min_number]

print(list1)