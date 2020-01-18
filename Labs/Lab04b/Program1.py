# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 04b Program 1
# Date:        22 September, 2019

height = float(input("What is the person's height [in inches]? "))
weight = float(input("What is the person's weight [in pounds]? "))

bmi = weight / (height**2.0) * 703.0

if bmi >= 30.0:
	print("The person is obese")
elif 25.0 <= bmi < 30.0:
	print("The person is overweight")
elif 18.5 <= bmi < 25.0:
	print("The person is normal or healthy weight")
else:
	print("The person is underweight")
