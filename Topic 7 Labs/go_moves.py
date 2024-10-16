# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Jonathon Fulton 
# Section:      504
# Assignment:   Team Lab 7a
# Date:         10 October 2022

#black character chr(9679)
#white character chr(9675)

#board for go 
board1= [
    
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.','.']
    
    ]

column=0

for i in range(len(board1)):
    for  j in board1[column]:
        print(j, end=" ")
    print()

print()

moves= 1

while True:
    print("Black Move")
    print(f"MOVE {moves}")
    black_move_column = input("Enter column coordinate (1-9): ")
    if black_move_column == 'stop':
        break
    else:
        black_move_column = int(black_move_column)
    black_move_row = int(input("Enter row coordinate (1-9): "))
    
    if moves > 1:
        while board1[black_move_column - 1][black_move_row -1] != '.':
            print("SPOT TAKEN! Input again:")
            black_move_column= input("Enter column coordinate (1-9): ")
            if black_move_column == 'stop':
                break
            else:
                black_move_column = int(black_move_column)
            black_move_row = int(input("Enter row coordinate (1-9): "))
            
    board1[black_move_row - 1][black_move_column - 1] = chr(9679)
    
    for row in range(9):
        for column in range(9):
            print(board1[row][column], end= " ")
        print()
        
    print()
    moves+=1
    
    
    print("White Move")
    print(f"MOVE {moves}")
    white_move_column = input("Enter column coordinate (1-9): ")
    if white_move_column == 'stop':
        break 
    else:
        white_move_column = int(white_move_column)
    white_move_row = int(input("Enter row coordinate (1-9): "))
    
    while board1[white_move_row -1][white_move_column - 1] != '.':
        print("SPOT TAKEN! Input again: ")
        white_move_column= input("Enter column coordinate (1-9): ")
        if white_move_column == 'stop':
            break 
        else:
            white_move_column = int(white_move_column)
        white_move_row= int(input("Enter row coordinate (1-9): "))
        
    board1[white_move_row - 1][white_move_column - 1] = chr(9675)
    
    for row in range(9):
        for column in range(9):
            print(board1[row][column], end= " ")
        print()
        
    moves += 1
        
    
            
    
    

    




