import numpy as np

def f(x):
    return x / (x + 1)

# Define the interval and number of rectangles
a, b = 0, 2  # interval [0, 2]

n = 100
dx = (b - a) / n

left_endpoints = np.linspace(a, b - dx, n)
left_approximations = f(left_endpoints)
left_sum = np.sum(left_approximations * dx)

right_endpoints = np.linspace(a + dx, b, n)
right_approximations = f(right_endpoints)
right_sum = np.sum(right_approximations * dx)

print(left_sum)
print(right_sum)
