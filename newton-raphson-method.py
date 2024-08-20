import math

# Newton-Raphson method
def newton_raphson(func, func_prime, x0, tolerance = 1e-6, max_iterations = 1000):
    x = x0
    for i in range(max_iterations):
        x_new = x - func(x) / func_prime(x)
        if abs(x_new - x) < tolerance:
            return x_new, i + 1
        x = x_new
    return None, max_iterations

# Equation functions
def f1(x):
    return x ** 3 - 2 * x - 5
def f1_prime(x):
    return 3 * x ** 2 - 2

def f2(x):
    return x ** 2 - 4 * x + 4
def f2_prime(x):
    return 2 * x - 4

def f3(x):
    return math.log(x) + x ** 2 - 4
def f3_prime(x):
    return 1 / x + 2 * x

root1, iterations1 = newton_raphson(f1, f1_prime, 2)
print(f"Root is {root1} in {iterations1} iterations")

root2, iterations2 = newton_raphson(f2, f2_prime, 1)
print(f"Root is {root2} in {iterations2} iterations")

root3, iterations3 = newton_raphson(f3, f3_prime, 2)
print(f"Root is {root3} in {iterations3} iterations")