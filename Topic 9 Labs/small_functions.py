# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Indivdual lab 9
# Date:         31 October 2022

from math import *

############## Part A ###############
def parta(R,r):
    
    #height of the cylinder
    h= sqrt(R**2 - r**2)
    hcylinder= 2 * h
    hcap= R - h
    
    #Volume of the cylinder
    Vcylinder= pi * (r**2) * hcylinder
    
    #volume of the sphere
    Vsphere= (4/3) * pi * (R**3)
    
    #volume of the cap
    Vcap= (1/3 * pi * hcap ** 2) * (3 * R - hcap)
    
    #Volume of the bead 
    Vbead= Vsphere - Vcylinder - (2 * Vcap)
    
    #final volume
    return Vbead

#print(parta(1,0.25))
############## Part B ###############
def partb(num):
    #find odd numbers and the sum of those 
    odd_nums= []
    for i in range(2,num):
        if (num % i == 0) and (num // i - i + 1) % 2 == 1:
            for j in range(i):
                odd_nums += [(num // i - i + 1) + j * 2]
            return odd_nums
        #returns false if the odd numbers don't equal the given number
    return False

#print(partb(4))
############## Part C ###############
def partc(symbols= " ", name= "?", company= "?", email= "?"):
    list1= [symbols, name, company, email]
    lenlist1= [len(symbols), len(name), len(company), len(email)]
    
    maxlength= max(lenlist1) + 6
    length2= maxlength - 6
    
    bigstring=""
    for i in range(maxlength):
        bigstring += symbols
    bigstring+= "\n"
    
    for i in list1:
        if i != symbols:
            bigstring += symbols + '  '
            bigstring += ' ' * ((length2 - len(i)) // 2)
            bigstring += i
            if len(i) % 2 ==1 and length2 % 2 == 0:
                bigstring += ' ' * ((length2 - len(i)) // 2 + 1)
            else:
                bigstring += ' ' * ((length2 - len(i)) // 2)
            bigstring += '  ' + symbols
            bigstring += '\n'
            
    for i in range(maxlength):
        bigstring += symbols
        
    return bigstring

#print(partc('*', 'John Davis', 'Texas A&M', 'suelliott@tamu.edu'))
############## Part D ###############
def partd(mylist):
    #sort values
    mylist.sort()
    
    #find minimum
    min_value= min(mylist)

    #find maximum
    max_value= max(mylist)

    #find median 
    if len(mylist) % 2 == 1:
        median_val= mylist[len(mylist) // 2]
    else:
        median_val= (mylist[len(mylist) // 2 - 1] + mylist[len(mylist) // 2]) / 2
    
    return min_value, median_val, max_value

#print(partd([1,2,3,9,8,7,6,5,4]))
############## Part E ###############
def parte(times, distances):
    velocities= []
    for i in range(len(times) - 1):
        velocities.append((distances[i + 1] - distances[i]) / (times[i+1] - times[i]))
    return velocities

#print(parte([0,1,2,3], [0,1,4,9]))
############## Part F ###############
def partf(listnum):
    product = False
    for num in listnum:
        for i in listnum:
            if num + i == 2026: #check for sum of each number in the list 
                product = num * i
                
    return product
#print(partf([102,216,217]))
            