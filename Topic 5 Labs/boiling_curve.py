# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 5a
# Date:         28 September 2022

from math import *
import math

#user input of excess heat 
excess= float(input("Enter the excess temperature: \n"))

#Slope of AB
AB_slope= (log10(7000/1000)) / (log10(5/1.3))
#Slope of BC
BC_slope= (log10(1.5E6/7000)) / (log10(30/5))
#Slope of CD
CD_slope= (log10(2.5E4/1.5E6)) / (log10(120/30))
#Slope of DE
DE_slope= (log10(1.5E6/2.5E4)) / (log10(1200/120))

#if else statement for different segments + final output 
if (excess>=1.3 and excess<=5):
    surface_heat= 1000*(excess/1.3)**AB_slope
    print(f"The surface heat flux is approximately {surface_heat:.0f} W/m^2")
elif (excess>5 and excess<30):
    surface_heat= 7000*(excess/5)**BC_slope
    print(f"The surface heat flux is approximately {surface_heat:.0f} W/m^2")
elif (excess>=30 and excess<120):
    surface_heat= 1.5E6*(excess/30)**CD_slope
    print(f"The surface heat flux is approximately {surface_heat:.0f} W/m^2")
elif (excess>=120 and excess <=1200): #for any negative numbers and numbers between 120 and 1200
    surface_heat= 2.5E4*(excess/120)**DE_slope
    print(f"The surface heat flux is approximately {surface_heat:.0f} W/m^2")
else:
    print("Surface heat flux is not available")
    
    