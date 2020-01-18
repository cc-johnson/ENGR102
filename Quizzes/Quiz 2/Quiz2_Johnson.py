# By submitting this assignment, I agree to the following:
#  “Aggies do not lie, cheat, or steal, or tolerate those who do”
#  “I have not given or received any unauthorized aid on this assignment”
#
# Name:           Chase Johnson
# Section:        413
# Assignment:     Quiz 2
# Date:           18 September 2019

# __init__
dist = 202.3

# Input for the cost of gas per gallon of fuel
costGal = float(input("What is the current cost per gallon of fuel? "))

vel1 = 55.0
mpg1 = (-5.9852) + (1.6052)*(vel1) - (0.0141)*(vel1**2)
cost1 = round(dist/mpg1*costGal,2)
time1 = round(dist/vel1,2)
print("At 55 mph it will take", time1, "minutes.")
print("At 55 mph it will cost $" + str(cost1))

vel2 = 70.0
mpg2 = (-5.9852) + (1.6052)*(vel2) - (0.0141)*(vel2**2)
cost2 = round(dist/mpg2*costGal,2)
time2 = round(dist/vel2,2)
deltVel = round(vel2-vel1,2)
deltCost = round(cost2-cost1,2)
deltTime = round(time2-time1,2)

speedWord = "faster"
moneyWord = "more"

if deltTime < 0:
    deltTime = abs(deltTime)
elif deltTime > 0:
    speedWord = "slower"

if deltCost < 0:
    deltCost = abs(deltCost)
elif deltCost > 0:
    moneyWord = "less"

print("At 70 mph it will take", time2, "minutes,", str(deltTime), "minutes", speedWord, "than at 55 mph.")
print("At 70 mph it will cost $" + str(cost2), "$" + str(deltCost) + " dollars", moneyWord, "than at 55 mph.")

