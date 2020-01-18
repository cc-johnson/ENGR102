# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 10b Program 2
# Date:        3 November, 2019

# Get inputs 
loanAmount = float(input("How much is your loan? "))
annualInterestRate = float(input("What is your annual interest rate? ")) / 100
monthlyPayment = float(input("What is your monthly payment? "))
accruedInterest = 0

# Create csv file
file = open('loan.csv', 'x+')

# Start the csv file with column titles
currentMonth = 0
file.write('Month,Principal Balance,Accrued Interest\n')
file.write(str(currentMonth) + ',' + str(loanAmount) + ',' + str(accruedInterest) + '\n')

# Do calculations for first month
oldLoan = loanAmount

interest = loanAmount * ((1/12) * annualInterestRate)
accruedInterest += interest
loanAmount = loanAmount + interest - monthlyPayment
currentMonth += 1

# Determine if the principal left is increasing or decreasing
if oldLoan > loanAmount:
	# While the loan is decreasing
	while loanAmount > 0:
		# Write out the most recent calculations
		file.write(str(currentMonth) + ',' + str(loanAmount) + ',' + str(accruedInterest) + '\n')

		oldLoan = loanAmount
		interest = loanAmount * ((1/12) * annualInterestRate)
		accruedInterest += interest
		loanAmount = loanAmount + interest - monthlyPayment
		currentMonth += 1
# Else do calculations up to month 30
else:
	for i in range(29):
		# Write out the most recent calculations
		file.write(str(currentMonth) + ',' + str(loanAmount) + ',' + str(accruedInterest) + '\n')

		oldLoan = loanAmount
		interest = loanAmount * ((1/12) * annualInterestRate)
		accruedInterest += interest
		loanAmount = loanAmount + interest - monthlyPayment
		currentMonth += 1
