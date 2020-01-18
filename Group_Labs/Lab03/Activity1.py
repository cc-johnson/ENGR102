# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 03 Activity 1
# Date:        15 September, 2019

# 1 pound = 4.44822 N
# 1 BTU = 1055.06 J
# 1 MPH = 0.44704 m/s
# C = (X°F − 32) * 5/9
# dBv = 20log(v)

from math import *

# Convert Pound to Newton:
pounds = input("Give me pounds: ")
newtons = float(pounds) * 4.44822
print("You have", newtons, "N")

# Convert BTU to Joule
btu = input("Give me BTU: ")
joule = float(btu) * 1055.06
print("That is", joule, "J")

# Convert MPH to m/s
print("Son, how fast do you think you were going? ")
mph = input("Officer I swear it was only: ")
mps = float(mph) * 0.44704
print("Welcome to Europe, you really went", mps, "m/s")

# Convert F to C
f = input("How hot is it outside? ")
c = (float(f) - 32) * 5/9
print("That is", c, "degrees Celcius")

# Convert Voltage to Voltage Level
v = input("What is the Voltage? ")
vl = 20*log(float(v))
print("The voltage level is", vl, "dB")