#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n):
    def solve(board, row):
        if row == n:
            solutions.append(list(board))
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(board, row + 1)

    solutions = []
    board = [-1] * n
    solve(board, 0)
    return solutions

def print_solutions(solutions):
    for solution in solutions:
        for col in solution:
            print("[{}, {}]".format(len(solution) - 1 - solution[::-1].index(col), col), end=" ")
        print()
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        solutions = solve_nqueens(n)
        print_solutions(solutions)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
