def dff1 (f, x, h):
  return (f(x + h) - f(x - h)) / (2 * h)

def dff2 (f, x, h):
  return (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)

def dff3 (f, x, h):
  return (f(x + 2 * h) - 2 * f(x) + f(x - 2 * h)) / (2 * h ** 3)

def central_differences(f, x, h):
  print("Solution by central difference")
  print(f"f'({x}) = {dff1(f, x, h)}")
  print(f"f''({x}) = {dff2(f, x, h)}")
  print(f"f'''({x}) = {dff3(f, x, h)}")
  
def f1(x):
  return (2 * x ** 3 + 3 * x ** 2 - 4)

central_differences(f1, 2.5, 0.5)