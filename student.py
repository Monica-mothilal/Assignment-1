class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Creating instances of the Student class
alice = Student("Alice", 10)
bob = Student("Bob", 12)
charlie = Student("Charlie", 9)

# List of students
students = [alice, bob, charlie]

# Print total number of students
print("Total number of students created:",len(students))

# Print list of all students and their details
print("List of all students:")
for student in students:
    print(f"Name: {student.name}, Grade: {student.grade}")
