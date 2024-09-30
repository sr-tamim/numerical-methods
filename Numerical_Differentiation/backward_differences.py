def dff1 (f, x, h):
  return (f(x) - f(x - h)) / h

def dff2 (f, x, h):
  return (f(x) - 2 * f(x - h) + f(x - 2 * h)) / (h ** 2)

def dff3 (f, x, h):
  return (f(x) - 3 * f(x - h) + 3 * f(x - 2 * h) - f(x - 3 * h)) / (h ** 3)

def backward_differences(f, x, h):
  print("Solution by backward difference")
  print(f"f'({x}) = {dff1(f, x, h)}")
  print(f"f''({x}) = {dff2(f, x, h)}")
  print(f"f'''({x}) = {dff3(f, x, h)}")
  
def f1(x):
  return (2 * x ** 3 + 3 * x ** 2 - 4)

backward_differences(f1, 2.5, 0.5)