# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 6b
# Date:         5 October 2022

from math import *

#needed inputs from user 
num= float(input("Enter a positive integer: \n"))
print(f"The Juggler sequence starting at {num:.0f} is: ")
count=0

#first number in sequence
if (num>1):
    print(f"{num:.0f}", end=", ")


#loops need for sequence 
while num>1:
    if (num % 2 == 0):
        count+=1
        num = floor(sqrt(num))
        if (num==1):
            break
        print(f"{num:.0f}", end=", ")
    else:
        num = floor(sqrt(num**3))
        count+=1
        if (num==1):
            break
        print(f"{num:.0f}", end=", ")
        
print(f"{num:.0f}", end="")
print()
print(f"It took {count} iterations to reach 1")


        

