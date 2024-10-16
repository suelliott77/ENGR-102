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

#Part A
# As a team, we have gone through all required sections of the  
# tutorial, and each team member understands the material 

import numpy as np
import matplotlib as plot

#Part B
A= np.arange(12).reshape(3,4)
print(f'A = {A}\n')

B= np.arange(8).reshape(4,2)
print(f'B = {B}\n')

C= np.arange(6).reshape(2,3)
print(f'C = {C}\n')

#Part C
D= A @ B @ C
print(f'D = {D}\n')

#Part D
D_T= np.transpose(D)
print(f'D^T ={D_T}\n')

#Part E
E= np.sqrt(D)/2
print(f'E = {E}\n')

