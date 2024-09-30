
x = list(eval(input("Enter the x values: ")))
y = list(eval(input("Enter the y values: ")))
m = len(x)
xp = float(input("Enter the x value for interpolation: "))
yp = 0

for i in range(m):
  L = 1
  for j in range(m):
    if i != j:
      L = L * (xp - x[j]) / (x[i] - x[j])
  
  yp = yp + L * y[i]

print(f"The interpolated value at {xp} is {yp}")

# Example Inputs
# Enter the x values: 5,7,11,13
# Enter the y values: 150,392,1452,2366
# Enter the x value for interpolation: 9
