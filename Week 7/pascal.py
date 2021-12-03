def PairwiseAdd(l):
	newList = []
	newList.append(l[0])
	for i in range(1, len(l)):
		newList.append(l[i-1] + l[i])
	newList.append(l[-1])
	return newList


"""	To create a pascal triangle with N lines:
N = int(input("Number of lines: "))

intermediateList = [1]

for i in range(1, N+1):
	print(intermediateList)
	intermediateList = PairwiseAdd(intermediateList)
"""

#l = [1, 2, 3, 4]
N = int(input("Number of iterations: "))
for i in range(1, N+ 1):
	print(l)
	l = PairwiseAdd(l)
