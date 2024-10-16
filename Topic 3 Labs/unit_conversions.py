# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Chris Shaji
# Section:      504
# Assignment:   Team Lab 3a
# Date:         14 September 2022

from math import *

#Starting Input 
print("Please enter the quantity to be converted: ")
conversion= float(input())

#Pounds of Force to Newtons
pounds_to_newtons= 4.4482216
newtons= pounds_to_newtons*conversion
print(f"{conversion:.2f} pounds force is equivalent to {newtons:.2f} Newtons")

#Meters to Feet
meters_to_feet= 3.2808399
feet= meters_to_feet*conversion
print(f"{conversion:.2f} meters is equivalent to {feet:.2f} feet")

#Atmospheres to Kilopascals
atmospheres_to_kPa= 101.325
kilopascals= atmospheres_to_kPa*conversion
print(f"{conversion:.2f} atmospheres is equivalent to {kilopascals:.2f} kilopascals")

#Watts to BTU per hour 
watts_to_BTU= 3.412141633
BTU= watts_to_BTU*conversion
print(f"{conversion:.2f} watts is equivalent to {BTU:.2f} BTU per hour")

#Liters per second to Us gallon per minute 
liters_to_gallons= 15.850324
gallons= liters_to_gallons*conversion
print(f"{conversion:.2f} liters per second is equivalent to {gallons:.2f} US gallons per minute")

#Celsius to Fahrenheit
fahrenheit= ((9/5)*conversion) + 32
print(f"{conversion:.2f}degrees Celsius is equivalent to {fahrenheit:.2f} degrees Fahrenheit")

