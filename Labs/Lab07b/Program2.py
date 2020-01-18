# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 07b Program 2
# Date:        13, October 2019

userWord = ""
finalWord = ""

# While loop to continue until user enters "stop"
while userWord != "stop":
	# Print the pig latin word
	print(finalWord)

	# Ask for a word
	userWord = input("Give me a word: ")

	# Check if word has a vowel first
	if userWord[0] in 'aeiou':
		finalWord = userWord + 'yay'
	# Do the consonant block thing if it is not a vowel first
	else:
		for index, char in enumerate(userWord):
			if char in 'aeiou':
				firstVowel = index
				break
		consonantBlock = userWord[0:firstVowel]
		finalWord = userWord[firstVowel:] + consonantBlock + 'ay'
	

