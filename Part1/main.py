import os

board = [[" " for a in range(12)] for b in range(12)]


def CreatingEnvironment():
    for a in range(12):
        board[0][a] = "-"
        board[11][a] = "-"
    f = 1
    while f < 11:
        board[f][0] = "|"
        board[f][11] = "|"
        f += 1


def printBoard():
    for count in board:
        print(" ".join(count))


def clearConsole():
    os.system('cls')


CreatingEnvironment()
printBoard()
