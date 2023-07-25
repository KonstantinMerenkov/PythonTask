from hometask_6_main import ChessBoard


if __name__ == '__main__':
    board = ChessBoard()
    position = ''
    count = 1
    print(board)
    while position.lower() != 'exit' and count <= 8 and board.list_of_free_cells():
        x, y = input(f'Координаты {count} ферзя через пробел: ').split()
        board.set(int(x), int(y))
        count += 1
        print(board)