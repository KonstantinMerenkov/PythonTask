import csv
import json
import random


# Нахождение корней квадратного уравнения
def quad_decor(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        if result['discriminant'] > 0:
            return (-result['b'] + result['discriminant'] ** 0.5) / 2 * result['a'], \
                   (-result['b'] - result['discriminant'] ** 0.5) / 2 * result['a']
        elif result['discriminant'] == 0:
            return -result['b'] / 2 * result['a']
        else:
            return f'Нет корней'

    return inner


@quad_decor
def discr(a, b, c):
    """Передаем три параметра, не стал заморачиваться с проверкой, думаю и так понятно
    функция возвращает словарь"""
    return {'a': a, 'b': b, 'c': c, 'discriminant': b ** 2 - (4 * a * c)}


print(discr(2, 5, 2))  # вернет (-2.0, -8.0)


# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def create_csv(file_name):
    def decorator(func):
        def inner(*args, **kwargs):
            numbers = func(*args, **kwargs)
            with open(f'{file_name}.csv', 'w', encoding='UTF-8') as csv_file:
                file_writer = csv.writer(csv_file)
                for _ in range(random.randint(100, 1000) + 1):
                    file_writer.writerow(numbers)
            random.shuffle(numbers)
            return csv_file

        return inner

    return decorator


@create_csv(file_name='name')
def incoming(x, y, z):
    return [random.randint(1, x), random.randint(1, y), random.randint(1, z)]


# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
def quad_tgo_csv(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        a, b, c = result[0], result[1], result[2]
        disc = b ** 2 - (4 * a * c)
        if disc > 0:
            return (-b + disc ** 0.5) / 2 * a, (-b - disc ** 0.5) / 2 * a
        elif disc == 0:
            return -b / 2 * a
        else:
            return f'Нет корней'

    return inner


@quad_decor
def get_nums(csv_file):
    """Функция получает имя файла, открывает и итерирует его, и передает цифры в список, и возвращает его
    для простоты прикинем что цифр всегда 3 и они корректные"""
    nums = []
    with open(f'{csv_file}.csv', encoding='UTF-8') as file:
        file_reader = csv.reader(file)
        for num in file_reader:
            nums.append(num)
    return nums


# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def save_to_json(func):
    def inner(*args, **kwargs):
        data = func(*args, **kwargs)
        with open('some_file.json', 'w', encoding='UTF-8') as file:
            json.dump(data, file)
        return data

    return inner


@save_to_json
def some_func(a, b):
    """Передаем цифры, получаем словарь с параметрами и результатом работы функции"""
    lst = list(filter(lambda x: x % 2 == 0, [i for i in range(a, b + 1)]))
    return {'parameters': (a, b), 'result': lst}
