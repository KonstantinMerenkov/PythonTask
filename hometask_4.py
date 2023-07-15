# Напишите функцию для транспонирования матрицы
def transposing_matrix(array: list) -> list:
    """Функция принимает матрицу(вложенные списки) и возвращает транспонированную матрицу"""
    n = len(array)
    return [list(line) for line in zip(*array)]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transposing_matrix(matrix))  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


# Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хэшируем, используйте его строковое представление.
def is_hashable(val) -> bool:
    """Функция для проверки на хешируемость"""
    try:
        hash(val)
    except TypeError:
        return False
    return True


def reversed_dict(**kwargs):
    """Функция принимает произвольное кол-во именованных аргументов,
    создаем 2 списка с ключами и значениями, создаем сигнальную переменную,
    если все элементы списка значений хэшируемы, то возвращаем "перевернутый" словарь,
    если элементы списка значений хэшируемы, то добавляем в пустой список строковое их представление
    в ответе на домашку напишите приз, это говнокод или еще более менее терпимо?)"""
    keys = kwargs.keys()
    vals = kwargs.values()
    modified_vals = []
    flag = True
    for arg in vals:
        if is_hashable(arg):
            flag = False
        elif not is_hashable(arg):
            modified_vals.append(' '.join(str(x) for x in arg))
    if not flag:
        return dict(zip(vals, keys))
    else:
        return dict(zip(modified_vals, keys))


print(reversed_dict(spisok=[1, 2, 3], some={4, 5, 6}))  # {'1 2 3': 'spisok', '4 5 6': 'some'}

# про банкомат делать не стал, уж больно задача просится быть сделанной через классы)
