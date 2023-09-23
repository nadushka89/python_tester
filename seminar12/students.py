# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие
# предметы в экземпляре недопустимы. Для каждого предмета можно хранить оценки (от 2 до 5)
# и результаты тестов (от 0 до 100). Также экземпляр должен сообщать средний балл по тестам
# для каждого предмета и по оценкам всех предметов вместе взятых.

import csv
class NameDescritpor:
    '''Дескриптор для имен'''
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


    def __set__(self, instance, value):
        if not value.istitle():
            raise ValueError("Имена должны начинаться с большой буквы")
        if not value.isalpha():
            raise ValueError("Имена должны состоять из букв")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Subject:
    '''Дескриптор для предметов'''
    def __init__(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            self.allowed_subjects = next(reader)

    def __get__(self, instance, owner):
        return instance.__dict__.get('subjects', {})

    def __set__(self, instance, subjects):
        if any(subj not in self.allowed_subjects for subj in subjects):
            raise ValueError("Неверный предмет")
        instance.__dict__['subjects'] = subjects

class Student:
    '''Основной класс студента'''
    first_name = NameDescritpor()
    middle_name = NameDescritpor()
    last_name = NameDescritpor()
    def __init__(self, f_name, m_name, l_name, filename= 'subjects.csv'):
        self.first_name = f_name
        self.middle_name = m_name
        self.last_name = l_name
        self.subjects_data = Subject(filename)
        self.subjects = {subject: {"grades": [], "test_scores":[]} for subject in
                         self.subjects_data.allowed_subjects}

    def add_grade(self,subject,grade):
        if grade<2 or grade>5:
            raise ValueError("Оценка должна быть от 2 до 5")
        self.subjects[subject]['grades'].append(grade)

    def add_test_score(self,subject,score):
        if score<0 or score>100:
            raise ValueError("Результаты теста должны быть от 0 до 100")
        self.subjects[subject]['test_scores'].append(score)

    def average_test_score(self,subject):
        """Возвращает средний результат по предмету."""
        return sum(self.subjects[subject]['test_scores']) / len(self.subjects[subject]['test_scores'])

    def average_grade(self):
        total_grades = []
        for subject_data in self.subjects.values():
            total_grades.extend(subject_data['grades'])
        return sum(total_grades) / len(total_grades)

    def subject_average_grade(self, subject):
        """Возвращает средний балл по предмету."""
        return sum(self.subjects[subject]['grades']) / len(self.subjects[subject]['grades'])

    def total_average_test_score(self):
        """Возвращает средний результат всех тестов."""
        total_scores = []
        for data in self.subjects.values():
            total_scores.extend(data['test_scores'])
        return sum(total_scores) / len(total_scores)

    def __str__(self):
        result = f"Студент: {self.first_name} {self.middle_name} {self.last_name}\n"
        result += "Оценки и результаты тестов по предметам:\n"

        for subject, data in self.subjects.items():
            avg_grade = self.subject_average_grade(subject)
            avg_test = self.average_test_score(subject)

            grades_str = ', '.join(map(str, data['grades']))
            test_scores_str = ', '.join(map(str, data['test_scores']))

            result += (f"{subject}: Оценки: {grades_str} (Средний балл: {avg_grade}), "
                       f"Результаты тестов: {test_scores_str} (Средний результат теста: {avg_test})\n")

        total_avg_grade = self.average_grade()
        total_avg_test_score = self.total_average_test_score()

        result += f"\nОбщий средний балл по всем предметам: {total_avg_grade}\n"
        result += f"Общий средний результат тестов: {total_avg_test_score}\n"

        return result

student1 = Student("Кристина", "Геннадиевна", "Иванова")

student1.add_grade("Математика", 4)
student1.add_grade("Математика", 5)
student1.add_test_score("Математика", 85)
student1.add_grade("Физика", 3)
student1.add_test_score("Физика", 90)
student1.add_grade("Физкультура", 4)
student1.add_test_score("Физкультура", 78)
student1.add_grade("Русский", 5)
student1.add_grade("Русский", 3)
student1.add_test_score("Русский", 98)

print(student1)
student2 = Student("Николай", "Евгеньевич", "Петров")

student2.add_grade("Математика", 2)
student2.add_grade("Математика", 3)
student2.add_test_score("Математика", 56)
student2.add_grade("Физика", 2)
student2.add_test_score("Физика", 20)
student2.add_grade("Физкультура", 5)
student2.add_test_score("Физкультура", 100)
student2.add_grade("Русский", 4)
student2.add_grade("Русский", 4)
student2.add_test_score("Русский", 85)

print(student2)

