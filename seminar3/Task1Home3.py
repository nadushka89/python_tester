# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 2, 4, 5, 6, 7, 2, 3, 7, 6, 8, 2]

my_list2 = set()
duplicates = set()

for item in my_list:
    if item in my_list2:
        duplicates.add(item)
    my_list2.add(item)

print(f'Изначальный список {my_list}')
print(f'Cписок с дублирующимися элементами {duplicates}')