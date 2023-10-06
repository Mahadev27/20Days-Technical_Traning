def is_safe(board, row, col, n):
    # Check if a queen can be placed at board[row][col]

    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, n):
    # Base case: If all queens are placed, add the solution to the result
    if row == n:
        solutions.append(["   ".join(["Q" if cell == 1 else "." for cell in row]) for row in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, n)
            board[row][col] = 0

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    global solutions
    solutions = []
    solve_n_queens_util(board, 0, n)
    return solutions

# Example usage:
n = int(input())
solutions = solve_n_queens(n)

for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()
