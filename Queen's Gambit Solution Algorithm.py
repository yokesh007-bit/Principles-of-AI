import copy

N = 8  # Chessboard dimension: 8x8

def printSolution(board):
    for row in board:
        print("  " + " ".join(["Q" if cell else "." for cell in row]))
    print()

def isSafe(board, row, col):
    # Check upper column
    for i in range(row):
        if board[i][col]:
            return False
    # Check upper-left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False
    # Check upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j]:
            return False
    return True

def solve(board, row, solutions):
    if row == N:
        solutions.append(copy.deepcopy(board))
        return
    for col in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1                 # Place queen
            solve(board, row + 1, solutions)    # Recurse for next row
            board[row][col] = 0                 # Backtrack

def eightQueens():
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve(board, 0, solutions)
    print(f"8-Queens Backtracking Solver Completed.")
    print(f"Total Unique Solutions Found: {len(solutions)}")
    print("\nDisplaying Solution #1:")
    printSolution(solutions[0])
    print("Displaying Solution #2:")
    printSolution(solutions[1])
    return solutions

solutions = eightQueens()
