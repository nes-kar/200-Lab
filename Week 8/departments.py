# Simple list of students:
li_students=[{"Name":"XXX YYY","Department":"Chemistry"},
			 {"Name":"AAA BBB","Department":"Physics"}, 
			 {"Name":"TTT VVV", "Department":"EE"},
			 {"Name":"LLL MMM","Department":"Chemistry"},
			 {"Name":"Enes Kandemir","Department":"Physics"},
			 {"Name":"NNN NNN","Department":"Biology"},
			 {"Name":"CCC DDD","Department":"Physics"},
			 {"Name":"MMM MMM","Department":"Biology"}]


departments = [student["Department"] for student in li_students]

departments = list(set(departments)) # Remove the duplicates

for department in departments:
	f = open(department + ".txt", "w")
	l = [] # Temporary list to hold the corresponding names.
	for student in li_students:
		if student["Department"] == department:
			l.append(student["Name"])
	l.sort()
	for name in l:
		f.write("{}\n".format(name))
	f.close()
