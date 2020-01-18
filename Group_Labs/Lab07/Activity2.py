# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 07 Activity 2
# Date:        13 October, 2019

nums = [1,5,4,65,7,5,34,57,4756,34,6547,4356243,2354,12,1]
smallNums = ''
userNum = float(input("What is your secret number? "))

for num in nums:
	if num <= userNum:
		smallNums += str(num) + ", "

print(smallNums[0:-2])