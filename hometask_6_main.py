class Cell:
    color = 'Black'
    count = 0

    @staticmethod
    def switch_color():
        if Cell.color == 'Black':
            Cell.color = 'White'
            return Cell.color
        else:
            Cell.color = 'Black'
            return Cell.color

    def __init__(self, value: str = '', empty: bool = True):
        self.color = Cell.switch_color()
        self.value = value
        self.empty = empty
        Cell.count += 1
        if not Cell.count % 8:
            Cell.switch_color()

    def set(self, figure: str):
        self.empty = False
        self.value = figure

    def print_cell(self):
        cell = ''
        if self.empty:
            cell = f'{"⬛" if self.color == "Black" else "⬜"}'
        else:
            cell = f'{self.value}'
        return cell


class ChessBoard:

    def __init__(self, size: int = 8):
        self.size = size
        self.board = [[Cell('0') for _ in range(self.size)] for _ in range(self.size)]
        self.free_cells = [(x, y) for y in range(1, self.size + 1) for x in range(1, self.size + 1)]

    def set(self, x: int, y: int) -> bool:
        row = y - 1
        column = x - 1
        if self.board[row][column].empty:
            for i in range(self.size):
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        cur_x, cur_y = row + x * i, column + y * i
                        if 0 <= cur_x < self.size and 0 <= cur_y < self.size:
                            self.board[cur_x][cur_y].set('🟥')
            self.board[row][column].set('♟️')
        else:
            return False
        return True

    def list_of_free_cells(self) -> list:
        free_cells = []
        y = 1
        for row in self.board:
            x = 1
            for cell in row:
                if cell.empty:
                    free_cells.append((x, y))
                x += 1
            y += 1
        return free_cells

    def clear(self):
        for row in self.board:
            for cell in row:
                cell.empty = True

    def __repr__(self):
        return ''.join([' '.join([cell.print_cell() for cell in row]) + '\n' for row in self.board])


class ListOfPosition:
    def __init__(self, list_of_position: list = []):
        self.list_of_position = list_of_position

    def new(self, new_list: list):
        self.list_of_position.append(new_list)

    def __eq__(self, other):
        if len(self.list_of_position) == len(other.list_of_position):
            for position in self.list_of_position:
                if not position in other.list_of_position:
                    return False
        else:
            return False
        return True
