from math import *
N = int(input("Enter an integer: "))

A = [cos(pi * n / 16) for n in range(N)]
B = [sin(pi * n / 21) for n in range(N)]

C = []

for i in range(N):
	C.append(A[i] + B[i])

print(C)