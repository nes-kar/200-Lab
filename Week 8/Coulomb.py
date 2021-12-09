from math import sqrt
def find_distance(c1, c2):
	x1, y1, z1 = c1
	x2, y2, z2 = c2
	return sqrt((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)
	
k = 1 # Unit not necessary 
def find_forces(c1, c2, q1, q2):
	r = find_distance(c1, c2)
	x1, y1, z1 = c1
	x2, y2, z2 = c2
	return [k * q1 * q2 * (x1 - x2) / r**3, 
			k * q1 * q2 * (y1 - y2) / r**3,
			k * q1 * q2 * (z1 - z2) / r**3]
c1=[1.3,-0.2,3.2]
c2=[5.3,7.2,-1.2]
q1=0.4
q2=-0.6
F=find_forces(c1,c2,q1,q2)
print(F)

