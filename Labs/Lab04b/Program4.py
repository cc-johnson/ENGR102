# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 04b Program 4
# Date:        22 September, 2019

stress = float(input("What is the current Stress value? "))
yInt = 0
if 0 <= stress <= .02:
	slope = 2200.0
elif stress == .03:
	yInt = 44.0
	slope = 0.0
elif .02 <= stress <= .06:
	yInt = 44.0
	slope = 44.0
elif .06 <= stress <= .18:
	slope = (400/3)
	yInt = 38.0
elif .18 <= stress <= .27:
	slope = -77.77777778
	yInt = 74.0
else:
	stress = abs(stress)
	slope = -1

strain = (slope * stress) + yInt

if strain > 0:
	print("\n\n------------------")
	print("Slope from 0 --> A = 2200.0")
	print("The current slope is:", slope)
	print("The current Strain level is:", strain)
else:
	print("\n\n\ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \\")
	print(" \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL ")
	print("L \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAI ")
	print("IL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAI")
	print("AIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FA")
	print("FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ F")
	print(" FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ ")
	print("\ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ FAIL \ \n")
	print("\n\n\nThat is not a valid stress level, please try again")