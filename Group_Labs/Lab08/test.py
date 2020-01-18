from matplotlib.pyplot import *
import math

subplot(2,1,1)

# Plot value lists
t = []
y1 = []
y2 = []

# Generate the values for the plots
for i in range(0,153,3):
	i = i / 50
	t.append(i)
	y1.append((i**2)*math.exp(-(i**2)))
	y2.append((i**4)*math.exp(-(i**2)))

# Annotated points
x = [0, 0.45, 1.1, 1.75, 2.25, 2.7]
y = [0, 0.23, 0.4, 0.18, 0.07, 0.01]

# Generate the plot
scatter(x,y, color="k", label="data")
plot(t, y1, color="r", linewidth=1.0, linestyle="-", label="f(x)")
plot(t, y2, color="b", linewidth=1.0, linestyle="-", label="g(x)")

# Plot information
title("Data and two curves vs. time")
xlabel("time")
ylabel("y")
legend(loc='upper right', frameon=True)
xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5], ['0', '0.5', '1.0', '1.5', '2.0', '2.5'])
yticks([0, 0.25, 0.5, 0.75, 1.0], ['0', '0.25', '0.5', '0,75', '1.0'])

subplot(2,1,2)
xticks([]), yticks([])
text(0.5,0.5, 'subplot(2,1,2)',ha='center',va='center',size=24,alpha=.5)

show()