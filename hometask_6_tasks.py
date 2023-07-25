from hometask_6_main import ChessBoard


def check_position(list_of_position: tuple) -> bool:
    board = ChessBoard()
    for index, coord in enumerate(list_of_position, 1):
        if not board.set(int(coord[0]), int(coord[1])):
            print(f'Ошибка на {index} фигуре')
            print(board)
            return False
    print(board)
    return True


if __name__ == '__main__':
    list_of_position = []
    for i in range(1, 9):
        list_of_pos = input(f'Введите координаты {i} ферзя через пробел: ').split()
        list_of_position.append((int(list_of_pos[0]), int(list_of_pos[1])))
    print(check_position(tuple(list_of_position)))
