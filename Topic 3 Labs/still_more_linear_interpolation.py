# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Chris Shaji
#
# Section:      504
# Assignment:   Team Lab 3b
# Date:         14 September 2022

from math import *
import math 

#starting variables 
time_initial= float(input("Enter time 1: \n"))
x_initial= float(input("Enter the x position of the object at time 1: \n"))
y_initial= float(input("Enter the y position of the object at time 1: \n"))
z_initial= float(input("Enter the z position of the object at time 1: \n"))

time_final= float(input("Enter time 2: \n"))
x_final= float(input("Enter the x position of the object at time 2: \n"))
y_final= float(input("Enter the y position of the object at time 2: \n"))
z_final= float(input("Enter the z position of the object at time 2: \n"))
print()

#slope equations
slope_x= ((x_final-x_initial)/(time_final-time_initial))
slope_y= ((y_final-y_initial)/(time_final-time_initial))
slope_z= ((z_final-z_initial)/(time_final-time_initial))

#times
time1= time_initial
time3= (time_final + time_initial) / 2
time2= (time_initial +time3) /2
time4= (time_final + time3) / 2
time5= time_final

#first time 
x1=(slope_x*(time1-time_initial) + x_initial)
y1=(slope_y*(time1-time_initial) + y_initial)
z1=(slope_z*(time1-time_initial) + z_initial)

print(f"At time {time1:.2f} seconds the object is at ({x1:.3f}, {y1:.3f}, {z1:.3f})")

#second time
x2=(slope_x*(time2-time_initial) + x_initial)
y2=(slope_y*(time2-time_initial) + y_initial)
z2=(slope_z*(time2-time_initial) + z_initial)

print(f"At time {time2:.2f} seconds the object is at ({x2:.3f}, {y2:.3f}, {z2:.3f})")

#third time
x3=(slope_x*(time3-time_initial) + x_initial)
y3=(slope_y*(time3-time_initial) + y_initial)
z3=(slope_z*(time3-time_initial) + z_initial)

print(f"At time {time3:.2f} seconds the object is at ({x3:.3f}, {y3:.3f}, {z3:.3f})")

#fourth time
x4=(slope_x*(time4-time_initial) + x_initial)
y4=(slope_y*(time4-time_initial) + y_initial)
z4=(slope_z*(time4-time_initial) + z_initial)

print(f"At time {time4:.2f} seconds the object is at ({x4:.3f}, {y4:.3f}, {z4:.3f})")

#last time
x5=(slope_x*(time5-time_initial) + x_initial)
y5=(slope_y*(time5-time_initial) + y_initial)
z5=(slope_z*(time5-time_initial) + z_initial)

print(f"At time {time5:.2f} seconds the object is at ({x5:.3f}, {y5:.3f}, {z5:.3f})")



