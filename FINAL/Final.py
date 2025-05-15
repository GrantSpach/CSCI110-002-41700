#-------------------------------------------------------------------------------
# Name:        Tic-tac-toe
# Purpose:
#
# Author:      grant
#
# Created:     04/05/2025
# Copyright:   (c) grant 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

import os
import time

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
player = 1

Win = 1
Draw = -1
Running = 0
Stop = 1

Game = Running
Mark = 'X'

def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   | ")

def CheckPosition(x):
    if board[x] == ' ':
        return True
    else:
        return False

def CheckWin():
    global Game

    if board[1] == board[2] and board[2] == board[3] and board[1] != ' ':
        Game = Win
    elif board[4] == board[5] and board[5] == board[6] and board[4] != ' ':
        Game = Win
    elif board[7] == board[8] and board[8] == board[9] and board[7] != ' ':
        Game = Win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != ' ':
        Game = Win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != ' ':
        Game = Win
    elif board[3] == board[6] and board[6] == board[9] and board[3] != ' ':
        Game = Win
    elif board[1] == board[5] and board[5] == board[9] and board[5] != ' ':
        Game = Win
    elif board[3] == board[5] and board[5] == board[7] and board[5] != ' ':
        Game = Win
    elif board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and \
            board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and \
            board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        Game = Draw
    else:
        Game = Running

print("Welcome to Tic-Tac-Toe, may the odds be ever in your favor")
print("Player 1 [X]     Player 2 [O]\n")

while Game == Running:
    os.system('cls')
    DrawBoard()

    if player % 2 != 0:
        print("Player 1's chance")
        Mark = 'X'
    else:
        print("Player 2's chance")
        Mark = 'O'

    choice = int(input("Select 1-9 on your keyboard to chose a position on the board : "))
    if CheckPosition(choice):
        board[choice] = Mark
        player += 1
        CheckWin()

    os.system('cls')
    DrawBoard()

    if Game == Draw:
        print("Get back out there and go again, it's a draw!")                                                     # draws the game
    elif Game == Win:
        player -= 1
        if player % 2 != 0:
            print("Way to kick em' to the curb. Flawless Victory for Player 1")                                                                         # Player 1 wins
        else:
            print("Uh oh we got ourselves a champion, Player 2 comes out on top!")                                                                         # Player 2 wins