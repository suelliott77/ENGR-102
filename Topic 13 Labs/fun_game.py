# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Jonathon Fulton 
# Section:      504
# Assignment:   Team Lab 13
# Date:         30 November 2022

import random
import turtle as turtle
import time



def winner(board):
    """This function accepts the Connect 4 board as a parameter.
    If there is no winner, the function will return the empty string "".
    If the user has won, it will return 'X', and if the computer has
    won it will return 'O'."""

    # Check rows for winner
    for row in range(6):
        for col in range(3):
            if (board[row][col] == board[row][col + 1] == board[row][col + 2] ==\
                board[row][col + 3]) and (board[row][col] != " "):
                return board[row][col]

    # Check columns for winner
    for col in range(6):
        for row in range(3):
            if (board[row][col] == board[row + 1][col] == board[row + 2][col] ==\
                board[row + 3][col]) and (board[row][col] != " "):
                return board[row][col]

    # Check diagonal (top-left to bottom-right) for winner

    for row in range(3):
        for col in range(4):
            if (board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] ==\
                board[row + 3][col + 3]) and (board[row][col] != " "):
                return board[row][col]


    # Check diagonal (bottom-left to top-right) for winner

    for row in range(5, 2, -1):
        for col in range(3):
            if (board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] ==\
                board[row - 3][col + 3]) and (board[row][col] != " "):
                return board[row][col]

    # No winner: return the empty string
    return ""

def display_board(board):
    '''This will create the board and all it to be seen after each turn'''
    print("   1   2   3   4   5   6   7")
    print("1: " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | " + board[0][3] + " | " + board[0][4] + " | " + board[0][5] + " | " + board[0][6] + " | " + board[0][7])
    print("  ---+---+---+---+---+---+---")
    print("2: " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | " + board[1][3] + " | " + board[1][4] + " | " + board[1][5] + " | " + board [1][6] + " | " + board [1][7])
    print("  ---+---+---+---+---+---+---+")
    print("3: " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | " + board[2][3] + " | " + board [2][4] + " | " + board [2][5] + " | " + board [2][6] + " | " + board [2][7])
    print("  ---+---+---+---+---+---+---+")
    print("4: " + board[3][0] + " | " + board[3][1] + " | " + board[3][2] + " | " + board[3][3] + " | " + board [3][4] + " | " + board [3][5] + " | " + board [3][6] + " | " + board [3][7])
    print("  ---+---+---+---+---+---+---+")
    print("5: " + board[4][0] + " | " + board[4][1] + " | " + board[4][2] + " | " + board[4][3] + " | " + board [4][4] + " | " + board [4][5] + " | " + board [4][6] + " | " + board [4][7])
    print("  ---+---+---+---+---+---+---+")
    print("6: " + board[5][0] + " | " + board[5][1] + " | " + board[5][2] + " | " + board[5][3] + " | " + board [5][4] + " | " + board [5][5] + " | " + board [5][6] + " | " + board [5][7])
    print()

def make_user_move(board):
    '''This function will look at each column and place where the user asks
    or it will tell the user to enter a new number if the number is invalid 
    because the column is full, not in range or something else'''
    try:
        valid_move = False
        while not valid_move:
            col = int(input("What col would you like to move to (1-7):"))
            for row in range (6,0,-1):
                if (1 <= row <= 6) and (1 <= col <= 7) and (board[row-1][col-1] == " "):
                    board[row-1][col-1] = 'X'
                    valid_move = True
                    break
            else:
                print("Sorry, invalid square. Please try again!\n")

    except NameError:
        print("Only numbers are allowed.")

    except IndexError:
        print("You can only select columns from (1-7), and rows from (1-6).")

def make_computer_move(board):
    '''This will do the computer's move with the O 
    it will be random so it does make the game pretty easy no cap'''
    valid_move = False
    while not valid_move:
        row = random.randint(0,5)
        col = random.randint(0, 6)
        for row in range (5,0,-1):
            if board[row][col] == " ":
                board[row][col] = "O"
                valid_move = True
                break

def main():
    '''This will start the game and allow you to see the rules. This will play the game until completion'''
    free_cells = 42
    users_turn = True
    count = 1
    ttt_board = [ [ " ", " ", " ", " ", " ", " "," ", " "], [ " ", " ", " ", " ", " "," ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "], [ " ", " ", " ", " ", " ", " ", " ", " "] ]
    print('The rules of the game are simple. Get four in a row before your opponent (the computer) for a chance to be put in the fun game Hall of Fame!')
    print('Just enter the column number (1-7) and the computer will enter the lowest place in that column')
    print("You can't enter a piece where there is already a piece or that is not within the board")
    print("\nHALL OF FAME \n")

    try:
        hall_of_fame = open("HallOfFame.txt", 'r')

        for name in hall_of_fame:
            print(str(count) + ".", name)
            print()
            count += 1

        hall_of_fame.close()

    except IOError:
        print("No Human Has Ever Beat Me.. mwah-ha-ha-ha!\n")

    choice = input("Would you like to go first? (y or n): ")

    if (choice == 'y' or choice=='Y'):
        users_turn = True

    elif (choice == 'n' or choice =='N') :
        users_turn = False

    else:
        print('invalid input')

    while not winner(ttt_board) and (free_cells > 0):
        display_board(ttt_board)
        if users_turn:
            make_user_move(ttt_board)
            users_turn = not users_turn
        else:
            make_computer_move(ttt_board)
            users_turn = not users_turn
        free_cells -= 1

    display_board(ttt_board)
    if (winner(ttt_board) == 'X'):
        print("You Won!")
        print("Your name will now be added to the Hall of Fame!")
        turtle.write("good job", align="center", font=("Cooper Black", 25, "italic"))

        hall_of_fame = open("HallOfFame.txt", 'a')
        name = input("Enter your name: ")
        hall_of_fame.write(name+ '\n')
        print("Your name has been added to the Hall of Fame!")

        hall_of_fame.close()

        print("\nGAME OVER")
    elif (winner(ttt_board) == 'O'):
        print("The Computer Won!")
        turtle.write("bad job", align="center", font=("Cooper Black", 25, "italic"))
        time.sleep(10)
        print("\nGAME OVER")
    else:
        print("Stalemate!")
        turtle.write("your both bad", align="center", font=("Cooper Black", 25, "italic"))
        time.sleep(10)
        print("\nGAME OVER \n")

#start the game

main()