from math import sin, pi

N = int(input("Number of lines to be written: "))

angles = [i * pi / (4*N) for i in range(N + 1)] # In radian
sines = [sin(angle) for angle in angles]

f = open("Sine.txt", "w")
for i in range(N + 1):
	f.write("{0:8.1f} {1:8.5f}\n".format(angles[i]*180/pi, # Convert it to degree
											 sines[i])) 
f.close()

