# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения
# с выводом подробной информации. Поднимайте исключения внутри основного кода. Например, нельзя создавать прямоугольник
# со сторонами отрицательной длины.

# Задача с треугольником
class TriangleError(Exception):

    def __init__(self, x: int or float, y: int or float, z: int or float) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'The triangle cant exist with such sides as: {self.x}, {self.y}, {self.z}'


class TriangleChecker:
    def __init__(self, a: int or float,  b: int or float, c: int or float) -> None:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
            raise TypeError('Only int or float numbers allowed')
        elif a > c + b or b > a + c or c > b + a:
            raise TriangleError(a, b, c)
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


triangle = TriangleChecker(50, 2, 12)  # The triangle can't exist with such sides as: 50, 2, 12

# Напишите функцию для транспонирования матрицы
class MatrixError(Exception):

    def __init__(self, arr: list) -> None:
        self.arr = arr

    def __str__(self) -> str:
        return f'Input values must be list in list'


def transposing_matrix(array: list) -> list:
    """Функция принимает матрицу(вложенные списки) и возвращает транспонированную матрицу"""
    if all(isinstance(i, list) for i in array):
        return [list(line) for line in zip(*array)]
    else:
        raise MatrixError(array)


matrix = [1, 2, 3]
print(transposing_matrix(matrix))  # Input values must be list in list

# Например, нельзя создавать прямоугольник со сторонами отрицательной длины.
class RectangleError(Exception):

    def __init__(self, x: int or float, y: int or float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'The rectangle cant exist with such sides as: {self.x}, {self.y}'


class Rectangle:

    def __init__(self, a: int or float, b: int or float) -> None:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError('Sides must be integer or float numbers')
        if a <= 0 or b <= 0:
            raise RectangleError(a, b)
        else:
            self.a = a
            self.b = b

    def __str__(self) -> str:
        return f'Class: {Rectangle.__name__}, first side={self.a}, second side={self.b}'


r1 = Rectangle('1', 2)  # ValueError: Sides must be integer or float numbers
r2 = Rectangle(-1488, 666)  # __main__.RectangleError: The rectangle can't exist with such sides as: -1488, 666
