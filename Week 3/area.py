# Let a = 6:
a = 6

area_square = a**2

from math import pi
area_circle = pi * (a / 2)**2

area_shaded = area_square - area_circle

print("Shaded area is: {} for given a = 6".format(area_shaded))

