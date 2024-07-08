import numpy as np

def f(x):
    return x / (x + 1)

a, b = 0, 2
n = 5
dx = (b - a) / n

midpoints = np.linspace(a + dx/2, b - dx/2, n)

midpoint_approximations = f(midpoints)

midpoint_sum = np.sum(midpoint_approximations * dx)

print(midpoint_sum)