# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
import csv
import json
import random
import math
import os

def find_roots(a, b, c):
    """Нахождение корней квадратного уравнения"""
    desc = b**2 - 4*a*c

    if desc < 0:
        return None  # нет решения
    elif desc == 0:
        x = -b / (2 * a)
        return (x,)  # одно решение
    else:
        x1 = (-b + math.sqrt(desc)) / (2 * a)
        x2 = (-b - math.sqrt(desc)) / (2 * a)
        return (x1, x2)  # два решения

def generate_csv(filename='random_numbers.csv'):
    '''Генерация CSV-файла'''
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        for _ in range(random.randint(1, 50)):
            writer.writerow([random.randint(1, 10) for _ in range(3)])

def csv_decorator(func):
    '''Декоратор для использования чисел из CSV-файла'''
    def wrapper(filename='random_numbers.csv'):
        results = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    a, b, c = map(int, row)
                    results.append(func(a, b, c))  # вызываем функцию на каждой тройке чисел и сохраняем результат
        return results
    return wrapper



def json_save_decorator(func):
    '''Декоратор для сохранения результатов в JSON'''
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        data = {
            "arguments": args,
            "results": results
        }
        with open("results.json", "w") as file:
            json.dump(data, file, indent=4)
        return results
    return wrapper



@json_save_decorator
@csv_decorator
def wrapped_roots(*args):
    return find_roots(*args)


generate_csv()
results = wrapped_roots()
print(results)
