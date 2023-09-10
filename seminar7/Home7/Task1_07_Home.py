# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
import os
import shutil


def sort_files_by_types(src_folder):
    file_types = {
        "Images": ['.jpg','.jpeg','.png','.bmp', '.giff'],
        "Videos": ['.mkv', '.avi', '.mp4', '.mov'],
        "Documents": ['.doc', '.txt', '.pdf']
    }
    for file in os.listdir(src_folder):
        src_file_path = os.path.join(src_folder,file)
        if os.path.isfile(src_file_path):
            file_extension = os.path.splitext(file)[1].lower() #получаем расширение файла
            for category, extensions in file_types.items():
                dest_folder_path = os.path.join(src_folder,category)
                if file_extension in extensions:
                    if not os.path.exists(dest_folder_path):
                        os.mkdir(dest_folder_path)
                    shutil.move(src_file_path, os.path.join(dest_folder_path,file))
                    break

src_folder_path = r'C:\Users\kitti\OneDrive\Рабочий стол\разработчик\tester\python\seminar7\Home7'
sort_files_by_types(src_folder_path)
print("Файлы отсортированы")