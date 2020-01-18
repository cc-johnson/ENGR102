import matplotlib.pyplot as plt
import math

t = []
y1 = []

for i in range(0, 153, 3):
    i /= 50
    t.append(i)
    y1.append(i ** 2 * math.exp(-i ** 2))

# Data points
x = [.45, 1.1, 1.75, 2.25]
y = [.23, .4, .18, .07]

plt.plot(x, y, color='yellow', label='data')
print(t)
plt.plot(t, y1, color='blue', linewidth=1.0, linestyle="-", label="t^2exp(-t^2)")
plt.axis([1, 2, 0, 0.5])

plt.scatter(x[1:3], y[1:3], color='yellow', marker='^')

# Plot and axes titles
plt.title('Data interpolation and Curve 1')
plt.xlabel('time')
plt.ylabel('y')

plt.legend(loc='upper right')

# Set intervals
plt.yticks([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
plt.xticks([1.0, 1.2, 1.4, 1.6, 1.8, 2.0])

plt.show()