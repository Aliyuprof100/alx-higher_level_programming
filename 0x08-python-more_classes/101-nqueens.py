#!/usr/bin/python3
"""This is header"""


import sys

def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col, N, solutions):
    """
    Solve the N-Queens problem using backtracking.
    """
    if col >= N:
        # Found a solution, append to solutions list
        solutions.append([[i, row.index(1)] for i, row in enumerate(board)])
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen
            board[i][col] = 1
            # Recur to place the rest
            solve_nqueens(board, col + 1, N, solutions)
            # Backtrack
            board[i][col] = 0

def nqueens(N):
    """
    Main function to solve the N-Queens problem and print solutions.
    """
    # Initialize the chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    # Validate the input
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem
    nqueens(N)
