# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 05b Program 2
# Date:        29 September, 2019

y = 2

while y <= 100:
	x = 2
	while x <= y:
		if y % x == 0:
			print(x, "divides", y)
		x += 1
	y += 1

print("Done")