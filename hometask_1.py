import random


# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c — стороны предполагаемого треугольника. Требуется сравнить длину каждого
# отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется
# больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно
# сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
def triangle_type(a, b, c):
    # Проверка существования треугольника
    if a + b <= c or a + c <= b or b + c <= a:
        return "Треугольник с такими сторонами не существует"

    # Определение типа треугольника
    if a != b and b != c and a != c:
        return "Треугольник разносторонний"
    elif a == b and b == c:
        return "Треугольник равносторонний"
    else:
        return "Треугольник равнобедренный"

# Примеры использования функции
side1 = int(input('Введите длину стороны 1 - '))
side2 = int(input('Введите длину стороны 2 - '))
side3 = int(input('Введите длину стороны 3 - '))

print(triangle_type(side1, side2, side3))  # Равнобедренный


# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на
# единицу и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
def is_simple(num: int) -> str:
    if num < 0 or num > 100000:
        return 'Некорректный ввод'
    else:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count <= 2:
            return f'Простое число'
        else:
            return f'Не простое число'


number = int(
    input('Введите Ваше число\n'))  
print(is_simple(number))

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
            raise ValueError('Неверный тип числа, повторите ввод')
        else:
            return number


def guess():
    count = 10
    nb = RandomNumApi(input('Enter - запустить генерацию случайного числа\n'))
    nb.starting()
    while count != 0:
        print('Введите Ваше число')
        n = int(input())
        if n < nb.num_randomizer():
            print('Слишком мало')
            count -= 1
        elif n > nb.num_randomizer():
            print('Слишком велико')
            count -= 1
        elif n == nb.num_randomizer():
            print('Угадано')
            break
    else:
        print('Не угадано - закончились попытки')


guess()
