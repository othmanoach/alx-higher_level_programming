def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    
    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True
#!/usr/bin/python3

def solve_nqueens(board, row, n, solutions):
    """Utilize backtracking to solve the N-Queens puzzle."""
    
    if row == n:
        # Found a solution
        solutions.append(board_to_result(board, n))
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_nqueens(board, row + 1, n, solutions)
            # Backtrack
            board[row][col] = 0

def board_to_result(board, n):
    """Convert the board to result format."""
    result = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                result.append([i, j])
                break
    return result

def n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    return solutions

# Example usage:
N = 4
solutions = n_queens(N)
for sol in solutions:
    print(sol)