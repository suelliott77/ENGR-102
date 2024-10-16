# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 7c
# Date:         12 October 2022

from math import *

#needed inputs from user 
vector_a= input("Enter the elements for vector A: \n")
vector_b= input("Enter the elements for vector B: \n")

sum_a=0
sum_b=0
dot=0
add= []
subtract= []

list_a= vector_a.split()
list_b= vector_b.split()    

#magnitude of a
for i in range(len(list_a)):
    squared_a= (float(list_a[i]))**2
    sum_a+= squared_a

mag_a= sqrt(sum_a)
print(f"The magnitude of vector A is {mag_a:.5f}")

#magnitude of b
for j in range(len(list_b)):
    squared_b= (float(list_b[j]))**2
    sum_b+= squared_b

mag_b= sqrt(sum_b)
print(f"The magnitude of vector B is {mag_b:.5f}")

#a + b 
for i in range(len(list_a)):
    add.append(float(list_a[i]) + float(list_b[i]))

print(f"A + B is", str(add))

#a - b 
for i in range(len(list_a)):
    subtract.append(float(list_a[i]) - float(list_b[i]))

print(f"A - B is", str(subtract))
      
#dot product 
for i in range(len(list_a)):
    num1= float(list_a[i])*float(list_b[i])
    dot+= num1
    
print(f"The dot product is {dot:.2f}")


        
