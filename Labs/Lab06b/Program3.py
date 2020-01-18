# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 06b Program 3
# Date:        6 October, 2019

logins = {} # Dictionary of usernames and passwords

numAccounts = int(input("How many account will there be? ")) # Number of accounts in the logins list
unames = [] # Username list
pwds = [] # Password list

for i in range(numAccounts):
	uname = input("What is the user name for for user " + str(i+1) + "? ")
	unames.append(uname)

for uname in unames:
	pwd = input("What is the password for for user: " + uname + "? ")
	pwds.append(pwd)

for i in range(len(unames)):
	logins[unames[i]] = pwds[i]

maxAttempts = 3 # The maximum number of attempts a user can submit to login
attempts = 0 # The current number of attempts a user has entered
done = False # Condition to end the while loop
fail = False
while not done:
	uname = input("What is your username? ")
	if uname in unames:
		while not done:
			pwd = input("What is the password for " + uname + "? ")
			if logins[uname] == pwd:
				print("Login successful")
				done = True
			else:
				print("Try again, you have: " + str(maxAttempts - attempts) + " attempts left")
				attempts += 1

			if attempts == maxAttempts:
				print("You have exceeded the maxmimum alloted login attempts, goodbye")
				done = True
				fail = True
	else:
		print("That user does not exist, please try again. You have: " + str(maxAttempts - attempts) + " attempts left")
		attempts += 1

	if attempts == maxAttempts and fail == False:
		print("You have exceeded the maxmimum alloted login attempts, goodbye")
		done = True