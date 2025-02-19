from nQueens import Position

def print_board_representation(assignment : dict[int, int]) -> str:
    """
    Create a string representation of the current board state.

    Args:
        assignment: dict
            The locations of the Queens in the board. Keys represent the rows, values represent the columns.

    Returns:
        A string showing the current board state with "Q" for queens and "." for empty squares
    """
    board = [["." for _ in range(len(assignment.keys()))] for _ in range(len(assignment.keys()))]
    for row, col in assignment.items():
        board[row][col] = "Q"
    print("\n".join(" ".join(row) for row in board))

def is_valid_assignment(assignment: dict[int, int]) -> bool:
    """
    Checks whether the given assignment/configuration is correct or not, according to
    the positions of the queens, whether any one is attacking another one or not.

    Args:
        assignment: dict[int, int]
            The result of solving the puzzle
    
    Returns:
        bool : whether the current assignment is valid or not.
    """
    if not assignment:
        return False # default case

    queens : list = [Position(row, assignment[row]) for row in assignment.keys()]

    while queens:
        current_queen = queens[0]
        queens.pop(0)
        for another_queen in queens:
            if current_queen.is_attacking(another_queen): # conflict found
                return False
    
    return True # no conflict found

