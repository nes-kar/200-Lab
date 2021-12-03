from math import exp

x0 = int(input("First point: "))
xN = int(input("Final Point: "))
N = int(input("Number of points: "))

h = (xN - x0) / N 

x = []
for i in range(N + 1): # Include the last element.
	x.append(x0 + i * h)

f = []
for xi in x:
	f.append(exp(- xi**2))

I = sum(f) * h 
print(I)