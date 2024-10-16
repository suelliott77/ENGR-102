# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sutton Elliott
# Section:      504
# Assignment:   Lab 3a- Using Input
# Date:         16th Septermber 2022

from math import *
import math

# The force of a 3 kg object going at 5.5m/s^2
print("This program calculates the applied force given mass and acceleration")
mass= float(input("Please enter the mass (kg): "))
print()
acceleration= float(input(("Please enter the acceleration (m/s^2): ")))
print()
force= mass * acceleration
print(f"Force is {force:.1f} N")
print()

#The wavelength of x-ray distance 0.025nm with a scattering angle 25 degrees 
#𝑛𝜆=2𝑑sin𝜃
print("This program calculates the wavelength given distance and angle")
xray_dist= float(input(("Please enter the distance (nm): ")))
print()
theta= (float(input(("Please enter the angle (degrees): "))))
print()
wavelength=(2*(xray_dist)*(math.sin((math.radians(theta)))))
print(f"Wavelength is {wavelength:.4f} nm")
print()

#The half-life of Radon-222 after 3 days. There are 5 grams and half-life=3.8
#𝑁(𝑡)=𝑁02^𝑡/𝑡1/2
halflife= 3.8
print("This program calculates how much Radon-222 is left given time and initial amount")
time_in_days= float(input(("Please enter the time (days): ")))
print()
starting_amount= float(input(("Please enter the initial amount (g):")))
print()
radon_halflife= starting_amount * 2**-(time_in_days/halflife)
print(f"Radon-222 left is {radon_halflife:.2f} g")
print()

#The Ideal Gas Law. 5 moles with volume 0.25 m^3 and temp 415K 8.314m^3Pa/K·mol
gasconstant= 8.314
print("This program calculates the pressure given moles, volume, and temperature")
moles= float(input(("Please enter the number of moles:")))
print()
V_gas= float(input(("Please enter the volume (m^3):")))
print()
temp_calvins= float(input(("Please enter the temperature (K):")))
print()
pressure= ((moles * gasconstant * temp_calvins) / V_gas)/1000
print(f"Pressure is", int(pressure) , "kPa")

