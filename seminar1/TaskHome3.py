# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

num = randint(1, 100)
count = 1
while count <= 10:
    res = int(input("Введите предполагаемое загаданное число: "))
    if res > num:
        print("Загаданное число меньше Вашего")

    elif res < num:
        print("Загаданное число больше Вашего")

    else:
        print(f'Вы угадали число. Это было число {num}. Вы угадали за {count} раз(а)')
        break
    count += 1
else:
    print(f'К сожалению, Вы не угадали число {num} за 10 попыток.')
