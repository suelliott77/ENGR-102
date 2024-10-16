# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Chris Shaji
# Section:      504
# Assignment:   Team Lab 4a
# Date:         19 September 2022

from math import *
import math 

#starting variables
payment = float(input("How much did you pay? \n"))
cost = float(input("How much did it cost? \n"))
quarter= 0
dime=0
nickel=0 
penny=0
total_change = payment - cost 
change = (payment - cost)*100

print(f"You received $ {total_change:.2f} in change. That is ...") 

#quarters
if (change >= 25):
    quarter = round(change // 25)
    change -= (quarter * 25)
else:
    print(end="")
    
if (quarter == 1):
    print("1 quarter")
elif(quarter > 1):
    print(f"{quarter:.0f} quarters")
else:
    print(end="")
    
#dimes
if (change >= 0.10):
    dime = round(change // 10)
    change -= (dime * 10)
else: 
    print(end="")
    
if (dime == 1):
    print("1 dime")
elif(dime > 1):
    print(f"{dime:.0f} dimes")
else:
    print(end="")
  
#nickels
if (change >= 5):
    nickel = round(change // 5)
    change -= nickel * 5
else: 
    print(end="")
    
if (nickel == 1):
    print("1 nickel")
elif(nickel > 1):
    print(f"{nickel:.0f} nickels")
else:
    print(end="")
    
#pennies
if (change >= 0.01):
    penny= round(change / 1)
    change -= penny * 1
else:  
    print(end="")
    
if (penny == 1):
    print("1 penny")
elif(penny > 1):
    print(f"{penny:.0f} pennies")
else:
    print(end="")
     



    



