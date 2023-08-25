# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ —
# значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его
# строковое представление.

def keyword_(**kwargs):      #только ключевые аргументы с помощью **kwargs
    result_dict = {}
    for key, value in kwargs.items():
        if hashable(value):
            result_dict[value] = key
        else:
            result_dict[str(value)] = key
    return result_dict

def hashable(value):    #проверяем можно ли хэшировать
    try:
        hash(value)
        return True
    except TypeError:
        return False

dict_result = keyword_(name = "Nadi", age=22, country="Russia", likes=["sport", "painting"])
print(dict_result)