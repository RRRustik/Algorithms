"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""

num = input("Введите любое натуральное число: ")

nums = list(num)
print(nums)
count = 0
uncount = 0
for i in nums:
    i = int (i)
    if i % 2 == 0:
        count += 1
    else:
        uncount += 1

print(f'Четных цифр: {count}, а нечетных {uncount}')
