import random


# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
# больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно
# сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
class TriangleExistError(Exception):
    """Создаю кастомное исключение только для проверки существования треугольника"""
    pass


class TriangleChecker:

    def __init__(self, a, b, c):
        """В инициализатор класса решил добавить проверку на типы данных"""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise TypeError('Only int or float numbers allowed')
        else:
            self.a = a
            self.b = b
            self.c = c

    def is_exist(self):
        """метод проверки существования треугольника"""
        if self.a > self.c + self.b or self.b > self.a + self.c or self.c > self.b + self.a:
            raise TriangleExistError('No triangle with these sides is possible')
        else:
            return f'The Triangle is possible'

    def is_isosceles(self):
        """проверка на равнобедренность, решил включить проверку на существование, ну типа как защита от дурака)"""
        if TriangleChecker.is_exist:
            if (self.a == self.b and self.b != self.c and self.a != self.c) or (
                    self.c == self.b and self.b != self.a and self.c != self.a):
                return f'Triangle is isosceles'
            else:
                return f'Triangle is not isosceles'
        else:
            return f'Your data is invalid, gimme another one'

    def is_fullside(self):
        """проверка на равносторонность"""
        if TriangleChecker.is_exist:
            if self.a == self.b == self.c:
                return f'Triangle is fullside'
            else:
                return f'Triangle is not fullside'
        else:
            return f'Your data is invalid, gimme another one'


# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на
# единицу и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
def is_simple(num):
    if num < 0 or num > 100000:
        return 'Sorry, dude, your number is invalid'
    else:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count <= 2:
            return f'This number is simple'
        else:
            return f'This number is not simple'


# number = int(
# input('Put your number right here\n'))  # решил запрашивать целое число, float думаю был бы здесь не в кассу)
# print(is_simple(number))

# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
class RandomNumApi:

    def __init__(self, name):
        self.name = name

    def starting(self):
        print(f'Hello fellow {self.name}')

    @staticmethod
    def num_randomizer():
        return random.randint(1, 1000)

    @staticmethod
    def verify_number(number):
        if not isinstance(number, int) and not 1 <= number <= 100:
            raise ValueError('Wrong type of number, try again')
        else:
            return number


def guess():
    count = 10
    nb = RandomNumApi(input('Whats your name\n'))
    nb.starting()
    while count != 0:
        print('Put your number')
        n = int(input())
        if n < nb.num_randomizer():
            print('Too small')
            count -= 1
        elif n > nb.num_randomizer():
            print('Too big')
            count -= 1
        elif n == nb.num_randomizer():
            print('Bulls eye')
            break
    else:
        print('Sorry, you ran out of tries')


guess()
