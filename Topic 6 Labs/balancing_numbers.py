# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 6c
# Date:         5 October 2022

from math import *

#needed inputs 
n= int(input("Enter a value for n: \n"))
count=0
count2=0
num= n+1
r=0
#needed loops 
for i in range(1,n):
    count+=i

while (count>count2):
    count2+=num
    num+=1
    r+=1
    
if (count==count2):
    print(f"{n} is a balancing number with r={r}")
else:
    print(f'{n} is not a balancing number')

    
    
    