# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sutton Elliott
# Section:      504
# Assignment:   Indivdual Lab 12a
# Date:         28 November 2022

import numpy as np
import matplotlib as plot
import matplotlib.pyplot as plt

# starting matrix, vector, and the new point
v= np.array([0,1]).reshape(2,1)
M= np.array([1.01,0.09,-0.09,1.01]).reshape(2,2)
new_point= M @ v

# lists of the different xvalues and yvalues
xvals=[]
yvals=[]

# loop for the 200 points that are needed
for i in range(200):
    xvals.append(new_point[0][0])
    yvals.append(new_point[1][0])
    new_point= M @ new_point
 
#plotting stuff
plt.plot(xvals,yvals, '*', color='r')
plt.title('Cinnamon Roll')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
    

