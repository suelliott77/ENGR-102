# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sutton Elliott
# Section:      504
# Assignment:   Lab 4d
# Date:         21 September 2022

from math import *

#coefficient variables 
a = float(input('Please enter the coefficient A: \n'))
b = float(input('Please enter the coefficient B: \n'))
c = float(input('Please enter the coefficient C: \n'))

d = b * b - (4*a*c)
sqrt_d = sqrt(abs(d))

if (a == 0 and b == 0):
    print("You entered an invalid combination of coefficients!")
elif (a == 0):
    print(f"The root is x = {-(c/b):.1f}")
elif (d > 0):
    print(f"The roots are x = {(-b + sqrt_d)/(2 * a)} and x = {(-b - sqrt_d)/(2 * a)}")
elif d == 0:
    print(f"The root is x = {-b / 2*a}")
elif d < 0:
    print(f"The roots are x = {-b / (2*a)} + 1.0i and x = -{sqrt_d} - 1.0i")
else:
    print("You entered an invalid combination of coefficients!")
