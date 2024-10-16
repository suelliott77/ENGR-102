# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
# Section:      504
# Assignment:   Quiz 5 debug
# Date:         21 September 2022
#input of integer 
num= int(input("Enter a 5-digit integer: "))

#changing numbers order 
num1= (num // 10000)
num2= ((num % 10000) // 1000)
num3= ((num % 1000) // 100)
num4= ((num % 100) // 10)
num5= (num % 10)

#output
print(f"{num} backwards is: {num5}{num4}{num3}{num2}{num1}")
