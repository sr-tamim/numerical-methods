import math

# Bisection Method
def bisection(func, a, b, tolerance = 1e-6, max_iterations = 1000):
    if func(a) * func(b) > 0:
        return None, max_iterations
    for i in range(max_iterations):
        c = (a + b) / 2
        if func(c) == 0 or (b - a) / 2 < tolerance:
            return c, i + 1
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return None, max_iterations

# Equation functions
def f1(x):
    return x ** 3 - 2 * x - 5

def f2(x):
    return x ** 3 - x - 2

def f3(x):
    return x ** 2 - 5

def f4(x):
    return math.e ** x - 3 * (x ** 2)

root1, iterations1 = bisection(f1, 1, 3)
print(f"Root is {root1} in {iterations1} iterations")

root2, iterations2 = bisection(f2, 1, 2)
print(f"Root is {root2} in {iterations2} iterations")

root3, iterations3 = bisection(f3, 2, 3)
print(f"Root is {root3} in {iterations3} iterations")

root4, iterations4 = bisection(f4, 0, 1)
print(f"Root is {root4} in {iterations4} iterations")