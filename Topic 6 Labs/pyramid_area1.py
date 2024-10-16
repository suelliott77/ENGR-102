# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Jonathon Fulton 
# Section:      504
# Assignment:   Team Lab 6a
# Date:         3 October 2022
from math import *

#needed inputs 
side= float(input("Enter the side length in meters: \n"))
layers= int(input("Enter the number of layers: \n"))
side_area=0
triangle_area= 0
total=0

#for loop to find the area 
for i in range(layers):
    #calculating the side area 
    side_area = (side**2) * (layers*3)
    
    #calculating the top area 
    triangle_area = ((sqrt(3)/4)*side**2) * (layers**2) - (layers-1)**2 * ((sqrt(3)/4)*side**2)
    
    #adding areas
    total += side_area + triangle_area
    layers-=1
    
print(f"You need {total:.2f} m^2 of gold foil to cover the pyramid")
    