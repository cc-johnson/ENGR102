# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson, Anna Olmedo, Bryan Jones, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 02_Act3_Bonus
# Date:        5 September, 2019

from math import *

# Set values
xi = 30 # Starting time
y = 50 # Distance Traveled
speed = 565/15
trackLength = 2*pi*0.5

choice = input("Are you giving me (m)inutes or (s)econds [s]? ")
ms = "s"
if "m" in choice:
    ms = "m"

timeToRace = float(input("How long do you want the car to drive? "))
if ms == "m":
    timeToRace = timeToRace*60

y += (timeToRace-xi)*(speed)  # Current position
print("Distance at time: " + str(int(timeToRace)) + " = " + str(y) + " meters")
