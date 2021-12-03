a = float(input("First side: "))
b = float(input("Second side: "))
c = float(input("Third side: "))

if a <= 0 or b <= 0 or c <= 0:
	print("Not a valid input!")
	exit()
else:
	if (a + b) < c or (a + c) < b or (b + c) < a:
		print("Can't form a triangle!")
		exit()
	else:
		if a == b == c:
			print("Triangle is equilateral.")
		elif a == b or a == c or b == c:
			print("Triangle is isosceles.")
		else:
			print("Triangle is scalene.")
