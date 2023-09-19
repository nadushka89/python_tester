# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
#
# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

# import json
# import os
# import random
# from typing import Callable
#
# def json_safe(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         atr_args = ','.join(map(str, args))
#         atr_kwargs = ','.join([f'{k}={v}' for k, v in kwargs.items()])
#         atr = f'{atr_args}|{atr_kwargs}'
#
#         if not os.path.exists(f'result.json'):
#             with open(f'result.json', 'w', encoding='utf-8') as f:
#                 json.dump({atr: result}, f, indent=4, ensure_ascii=False)
#         else:
#             with open(f'result.json', 'r', encoding='utf-8') as f_read:
#                 json_data = json.load(f_read)
#             with open(f'result.json', 'w', encoding='utf-8') as f_write:
#                 json_data[atr] = result
#                 json.dump(json_data, f_write, indent=4, ensure_ascii=False)
#         return result
#     return wrapper
#
# def decor(loop: int):
#     def inner(func):
#         def wrapper(*args, **kwargs):
#             result = []
#             for _ in range(loop):
#                 result.append(func(*args, **kwargs))
#             return result
#         return wrapper
#     return inner
#
# def check_nums(func: Callable):
#     def wrapper(l_lim: int, h_lim: int, tries_: int):
#         if l_lim > h_lim or l_lim < 0 or h_lim > 100:
#             l_lim = 1
#             h_lim = 100
#         if tries_ not in range(1, 11):
#             tries_ = random.randint(1, 10)
#         return func(l_lim, h_lim, tries_)
#     return wrapper
#
# @decor(3)
# @json_safe
# @check_nums
# def guess_number(low: int = 10, high: int = 100, tries: int = 10) -> str:
#     count = 1
#     number = random.randint(low, high)
#     while count <= tries:
#         my_num = int(input(f'{count} из {tries} попытка. Введите число от {low} до {high}: '))
#         if my_num > number:
#             print('Я загадал меньше')
#         elif my_num < number:
#             print('Я загадал больше')
#         else:
#             result = f'Да ты победил c {count} попытки, я загадал {number}'
#             break
#         count += 1
#     else:
#         result = 'Извини, но ты проиграл, все попытки закончились'
#     return result
#
# guess_number(1, 1000, 15)

# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.

import json
import os
import random
from typing import Callable
from functools import wraps

def json_safe(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        atr_args = ','.join(map(str, args))
        atr_kwargs = ','.join([f'{k}={v}' for k, v in kwargs.items()])
        atr = f'{atr_args}|{atr_kwargs}'

        if not os.path.exists(f'result.json'):
            with open(f'result.json', 'w', encoding='utf-8') as f:
                json.dump({atr: result}, f, indent=4, ensure_ascii=False)
        else:
            with open(f'result.json', 'r', encoding='utf-8') as f_read:
                json_data = json.load(f_read)
            with open(f'result.json', 'w', encoding='utf-8') as f_write:
                json_data[atr] = result
                json.dump(json_data, f_write, indent=4, ensure_ascii=False)
        return result
    return wrapper

def decor(loop: int):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = []
            for _ in range(loop):
                result.append(func(*args, **kwargs))
            return result
        return wrapper
    return inner

def check_nums(func: Callable):
    @wraps(func)
    def wrapper(l_lim: int, h_lim: int, tries_: int):
        if l_lim > h_lim or l_lim < 0 or h_lim > 100:
            l_lim = 1
            h_lim = 100
        if tries_ not in range(1, 11):
            tries_ = random.randint(1, 10)
        return func(l_lim, h_lim, tries_)
    return wrapper

@decor(3)
@json_safe
@check_nums
def guess_number(low: int = 10, high: int = 100, tries: int = 10) -> str:
    count = 1
    number = random.randint(low, high)
    while count <= tries:
        my_num = int(input(f'{count} из {tries} попытка. Введите число от {low} до {high}: '))
        if my_num > number:
            print('Я загадал меньше')
        elif my_num < number:
            print('Я загадал больше')
        else:
            result = f'Да ты победил c {count} попытки, я загадал {number}'
            break
        count += 1
    else:
        result = 'Извини, но ты проиграл, все попытки закончились'
    return result

guess_number(0, 1000, 15)

