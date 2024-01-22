class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        for index, el in enumerate(self.board):
            print(f'{el}', end='|')
            if index in (2, 5, 8):
                print("\b")

    def make_move(self, position):
        if position < 0 or position > 8:
            print('Неверный ввод!')
        elif self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Позиция занята!')
        winner = self.check_winner()
        if winner:
            print(f'Победил: {winner} !')

    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != ' ':
                return self.board[line[0]]
        if ' ' not in self.board:
            return 'Ничья !'
        return None


if __name__ == '__main__':
    game = TicTacToe()
    print('Игра: крестики нолики')
    print('Перед вами поле 3*3, и номера позиций, выбирайте, первый ходит "X"\n1|2|3\n4|5|6\n7|8|9\n')
    while not game.check_winner():
        game.make_move(int(input(f'Какую позицию вы выбираете({game.current_player}): ')) - 1)
        game.print_board()
