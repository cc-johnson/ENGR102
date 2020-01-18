# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 07 Activity 1
# Date:        13 October, 2019

strings = ['arroyo', 'elephantine', 'toy', 'shines']
count = 0

for str in strings:
	if len(str) >= 2 and str[0] == str[-1]:
		count += 1

print(count)
