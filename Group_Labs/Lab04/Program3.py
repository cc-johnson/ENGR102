# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 04 Activity 3
# Date:        22 September, 2019

# __init__
points = 0
print("This program evaluates the 10-year risk for a Male of a heart attack")
print("---------------")

# Inputs
age = int(input("What is your age? "))
totChol = int(input("What is your total cholesterol? "))
smoker = input("Do you smoke (Y/N)? ")
hdl = int(input("What is your high density lipoprotein level (HDL level)? "))
systolicBP = int(input("What is your systolic blood pressure? "))
treatment = input('Has your systolic blood pressure been treated (Y/N)? ')

# Add poitns for age
if 20 <= age <= 34:
	points -= 9
elif 35 <= age <= 39:
	points -= 4
elif 45 <= age <= 49:
	points += 3
elif 50 <= age <= 54:
	points += 6
elif 55 <= age <= 59:
	points += 8
elif 60 <= age <= 64:
	points += 10
elif 65 <= age <= 69:
	points += 11
elif 70 <= age <= 74:
	points += 12
elif 75 <= age <= 79:
	points += 13

# Add points for cholesterol
if totChol >= 240 and age >= 70:
	points += 1
elif 160 <= totChol <= 199 and 60 <= age <= 69:
	points += 1
elif 140 <= totChol <= 279 and 60 <= age <= 69:
	points += 2
elif totChol >= 280 and 60 <= age <= 69:
	points += 3
elif 160 <= totChol <= 199 and 50 <= age <= 59:
	points += 2
elif 200 <= totChol <= 239 and 50 <= age <= 59:
	points += 3
elif 240 <= totChol <= 279 and 50 <= age <= 59:
	points += 4
elif totChol >= 280 and 50 <= age <= 59:
	points += 5
elif 160 <= totChol <= 199 and 40 <= age <= 49:
	points += 3
elif 200 <= totChol <= 239 and 40 <= age <= 49:
	points += 5
elif 240 <= totChol <= 279 and 40 <= age <= 49:
	points += 6
elif totChol >= 280 and 40 <= age <= 49:
	points += 8
elif 160 <= totChol <= 199 and 20 <= age <= 39:
	points += 4
elif 200 <= totChol <= 239 and 20 <= age <= 39:
	points += 7
elif 240 <= totChol <= 279 and 20 <= age <= 39:
	points += 9
elif totChol >= 280 and 20 <= age <= 39:
	poitns += 1

# Add points for HDL
if hdl < 40:
	points += 2
elif 40 <= hdl <= 49:
	points += 1
# hdl 50-59 does not add points
elif hdl >= 60:
	points -= 1

# Determine if systolic blood pressure has been treated based on response
if "y" in treatment:
	treatment = True
else:
	treatment = False

# Add points for systolicBP in relation treatment
if (120 <= systolicBP <= 129) and (treatment == True):
	points += 1
elif (130 <= systolicBP <= 139) and (treatment == True):
	points += 2
elif (130 <= systolicBP <= 139) and (treatment == False):
	points += 1
elif (140 <= systolicBP <= 159) and (treatment == True):
	points += 2
elif (140 <= systolicBP <= 159) and (treatment == False):
	points += 1
elif (systolicBP >= 160) and (treatment == True):
	points += 3
elif (systolicBP >= 160) and (treatment == False):
	points += 2


# Determine if the person smokes based on response
if "y" in smoker:
	smoker = True
else:
	smoker = False

# Add points for if the person smokes in relation to age
if smoker == True and age >= 60:
	points += 1
elif smoker == True and age >= 50:
	points += 3
elif smoker == True and age >= 40:
	points += 5
elif smoker == True and age >= 20:
	points += 8

# Print final message based on number of points
if points <= 4:
	print("Your 10-Year risk: 1%")
elif points <= 6:
	print("Your 10-Year risk: 2%")
elif points <= 7:
	print("Your 10-Year risk: 3%")
elif points <= 8:
	print("Your 10-Year risk: 4%")
elif points <= 9:
	print("Your 10-Year risk: 5%")
elif points <= 10:
	print("Your 10-Year risk: 6%")
elif points <= 11:
	print("Your 10-Year risk: 8%")
elif points <= 12:
	print("Your 10-Year risk: 10%")
elif points <= 13:
	print("Your 10-Year risk: 12%")
elif points <= 14:
	print("Your 10-Year risk: 16%")
elif points <= 15:
	print("Your 10-Year risk: 20%")
elif points <= 16:
	print("Your 10-Year risk: 25%")
elif points >= 17:
	print("Your 10-Year risk is greater than 30%")
