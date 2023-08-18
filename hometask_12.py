import csv


# Создайте класс студента. Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100). Также экземпляр должен
# сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
class DataChecker:
    """Дескриптор для валидации ФИО учеников"""

    def __init__(self, data=None):
        self.data = data

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.check_data(value):
            setattr(instance, self.param_name, value)

    @staticmethod
    def check_data(val):
        if val.istitle() and all(list(filter(lambda x: x.isalpha(), val))):
            return True
        else:
            raise ValueError('Only titled strings are allowed')


class Student:
    name = DataChecker()
    surname = DataChecker()
    middlename = DataChecker()

    def __init__(self, name, surname, middlename, file_path):
        self.name = name
        self.surname = surname
        self.middlename = middlename
        self.file_path = file_path
        self.__inner_journal = {}
        self.__test_results = {}
        with open(f'{self.file_path}.csv', 'r', encoding='UTF-8') as file:
            file_reader = csv.reader(file, delimiter='\n')
            for row in file_reader:
                self.__inner_journal[row] = self.__inner_journal.get(row, [])
                self.__test_results[row] = self.__test_results.get(row, [])

    def get_score(self, subject, score):
        if subject in self.__inner_journal.keys():
            if score.isdigit() and 2 <= score <= 5:
                self.__inner_journal[subject].append(score)
            else:
                raise ValueError('Score must be bigger than 1 and less than 6')
        else:
            raise KeyError('There is no such subject')

    def test_result(self, subject, score):
        if subject in self.__test_results.keys():
            if score.isdigit() and 1 <= score <= 100:
                self.__test_results[subject].append(score)
            else:
                raise ValueError('Score must be between 1 and 100')
        else:
            raise KeyError('There is no such subject')

    def get_average(self, subject):
        if subject in self.__test_results.keys() and subject in self.__inner_journal.keys():
            return f'''Средняя оценка: {sum(self.__inner_journal[subject]) / len(self.__inner_journal[subject])}
Средний результат тестирования: {sum(self.__test_results[subject]) / len(self.__test_results[subject])}'''
        else:
            raise KeyError('There is no such subject')

    def __str__(self):
        return f'Student(name={self.name}, surname={self.surname}, middlename={self.middlename}'
