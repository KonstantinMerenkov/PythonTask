import random
# Создайте класс-фабрику. Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
class Animal:
    def __init__(self, species: str) -> None:
        self.species = species


class Turtle(Animal):
    def __init__(self) -> None:
        super().__init__('Turtle')


class Dinosaur(Animal):
    def __init__(self) -> None:
        super().__init__('Dinosaur')


class AnimalFabric:

    @staticmethod
    def create_animal(animal_species: str):
        if animal_species == 'Turtle':
            return Turtle()
        elif animal_species == 'Dinosaur':
            return Dinosaur()
        else:
            return f'Wrong animal species'


fabric = AnimalFabric()
turtle = fabric.create_animal('Turtle')
dinosaur = fabric.create_animal('Dinosaur')
print(turtle.species)  # вернет Turtle
print(dinosaur.species)  # вернет Dinosaur
print(fabric.create_animal('Dog'))  # вернет Wrong animal species

# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.

# 1) Напишите программу банкомат:# Начальная сумма равна нулю; Допустимые действия: пополнить, снять, выйти;Сумма
# пополнения и снятия кратны 50 у.е.; Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.;
# После каждой третей операции пополнения или снятия начисляются проценты - 3%; Нельзя снять больше,
# чем на счёте;# Любое действие выводит сумму денег.
class AtmMachine:
    def __init__(self, deposit: int = 0, low_tax: float = 0.015, high_tax: float = 0.030) -> None:
        self.deposit = deposit
        self.low_tax = low_tax
        self.high_tax = high_tax

    def __get_low_tax(self, bucks: int) -> None:
        """Метод класса для взятия комиссии в 1.5%"""
        min_summ = bucks * self.low_tax
        if min_summ <= 30:
            self.deposit -= 30
        elif 30 < min_summ < 600:
            self.deposit -= min_summ
        elif min_summ >= 600:
            self.deposit -= 600

    def __get_high_tax(self, bucks: int) -> None:
        """Метод класса для взятия комиссии в 3%"""
        max_summ = bucks * self.high_tax
        if max_summ <= 30:
            self.deposit -= 30
        elif 30 < max_summ < 600:
            self.deposit -= max_summ
        elif max_summ >= 600:
            self.deposit -= 600

    def add_cash(self, quant: int):
        """Метод для внесения денег"""
        count = 0
        if quant % 50 == 0:
            self.deposit += quant
            count += 1
            if count % 3 != 0:
                self.__get_low_tax(quant)
            else:
                self.__get_high_tax(quant)
            print(f'Your balance: {self.deposit}')
        else:
            print(f'Wrong banknote')

    def get_cash(self, quant: int):
        """Метод для снятия денег"""
        count = 0
        if (self.deposit - quant) - 600 >= 0 and quant % 50 == 0:
            self.deposit -= quant
            count += 1
            if count % 3 != 0:
                self.__get_low_tax(quant)
            else:
                self.__get_high_tax(quant)
            print(f'Your balance: {self.deposit}')
        elif (self.deposit - quant) - 600 < 0:
            print(f'Not enough money')
        elif quant % 50 != 0:
            print(f'Wrong banknote')


def atm_work(command, cash: int) -> str:
    customer = AtmMachine()
    options = {'Put money': customer.add_cash, 'Take money': customer.get_cash}
    if command in options.keys() and command != 'Exit':
        return options[command](cash)
    elif command == 'Exit':
        return f'Good bue!Thanx for choosing us!'
    else:
        return f'Wrong command'


atm_work('Put money', 1000)  # Вернет Your balance: 970
atm_work('Take money', 500)  # Вернет Your balance: 462

# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
# больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно
# сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
class TriangleChecker:
    def __init__(self, a: int, b: int, c: int) -> None:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise TypeError('Only int or float numbers allowed')
        elif a > c + b or b > a + c or c > b + a:
            raise ValueError('No triangle with these sides is possible')
        else:
            self.a = a
            self.b = b
            self.c = c
            print('This triangle can exist')

    def is_isosceles(self) -> str:
        """Проверка на равнобедренность"""
        if (self.a == self.b and self.b != self.c and self.a != self.c) or (
                self.c == self.b and self.b != self.a and self.c != self.a):
            return f'Triangle is isosceles'
        else:
            return f'Triangle is not isosceles'

    def is_fullside(self) -> str:
        """Проверка на равносторонность"""
        if self.a == self.b == self.c:
            return f'Triangle is fullside'
        else:
            return f'Triangle is not fullside'


triangle = TriangleChecker(10, 15, 20)  # This triangle can exist
print(triangle.is_fullside())  # Triangle is not fullside
triangle_1 = TriangleChecker(10, 10, 15)  # This triangle can exist
print(triangle_1.is_isosceles())  # Triangle is isosceles
triangle_2 = TriangleChecker(10, 10, 10)  # This triangle can exist
print(triangle_2.is_fullside())   # Triangle is fullside

# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
class RandomNumApi:
    def __init__(self, name: str) -> None:
        self.name = name

    def starting(self):
        print(f'Hello fellow {self.name}')

    @staticmethod
    def num_randomizer() -> int:
        return random.randint(0, 1000)

    @staticmethod
    def verify_number(num) -> int:
        if not isinstance(num, int) and not 1 <= num <= 100:
            raise ValueError('Wrong type of number, try again')
        else:
            return num


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
