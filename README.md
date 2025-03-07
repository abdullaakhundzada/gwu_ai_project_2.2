# N-Queens Problem Solver (Backtracking Search with AC3 and MRV)

## Description

This project implements a solution to the N-Queens problem using backtracking search, enhanced with Arc Consistency (AC3) constraint propagation and the Minimum Remaining Values (MRV) heuristic. The goal is to find a valid placement of N queens on an N x N chessboard such that no two queens threaten each other (i.e., no two queens are in the same row, column, or diagonal).

## Files Description

**Project Directory:**
```bash
nQueens_project
├── document.pdf
├── nQueens.py
├── utils.py
├── main.py
├── test.py
└── README.md
```

*   **`nQueens.py`**: Contains the core algorithm implementation for the N-Queens problem. This includes the `NQueensSolver` class with methods for backtracking search, AC3 constraint propagation, MRV heuristic, and related helper functions. Also includes the `Position` class to represent a position on the chessboard.
*   **`utils.py`**: Provides utility functions such as `print_board_representation` for displaying the chessboard and `is_valid_assignment` for verifying the correctness of a queen placement.
*   **`main.py`**: The main entry point of the program. It handles command-line argument parsing, initializes the `NQueensSolver`, runs the solver, and prints the results (solution, board representation, and execution time).
*   **`test.py`**: Contains unit tests using the `unittest` framework to verify the correctness of the `NQueensSolver` for various board sizes.
*   **`README.md`**: This file, providing project description and usage instructions.

## How to Run

1.  **Save the project files:** Ensure you have saved all Python files (`nQueens.py`, `utils.py`, `main.py`, `test.py`) in the same directory, under the project name `nQueens_project`.

2.  **Run the `main.py` script:**

    You can execute the solver using the `main.py` script. By default, it solves the N-Queens problem for N=16. You can specify a different board size and control the output using command-line arguments:

    ```bash
    python main.py
    ```

    To see the description of available arguments, run:

    ```bash
    python main.py --help
    ```

    Which would give the description:

    ```
    usage: main.py [-h] [--n N] [--dont_print_result]
                   [--dont_print_representation] [--dont_print_timing]

    options:
      -h, --help            show this help message and exit
      --n N                 The shape of the rectangular board. (default: 16)
      --dont_print_result   If set, does not print the output of the N-Queens
                            solver directly.
      --dont_print_representation
                            If set, does not print the simple view of the output
                            on a 2D board with dots for empty places and 'Q'
                            letters for queens
      --dont_print_timing   If set, does not print the ellapsed processing time.
    ```

    To solve for a different board size (e.g., N=8):

    ```bash
    python main.py --n 8
    ```

    To suppress printing the raw solver output:

    ```bash
    python main.py --dont_print_result
    ```

    To suppress printing the board representation:

    ```bash
    python main.py --dont_print_representation
    ```

    To suppress printing the execution time:

    ```bash
    python main.py --dont_print_timing
    ```

    You can combine these arguments as needed. For example, to solve for an 8x8 board and only print the board representation:

    ```bash
    python main.py --n 8 --dont_print_result --dont_print_timing
    ```

    The program will output the solution, board representation, and execution time based on the specified arguments.

## Algorithm Explanation (Brief)

This project employs **Backtracking Search** enhanced with **AC3 constraint propagation** and the **MRV heuristic** to solve the N-Queens problem.

*   **State:** Implicitly represented by the partial assignment of queens to rows during the backtracking process. Domains of possible columns for each row are maintained and updated.
*   **Constraints:** No two queens can be in the same row, column, or diagonal.
*   **MRV Heuristic:** The Minimum Remaining Values (MRV) heuristic is used to select the next row to assign a queen, choosing the row with the fewest remaining valid column options.
*   **AC3 Constraint Propagation:** The Arc Consistency Algorithm #3 (AC3) is used to proactively reduce the search space by removing inconsistent values from the domains of unassigned variables. It enforces arc consistency between rows, pruning domains and detecting failures earlier in the search.
*   **Backtracking Search:** A depth-first search approach that systematically explores possible queen placements. When a conflict is detected or a dead-end is reached, the algorithm backtracks to a previous state and tries a different placement.

## Test Cases

Unit tests are implemented in `test.py` using the `unittest` framework. These tests cover:

*   Randomly generated board sizes within the range of N=10 to N=150.
*   Verification of solution validity using the `is_valid_assignment` function.
*   Timing measurements for performance evaluation.

To run the tests, execute:

```bash
python test.py
```

The tests will run and report whether the N-Queens solver implementation is working correctly. Successful tests will indicate "OK".

## Note
The project document can be found under the name of document.pdf in the project repository