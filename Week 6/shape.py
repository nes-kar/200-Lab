M = [[1,2,3], [4,5,6], [7,8,9]] 

V = []

for row in M:
	for i in range(len(row)):
		V.append(row[i])

print(V)