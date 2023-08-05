# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

balance = 0
operation = 0

while True:
    print(f"Текущий баланс равен: {balance} у.е")
    action = input("Выберите действие: \n"
                   "1. пополнить\n"
                   "2. снять\n"
                   "3. выйти: \n").lower()
    if action == "пополнить":
        amount = int(input("Введите сумму, которую хотите положить на счет: "))
        if amount % 50 !=0:
            print("сумма должна быть кратна 50 у.е")
            continue
        operation += 1
        if balance > 5000000:
            tax = balance * 0.1
            balance -= tax
            print(f"Налог на богатство равен: {tax} у.е")
        balance += amount
        if operation % 3 ==0:
            bonus = balance *0.03
            balance +=bonus
            print(f"Ваш бонус: {bonus} у.е")
        continue
    if action == "снять":
        amount = int(input("Введите сумму, которую хотите снять на счет: "))
        if amount % 50 != 0:
            print("сумма должна быть кратна 50 у.е")
            continue
        if amount > balance:
            print("Недостаточно средств")
        operation += 1
        if balance > 5000000:
            tax = balance * 0.1
            balance -= tax
            print(f"Налог на богатство равен: {tax} у.е")
        fee = max(30, min(600, amount * 0.015))
        balance -= (amount + fee)
        print(f"Комиссия за снятие: {fee} у.е")
        if operation % 3 ==0:
            bonus = balance *0.03
            balance +=bonus
            print(f"Ваш бонус: {bonus} у.е")
        continue
    elif action == "выйти":
        break
    else:
        print("Неизвестная команда")