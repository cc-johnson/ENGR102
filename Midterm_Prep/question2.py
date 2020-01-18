"""
Write a program that will ask a user to enter names and ages of people, stopping when an age of 0 is entered
(and not processing that person). The program should collect this information, and then output the average
age, the name of the oldest person, and the name of the youngest person. Assume no two people have the
same age.
"""

ages = [] # list to store ages
names = [] # list to store names

age = 1 # Initializing $age so that it will enter the while loop
while age != 0:
	name = input("Whaat is this person's name? ") # input for $name
	age = int(input("How old is " + name + ": ")) # input for $age

	if age > 0: # So long as the $age is greater than 0, append everything
		names.append(name) # Append $name to the $names list 
		ages.append(age) # Appen $age to the $ages list

# This  block of code sorts the $names list in conjunction with the $ages list
for i in range(len(ages)): # Iterate through the $ages list
	for j in range(len(ages)): # Iterate through the $ages list
		if ages[i] < ages[j]: # If the $age at $ages[i] is less than the $age at $ages[j], swap them
			# Move $age to new location with new index
			tmpAge = ages[j]
			ages[j] = ages[i]
			ages[i] = tmpAge

			# Move $name to new location with the new $age index
			tmpName = names[j]
			names[j] = names[i]
			names[i] = tmpName

averageAge = sum(ages)/len(ages) # Determine the average age
oldestPerson = ages[-1] # Get the oldest person's name
youngestPerson = ages[0] # Get the youngest person's name

# Print everything
print("Average age:", averageAge)
print("Oldest person:", oldestPerson)
print("Youngest person:", youngestPerson)