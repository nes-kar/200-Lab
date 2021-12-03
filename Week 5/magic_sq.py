V = int(input("Initial Velocity (positive in the upward direction): "))
h = int(input("Initial Height: "))

g = 9.8

t = 0
dt = 0.001 
while h >= 0: # While the object is above the ground:
	h += V*dt
	V -= g*dt
	t += dt 

print(t)
