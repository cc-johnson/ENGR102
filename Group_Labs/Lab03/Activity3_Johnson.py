# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 03 Activity 3
# Date:        15 September, 2019

name = str(input("Give me a name: "))
verb = str(input("Give me a verb: "))
age = int(input("How old is " + name + "? "))
adjective = str(input("Give me an adjective: "))
wealth = str(input("How much money does " + name + " have? "))
noun = str(input("Give me a noun: "))

message = "\n" + name + " drove to the store at 3:00AM on THE DAY it was supposed to happen.\n"
message += "It was the first time they ever felt this way about another person.\n"
message += name + " picked up the appropriate items for the occasion, "
message += "and " + verb + " them in the front seat of the car so they would be safe.\n"
message += "The person in mind was, like " + name + ", only " + str(age) + " but " + name + " didn’t care because it was "
message += "worth the " + adjective + " sacrifice.\nAfter making " + wealth + " billion dollars "
message += "from the project with the other person, " + name + " knew it was time to close the circle.\n"
message += "\n\tAt 6:00AM exactly, as the person of interest walked out of the front door, "
message += name + " walked up and took care of business,\n\t" + name + " got down on one knee "
message += "and " + verb + " them after showing them a \'" + noun + "\'."

print(message)