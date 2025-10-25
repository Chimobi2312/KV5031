
from student import Student

# Creating a new student
student = Student("Raphael", 23066598)

# Enrolling the student in courses
student.enroll("Math")
student.enroll("History")

# Adding grades
student.add_grade("Math", 90)
student.add_grade("History", 85)

# Getting the GPA
print(f"GPA: {student.get_gpa()}")

# Displaying the student's information
print(student)

# Expected output:
# GPA: 87.5
# Student Name: Raphael Eze, ID: 23066598, Courses: ['Math', 'History']
