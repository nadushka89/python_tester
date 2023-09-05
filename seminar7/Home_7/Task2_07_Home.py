# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os
def rename_files(target_name, num_digits, src_ext,dest_ext, name_range, folder_path = '.'):
    files = [f for f in os.listdir(folder_path) if f.endswith(src_ext)]
    count = 1
    for file in files:
        part_original_name = file[name_range[0]:name_range[1]]
        new_name = f'{part_original_name}{target_name}{str(count).zfill(num_digits)}.{dest_ext}'

        os.rename(os.path.join(folder_path,file), os.path.join(folder_path,new_name))
        count+=1

rename_files('New', 3, 'doc', "pdf",[0,3], './TestFolder')
