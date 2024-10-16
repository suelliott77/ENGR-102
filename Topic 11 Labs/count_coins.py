# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 10b
# Date:         16 November 2022


valid = open('coins.txt', 'w')
#puts the list from the game into a list to iterate through
coinlist= []
with open('game.txt', 'r') as coincounter:
    for eachline in coincounter:
        coinstep= eachline.strip('\n').split()
        coinlist.append(coinstep)
    
num_coins= 0
steps = 0 
infinite= 0

while infinite == 0:
    #makes the loop stop when it gets to the end of the list
    if coinlist[steps] == coinlist[-1]:
        break 
    #if the first part of the steps is coin then it adds the number and then moves to the next step 
    if coinlist[steps][0] ==  'coin':
        if coinlist[steps][1][0] == '+':
            valid.write(f'{coinlist[steps][1][1:]}\n')
        else:
            valid.write(f'{coinlist[steps][1]}\n')
        num_coins += int(coinlist[steps][1])
        steps+=1
        continue
    #if the first part of steps is jump then it will jump that many in steps 
    if coinlist[steps][0] == 'jump':
        steps += int(coinlist[steps][1])
        continue
    #if the first part of the steps is none then nothing happens just goes to next step 
    if coinlist[steps][0] == 'none':
        steps+=1
        continue
    
print(f'Total coins collected: {num_coins}')
valid.close()
        