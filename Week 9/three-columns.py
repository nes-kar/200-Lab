N = int((input("Enter an integer: ")))

X = [i/N for i in range(N + 1)]

f = open("data.txt", "w")

for x in X:
	f.write("{0:<6} {1:<8.4f} {2:<8.4f}\n".format(x, x**2, x**3)) # Left justified
f.close()
