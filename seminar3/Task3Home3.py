# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно
# вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.

items = {
    "палатка": 2.0,
    "спальник": 1.0,
    "еда": 1.5,
    "фонарик": 0.3,
    "аптечка": 0.7,
    "топорик": 0.5,
    "нож": 0.2,
    "вода": 0.5,
    "кастрюля": 0.7,
}
# Сортировка вещей по массе
def sort_key(item):
    return item[1]
sorted_items = sorted(items.items(), key=sort_key)
print(*sorted_items)

# Подбор вещей для рюкзака
def fill_backpack(max_weight, items):
    total_weight = 0
    backpack = []

    for item, weight in items:
        if total_weight + weight <= max_weight:
            backpack.append(item)
            total_weight += weight

    return backpack

max_weight = 3.0  # максимальная кг рюкзака
backpack = fill_backpack(max_weight, sorted_items)

print(f"Выбранные вещи для рюкзака:{ backpack}")
