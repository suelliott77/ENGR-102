# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Jonathon Fulton
# Section:      504
# Assignment:   Team Lab 6b
# Date:         3 October 2022
from math import *

#needed inputs 
# formual for number of vertical sides if 1.5x^2 + 1.5x 
side= float(input("Enter the side length in meters: \n"))
layer= int(input("Enter the number of layers: \n"))

#finding the area using the sum function
sides = (1.5) * (layer**2) + (1.5) * (layer)
sides_area= sides*(side**2)

#area of the top parts 
top = (layer**2)* ((sqrt(3)/4) * (side**2))

#total area top + sides 
area= top + sides_area
 
#final output                  
print(f"You need {area:.2f} m^2 of gold foil to cover the pyramid")


