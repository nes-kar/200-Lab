A=[1, 2, 3, 5]
B=[3, 4, 2, 1]

M = [[] for _ in range(len(A))]
print(M)
for i in range(len(A)):
	for j in range(len(B)):
		M[i].append(A[i] * B[j])
print(M)