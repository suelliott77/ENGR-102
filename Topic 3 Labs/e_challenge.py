# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name          Sutton Elliott 
# Section:      504
# Assignment:   Challenge Program Lab 3
# Date:         14th Septermber 2022

from math import *
import math 

digits = int(input("Please enter the number of digits of precision for e: "))
print(f"The value of e to {digits} digits is: ", end='')
print('%.*f' % (digits,math.e))