import numpy as np



def f(x) :
    return np.exp(-x**2)
 
print(f(2))
a, b = -1, 2
n = [5, 10, 50, 100]


for num in n:
    dx = (b - a) / num
    left_endpoints = np.linspace(a, b - dx, num)
    left_approximations = f(left_endpoints)
    left_sum = sum(left_approximations * dx)
    print(f"n = {num}, left Riemann sum = {left_sum:.4f}")

    right_endpoints = np.linspace(a + dx, b, num)
    right_approximations = f(right_endpoints)
    right_sum = sum(right_approximations * dx)
    print(f"n = {num}, right Riemann sum = {right_sum:.4f}")