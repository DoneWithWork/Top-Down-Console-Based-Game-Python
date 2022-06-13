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


class Enemy:
    count = 1
    health = 6
    XPos = 0
    YPos = 0
    canMove = False
    dead = False
    range = 3
    graphics = "#"
    damage = 2
    player = "@"

    def GettingDamaged(self):
        self.health -= Player1.damage

    def HealthCheck(self):
        global waitTime
        if self.health <= 0 and not self.dead:
            board[self.YPos][self.XPos] = " "
            print("The enemy died!!")
            time.sleep(waitTime)
            self.dead = True

    def Position(self):
        global board
        board[self.YPos][self.XPos] = self.graphics

    def Moving(self):
        global board
        if not self.canMove and not self.dead:
            if board[self.YPos - self.range][self.XPos] == self.player or board[self.YPos + self.range][
                self.XPos] == self.player or board[self.YPos][self.XPos - self.range] == self.player or \
                    board[self.YPos][self.XPos + self.range] == self.player:
                self.canMove = True
        if self.canMove and not self.dead:
            if self.YPos - Player1.yPos > 0:
                if board[self.YPos - 1][self.XPos] == "@":
                    Player1.health -= self.damage
                    print("Enemy attacked you!!")
                    time.sleep(waitTime)
                else:
                    if board[self.YPos - 1][self.XPos] == " ":
                        board[self.YPos][self.XPos] = " "
                        self.YPos -= 1
                        board[self.YPos][self.XPos] = self.graphics

            if self.YPos - Player1.yPos < 0:  # On Top
                if board[self.YPos + 1][self.XPos] == "@":
                    Player1.health -= self.damage
                    print("Enemy attack you!!")
                    time.sleep(waitTime)
                else:
                    if board[self.YPos + 1][self.XPos] == " ":
                        board[self.YPos][self.XPos] = " "
                        self.YPos += 1
                        board[self.YPos][self.XPos] = self.graphics

            if self.XPos - Player1.xPos < 0:  # On Top
                if board[self.YPos][self.XPos + 1] == "@":
                    Player1.health -= self.damage
                    print("Enemy attack you!!")
                    time.sleep(waitTime)
                else:
                    if board[self.YPos][self.XPos + 1] == " ":
                        board[self.YPos][self.XPos] = " "
                        self.XPos += 1
                        board[self.YPos][self.XPos] = self.graphics

            if self.XPos - Player1.xPos > 0:  # On Top
                if board[self.YPos][self.XPos - 1] == "@":
                    Player1.health -= self.damage
                    print("Enemy attack you!!")
                    time.sleep(waitTime)
                else:
                    if board[self.YPos][self.XPos - 1] == " ":
                        board[self.YPos][self.XPos] = " "
                        self.XPos -= 1
                        board[self.YPos][self.XPos] = self.graphics


class HealthPot:
    healAmount = 5
    xPos = 3
    yPos = 3
    graphics = "o"
    isdead = False

    def heal(self):
        if board[Player1.yPos][Player1.xPos] == board[self.yPos][self.xPos]:
            if not self.isdead:
                Player1.health += self.healAmount
                print("You healed!!")
                board[self.yPos][self.xPos] = " "
                board[self.yPos][self.xPos] = Player1.char
                self.isdead = True
                time.sleep(waitTime)
            else:
                pass

    def Position(self):
        board[self.yPos][self.xPos] = self.graphics


healthPots = []
healthPot1 = HealthPot()
healthPot1.Position()
healthPots.append(healthPot1)
enemy = []
Enemy1 = Enemy()
Enemy1.XPos = 5
Enemy1.YPos = 5
Enemy1.Position()
enemy.append(Enemy1)
Player1 = Player()
Player1.Position()
CreatingEnvironment()

while True:
    printBoard()
    PlayerInput()
    for i in range(len(enemy)):
        enemy[i].Moving()
        enemy[i].HealthCheck()
    for e in range(len(healthPots)):
        healthPots[e].heal()
    clearConsole()
