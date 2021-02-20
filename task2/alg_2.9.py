"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""

amount_numbers = int(input("Введите количество вводимых чисел для сравнения: "))

n = 1

def count_number(number):
    count = 0
    for i in number:
        i = int(i)
        count += i
    return count

max_number = 0
while n <= amount_numbers:
    number = str(input("Введите любое целое число: "))
    amount = count_number(number)
    n += 1
    if amount > max_number:
        max_number = amount
        max_sum = number


print(f'Это число {max_sum}')
print(f' Сумма цифр равна {max_number}')

