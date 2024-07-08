import numpy as np
import matplotlib.pyplot as plt  # Ensure this line is correct

# Define the function
def f(x):
    return x / (x + 1)

# Define the interval and number of rectangles
a, b = 0, 2  # interval [0, 2]
n = 20        # number of rectangles
dx = (b - a) / n  # width of each rectangle

# Compute the midpoints
midpoints = np.linspace(a + dx/2, b - dx/2, n)
print(midpoints)

# Compute the function values at the midpoints
midpoint_approximations = f(midpoints)
print(midpoint_approximations)

# Calculate the midpoint Riemann sum
midpoint_sum = np.sum(midpoint_approximations * dx)

print(midpoint_sum)

# Plot the function and the rectangles
x = np.linspace(a, b, 1000)  # create a fine grid for plotting the function
y = f(x)  # compute the function values

plt.plot(x, y, label='f(x) = x / (x + 1)')  # plot the function
plt.bar(midpoints, midpoint_approximations, width=dx, alpha=0.5, align='center', edgecolor='blue')  # plot the rectangles

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Midpoint Riemann Sum Approximation')
plt.legend()
plt.show()

# Print the result
print("Midpoint Riemann Sum Approximation:", midpoint_sum)
