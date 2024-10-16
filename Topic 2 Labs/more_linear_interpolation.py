# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sutton Elliott
# Section:      504
# Assignment:   Lab 2b- more linear interpolation
# Date:         11th Septermber 2022

import math 

#starting variables 
time_initial= 12
time_final= 85
x_initial= 8
y_initial= 6
z_initial= 7
x_final= -5
y_final= 30
z_final= 9
time1= 30.0

#slope equations
slope_x= ((x_final-x_initial)/(time_final-time_initial))
slope_y= ((y_final-y_initial)/(time_final-time_initial))
slope_z= ((z_final-z_initial)/(time_final-time_initial))

#final equations- 30 seconds 
x1=(slope_x*(time1-time_initial) + x_initial)
y1=(slope_y*(time1-time_initial) + y_initial)
z1=(slope_z*(time1-time_initial) + z_initial)

#30 second outputs 
print("At time ", time1, "seconds:")
print("x1= ", x1, "m")
print("y1= ", y1, "m")
print("z1= ", z1, "m")
print("-----------------------")

time2= 37.5
#final equations- 37.5 seconds 
x2=(slope_x*(time2-time_initial) + x_initial)
y2=(slope_y*(time2-time_initial) + y_initial)
z2=(slope_z*(time2-time_initial) + z_initial)

#37.5 second outputs 
print("At time ", time2, "seconds:")
print("x2= ", x2, "m")
print("y2= ", y2, "m")
print("z2= ", z2, "m")
print("-----------------------")

time3= 45.0
#final equations- 45 seconds 
x3=(slope_x*(time3-time_initial) + x_initial)
y3=(slope_y*(time3-time_initial) + y_initial)
z3=(slope_z*(time3-time_initial) + z_initial)

#45 second outputs 
print("At time ", time3, "seconds:")
print("x3= ", x3, "m")
print("y3= ", y3, "m")
print("z3= ", z3, "m")
print("-----------------------")
    
time4= 52.5
#final equations- 52.5 seconds 
x4=(slope_x*(time4-time_initial) + x_initial)
y4=(slope_y*(time4-time_initial) + y_initial)
z4=(slope_z*(time4-time_initial) + z_initial)

#52.5 second outputs 
print("At time ", time4, "seconds:")
print("x4= ", x4, "m")
print("y4= ", y4, "m")
print("z4= ", z4, "m")
print("-----------------------")

time5= 60.0
#final equations- 60 seconds 
x5=(slope_x*(time5-time_initial) + x_initial)
y5=(slope_y*(time5-time_initial) + y_initial)
z5=(slope_z*(time5-time_initial) + z_initial)

#60 second outputs 
print("At time ", time5, "seconds:")
print("x5= ", x5, "m")
print("y5= ", y5, "m")
print("z5= ", z5, "m")