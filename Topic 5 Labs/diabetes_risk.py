# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Sutton Elliott
#               Justin Smonko
#               Vedanti Naktode
#               Chris Shaji
# Section:      504
# Assignment:   Team Lab 4c
# Date:         19 September 2022

from math import *

#inputs from the user 
sex= input("Enter your sex (M/F): \n")
age= float(input("Enter your age (years): \n"))
bmi= float(input("Enter your BMI: \n"))
hyperextention= input("Are you on medication for hypertension (Y/N)? \n")
steriods= input("Are you on steroids (Y/N)? \n")
smoke= input("Do you smoke cigarettes (Y/N)? \n")

#if statements for calculation of risk 
#sex risk stuff
if (sex=='M' or sex=='m'):
    sex_risk=0
elif (sex=='F' or sex=='f'):
    sex_risk=0.879

#bmi risk stuff
if (bmi<25):
    bmi_risk=0
elif (bmi>=25 and bmi<=27.49):
    bmi_risk=0.699
elif (bmi>=27.5 and bmi<=29.99):
    bmi_risk=1.97
elif (bmi>=30):
    bmi_risk=2.518
  
#hyperextention risk stuff
if (hyperextention=='Y' or hyperextention== 'y'):
    hyperextention_risk= 1.222
elif (hyperextention=='N' or hyperextention== 'n'):
    hyperextention_risk= 0

#steriods risk stuff
if (steriods=='Y' or steriods== 'y'):
    steriod_risk= 2.191
elif (steriods=='N' or steriods== 'n'):
    steriod_risk= 0

#smoke risk stuff    
if (smoke=='Y' or smoke=='y'):
    smoke_risk= 0.855
if (smoke=='N' or smoke=='n'):
    used_or_no_smoke= input("Did you used to smoke (Y/N)? \n") 
    if (used_or_no_smoke=='Y' or used_or_no_smoke=='y'):
        smoke_risk= -0.218
    elif (used_or_no_smoke=='N' or used_or_no_smoke=='n'):
        smoke_risk=0

#family risks stuff
family= input("Do you have a family history of diabetes (Y/N)? \n")
if (family=='Y' or family=='y'):
        sibling_parent= input('Both parent and sibling (Y/N)? \n')
        if (sibling_parent=='Y' or sibling_parent=='y'):
            family_risk=0.753
        elif (sibling_parent=='N' or sibling_parent=='n'):
            family_risk= 0.728
elif (family=='N' or family=='n'):
    family_risk=0
    
#n calculation
n = (6.322 + sex_risk - (0.063 * age) - bmi_risk - hyperextention_risk - steriod_risk - smoke_risk - family_risk)
#risk calculation
risk= (100/(1+(e**n)))
print(f'Your risk of developing type-2 diabetes is {risk:.1f}%')
