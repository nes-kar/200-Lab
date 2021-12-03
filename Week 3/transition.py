# Energy for n2:
E2 = -13.6 / (2**2)

# Energy for n3:
E3 = -13.6 / (3**2)

E_diff = E3 - E2
print(E_diff)

h = 4.135667E-15 

# Using the formula E = hf:

f = E_diff / h
print(f)

c = 3E8

# Wavelength L = c / f and convert it to nm:
L = (c / f) * 10**9

print(L)

print("{} nm wavelength corresponds to red light. ".format(round(L,1)))