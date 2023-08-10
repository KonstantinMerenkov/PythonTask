# Создайте класс Матрица.
# Добавьте методы для:
# -вывода на печать,
# -сравнения,
# -сложения,
# -умножения матриц
class CreationMatrixx:

    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def show_matrix(self) -> list:
        return self.matrix

    def __add__(self, other):
        """Метод сложения матриц"""
        if len(self.matrix) != len(other.matrix):
            return f'Only same size matrix allowed'
        else:
            return CreationMatrixx([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                                    for i in range(len(self.matrix))])

    def __mul__(self, other):
        """Метод умножения матриц"""
        if len(self.matrix[0]) != len(other.matrix):
            return f'Only same size matrix allowed'
        else:
            mul_matrix = [[sum(one * two for one, two in zip(one_row, two_col)) for two_col in zip(*other.matrix)]
                          for one_row in self.matrix]
            return CreationMatrixx(mul_matrix)

    def __eq__(self, other):
        """Метод сравнения матриц"""
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            return f'Only same size matrix allowed'
        else:
            for one in range(len(self.matrix)):
                for two in range(len(self.matrix[0])):
                    if self.matrix[one][two] != other.matrix[one][two]:
                        return False
            return True

    def __str__(self):
        """Метод строкового представления матрицы"""
        result = ''
        for char in range(len(self.matrix)):
            result += str(self.matrix[char]) + '\n'
        return result


matrix_1 = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [22, 33, 44, 55, 66],
            [333, 777, 666, 1488, 1]]
matrix_2 = [[3, 9, 12, 15, 18],
            [22, 33, 44, 55, 66],
            [333, 777, 666, 1488, 1],
            [6, 7, 8, 9, 10],
            [1, 2, 3, 4, 5]]

obj_1 = CreationMatrixx(matrix_1)
obj_2 = CreationMatrixx(matrix_2)
print(obj_1.__add__(obj_2))
# Вернет:
#  [4, 11, 15, 19, 23]
# [28, 40, 52, 64, 76]
# [344, 789, 679, 1502, 16]
# [28, 40, 52, 64, 76]
# [334, 779, 669, 1492, 6]
print(obj_1.__mul__(obj_2))
# Вернет:
# [1075, 2444, 2145, 4645, 218]
# [2900, 6584, 5810, 12500, 718]
# [4725, 10724, 9475, 20355, 1218]
# [15840, 35992, 31658, 68376, 3498]
# [248800, 556538, 493647, 1052134, 72827]
print(obj_1.__eq__(obj_2))
# Вернет:
# False
