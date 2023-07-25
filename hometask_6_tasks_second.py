import random
from hometask_6_main import ListOfPosition, ChessBoard
from hometask_6_tasks import check_position


def random_set():
    board = ChessBoard()
    positions = []
    count = 0
    while count < 8:
        count = 0
        board.clear()
        positions = []
        list_of_free_cells = board.list_of_free_cells()
        while list_of_free_cells:
            list_of_free_cells = board.list_of_free_cells()
            if list_of_free_cells:
                x, y = random.choice(list_of_free_cells)
                board.set(x, y)
                positions.append((x, y))
                count += 1
    return positions


def list_of_positions(amount: int) -> ListOfPosition:
    count = 0
    list_of_pos = ListOfPosition()
    while count < amount:
        new_list = random_set()
        if not new_list in list_of_pos.list_of_position:
            list_of_pos.new(new_list)
            count += 1
    return list_of_pos


if __name__ == '__main__':
    list_queen = list_of_positions(int(input('Сколько вариантов расстановок выдать? ')))
    for lop in list_queen.list_of_position:
        check_position(tuple(lop))