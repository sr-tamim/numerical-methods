import math

# Simple iteration method
def simple_iteration(func, x0, tolerance = 1e-6, max_iterations = 1000):
    x = x0
    for i in range(max_iterations):
        x_new = func(x)
        if abs(x_new - x) < tolerance:
            return x_new, i + 1
        x = x_new
    return None, max_iterations

# Equation functions
def g1(x):
    return (2 * x ** 2 + 3) / 5

def g2(x):
    return math.cos(x)

def g3(x):
    return math.e**x / 3

root1, iterations1 = simple_iteration(g1, 0.5)
print(f"Root is {root1} in {iterations1} iterations")

root2, iterations2 = simple_iteration(g2, 0.5)
print(f"Root is {root2} in {iterations2} iterations")

root3, iterations3 = simple_iteration(g3, 0.5)
print(f"Root is {root3} in {iterations3} iterations")