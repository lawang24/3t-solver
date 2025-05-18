import numpy as np

class Board:

    """
    Tic-tac-toe Game Board
    """

    def __init__(self, size: int = 3):
        self.size = size
        self.board = np.array([[None for _ in range(size)] for _ in range(size)])

    def has_player_won(self, player: str):

        row = np.any(np.all(self.board == player, axis=1))
        col = np.any(np.all(self.board == player, axis=0))
        main_diag = np.all(np.diag(self.board == player))
        reg_diag = np.all(np.diag(np.fliplr(self.board == player)))

        return row or col or main_diag or reg_diag

    def get_hash(self):
        return (tuple(tuple(row) for row in self.board))

    def copy(self):
        copy = Board(self.size)
        copy.board = self.board.copy()
        return copy
