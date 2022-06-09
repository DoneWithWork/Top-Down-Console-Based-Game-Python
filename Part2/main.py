import os
import time

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


class Player:
    health = 50
    xPos = 1
    yPos = 1
    damage = 2
    char = "@"
    dead = False

    def CheckHealth(self):
        if self.health <= 0:
            board[self.yPos][self.xPos] = " "
            self.dead = True
            print("You died!!")
            time.sleep(2)
            quit()

    def Position(self):
        board[self.yPos][self.xPos] = self.char


Player1 = Player()
Player1.Position()
CreatingEnvironment()
printBoard()
