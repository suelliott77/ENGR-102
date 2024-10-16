# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sutton Elliott, Jake Nemetz, Jonathan Gao, Chris Shaji
# Section:      504
# Assignment:   Team Lab 1c
# Date:         11th Septermber 2022

import math

#initial variables 
time_initial=10
time_final=55
kmpast_initial=2026
kmpast_final=23026

#needed formulas
slope=((kmpast_final - kmpast_initial) / (time_final- time_initial))
time= 25

findposition=(slope*(time-time_initial) + kmpast_initial)

#part 1
print("Part 1:")
print("For t = ", (time), "minutes, the position p= ", (findposition), "kilometers")
print()

timepart2= 300
findposition2= ((slope*(timepart2-time_initial) + kmpast_initial) % (2*math.pi*6745))

#part 2
print("Part 2:")
print("For t = ", (timepart2), "minutes, the position p =", (findposition2), "kilometers" )