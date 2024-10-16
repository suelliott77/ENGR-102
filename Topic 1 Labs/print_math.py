# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sutton Elliott
# Section:      504
# Assignment:   Lab 1b
# Date:         1st Septermber 2022

from math import *
import math

# The force of a 3 kg object going at 5.5m/s^2
print("Force is", (3*5.5), "N")

#The wavelength of x-ray distance 0.025nm with a scattering angle 25 degrees 
#𝑛𝜆=2𝑑sin𝜃
print("Wavelength is",(2*(0.025)*sin(5*(math.pi)/36)),"nm")

#The half-life of Radon-222 after 3 days. There are 5 grams and half-life=3.8
#𝑁(𝑡)=𝑁02^𝑡/𝑡1/2
print("Radon-222 left is",(5*2**-(3/3.8)) ,"g")

#The Ideal Gas Law. 5 moles with volume 0.25 m^3 and temp 415K 8.314m^3Pa/K·mol 
print("Pressure is",((5*8.314*415)/0.25)/1000, "kPa")
