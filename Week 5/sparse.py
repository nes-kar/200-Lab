elements = [[1,0,0],[3,1,0],[2,1,1],[5,2,1],[4,2,2]]
N = 3

M = [[0,0,0], [0,0,0], [0,0,0]]

for elem in elements:
	A, B, C = elem
	M[B][C] = A

print(M)