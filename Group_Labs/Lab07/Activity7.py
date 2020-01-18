# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 07 Activity 7
# Date:        13 October, 2019

names = []
round1Scores = []
round2Scores = []

num = 1
round1Score = 1
# Collect user input for round1, round2, and the player's name
while round1Score > 0:
	round1Score = int(input("What was player " + str(num) + "'s score for round 1? "))
	if round1Score > 0:
		round1Scores.append(round1Score)
		round2Scores.append(int(input("What was player " + str(num) + "'s score for round 2? ")))
		names.append(input("What is player " + str(num) + "'s name? "))
	num += 1

# Sum the scores of the two rounds
sumedScores = []
for i in range(len(names)):
	sumedScores.append(round1Scores[i] + round2Scores[i])

print(sumedScores)
# Sort the scores and corresponding names
for i in range(len(names)):
	for j in range(len(names)):
		if sumedScores[i] < sumedScores[j]:
			# Temporary values
			tmp = sumedScores[i]
			tmpName = names[i]

			# Replace the value at i with the value at j
			sumedScores[i] = sumedScores[j]
			names[i] = names[j]

			# Replace the value at j with the value at i
			sumedScores[j] = tmp
			names[j] = tmpName

# Determine the median of the sumedScores list
if len(sumedScores) % 2 == 0:
	medianIndex = int(len(sumedScores) / 2)
	median = (sumedScores[medianIndex - 1] + sumedScores[medianIndex]) / 2
else:
	medianIndex = int(len(sumedScores) / 2) + 1
	median = sumedScores[medianIndex]

# Separate the lists into those that go on, and those that do not
winningGolfers = names[0:medianIndex]
losingGolfers = names[medianIndex:]

# Print the final results
print("-------------------------")
print("The golfers moving on are:", winningGolfers)
print("The golfers who did not make the cut are:", losingGolfers)