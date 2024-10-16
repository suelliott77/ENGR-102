# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Sutton Elliott
# Section:      504
# Assignment:   Lab 2a
# Date:         11th Septermber 2022

from math import *
import math

# The force of a 3 kg object going at 5.5m/s^2
force= 3
acceleration=5.5
forceofobject= force * acceleration
print("Force is", (forceofobject), "N")

#The wavelength of x-ray distance 0.025nm with a scattering angle 25 degrees 
#𝑛𝜆=2𝑑sin𝜃
xray_dist= 0.025
theta= sin(5*(math.pi)/36)
wavelength=(2*(xray_dist)*theta)
print("Wavelength is ",wavelength, "nm")

#The half-life of Radon-222 after 3 days. There are 5 grams and half-life=3.8
#𝑁(𝑡)=𝑁02^𝑡/𝑡1/2
starting_amount= 5
time_in_days= 3
halflife= 3.8
radon_halflife=starting_amount * 2**-(time_in_days/halflife)
print("Radon-222 left is",(radon_halflife) ,"g")

#The Ideal Gas Law. 5 moles with volume 0.25 m^3 and temp 415K 8.314m^3Pa/K·mol
moles= 5
V_gas= 0.25
temp_calvins= 415
gasconstant= 8.314
pressure_5moles= ((moles* gasconstant *temp_calvins) / V_gas)/1000
print("Pressure is",pressure_5moles, "kPa")