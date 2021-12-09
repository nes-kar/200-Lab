""" Exemplary File
F = open("numbers.txt", "w")
for i in range(100):
	F.write("{}\n".format(i))
F.close()
"""
f = open("numbers.txt")
evens = []
odds = []

for line in f:
	line.strip()
	number = int(line)
	if number > 0:
		if number % 2 == 0:
			evens.append(number)
		else:
			odds.append(number)
	else:
		continue
f1 = open("even.txt", "w")
for number in evens:
	f1.write("{}\n".format(number))
f1.close()

f2 = open("odd.txt", "w")
for number in odds:
	f2.write("{}\n".format(number))
f2.close()