byte = "11000101"
l = [2**7, 2**6, 2**5, 2**4, 2**3, 2**2, 2**1, 2**0]
s = 0
for i in range(8): # For 8 bits.
	s += l[i] * int(byte[i]) # Multiply one by one and add them up. 
print(s)