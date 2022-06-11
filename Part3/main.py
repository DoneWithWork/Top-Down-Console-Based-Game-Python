import os
import time

board = [[" " for a in range(12)] for b in range(12)]

waitTime = 1
enemyCount = 2
healthPotCount = 3
attackrange = 1


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


def PlayerInput():
    global waitTime, attackrange, enemyCount
    print("Press Q to quit")
    print("Health: ", Player1.health)
    move = str(input("Enter move:"))
    if move == "w":
        if board[Player1.yPos - attackrange][Player1.xPos] != " " and board[Player1.yPos - attackrange][
            Player1.xPos] != "X" and board[Player1.yPos - attackrange][Player1.xPos] != "o":
            DenyMove()
        else:
            board[Player1.yPos][Player1.xPos] = " "
            Player1.yPos -= 1
            board[Player1.yPos][Player1.xPos] = Player1.char
    if move == "s":
        if board[Player1.yPos + 1][Player1.xPos] != " " and board[Player1.yPos + 1][Player1.xPos] != "X" and \
                board[Player1.yPos + 1][Player1.xPos] != "o":
            DenyMove()
        else:
            board[Player1.yPos][Player1.xPos] = " "
            Player1.yPos += 1
            board[Player1.yPos][Player1.xPos] = Player1.char

    if move == "d":
        if board[Player1.yPos][Player1.xPos + 1] != " " and board[Player1.yPos][Player1.xPos + 1] != "X" and \
                board[Player1.yPos][Player1.xPos + 1] != "o":
            DenyMove()
        else:
            board[Player1.yPos][Player1.xPos] = " "
            Player1.xPos += 1
            board[Player1.yPos][Player1.xPos] = Player1.char

    if move == "a":
        if board[Player1.yPos][Player1.xPos - 1] != " " and board[Player1.yPos][Player1.xPos - 1] != "X" and \
                board[Player1.yPos][Player1.xPos - 1] != "o":
            DenyMove()
        else:
            board[Player1.yPos][Player1.xPos] = " "
            Player1.xPos -= 1
            board[Player1.yPos][Player1.xPos] = Player1.char
    if move == "q":
        print("Goodbye")
        quit()


def DenyMove():
    global waitTime
    print("Cannot move!!")
    time.sleep(waitTime)


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

while True:
    printBoard()
    PlayerInput()
    clearConsole()
