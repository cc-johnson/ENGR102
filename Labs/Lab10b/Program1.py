# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 10b Program 1
# Date:        3 November, 2019

temps = []
with open('Celcius.dat', 'r') as file:
	temps = file.readlines()
	for i, temp in enumerate(temps):
		temp = temp.strip()
		temps[i] = float(temp)
	
with open('Fahrenheit.dat', 'x+') as file:
	for temp in temps:
		converted = (temp * (9 / 5)) + 32
		file.write(str(converted) + '\n')

