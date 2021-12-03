student1 = {"Name": "XXX YYY",
			"Homework": [80, 40, 67],
			"Midterms": [80, 90],
			"Final": 45}

student2 = {"Name": "AAA BBB",
			"Homework": [56, 90, 93],
			"Midterms": [90, 60],
			"Final": 85}

l = [student1, student2]

grade1 = sum(l[0]["Homework"])*0.1 + sum(l[0]["Midterms"])*0.2 + l[0]["Final"]*0.3

grade2 = sum(l[1]["Homework"])*0.1 + sum(l[1]["Midterms"])*0.2  + l[1]["Final"]*0.3

print("Grade of the first student :" , grade1)
print("Grade of the second student: ", grade2)