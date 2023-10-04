import os
import logging
import sys
from collections import namedtuple

logging.basicConfig(filename='directory.txt', level=logging.INFO, format="%(message)s")

FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_dir', 'parent'])

def gather_info(directory_path):
    try:
        for root, dirs, files in os.walk(directory_path):
            for dir_name in dirs:
                info = FileInfo(name=dir_name, extension=None, is_dir=True, parent=root)
                logging.info(info)
            for file_name in files:
                name, extension = os.path.splitext(file_name)
                info=FileInfo(name=name, extension=extension or None, is_dir=False, parent=root)
                logging.info(info)
    except Exception as e:
        logging.error(f"ОШИБКА: {e}")

if __name__ =="__main__":
    if len(sys.argv) !=2:
        print("Используйте, пожалуйста: python file.py <path_directory> ")
        sys.exit(1)
    path_directory = sys.argv[1]

    if not os.path.exists(path_directory) or not os.path.isdir(path_directory):
        print(f'Неправильный путь: {path_directory}')
        sys.exit(1)

    gather_info(path_directory)
    print(f'Информация сохранена в файле directory.txt')


