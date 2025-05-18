import unittest
import numpy as np
from board import Board  # Replace with your actual module if needed

class TestBoard(unittest.TestCase):
    
    def test_row_win(self):
        board = Board()
        board.board[1] = ['X', 'X', 'X']
        self.assertTrue(board.has_player_won('X'))
        self.assertFalse(board.has_player_won('O'))

    def test_column_win(self):
        board = Board()
        board.board[:, 2] = ['O', 'O', 'O']
        self.assertTrue(board.has_player_won('O'))
        self.assertFalse(board.has_player_won('X'))

    def test_main_diagonal_win(self):
        board = Board()
        for i in range(board.size):
            board.board[i, i] = 'X'
        self.assertTrue(board.has_player_won('X'))

    def test_anti_diagonal_win(self):
        board = Board()
        for i in range(board.size):
            board.board[i, board.size - 1 - i] = 'O'
        self.assertTrue(board.has_player_won('O'))

    def test_no_win(self):
        board = Board()
        board.board = np.array([
            ['X', 'O', 'X'],
            ['O', 'O', 'X'],
            ['X', 'X', 'O']
        ])
        self.assertFalse(board.has_player_won('X'))
        self.assertFalse(board.has_player_won('O'))

    def test_board_copy(self):
        board = Board()
        board.board[0, 0] = 'X'
        board_copy = board.copy()
        self.assertEqual(board.board[0, 0], board_copy.board[0, 0])
        board_copy.board[0, 0] = 'O'
        self.assertNotEqual(board.board[0, 0], board_copy.board[0, 0])

    def test_board_hash(self):
        board1 = Board()
        board2 = Board()
        self.assertEqual(board1.get_hash(), board2.get_hash())

        board1.board[0, 0] = 'X'
        self.assertNotEqual(board1.get_hash(), board2.get_hash())


if __name__ == '__main__':
    unittest.main()
