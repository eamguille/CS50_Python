"""

students = ["Hermione", "Harry", "Ron"]
for i in range(len(students)):
    print(i + 1, students[i])

"""


# DICTIONARIES
students = {
    "Hermione": "Gryffindor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep=": ")

