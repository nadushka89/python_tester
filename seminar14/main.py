# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json
import os


#
# from random import randint, sample, uniform
# from string import ascii_lowercase
#
# NUM_OF_NAMES = randint(3, 10)
# vowels = 'aeiouy'
#
# def gen_names(string=None):
#     names = []
#     while len(names) < NUM_OF_NAMES:
#         res = sample(string.ascii_lowercase, randint(4, 7))
#         if len(set(res) & set(vowels)) > 0:
#             names.append(''.join(res).title())
#     with open('names.txt', 'a', encoding='utf-8') as f:
#         f.writelines('\n'.join(names))
#
# gen_names()
#
#
# MIN_SIZE = -1000
# MAX_SIZE = 1000
#
# def write_in_file(num_of_str: int, file_name):
#     with open(f'{file_name}.txt', 'a', encoding='utf-8') as f:
#         f.writelines('\n'.join([f'{randint(MIN_SIZE, MAX_SIZE)} | {uniform(MIN_SIZE, MAX_SIZE)}'
#     for i in range(num_of_str)]))
#
#
# write_in_file(12, 'seminar_07_01')

# def create_json(list_, file_path):
#     dict_=dict()
#     with open('result.txt', 'r', encoding='utf-8') as f:
#         names = f.readlines()
#         for name in names:
#             name = name.srip().split(' -> ')
#             print(f'{name=}')
#             dict_[name[0]] = float(name[1])
#         print(dict_)
#     with open(file_path, 'a',encoding='utf-8') as f:
#         json.dump(dict_, f, indent=4, ensure_ascii=False)
# create_json(list_to_write, os.path.join(os.getcwd(),'first_json.json'))

# Задание №2
# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7). После каждого ввода добавляйте новую информацию в
# JSON файл. Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.  Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа. При перезапуске функции уже записанные в файл данные должны сохраняться.


import os
import json
from classes import User

MIN_LVL = 1
MAX_LVL = 7

def create_json(path: str = 'users.json'):
    user_data = {}
    id_list =[]
    while True:
        if os.path.exists(path):
            with open(path, 'r', encoding='UTF-8') as file:
                user_data = json.load(file)
        if user_data:
            for users in user_data.values():
                for user in users:
                    id_list.append(user[1])
        name = input("Введите имя пользователя: ")
        if not name:
            break
        while True:
            u_id = input("Введите личный ID: ")
            if u_id.isdigit():
                if int(u_id) not in id_list:
                    u_id = int(u_id)
                    break
                else:
                    print(f'ID {u_id} уже занят. Введите другой ID.')
            else:
                print('ID должен быть целым числом')
        while True:
            u_lvl = input("Введите уровень доступа: ")
            if u_lvl.isdigit() and MIN_LVL <= int(u_lvl) <= MAX_LVL:
                break
            else:
                print(f'Уровень доступа должен быть от {MIN_LVL} до {MAX_LVL}')

        if u_lvl in user_data:
            user_data[u_lvl].append((name, u_id))
        else:
            user_data[u_lvl] = [(name, u_id)]

        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(user_data, file, indent=6, ensure_ascii=False)

if __name__ == '__main__':
    create_json()
def load_users():
    user_list=set()
    with open("users.json", 'r', encoding="UTF-8") as file:
        data_users = json.load(file)
    for  lvl, users in data_users.items():
        for user in users:
            name, u_id = user
            user_list.add(User(name, u_id, lvl))
    return  user_list
data = load_users()
print(data)