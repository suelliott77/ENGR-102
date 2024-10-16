# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Chris Shaji
# Section:      504
# Assignment:   Team Lab 4b
# Date:         19 September 2022

#starting variables
var_a = int(input("Please enter the coefficient A: "))
var_b = int(input("Please enter the coefficient B: "))
var_c = int(input("Please enter the coefficient C: "))
sign_of_a= ""
sign_of_b= ""
sign_of_c= ""

#variable a
if (var_a < 0):
    sign_of_a= "-"
else:
    print(end="")
    
#variable b
if (var_b < 0):
    sign_of_b= "-"
elif (var_b > 0):
    sign_of_b= "+"
elif (var_b==0):
    sign_of_b = ""
else:
    print(end="")
    
#variable c
if (var_c < 0):
    sign_of_c= "-"
elif (var_c > 0):
    sign_of_c= "+"
elif (var_c==0):
    sign_of_c = ""
else:
    print(end="")
    

#final equation
if (var_a==1 and var_b==1):
    print(f"The quadratic equation is {sign_of_a} x^2 {sign_of_b} x {sign_of_c} {abs(var_c)} = 0")
elif (var_a==0 and var_b==0):
    print(f"The quadratic equation is {sign_of_c} {abs(var_c)} = 0")
elif ((var_a==-1 or var_a==1) and var_b==0):
    print(f"The quadratic equation is {sign_of_a}x^2 {sign_of_c} {abs(var_c)} = 0")
elif (var_a==0):
    print(f"The quadratic equation is {var_b}x {sign_of_c} {abs(var_c)} = 0")
elif (var_c==0 and var_b==1):
    print(f"The quadratic equation is{sign_of_a} {abs(var_a)}x^2 {sign_of_b} x = 0")
elif (var_b==0):
    print(f"The quadratic equation is{sign_of_a} {abs(var_a)}x^2 {sign_of_c} {abs(var_c)} = 0")
elif (var_c==0):
    print(f"The quadratic equation is {sign_of_a} {abs(var_a)}x^2 {sign_of_b} {abs(var_b)}x = 0")
elif (var_a==1 or var_a==-1):
    print(f"The quadratic equation is {sign_of_a} x^2 {sign_of_b} {abs(var_b)}x {sign_of_c} {abs(var_c)} = 0")
elif (var_b==1 or var_a==-1):
    print(f"The quadratic equation is {sign_of_a} {abs(var_a)}x^2 {sign_of_b}x {sign_of_c} {abs(var_c)} = 0")
else:
    print(f"The quadratic equation is {sign_of_a} {abs(var_a)}x^2 {sign_of_b} {abs(var_b)}x {sign_of_c} {abs(var_c)} = 0")