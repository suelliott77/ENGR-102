# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Chris Shaji
# Section:      504
# Assignment:   Team Lab 4c
# Date:         19 September 2022

############ Part A ############
a = input('Enter True or False for a:\n')
b = input('Enter True or False for b:\n')
c = input('Enter True or False for c:\n')

# a values 
if a == 'True' or a == 't' or a == 'T':
    a = True
elif a == 'False' or a == 'f' or a== 'F':
    a = False
    
# b values 
if b == 'True' or b == 't' or b == 'T':
    b = True
elif b == 'False' or b == 'f' or b== 'F':
    b = False 
    
# c values 
if c == 'True' or c == 't' or c == 'T':
    c = True
elif c == 'False' or c== 'f' or c == 'F':
    c = False 
    
############ Part B ############
print("a and b and c: ", a and b and c)
print("a or b or c: ", a or b or c)

############ Part C ############
print("XOR:", not(a == b))
print("Odd number: " , a and b and c)

############ Part D ############
print("Complex 1: " , (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b))
print("Complex 2: " , (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b)))))
print("Simple 1: " , (a and b) or (c or b) or (a or c) or a)
print("Simple 2: " , (b or c) and (a or c) or (not c))

    
    
    
    
    
