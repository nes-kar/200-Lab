""" Simple list:
li_students=[{"Name":"XXX YYY","Department":"Chemistry"},
			 {"Name":"AAA BBB","Department":"Physics"}, 
			 {"Name":"TTT VVV", "Department":"EE"},
			 {"Name":"LLL MMM","Department":"Chemistry"},
			 {"Name":"Enes Kandemir","Department":"Physics"},
			 {"Name":"NNN NNN","Department":"Biology"},
			 {"Name":"MMM MMM","Department":"Biology"}]
"""

departments = [student["Department"] for student in li_students]

departments = list(set(departments)) # Remove the duplicates

for department in departments:
	f = open(department + ".txt", "w")
	for student in li_students:
		if student["Department"] == department:
			f.write("{}\n".format(student["Name"]))
	f.close()
