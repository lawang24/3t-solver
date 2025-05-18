# 3t-solver

**Tic Tac Toe Dynamic Programming Solver**

This project implements a complete solver for the game of Tic Tac Toe (3x3) using **Dynamic Programming** and **Value Iteration** to compute optimal strategies for each game state.

## Features

- ✅ Exhaustive enumeration of all valid board states
- ♟️ Turn-aware generation: ensures legal X/O counts
- 🔁 Value Iteration algorithm for solving the game tree with discounting

- 🧩 Clean and modular design, ideal for experimentation

## Project Structure

```
3t-solver/
├── board.py                # representation
├── value_iteration.py      # main engine logic
├── tests/                  # Unit tests
├── custom_types.py/        # mypy typing
└── README.md               # This file
```

## How It Works

1. **State Generation**: Recursively generates all valid Tic Tac Toe board configurations with correct turn balance.
2. **Terminal States**: Assigns +1 for X wins, -1 for O wins, and 0 for draws.
3. **Value Iteration**: Applies Bellman's principle to compute the value of each state assuming optimal play.

The algorithm effectively builds a complete value map for every possible game situation.

## Example Output

```
Board:
X | O | X
---------
O | X |  
---------
  | O |  

Value: +1 → X will win if both play optimally
```

## Usage

```bash
# Run the solver
python value_iteration.py
```

You can also edit `main.py` to test specific states or print value statistics.

## Requirements

- Python 3.8+
- numpy
- (dev) mypy and typing for type checking

## Run Tests

```bash
python -m unittest discover tests
```
