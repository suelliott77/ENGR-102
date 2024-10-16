# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 6a
# Date:         5 October 2022

#needed inputs from user 
howdy= int(input("Enter an integer: \n"))
whoop= int(input("Enter another integer: \n"))

#for loop for numbers 1-100
for i in range(1,101): 
    #both are divisible
    if (i % howdy == 0 and i % whoop == 0):
        print("Howdy Whoop")
    #howdy is evenly divisible
    elif (i % howdy == 0):
        print("Howdy")
    #whoop is evenly divisible
    elif (i % whoop == 0):
        print("Whoop")
    #neither are dividsible
    else:
        print(i)
        
        