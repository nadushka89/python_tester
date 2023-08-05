# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.
import math
from fractions import Fraction


def get_fraction(str):
    parts = str.split('/')
    # числитель
    numerator = int(parts[0])
    # знаменатель
    denominator = int(parts[1])
    return numerator,denominator

#Находим НОД
def simplify(numerator,denominator):
    gcd = math.gcd(numerator,denominator)
    return numerator//gcd, denominator//gcd

str1 = input(" Введите первую дробь вида “a/b”: ")
str2 = input(" Введите вторую дробь вида “a/b”: ")

numerator1,  denominator1 = get_fraction(str1)
numerator2,  denominator2 = get_fraction(str2)

# вычисляем сумму
sum_num = numerator1*denominator2 + numerator2 * denominator1
sum_den = denominator1*denominator2
sum_num, sum_den = simplify(sum_num, sum_den )

# вычисляем произведение
prod_num = numerator1* numerator2
prod_den = denominator1*denominator2
prod_num, prod_den = simplify(prod_num, prod_den)

print (f'Сумма дробей: {sum_num}/{sum_den},проверка: {Fraction(str1) + Fraction(str2)}')
print (f'Произведение дробей: {prod_num}/{prod_den},проверка: {Fraction(str1) * Fraction(str2)}')


