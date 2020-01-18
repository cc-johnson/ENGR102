xList = [3, 4, 5, 7, 8]
yList = [6, 7, 9, 3, 4]
x = float(input("Type an x-value you would like to find: "))

Counter = 0
while x > xList[Counter]:
    Counter += 1

y = yList[Counter - 1] + (x - xList[Counter-1]) * ((yList[Counter] - yList[Counter - 1]) / (xList[Counter] - xList[Counter - 1]))
print(y)
