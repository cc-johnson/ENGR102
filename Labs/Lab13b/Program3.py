# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:        Chase Johnson
# Section:     413
# Assignment:  Lab 13b Program 1
# Date:        24 November, 2019
import numpy as np

requirements = np.array([[200,975,3,2,1],[225,850,8,2,1],[250,850,3,3,1],[100,850,3,3,2],[0,500,0,5,0],[0,500,0,5,1],[150,595,5,8,1],[175,675,20,8,3],[250,1080,9,10,1],[250,800,8,10,1],[800,850,0,12,2],[0,725,50,12,0]])
costAtShops = np.array([[0.14,0.09,0.10],[0.22,0.21,0.22],[5.50,5.75,5.65],[8.95,8.94,7.00],[185.00,195.00,205.00]])

costsMultiplied = requirements @ costAtShops

shopSums = costsMultiplied.sum(axis=0)
cheapestShop = np.where(shopSums == np.min(shopSums))[0][0]
shops = {0:'Shop A', 1:'Shop B', 2:'Shop C'}
shopName = shops[cheapestShop]
print('It is cheapest to shop annually at: ' + shopName + ' for a total cost of $' + str(round(shopSums[cheapestShop],2)))

shopDuringMonths = np.array([])
monthlyCosts = np.array([])
for costs in costsMultiplied:
	cheapestShopInMonth = np.where(costs == np.min(costs))[0][0]
	shopDuringMonths = np.append(shopDuringMonths,cheapestShopInMonth)
	monthlyCosts = np.append(monthlyCosts,round(np.min(costs),2))

months = {0:'January',1:'February',2:'March',3:'April',4:'May',5:'June',6:'July',7:'August',8:'September',9:'October',10:'November',11:'December'}
for i in range(len(shopDuringMonths)):
	shopForMonth = shops[shopDuringMonths[i]]
	print('The best shop to shop at for ' + months[i] + ' is: ' + shopForMonth + ' with a total cost of $' + str(monthlyCosts[i]))