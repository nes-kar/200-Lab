def isPrime(n):
	l = [n % i for i in range(2, n)]
	if 0 in l:
		return False
	else:
		return True

def isTwin(N1, N2):
	if isPrime(N1) == isPrime(N2) == True:
		if abs(N1 - N2):
			print("Twin Primes")
	else:
		print("...Error: Not twin primes")

N1 = int(input("1st number: "))
N2 = int(input("2nd number: "))

isTwin(N1, N2)