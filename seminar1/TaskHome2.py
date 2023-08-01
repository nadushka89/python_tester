# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_prime(numb):
    if numb==1:
        return None
    for i in range(2, int(numb ** 0.5) + 1):
        if numb%i ==0:
            return False
    return True

while True:
    number = input("Введите число: ")
    if number.isdigit():
        number = int(number)
        if 0<number<=10000:
            if (is_prime(number)):
                print(f"Число {number} является простым")
            elif is_prime(number) is None:
                print (f"Число {number} не является ни составным, ни простым")
            else:
                print(f"Число {number}  является составным")
            break
        else:
            print(" Число не должно быть отрицательным чисел и  больше 100 тысяч.")
    else:
        print("Вы ввели не число")

