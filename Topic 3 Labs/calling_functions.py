# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sutton Elliott 
# Section:      504
# Assignment:   Individual Lab- Calling Functions
# Date:         14th Septermber 2022

from math import *

def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# printresult('square', 2.236, 5)
# Your code goes here

#Area of a Triangle 
side = float(input("Please enter the side length: "))
print()
area = (sqrt(3)/4) * side * side
shape = "triangle"
printresult(shape , side , area)

#Area of a Square 
area = side * side
shape = "square"
printresult(shape , side , area)

#Area of a Pentagon
area = 1/4 * sqrt(5*(5+2*sqrt(5))) * side * side
shape = "pentagon"
printresult(shape , side , area)

#Area of a Dodecagon 
area = (3 * (2 + sqrt(3))* (side * side))
shape = "dodecagon"
printresult(shape , side , area)
