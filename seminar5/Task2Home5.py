# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

names = ["Alice", "Fedor", "Alexey"]
rates = [100_000, 125_000, 75_000]
bonuses = ["10.25%", "7.75%", "12.25%"]

print({name: rate * float(bonus.strip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)})