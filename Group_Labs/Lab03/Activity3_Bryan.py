# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones
# Section:     513
# Assignment:  Lab 03 Activity 3
# Date:        15 September, 2019

name = str(input("Give a name: "))
verb = str(input("Give a verb: "))
age = int(input("How old is " + name + "? "))
adjective = str(input("Give an adjective: "))
wealth = str(input("How much money? "))
noun = str(input("Give a noun: "))

story = "\n\t" + name + " was ready for the big day."
story += " It\'s time for " + name + " to " + verb + " into action in a game of rock, paper, scissors.\n"
story += "Although " + name + " is only " + str(age) + ", this was their only time to prove everyone wrong "
story += "and show how " + adjective + " " + name + " is. "
story += name + " \nis attending a rock, paper, scissors tournament that will reward up to " + wealth
story += " dollars to whoever is the winner.\n"
story += "Sadly, " + name + " was not victorious in most matches but still left with a special " + noun + "."
print(story)
