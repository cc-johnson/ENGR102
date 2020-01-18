# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Bryan Jones, Chase Johnson, Anna Olmedo, Gustavo Rodriguez
# Section:     413
# Assignment:  Lab 07 Activity 1
# Date:        13 October, 2019

# ---------------
# Warmup 1
# ---------------
strings = ['arroyo', 'elephantine', 'toy', 'shines']
count = 0

for str in strings:
	if len(str) >= 2 and str[0] == str[-1]:
		count += 1

print(count)

# ---------------
# Warmup 2
# ---------------
nums = [1,5,4,65,7,5,34,57,4756,34,6547,4356243,2354,12,1]
smallNums = ''
userNum = float(input("What is your secret number? "))

for num in nums:
	if num <= userNum:
		smallNums += str(num) + ", "

print(smallNums[0:-2])

# ---------------
# Warmup 3
# ---------------
sentence = input("Write me a sentence: ")
letter = input("What letter do you want to count? ")
count = 0

for char in sentence:
	char = char.lower()
	if char == letter:
		count += 1

print("The letter", letter, "appears:", count, "times")

# ---------------
# Warmup 4
# ---------------
# Quadratic function (x ** 2) - (10 * x) + 25
print('x^2 - 10x + 25')

# User input x interval
minX = int(input('Enter an integer: '))
maxX = int(input('Enter an integer higher than before: '))

# find zeros of func
zeros = []
for i in range(minX, (maxX + 1), .01):
    if ((i ** 2) - (10 * i) + 25) == 0:
        zeros.append(i)
maxZero = max(zeros)
print('The maximum value of the function is,', maxZero)
print('The solutions of the function are x =', zeros)
