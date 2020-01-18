def printMenu(): # Anna
	"""Function to print the main menu"""
	# print (1) Print your pokemon
	# print (2) Print currently selected pokemon
	# print (3) Catch a new pokemon
	# print (4) Level currently selected pokemon
	# print (5) Battle the another player
	# print (6) Switch to a different player

	# Provide user with option

	# return userChoice
	pass

def printStoredPokemon(playerID): # Gus
	"""Function to print the players stored pokemon,
	   and menu asscocaited with it"""
	# for each pokemon:
		# print Current CP:
		# print Current Level: 

	# Pick a new pokemon (1-len(userPMon))
	
	# Provide user with option

	# return userChoice
	pass

def printCurrentPokemon(playerID, pokemonName): # Anna
	"""Function to print the information about the current pokemon"""
	# print Pokemon name
	# print Current CP
	# print Current Level
	# (1) - Use Candy to Level - Up
	# (2) - Exit to Main Menu

	# return userChoice
	pass

def catchNewPokemon(): # Bryan
	"""Function to start a minigame to 'catch' a new pokemon.
	   If player wins, award candies"""

	# Start RPS script
	# if user wins:
		# give random selection of pokemon
		# userChoice for pMon
		# Generate candies randomly based on computer generated rand
	# else
		# return fail
	# return userChoice, candies
	pass

def RPS(): # Bryan
	"""Function to play rock paper scissors (RPS)"""
	# Play best two out of three
	# $userWin
	# for range(3):
		# randomNum = 1-3
			# 1: rock
			# 2: paper
			# 3: scissors
		# Ask user to pick 1-3
		# if player wins, add one to $userWin
	
	# if $userWin >= 2
		# return win
	# else
		# return naw
	pass

def levelPokemon(playerID, pokemonName): # Chase
	"""Function to calculate the pokemon's level-up capability
	   based on player's candies, pokemon's CP"""
	# Pick pokemon
	# insert lab06.program1 code
	# return pokemon, level
	pass

def battle(pMon1, pMon2): # Chase
	"""Function to determine the winner of a battle
	   based on each pokemon's fight value"""
	# calcFightValue(pMon1) vs. calcFightValue(pMon2)
	# whichever is greater is the winner
	# return winner
	pass

def calcFightValue(pMonData): # Chase
	"""Function to calculuate the fightValue of an individual pokemon"""
	# fight value = pokemon CP * random number from 1-50 / pokemon level
	# return fight value
	pass

def calcCP(currentCP, currentLevel): # Chase
	"""Function to determine the currentCP level of the pMon"""
	# CP * 0.0094 / (0.095 * sqrt(Current Level)) for levels 1–30 
	# CP * 0.0045 / (0.095 * sqrt(Current Level)) for levels 31–40 
	# return calculated CP
	pass

def getStats(playerID, pokemonName): # Chase
	# return (level, CP)
	pass

# gameData = {playerID : [{pokemonName = [level, cp]}, candies, currentPMon], ...}
# currentPlayer = {playerID = [stuff, currentPMon]}

gameData = {Ash:[{pikachu:[13,138], charizard:[38,738], squirtle:[29,576]}, 50, pikachu]}