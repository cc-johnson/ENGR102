# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Team:        23
# Assignment:  Quiz 5
# Date:        09 October, 2019

# list to contain the user's top 5 favorite acts
acts = []

# for loop to take input for all of the acts and append them to the list $acts
for i in range(5):
    act = input("What is your number " + str(i+1) + " artist? ")
    acts.append(act)

maxHit = 0 # variable to determine the length of the longest act for printing purposes
bieberExists = False # boolean used to determine if the name "bieber" is contained in the list

# for loop to iterate through the $acts list and determine if "bieber" exists within the list
# for loop also changes the value of $maxHit as it goes through checking for "bieber"
for act in acts:
    if "bieber" in act.lower():
        bieberExists = True

    if len(act) > maxHit:
        maxHit = len(act) + 14
        print("maxHit is now: " + str(maxHit))

# determines if "bieber" does not exist, remove the last user entry and insert "Justin Bieber" to index 0
# also ensures that maxHit is long enough, if a user entry is not longer than one with ^
if bieberExists != True:
    acts.pop()
    acts.insert(0, 'Justin Bieber')

    if maxHit < 27:
        maxHit = 27

# Print the "-------------" stuff
print('-' * maxHit)

# print out each of the acts, in order of the list
for i, act in enumerate(acts):
    print("Number", i + 1, "Hit: " + act)

# Print the "-------------" stuff
print('-' * maxHit)