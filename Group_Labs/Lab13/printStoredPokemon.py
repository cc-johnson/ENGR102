# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab ##
# Date:        DD MMMMMMMMM, 2019

def printStoredPokemon(playerID):
	"""Function to print the players stored pokemon,
	   and menu asscocaited with it"""
	# for each pokemon:
	for userPMon in playerID:
		# print Current pokemon
		print('======================')
		currentPMon = userPMon.keys()
		for i in currentPMon:
			print(i)
			stats = getStats(playerID, userPMon)
			# print Current CP:
			print('Current CP:', str(stats[0]))
			# print Current Level:
			print('Current Level:', str(stats[1]))
			print('======================')



def pickNewPokemon(playerID):
	"""Function to choose a new active pokemon"""
	# Print list of stored pokemon
	for userPMon in playerID:


	# Provide user with option

	# return userChoice
	return pokemonName
	pass
