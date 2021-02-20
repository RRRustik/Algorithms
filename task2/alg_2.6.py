"""6. В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то, что загадано.
Если за 10 попыток число не отгадано, вывести ответ"""

import random

rand = random.randint(1, 101)
n = 1
#print(rand)
while n <= 10:
    num = int(input("Введите натуральное число: "))
    if num < rand:
        print ("Загаданное число больше")
    elif num > rand:
        print("Загаданное число меньше")
    else:
        print(f"Число отгадано, ВЫ ПОБЕДИЛИ!, это число {rand}")
        break
    n += 1
else:
    print(f"Попытки закончились, было загадано {rand}")

print(rand)