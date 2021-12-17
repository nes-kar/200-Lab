import matplotlib.pyplot as plt
from math import *
N = int(input("Enter an integer: "))

X = [-6*pi + i*(12*pi)/N for i in range(N + 1)]
Y = []
for x in X:
	if x == 0:
		Y.append(1)
	else:
		Y.append(sin(x) / x)

plt.plot(X, Y, label="y=sinc(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()