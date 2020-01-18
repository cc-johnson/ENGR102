# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 07 Activity 3
# Date:        13 October, 2019

sentence = input("Write me a sentence: ")
letter = input("What letter do you want to count? ")
count = 0

for char in sentence:
	char = char.lower()
	if char == letter:
		count += 1

print("The letter", letter, "appears:", count, "times")