class Nodo:
    def __init__(self, fila, col):
        self.fila = fila
        self.col = col

def isSafe(board, row, col):
    for i in range(col):
        if board[i].fila == row or abs(board[i].fila - row) == abs(board[i].col - col):
            return False
    return True

def solveNQUtil(board, col):
    if col >= len(board):
        return True

    for row in range(len(board)):
        if isSafe(board, row, col):
            board[col] = Nodo(row, col)
            if solveNQUtil(board, col + 1):
                return True
            board[col] = None

    return False

def solveNQ(n):
    board = [None] * n

    if not solveNQUtil(board, 0):
        return None

    sol = [None] * n
    for i in range(n):
        sol[i] = board[i].fila

    return sol

# Imprimir las soluciones para distintas cantidades de PokéBolas
for n in range(1, 16):
    sol = solveNQ(n)
    print(f"{n}-Pokeballs solution: {sol}")
