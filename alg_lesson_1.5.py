"""
5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""


"""
alph = ['a', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я']

for i in range(len(alph)):
    if letter == i:
        print(f'Под номером {letter} расположена буква {alph[i-1]}')

"""
letter = int(input("Введите номер от 1 до 33: " ))
print(chr(letter+96))