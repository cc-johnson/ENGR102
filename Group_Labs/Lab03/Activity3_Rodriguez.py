# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Gus Rodriguez, Anna Olmedo, Chase Johnson, Bryan Jones
# Section:     413
# Assignment:  Lab 3, Activity 3
# Date:        13 September 2019

name = str(input("Give a name: "))
verb = str(input("Give a verb: "))
age = str(int(input("How old?: ")))
adjective = str(input("Give an adjective: "))
noun = str(input("Give a noun: "))
wealth = str(int(input("How much money?: ")))

madlib = "\t" + name + " is " + verb + "ing with his " + age + " year old sibling. \nThey find a " + adjective + " "
madlib += noun + " that\'s worth " + wealth + " dollars. "

print(madlib)