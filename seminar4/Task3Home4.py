# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

balance = 0
operation = 0
history = []
def deposit(balance, operation):
    amount = int(input("Введите сумму, которую хотите  положить на счет: "))
    if amount % 50 != 0:
        print("сумма должна быть кратна 50 у.е")
        return balance, operation
    operation += 1
    if balance > 5000000:
        tax = balance * 0.1
        balance -= tax
        print(f"Налог на богатство равен: {tax} у.е")
    balance += amount
    if operation % 3 == 0:
        bonus = balance * 0.03
        balance += bonus
        print(f"Ваш бонус: {bonus} у.е")
    return balance, operation


def withdrawal_of_money(balance, operation):
    amount = int(input("Введите сумму, которую хотите снять на счет: "))
    if amount % 50 != 0:
        print("сумма должна быть кратна 50 у.е")
        return balance, operation
    if amount > balance:
        print("Недостаточно средств")
        return balance, operation
    operation += 1
    if balance > 5000000:
        tax = balance * 0.1
        balance -= tax
        print(f"Налог на богатство равен: {tax} у.е")
    fee = max(30, min(600, amount * 0.015))
    balance -= (amount + fee)
    print(f"Комиссия за снятие: {fee} у.е")
    if operation % 3 == 0:
        bonus = balance * 0.03
        balance += bonus
        print(f"Ваш бонус: {bonus} у.е")
    return balance, operation


while True:
    print(f"Текущий баланс равен: {balance} у.е")
    action = input("Выберите действие: \n"
                   "1. пополнить.\n"
                   "2. снять.\n"
                   "3. выйти. \n").lower()
    if action == "пополнить" or action == "1":
        balance, operation  = deposit(balance, operation)
        history.append(("пополнить", balance))
    elif action == "снять" or action == "2":
        balance, operation = withdrawal_of_money(balance, operation)
        history.append(("снять", balance))
    elif action == "выйти" or action == "3":
        break
    else:
        print("Неизвестная команда")

print("История всех операций:")
for action, amount in history:
    print(action, amount, "y.e.")