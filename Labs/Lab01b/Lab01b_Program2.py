from math import *

print("This shows the function 5*x/(x-2) evaluated close to x=1")
x = 1.1
print(5*x/(x-2))
x = 1.01
print(5*x/(x-2))
x = 1.001
print(5*x/(x-2))
x = 1.0001
print(5*x/(x-2))
x = 1.00001
print(5*x/(x-2))
x = 1.000001
print(5*x/(x-2))

print("\nThis shows the function sin(x)/x evaluated close to x=0")
x = 1
print(sin(x)/x)
x = .1
print(sin(x)/x)
x = .01
print(sin(x)/x)
x = .001
print(sin(x)/x)
x = .0001
print(sin(x)/x)
x = .00001
print(sin(x)/x)
x = .000001
print(sin(x)/x)
x = .0000001
print(sin(x)/x)

print("\nThis shows the function (1-cos(x))/(x^2) evaluated close to x=0")
x = 1
print((1-cos(x))/(x**2))
x = .1
print((1-cos(x))/(x**2))
x = .01
print((1-cos(x))/(x**2))
x = .001
print((1-cos(x))/(x**2))
x = .0001
print((1-cos(x))/(x**2))
x = .00001
print((1-cos(x))/(x**2))
x = .000001
print((1-cos(x))/(x**2))

print("\nThis shows the function (1+(1/x))**x evaluated close to x=[positive infinity]")
x = 1
print((1+(1/x))**x)
x = 10
print((1+(1/x))**x)
x = 100
print((1+(1/x))**x)
x = 1000
print((1+(1/x))**x)
x = 10000
print((1+(1/x))**x)
x = 100000
print((1+(1/x))**x)
x = 1000000
print((1+(1/x))**x)