# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные.

# a=1
# b=0.2
# c="hi"
# d=True
# e=[1,2,"три"]
#
# print(type(a))
# print(type(b))
# print(isinstance(c,str))
# print(type(d))
# print(type(e))

# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

# import sys
#
# data = [1,2.45, "three", True, 43, False, 1, True, (1,2)]
#
# for i in range(len(data)):
#     print(i+1)
#     print(data[i])
#     print(id(data[i]))
#     print(sys.getsizeof(data[i]))
#     print(hash(data[i]))
#     if isinstance(data[i],int):
#         print("int",isinstance(data[i],int))
#     if isinstance(data[i],str):
#         print("str", isinstance(data[i],str))
#
#     print("__________________")


# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

# num=int(input("введите число: "))
# res_8 = ""
# res_2 = ""
# num1=num2=num
# while num1>0:
#     res_2 = str(num1 % 2) + res_2
#     num1 //=2
# print(res_2, bin(num).replace("0b", ""))
# while num2>0:
#     res_8 = str(num2 % 8) + res_8
#     num2 //=8
# print(res_8, oct(num).replace("0o", ""))

# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# import decimal
# from math import pi
#
# num = -1
# decimal.getcontext().prec=42
# while num<0 or num>1000:
#     num=decimal.Decimal(input("Введи число от 0 до 1000: "))
#
# print(num)
# sq=decimal.Decimal(pi) * (num/2)**2
# dlina = decimal.Decimal(pi) * num
# print(sq, dlina)

# ✔ Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
# ✔ Используйте комплексные числа
# для извлечения квадратного корня.

a,b,c = int(input("a: ")), int(input("b: ")),int(input("c: "))
d = b**2 - 4*a*c
if d==0:
    res = -b/2/a
elif d>0:
    res = ((-b - d**0.5)/(2*a), (-b + d**0.5)/(2*a))
else:
    d = complex(d, 0)
    res = ((-b - d**0.5)/(2*a), (-b + d**0.5)/(2*a))
print(res)

