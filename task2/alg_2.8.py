"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""

amount_numbers = int(input("Введите количество вводимых чисел: "))
find_number = str(input("Введите цифру, которую необходимо посчитать: "))

n = 1

def count_number(number, find_number):
    count = 0
    for i in number:
        if i == find_number:
            count += 1
    return count

total_amount = 0
while n <= amount_numbers:
    number = str(input("Введите любое целое число: "))
    amount = count_number(number, find_number)
    n += 1
    total_amount += amount

print(total_amount)

