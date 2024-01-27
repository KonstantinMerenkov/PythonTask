# Ваша задача
# Реализовать с использованием функциональной парадигмы процедуру normalization, которая выполняет
# нормализацию полученного массива по приведенной формуле нормализованного значения элемента, где
# ○ x_norm - нормализованное значение элемента
# ○ x - исходное значение элемента
# ○ x_max, x_min - максимальное и минимальное значение в массиве
def normalize(data):
    max_val = max(data)
    min_val = min(data)

    def normalize_element(x):
        return (x - min_val) / (max_val - min_val)

    return list(map(normalize_element, data))


data_2 = [1, 2, 3, 4, 5]
print(normalize(data_2))

# Написать скрипт принимающий на вход массив с данными о людях и число - возраст, а возвращающий
# число - количество людей старше указанного возраста.
people = [
    {'name': 'Liza', 'age': 25},
    {'name': 'Ser', 'age': 30},
    {'name': 'Vas', 'age': 35},
    {'name': 'Ivan', 'age': 40},
]


def filter_by_age(list_dic: list, min_age: int) -> list:
    return list(filter(lambda pers: min_age < pers['age'], list_dic))


age = 30
filtered_people = filter_by_age(people, age)
print(filtered_people)
print(len(filtered_people))


# Ваша задача реализовать с использованием функциональной парадигмы процедуру для поиска дубликатов. На вход
# подается массив, где могут присутствовать дубликаты (а могут и не присутствовать). При применении к
# массиву, дубликаты должны быть выведены на экран в виде списка.
def find_duplicates(numbers):
    unique_numbers = set()
    return list(filter(lambda x: x in unique_numbers or unique_numbers.add(x), numbers))


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 3, 10]
print(find_duplicates(num))
