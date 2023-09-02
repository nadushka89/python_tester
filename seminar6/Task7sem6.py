# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

import sys
def _is_leap(year: int) -> bool:
    return not year % 4 and year % 100 or not year % 400


def check_date(date: str) -> bool | str:
    separator = [sep for sep in date if not sep.isdigit()]
    if len(set(separator)) > 1:
        return 'Ошибка ввода данных'
    else:
        separator = separator[0]

    day, month, year = list(map(int, date.split(separator)))
    months = {1: 31, 2: 29 if _is_leap(year) else 28, 3: 31, 4: 30,
              5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if 0 < year < 10000:
        if 0 < month < 13:
            if 0 < day <= months[month]:
                return True
    return False

# print(check_date('20.06.1984'))
# print(check_date('31/02/2021'))
# print(check_date('29-02-1996'))
# print(check_date('32-01-1997'))
# print(check_date('32/01-1997'))


if __name__ == '__main__':
    if len(sys.argv) >1:
        date = sys.argv[1]
        print(check_date(date))
    else:
        print("Пожалуйста передайте дату в формате  дд.мм.гггг")


