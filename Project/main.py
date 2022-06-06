# Packages
import os
import time
import pygame
from pygame import mixer

mixer.init()

# Importing sounds
HurtSound = pygame.mixer.Sound("Sounds/Hurt.wav")
HealSound = pygame.mixer.Sound("Sounds/Heal.wav")
LoseSound = pygame.mixer.Sound("Sounds/Lose.wav")
WinSound = pygame.mixer.Sound("Sounds/Win.wav")
# Changing Sound levels
HurtSound.set_volume(0.3)
HealSound.set_volume(0.3)
LoseSound.set_volume(0.3)
WinSound.set_volume(0.4)

# Board
board = [[" " for a in range(12)] for b in range(12)]

# Extra Vars
waitTime = 1
enemyCount = 2
healthPotCount = 3
attackrange = 1
menu = True

# World data
data = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 4, 0, 0, 0, 0, 2, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 0, 0, 4, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 3, 2, 0, 0, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

# Lists to store objs
enemy = []
healthPots = []
exits = []


# Board creation
def CreatingEnvironmentLevel():
    global data
    # Creating borders of the board
    for a in range(12):
        board[0][a] = "-"

        board[11][a] = "-"
    f = 1
    while f < 11:
        board[f][0] = "|"
        board[f][11] = "|"
        f += 1


def Environment(boardData):
    row_count = 0
    # Adding in walls, enemies, etc
    for row in boardData:  # Going through the data row then column
        col_count = 0
        for num in row:
            if num == 1:
                board[row_count][col_count] = "-"
            if num == 2:
                board[row_count][col_count] = "|"
            if num == 3:
                Enemy = MainEnemy()
                Enemy.XPos = col_count
                Enemy.YPos = row_count
                Enemy.Position()
                enemy.append(Enemy)
            if num == 4:
                pot = HealthPot()
                pot.xPos = col_count
                pot.yPos = row_count
                pot.Position()
                healthPots.append(pot)
            if num == 5:
                Exit = ExitClass()
                Exit.xPos = col_count
                Exit.yPos = row_count
                Exit.Position()
                exits.append(Exit)
            col_count += 1
        row_count += 1


# Extra stuff
def Menu():
    global menu, waitTime
    print("Welcome to top down game in the console")
    print("@ is Player")
    print("Move with WASD keys")
    print("Press e to attack")
    print("o is a health Pot")
    print("# are enemies")

    choice = str(input("Ready to begin? (y/n)"))
    if choice == "y":
        clearConsole()
        menu = False
    elif choice == "n":
        clearConsole()
        print("Goodbye")
        quit()
    else:
        print("Please enter a correct input!!")
        time.sleep(waitTime)
        clearConsole()
        Menu()


def clearConsole():
    os.system('cls')


def printBoard():
    for count in board:
        print(" ".join(count))


# Movement

def DenyMove():
    global waitTime
    print("Cannot move!!")
    time.sleep(waitTime)


def PlayerInput():
    global waitTime, attackrange, enemyCount
    print("Press Q to quit")
    print("Health: ", Player1.health)
    move = str(input("Enter move: "))
    if move == "w":
        if board[Player1.yPos - 1][Player1.xPos] != " " and board[Player1.yPos - 1][Player1.xPos] != "X" and \
                board[Player1.yPos - 1][Player1.xPos] != "o":
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

    if move == "e":
        if board[Player1.yPos - attackrange][Player1.xPos] == "#":
            for count in range(enemyCount):
                if enemy[count].YPos == Player1.yPos - 1:
                    enemy[count].GettingDamaged()
                    print("You attacked the enemy!!")
                    time.sleep(waitTime)
        if board[Player1.yPos + attackrange][Player1.xPos] == "#":
            for count in range(enemyCount):
                if enemy[count].YPos == Player1.yPos + 1:
                    enemy[count].GettingDamaged()
                    print("You attacked the enemy!!")
                    time.sleep(waitTime)
        if board[Player1.yPos][Player1.xPos + attackrange] == "#":
            for count in range(enemyCount):
                if enemy[count].XPos == Player1.xPos + attackrange:
                    enemy[count].GettingDamaged()
                    print("You attacked the enemy!!")
                    time.sleep(waitTime)
        if board[Player1.yPos][Player1.xPos - attackrange] == "#":
            for count in range(enemyCount):
                if enemy[count].XPos == Player1.xPos - 1:
                    enemy[count].GettingDamaged()
                    print("You attacked the enemy!!")
                    time.sleep(waitTime)
        if board[Player1.yPos][Player1.xPos - attackrange] != "#" and board[Player1.yPos][
            Player1.xPos + attackrange] != "#" and board[Player1.yPos + attackrange][Player1.xPos] != "#" and \
                board[Player1.yPos - attackrange][Player1.xPos] != "#":
            print("There is nothing to attack here!!")
            time.sleep(waitTime)
    if move == "q":
        print("Goodbye")
        quit()


# Main classes

class MainEnemy:
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
        HurtSound.play()
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
        global waitTime
        if not self.canMove and not self.dead:
            if board[self.YPos - self.range][self.XPos] == self.player or board[self.YPos + self.range][
                self.XPos] == self.player or board[self.YPos][self.XPos - self.range] == self.player or \
                    board[self.YPos][self.XPos + self.range] == self.player:
                self.canMove = True

        if self.canMove and not self.dead:
            if self.YPos - Player1.yPos > 0:
                if board[self.YPos - 1][self.XPos] == "@":
                    Player1.health -= self.damage
                    HurtSound.play()
                    print("Enemy attack you!!")
                    time.sleep(waitTime)
                else:
                    if board[self.YPos - 1][self.XPos] == " ":
                        board[self.YPos][self.XPos] = " "
                        self.YPos -= 1
                        board[self.YPos][self.XPos] = self.graphics

            if self.YPos - Player1.yPos < 0:  # On Top
                if board[self.YPos + 1][self.XPos] == "@":
                    Player1.health -= self.damage
                    HurtSound.play()
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
                    HurtSound.play()
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
                    HurtSound.play()
                    time.sleep(waitTime)
                else:
                    if board[self.YPos][self.XPos - 1] == " ":
                        board[self.YPos][self.XPos] = " "
                        self.XPos -= 1
                        board[self.YPos][self.XPos] = self.graphics


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
            LoseSound.play()
            print("You died!!")
            time.sleep(2)
            quit()

    def Position(self):
        global board
        board[self.xPos][self.yPos] = self.char


class HealthPot:
    healAmount = 5
    xPos = 4
    yPos = 4
    graphics = "o"
    isdead = False

    def heal(self):
        global waitTime
        if board[Player1.yPos][Player1.xPos] == board[self.yPos][self.xPos]:
            if not self.isdead:
                Player1.health += self.healAmount
                print("You healed")
                HealSound.play()
                board[self.yPos][self.xPos] = " "
                board[self.yPos][self.xPos] = Player1.char
                self.isdead = True
                time.sleep(waitTime)
            else:
                pass

    def Position(self):
        global board
        board[self.yPos][self.xPos] = self.graphics


class ExitClass:
    xPos = 0
    yPos = 0
    gameOver = False
    graphics = "X"

    def Position(self):
        global board
        board[self.yPos][self.xPos] = self.graphics

    def CheckGameOver(self):
        global waitTime
        if board[Player1.yPos][Player1.xPos] == board[self.yPos][self.xPos]:
            WinSound.play()
            print("You Win")
            time.sleep(waitTime)
            quit()


# Creating Player instance
Player1 = Player()
Player1.Position()

# Setting up Level
Environment(data)
CreatingEnvironmentLevel()

# Main game update loop
while True:

    # Menu
    if menu:
        Menu()
    else:
        printBoard()
        PlayerInput()

        # Updating each object on board
        for e in range(enemyCount):
            enemy[e].HealthCheck()
            enemy[e].Moving()
        for i in range(healthPotCount):
            healthPots[i].heal()
        for q in range(1):
            exits[q].CheckGameOver()
        Player.CheckHealth(Player1)
        clearConsole()
