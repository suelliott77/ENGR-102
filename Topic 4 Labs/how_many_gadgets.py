# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sutton Elliott
# Section:      504
# Assignment:   Lab 4c
# Date:         21 September 2022

days= int(input('Please enter a positive value for day: \n'))

#needed variables
plus60_days= (days-60) 
gadgets_60plus= 49 - plus60_days

#if statements 
if (days>0 and days<=10):
    print(f'The total number of gadgets produced on day {days:.0f} is', (days * 5))
elif (days>=11 and days<=60):
    print(f'The total number of gadgets produced on day {days:.0f} is', (50 + (50*(days-10))))
elif (days>=61 and days<=101):
    print(f'The total number of gadgets produced on day {days:.0f} is {(2550 + (plus60_days/2)*(50+gadgets_60plus)):.0f}')
elif(days==102):
    print(f'The total number of gadgets produced on day {days:.0f} is {3730}')
elif(days<0 or days>102):
    print('You entered an invalid number!')