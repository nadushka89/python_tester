# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

def path_parts_generator(path):
    parts = path.split('/')
    filename_parts = parts[-1].split('.')

    yield '/'.join(parts[:-1])
    yield filename_parts[0] if len(filename_parts) > 1 else filename_parts[0]
    yield filename_parts[1] if len(filename_parts) > 1 else ''

def split_path(path):
    parts_generator = path_parts_generator(path)
    directory = next(parts_generator)
    filename = next(parts_generator)
    extension = next(parts_generator)
    return directory, filename, extension


filepath = "/home/gb/documents/file.pdf"
print(split_path(filepath))

