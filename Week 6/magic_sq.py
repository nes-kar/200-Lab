M=[[1, 2, 5],[3, 4, 1],[2, 6, 8]]
#M = [[7, 12, 1, 14], [2, 13, 8, 11],[16, 3, 10, 5],[9, 6, 15, 4]]

sum_first = sum(M[0])

for row in M: # Check all the rows first
	if sum(row) != sum_first:
		print("Nonmagic")
		exit()
for column in range(len(M)): # Now for the columns
	s = 0
	for row in M:
		s += row[column]
	if s != sum_first:
		print("Nonmagic")
		exit()
print("Magic")

