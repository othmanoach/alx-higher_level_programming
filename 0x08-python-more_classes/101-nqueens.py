#!/usr/bin/python3
import sys

def is_safe(queen, queens):
    for (row, col) in queens:
        if row == queen[0] or col == queen[1]:
            return False
        if (queen[0] - row) == (queen[1] - col) or (queen[0] - row) == (col - queen[1]):
            return False
    return True

def n_queens(n, row=0, queens=[]):
    if row == n:
        print(queens)
        return
    for col in range(n):
        queen = [row, col]
        if is_safe(queen, queens):
            queens.append(queen)
            n_queens(n, row + 1, queens)
            queens.pop()

if name == "main":
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
    n_queens(N)