# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 03 Activity 2
# Date:        15 September, 1019

""" Instructions:
		1. Give each person a number
		2. Run the program
		3. Enter in each person’s name based on their consecutive number (1, 2, 3, 4…)
		4. Enter in each person’s birthday based on their consecutive number (1, 2, 3, 4…) """

# Names
person1 = input("What is the first person's name? ")
person2 = input("What is the second person's name? ")
person3 = input("What is the third person's name? ")
person4 = input("What is the fourth person's name? ")
# Birthdays
bDay1 = input("What is the first person's birthday [DD/MM/YYYY]?")
bDay2 = input("What is the second person's birthday [DD/MM/YYYY]?")
bDay3 = input("What is the third person's birthday [DD/MM/YYYY]?")
bDay4 = input("What is the fourth person's birthday [DD/MM/YYYY]?")

print("Names".ljust(10), "Birthdays [DD/MM]".rjust(10))
print(person1.ljust(10), bDay1.rjust(10))
print(person2.ljust(10), bDay2.rjust(10))
print(person3.ljust(10), bDay3.rjust(10))
print(person4.ljust(10), bDay4.rjust(10))