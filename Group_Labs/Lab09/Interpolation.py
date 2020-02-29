import random

xList = [3, 4, 5, 7, 8]
yList = [6, 7, 9, 3, 4]
x = float(input("Type an x-value you would like to find: "))

x_index = 0
while x > xList[x_index]:
    x_index += 1

y = yList[x_index - 1] + (x - xList[x_index-1]) * ((yList[x_index] - yList[x_index - 1]) / (xList[x_index] - xList[x_index - 1]))
print(y)
