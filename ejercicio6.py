def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solveNQUtil(board, col):
    # base case: If all Pokemon are placed then return true
    if col >= len(board):
        return True

    # Consider this column and try placing this Pokemon in all rows one by one
    for i in range(len(board)):
        if isSafe(board, i, col):
            # Place this Pokemon in board[i][col]
            board[i][col] = 1

            # recur to place rest of the Pokemon
            if solveNQUtil(board, col + 1):
                return True

            # If placing Pokemon in board[i][col] doesn't lead to a solution then remove Pokemon from board[i][col]
            board[i][col] = 0

    # if the Pokemon can not be placed in any row in this column col then return false
    return False

def solveNQ(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solveNQUtil(board, 0):
        return None

    # Return first solution
    return [i for i in range(n) for j in range(n) if board[i][j] == 1]

# Results
for n in range(1, 16):
    sol = solveNQ(n)
    print(f"{n}-Pokeballs solution: {sol}")
