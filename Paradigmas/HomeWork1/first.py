# Задача №1.
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
numbers = [1, 2, 0, 4, 5, 3, 6, 8, 7, 9]


def sort_list_imperative(numbers_list):
    for i in range(len(numbers_list)):
        for k in range(len(numbers_list)):
            if numbers_list[i] > numbers_list[k]:
                numbers_list[i], numbers_list[k] = numbers_list[k], numbers_list[i]
    return numbers_list


print(sort_list_imperative(numbers))


def choice(array):
    for i in range(len(array) - 1):
        min_index = i
        for k in range(i+1, len(array)):
            if array[k] > array[min_index]:
                min_index = k
        array[i], array[min_index] = array[min_index], array[i]
    return array


print(choice(numbers))
