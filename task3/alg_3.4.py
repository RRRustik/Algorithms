"""4. Определить, какое число в массиве встречается чаще всего."""

#list1 = [int(num) for num in input("Введите числа через пробел: ").split()]

#print(list1)


list2 = [2, 2, 3, 1, 2, 3, 3, 3]


for i in range(len(list2)):
    count = 0
    max_count = 0
    element = list2[i]
    for n in range(len(list2)):
        if list2[n] == element:
            count += 1
            if count >= max_count:
                max_count = count
                number = list2[n]

                print(f' Число {number} встречается в массиве {max_count} раз/раза')
