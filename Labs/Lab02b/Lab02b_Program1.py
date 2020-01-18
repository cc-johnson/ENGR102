# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 02b
# Date:        8 September, 2019

from math import *

# [1.a] My name and UIN
name = "Chase Johnson"
uin= "327008712"
partA = "Name: " + name + " UIN: " + uin
print(partA)

# [1.b] Interesting fact about myself
fact = "I grew up on a farm"
print(fact)

# [1.c] Voltage Calculation
current = 20
resistance = 5
voltage = current * resistance
print(voltage)

# [1.d] Kinetic Energy Calculation
mass = 100
velocity = 21 ** 2
kineticEnergy = (mass)*(velocity)/2
print(str(kineticEnergy))

# [1.e] Reynolds Number Calculation
fluidVel = 100
charLinDim = 2.5
kinVis = 1.2
reynolds = fluidVel * charLinDim / kinVis
print(reynolds)

# [1.f] Energy Radiated per Unit Surface Area Calculation
constProp = 5.67 * (10 ** (-8))
absTemp = 2200
radiated = constProp * (absTemp ** 4)
print(radiated)

#  [1.g] Shear Stress Calculation
effStress = 20
cohesion = 2
angleFric = 35
shearStress = cohesion + (effStress * tan(angleFric))
print(shearStress)
