def dff1 (f, x, h):
  return (f(x + h) - f(x)) / h

def dff2 (f, x, h):
  return (f(x + 2 * h) - 2 * f(x + h) + f(x)) / (h ** 2)

def dff3 (f, x, h):
  return (f(x + 3 * h) - 3 * f(x + 2 * h) + 3 * f(x + h) - f(x)) / (h ** 3)

def forward_differences(f, x, h):
  print("Solution by forward difference")
  print(f"f'({x}) = {dff1(f, x, h)}")
  print(f"f''({x}) = {dff2(f, x, h)}")
  print(f"f'''({x}) = {dff3(f, x, h)}")

def f1(x):
  return (2 * x ** 3 + 3 * x ** 2 - 4)

forward_differences(f1, 2.5, 0.5)