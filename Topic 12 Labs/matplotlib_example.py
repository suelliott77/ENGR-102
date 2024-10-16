# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Jonathon Fulton 
# Section:      504
# Assignment:   Team Lab 12a
# Date:         23 November 2022

# As a team, we have gone through all required sections of the 
# tutorial, and each team member understands the material

import numpy as np
import matplotlib as plot
import matplotlib.pyplot as plt

#first plot
x= np.linspace(-10,2)

plt.plot(x,(1/8)*x**2, color= 'r', linewidth=2, label='f=2')
plt.plot(x,(1/24)*x**2, color= 'b', linewidth=6, label='f=6')
plt.axis([-2,2,0,0.5]) # xmin, xmax, ymin, ymin
plt.title(label= 'Parabola plots with varying focal length') #title of the graph
plt.xlabel('x') #x axis label 
plt.ylabel('y') #y axis label
plt.legend(loc='lower left'); #makes a legend with labels from orginal plot, loc= is where the legend is
plt.ylim(-0.05,0.55) #gives the graph a little space 
plt.xlim(-2.05,2.05)
plt.show() #shows the graph almost like a close on files 

#second plot
x= np.linspace(-4,4,25)

plt.plot(x,2*x**3 + 3*x**2 - 11*x - 6, '*' ,color='y') #asterisk is for figure 
plt.axis([-4,4,-50,125])
plt.title(label= 'Plot of cubic polynomial')
plt.xlabel('x values')
plt.ylabel('y values')
plt.show()

#third plot 
x= np.linspace(-2*np.pi,2*np.pi)

plt.subplot(2,1,1) #does a subplot (rows, columns, plot number)
plt.plot(x, np.cos(x), color= 'm', label='cos(x)')
plt.axis([-2*np.pi,2*np.pi,-1,1])
plt.title(label= 'Plot of cos(x) and sin(x)')
plt.grid(); #makes a grid on the graph 
plt.ylabel('y=cos(x)')
plt.legend(loc='lower right')
plt.ylim(-1.10,1.10)

plt.subplot(2,1,2) #does a subplot (rows, columns, plot number)
plt.plot(x, np.sin(x), color= 'g', label='sin(x)')
plt.axis([-2*np.pi,2*np.pi,-1,1])
plt.grid(); #makes a grid on the graph 
plt.ylabel('y=sin(x)')
plt.legend(loc='upper right')
plt.ylim(-1.10,1.10)

plt.show()