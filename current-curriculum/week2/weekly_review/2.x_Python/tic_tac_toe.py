import numpy as np


class TicTacToe(object):

    def __init__(self, size=3):
        """ Initialize the board of size using np.chararray with ''.

        Args:
            size of the board

        Returns:
            None

        """
        self.size = size
        self.board = np.chararray((self.size, self.size))
        self.board[:] = ''

    def is_valid_move(self, i, j):
        """ Checks if move at i, j is a valid move.

        Args:
            self
            i (int): row location of the move
            j (int): column location of move

        Returns:
            bool: False if i,j out of range or used, True otherwise

        """

        # check if i, j are out of range
        if i < 0 or i > self.size - 1 or j < 0 or j > self.size - 1:
            print 'Give Valid Index Inputs'
            return False

        # check if i, j already used
        if self.board[i, j] is not '':
            print 'Move Taken'
            return False

        return True

    def is_row_column_victory(self, column=0):
        """ Check if there is a victory in rows or columns of the board.

        Args:
            self
            column (int): indicator checking rows or columns

        Returns:
            bool: True if victory on board, False otherwise

        """

        board = self.board
        if column:
            board = self.board.T

        for i in range(self.size):
            if np.all(board[i] == 'X'):
                self.winner = 'X'
                return True

            if np.all(board[i] == 'O'):
                self.winner = 'O'
                return True

        return False

    def is_diag_victory(self):
        """ Check if there is a victory across the diagnals of the board.

        Args:
            self

        Returns:
            bool: Returns True if either diagnols have a victory.


        """

        def diag_vic(symb, flip=0):

            if flip:
                return np.all(np.diag(np.fliplr(self.board)) == symb)

            return np.all(np.diag(self.board) == symb)

        if diag_vic('X') | diag_vic('X', 1):
            self.winner = 'X'
            return True
        elif diag_vic('O') | diag_vic('O', 1):
            self.winner = 'O'
            return True

        return False

    def is_game_over(self):
        """ Check if the game is over due to victory or tie.

        Args:
            self

        Returns:
            bool: Returns True if victory on board or full board and tie

        """

        if self.is_row_column_victory() | self.is_row_column_victory(column=1) | self.is_diag_victory():
            return True
        elif np.sum(self.board == '') == 0:
            self.winner = 'Game Tied'
            return True
        else:
            return False

    def declare_winner(self):
        """ Print out who the winner is at the end of the game.

        Args:
            self

        Returns:
            None: Prints who won the game or if the game is tied

        """

        if self.winner == 'Game Tied':
            print 'Game Tied'
        else:
            print "Player {} won the game!".format(self.winner)

    def play_game(self):
        """ Plays the game by maintaing and updating the board.

        Args:
            self

        Returns:
            None: Stays in the while loop until there is a winner

        """

        move = np.random.choice(['X', 'O'])
        print "{} will go first!".format(move)

        while not self.is_game_over():
            loc = raw_input("Where do you want to move " + move + ': ')
            try:
                i, j = map(int, loc.split(','))
                if self.is_valid_move(i, j):
                    self.board[i, j] = move
                    if move == 'X':
                        move = 'O'
                    else:
                        move = 'X'
            except ValueError:
                print "Give Valild Integer Inputs. Try again!"

            print self.board

        self.declare_winner()


if __name__ == '__main__':
    import sys
    size = int(sys.argv[1])
    tictac = TicTacToe(size=size)
    tictac.play_game()
