import matplotlib.pyplot as plt
from random import randrange
n = int(input("Enter the order of polynomial: "))

# Random integer coefficients from -100 to 100 of the form [1,x,x2,..,xn]:
coefficients = [randrange(-100,100) for _ in range(n + 1)]

X = [-2 + i*4/100 for i in range(101)]
Y = []

for x in X:
	y = 0
	for i in range(len(coefficients)):
		y += coefficients[i] * (x ** i)
	Y.append(y)

plt.plot(X, Y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()