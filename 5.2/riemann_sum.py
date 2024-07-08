import sympy as sp

# Define the variable and function
x = sp.symbols('x')
f = 1 / x

# Define the midpoints
midpoints = [1.125, 1.375, 1.625, 1.875]

# Calculate the sum using the midpoints
delta_x = 0.25
riemann_sum = sum(f.subs(x, xi) * delta_x for xi in midpoints)

# Evaluate the sum
result = riemann_sum.evalf()
print(result)