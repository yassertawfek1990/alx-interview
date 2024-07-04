#!/usr/bin/python3
"""N-Queens problem solver."""
import sys


def validate_and_get_n():
    """Validates the input and retrieves the size of the chessboard.

    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_conflict(queen1, queen2):
    """Determines if two queens are in conflict.

    Args:
        queen1 (tuple): Position of the first queen.
        queen2 (tuple): Position of the second queen.

    Returns:
        bool: True if queens conflict, False otherwise.
    """
    return (queen1[0] == queen2[0] or
            queen1[1] == queen2[1] or
            abs(queen1[0] - queen2[0]) == abs(queen1[1] - queen2[1]))


def solve_nqueens(n):
    """Finds all solutions for the N-Queens problem.

    Args:
        n (int): The size of the chessboard.

    Returns:
        list: All solutions for the N-Queens problem.
    """
    def place_queens(row, current_solution):
        if row == n:
            solutions.append(current_solution[:])
        else:
            for col in range(n):
                new_queen = (row, col)
                if all(not is_conflict(new_queen, q)
                        for q in current_solution):
                    current_solution.append(new_queen)
                    place_queens(row + 1, current_solution)
                    current_solution.pop()

    solutions = []
    place_queens(0, [])
    return solutions


if __name__ == "__main__":
    n = validate_and_get_n()
    solutions = solve_nqueens(n)
    for solution in solutions:
        print([[r, c] for r, c in solution])
