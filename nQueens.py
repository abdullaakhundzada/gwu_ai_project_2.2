from dataclasses import dataclass
from typing import Optional
from collections import deque

@dataclass
class Position:
    """
    Representing a position on the chessboard.
    """
    row   : int
    column: int

    def is_attacking(self, other: 'Position') -> bool:
        """
        Check if this position attacks another position according to queen movement rules.
        """
        return (
            self.column == other.column or  # Same column
            abs(self.column - other.column) == abs(self.row - other.row)  # Same diagonal
        )

class NQueensSolver:
    """
    Solves the N-Queens problem using Constraint Satisfaction Problem (CSP) techniques.
    
    This implementation uses a combination of:
    - Backtracking search
    - AC3 (Arc Consistency Algorithm #3) for constraint propagation
    - Basic variable selection heuristic
    """

    def __init__(self, board_size: int):
        """
        Args:
            board_size: int
                The size of the chessboard (N x N)
        """
        assert board_size > 1, "Board size must be a positive integer."
            
        self.size = board_size
        self.all_positions = range(board_size)
        self.domains = {row: set(self.all_positions) for row in self.all_positions}
        self.assignment: dict[int, int] = {}

    def solve(self) -> Optional[dict[int, int]]:
        """
        Find a solution to the N-Queens problem.

        Returns:
            dict mapping row -> column positions of queens, or None if no solution exists
        """
        self.assignment = {}  # Reset assignment for multiple runs with single object
        return self._backtrack_with_ac3(self.domains)

    def _backtrack_with_ac3(self, current_domains: dict[int, set[int]]) -> Optional[dict[int, int]]:
        """
        Recursive backtracking search with AC3 constraint propagation.

        Args:
            current_domains: dict[int, set[int]]
                Available values for unassigned variables

        Returns:
            Complete valid assignment or None if no solution exists
        """
        # Base case: all rows assigned
        if len(self.assignment) == self.size:
            return self.assignment

        # Select unassigned row with smallest domain (MRV heuristic)
        row = self._select_unassigned_variable(current_domains)
        if row is None:
            return None

        for column in current_domains[row]:
            position = Position(row, column)
            if self._is_valid_placement(position):
                self.assignment[row] = column
                
                local_domains = {r: set(current_domains[r]) for r in self.all_positions}
                local_domains[row] = {column}  # Fix domain of current variable

                revised_domains = self._enforce_arc_consistency(local_domains)
                
                if revised_domains:  # No domain wipeout occurred
                    next_domains = {r: set(domain) for r, domain in revised_domains.items()}
                    result = self._backtrack_with_ac3(next_domains)
                    if result:
                        return result
                
                # Backtrack: remove assignment and try next value, if no result
                del self.assignment[row]

        return None

    def _select_unassigned_variable(self, domains: dict[int, set[int]]) -> Optional[int]:
        """
        Select an unassigned variable (row) using the Minimum Remaining Values (MRV) heuristic.
        
        Args:
            domains: dict[int, list[int]]
                Current domains for all variables
            
        Returns:
            Row index of selected variable, or None if all assigned
        """
        unassigned = [row for row in self.all_positions if row not in self.assignment]
        if not unassigned:
            return None
            
        return min(unassigned, key=lambda row: len(domains[row]))

    def _is_valid_placement(self, position: Position) -> bool:
        """
        Check if placing a queen at the given position conflicts with existing queens.

        Args:
            position: Position
                Proposed queen position to check

        Returns:
            True if placement is valid, False if it conflicts with any existing queen
        """
        return all(
            not position.is_attacking(Position(row, col))
            for row, col in self.assignment.items()
        )

    def _enforce_arc_consistency(self, domains: dict[int, set[int]]) -> Optional[dict[int, set[int]]]:
        """
        Apply AC3 algorithm to enforce arc consistency between all pairs of variables.

        Args:
            domains: dict[int, set[int]]
                Current domains for all variables

        Returns:
            Arc consistent domains, or None if domain wipeout occurs
        """
        # Initialize queue with all arcs
        queue = deque(
            (row1, row2)
            for row1 in self.all_positions
            for row2 in self.all_positions
            if row1 != row2
        )

        while queue:
            row1, row2 = queue.popleft()
            if self._revise_arc(row1, row2, domains):
                if not domains[row1]:
                    return None  # Domain wipeout
                # Add affected arcs back to queue
                queue.extend(
                    (row3, row1)
                    for row3 in self.all_positions
                    if row3 != row1 and row3 != row2
                )
        
        return domains

    def _revise_arc(self, row1: int, row2: int, domains: dict[int, set[int]]) -> bool:
        """
        Revise the domain of row1 with respect to row2.

        Args:
            row1: int
                First row (variable to be revised)
            row2: int
                Second row (constraint variable)
            domains: dict[int, set[int]]
                Current domains of all variables

        Returns:
            True if domain was revised, False otherwise
        """
        revised = False
        
        for col1 in list(domains[row1]):
            pos1 = Position(row1, col1)
            
            if not any(
                not pos1.is_attacking(Position(row2, col2))
                for col2 in domains[row2]
            ):
                domains[row1].remove(col1)
                revised = True
                
        return revised