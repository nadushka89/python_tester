

import unittest
from unittest.mock import patch
from classes import Terminal, User
from exceptions import AccessError, LevelError, NameAccessError, IdAccessError


class TestUser(unittest.TestCase):
    def setUp(self):
        self.terminal = Terminal()
        self.user1 = User('Стоун', '000017', 2)
        self.user2 = User('Антон', '000666', 6)

    def test_login(self):
        log_user = self.terminal.login('Стоун', '000017')
        self.assertEqual(log_user, self.user1)

    def test_user_eq(self):
        dubl_user = User('Стоун', '000017', 2)
        self.assertEqual(self.user1, dubl_user)

    def test_user_str(self):
        self.assertEqual(str(self.user1), 'Имя: Стоун (000017) | Уровень доступа: 2')

    def test_user_level_error(self):
        self.assertTrue(User('Стоунн', '000017',2),'Имя Стоунн не совпадает с ID 000017 ')

    def test_user_name_error(self):
        self.assertTrue(User('Катеринааа', '000018',2),'Пользователя с именем Катеринааа нет в базе данных')

    def test_create_new_user_name_error(self):
        with self.assertRaises(LevelError) as context:
            self.terminal.create_new_user(User('Стоун', '000017', 2), User('Катерина', '000020', 1))

        self.assertEqual(str(context.exception),'Ошибка уровня доступа. Ваш уровень (2) меньше требуемого'
                                                ' для создания пользователя уровня 1')
if __name__ == '__main__':
    unittest.main()
