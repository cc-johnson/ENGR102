# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 11 Activity 2
# Date:        10 November, 2019

# Function that takes in arguments $times, and $dists
# assuming $times, and $dists are lists 
def avgVel(times, dists):
	# List of averages
	averages = []
	# Iterate through $dists and $times
	for i in range(len(times) - 1):
		# Take the average of accross two different times
		avg = (dists[i+1] - dists[i]) / (times[i+1] - times[i])
		# Append that average
		averages.append(avg)
	# Return a list of averages
	return averages
