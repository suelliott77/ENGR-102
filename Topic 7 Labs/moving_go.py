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

col=1
#board plus numbers for rows and columns 
print("1 2 3 4 5 6 7 8 9")

#board for go 
board1= [[". "*9]]*9

for i in board1:
    for j in i :
        print(j, end=" ")
    print(col, end=" ")
    print()
    col+=1
    
for i in range(81):
    print(f"Turn number: {i+1}")
    column= int(input("Please enter the column number you want to use: \n"))
    row= int(input("Please enter the row number you want to use \n"))
    if i % 2 ==1:
        
    else:
        board1[column,row]= chr(9675)
    




