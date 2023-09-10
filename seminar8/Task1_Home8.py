# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней
# с учётом всех вложенных файлов и директорий.
import csv
import json
import os
import pickle


def get_size(path):
    total = 0
    if os.path.isdir(path):
        for item in os.listdir(path):
            item_path = os.path.join(path,item)
            total += get_size(item_path)
    else:
        total += os.path.getsize(path)
    return total

def recurs_directory_list(start_path):
    result = []
    for root, dirs, files in os.walk(start_path):
        for name in dirs:
            dir_path = os.path.join(root, name)
            result.append({
                'parent': root,
                'type': 'directory',
                'name': name,
                'size': get_size(dir_path)
            })
        for name in files:
            file_path = os.path.join(root, name)
            result.append({
                'parent': root,
                'type': 'file',
                'name': name,
                'size': os.path.getsize(file_path)
            })
    return result

def save_results(data, start_path):
    with open(os.path.join(start_path, 'result.json'),'w') as f:
        json.dump(data, f, indent=4)

    with open(os.path.join(start_path, 'result.csv'), 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['parent', 'type', 'name', 'size'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    with open(os.path.join(start_path,'results.pkl'), 'wb') as f:
        pickle.dump(data, f)


start_directory = r'C:\Users\kitti\OneDrive\Рабочий стол\разработчик\tester\python\seminar8'
data = recurs_directory_list(start_directory)
save_results(data,start_directory)