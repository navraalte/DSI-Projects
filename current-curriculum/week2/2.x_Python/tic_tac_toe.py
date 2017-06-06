import numpy as np


class TicTacToe(object):

    def __init__(self, size=3):
        self.size = size
        # need to introduce
        self.board = np.chararray((self.size, self.size))
        self.board[:] = ''

    def is_board_empty(self):
        return np.sum(self.board == '') == self.size * self.size

    def is_valid_move(self, i, j):
        if i < 0 or i > self.size - 1 or j < 0 or j > self.size - 1:
            return False
        elif self.board[i, j] != '':
            return False
        else:
            return True

    def is_row_victory(self, board):
        for i in range(self.size):
            if np.all(self.board[i] == 'X'):
                self.winner = 'X'
                return True

            if np.all(self.board[i] == 'O'):
                self.winner = 'O'
                return True
        return False

    def is_diag_victory(self, board):
        # need to introdue flipr, diag
        if np.all(np.diag(board) == 'X') | np.all(np.diag(np.fliplr(board) == 'X')):
            self.winner = 'X'
            return True
        elif np.all(np.diag(board) == 'O') | np.all(np.diag(np.fliplr(board) == 'O')):
            self.winner = 'O'
            return True
        else:
            return False

    def is_game_over(self):
        if self.is_row_victory(self.board) | self.is_row_victory(self.board.T) | self.is_diag_victory(self.board):
            return True
        elif np.sum(self.board == '') == 0:
            self.winner = 'Game Tied'
            return True
        else:
            return False

    def declare_winner(self):
        if self.winner != 'Game Tied':
            return 'Player {} Won the Game'.format(self.winner)
        return 'Game Tied'

    def play_game(self):
        while not self.is_game_over():
            xo = raw_input("Input X or O: ")
            loc = raw_input("Where do you want to move: ")
            if not self.is_board_empty():
                if last_move == xo:
                    print('Two consecutive moves from same player. Try again!')
            try:
                i, j = map(int, loc.split(','))

                if self.is_valid_move(i, j):
                    self.board[i, j] = xo
                else:
                    print('Not a Valid Move. Try again!')

            except ValueError:
                print('Give Valid Index Inputs. Try Again!')

            print self.board
            last_move = xo
        self.declare_winner()

tictac1 = TicTacToe()
tictac1.play_game()
