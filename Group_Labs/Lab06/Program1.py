from math import sqrt
name = input("What is your pokemon's name? ")
initCP = float(input("What is your pokemon's current number of combat points? "))
initLevel = int(input("What is your pokemon's current level? "))
initCandies = int(input("How many candies does your pokemon have? "))
stats = [name, initCP, initLevel, initCandies]

choice = 0
while choice != 3:
	# Calculate the current level
	if choice == 1:
		addCandies = int(input("How many candies do you want to add? "))
		stats[3] += addCandies
	elif choice == 2:
		if stats[2] <= 30 and stats[3] > 0 and stats[2] + stats[3] <= 30: 
			stats[2] += stats[3]
			stats[3] = 0
		elif stats[2] <= 30 and stats[3] > 0 and stats[2] + stats[3] >= 30:
			more30 = stats[2] + stats[3] - 30
			levelsOver30 = more30 // 2
			stats[3] = more30 % 2
			stats[2] = 30 + levelsOver30
		elif 30 < stats[2] < 40 and stats[3] > 1 and 30 < stats[2] + stats[3]:
			if stats[3] <= 20:
				stats[2] += stats[3] // 2
				stats[3] = stats[3] % 2
			else:
				stats[2] = 40
				stats[3] = 0

	# Calculate the current CP
	if stats[2] <= 30:
		stats[1] = (stats[1]*.0094)/((.0095*sqrt(stats[2]))**2)
	elif 30 < stats[2] <= 40:
		stats[1] = (stats[1]*.0045)/((.0095*sqrt(stats[2]))**2)
	
	# default the level to 40 if it goes over
	if stats[2] > 40:
		stats[2] = 40

	print("Current CP", stats[1])
	print("Current Level:", stats[2])
	print("Candies", stats[3])
	print("1 - Add candy")
	print("2 - Use candy to level up")
	print("3 - Exit to main menu")
	choice = int(input("What would you like to do? "))
	