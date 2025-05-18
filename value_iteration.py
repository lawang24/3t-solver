from typing import Dict, List
from board import Board
from custom_types import BoardHashType


class ValueIterationEngine:
    """
    Value Iteration Engine for the game tic-tac-toe
    """

    def __init__(self, board_size: int = 3) -> None:
        self.board_size = board_size

        # used to represent values at all states
        self.state_to_value: Dict[BoardHashType, float] = {}

        # create adjacency list for easier graph traversal for value iteration
        self.adj: Dict[BoardHashType, List[BoardHashType]] = {}

        self.total_cells: int = board_size * board_size  # assuming 3x3 board
        self._generate_all_states()

    def _generate_all_states(self) -> None:
        starting_board = Board(self.board_size)
        self._backtrack(starting_board, x_count=0, o_count=0)

    def _backtrack(self, board: Board, x_count: int, o_count: int) -> None:

        curr_hash = board.get_hash()

        if curr_hash in self.state_to_value:
            return

        # give a winning reward for player 1
        if board.has_player_won("X"):
            self.state_to_value[curr_hash] = 1
            return

        # give a losing reward for player 2
        if board.has_player_won("O"):
            self.state_to_value[curr_hash] = -1
            return

        # add current state
        self.state_to_value[curr_hash] = 0.0
        self.adj[curr_hash] = []

        for row in range(self.board_size):
            for col in range(self.board_size):
                if board.board[row][col] is None:
                    # X player's turn
                    if x_count <= o_count:

                        # new move
                        board_copy = board.copy()
                        board_copy.board[row, col] = "X"

                        # transition
                        self.adj[curr_hash].append(board_copy.get_hash())

                        # recurse
                        self._backtrack(board_copy, x_count + 1, o_count)

                    # Y player's turn
                    else:

                        # new move
                        board_copy = board.copy()
                        board_copy.board[row, col] = "O"

                        # transition
                        self.adj[curr_hash].append(board_copy.get_hash())

                        # recurse
                        self._backtrack(board_copy, x_count, o_count + 1)

    def run_value_iteration(self):

        max_ep = float('inf')

        count = 0

        while max_ep > 10**-6:

            max_ep = 0

            for state, old_value in self.state_to_value.items():
                champ = float("-inf")

                # not an end reward state
                if state in self.adj:
                    for nei in self.adj[state]:
                        champ = max(champ, self.state_to_value[nei])

                    new = 0.9 * champ
                    self.state_to_value[state] = new

                    max_ep = max(max_ep, old_value - new)

            count += 1

        print('count', count)
            

if __name__ == "__main__":
    engine = ValueIterationEngine()
    engine.run_value_iteration()

    empty_board = Board()

    for neighbor in engine.adj[empty_board.get_hash()]:
        print(neighbor)
        print(engine.state_to_value[neighbor])
