import matplotlib.pyplot as plt
f = open("input.txt", "r")
X, Y = [], []

for line in f:
	line.strip()
	x, y = line.split()
	X.append(float(x))
	Y.append(float(y))

plt.plot(X, Y)
plt.xlabel("X")
plt.ylabel("Y")
plt.show()