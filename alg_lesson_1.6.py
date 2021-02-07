"""6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
равнобедренным или равносторонним."""


line1 = int(input("Введите длину отрезка 1: "))
line2 = int(input("Введите длину отрезка 2: "))
line3 = int(input("Введите длину отрезка 3: "))

if line1 == 0 or line2 == 0 or line3 == 0 or line1+line2 <= line3 or line1+line3 <= line2 or line2+line3 <= line1:
    print("Это не треугольник")
elif line1 == line2 or line2 == line3 or line1 == line3:
    if line1 == line2 and line2 == line3:
        print ('Это равносторонний треугольник')
    else:
        print ('Это равнобедренный треугольник')
else:
    print('Треугольник с разной длиной сторон')