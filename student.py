
class Student:
    """A class to represent a student."""

    def __init__(self, name: str, student_id: int):
        """Initializes a new Student object."""
        self.name = name
        self.student_id = student_id
        self.courses = []
        self.grades = {}

    def enroll(self, course_name: str):
        """Enrolls the student in a new course."""
        if course_name not in self.courses:
            self.courses.append(course_name)

    def add_grade(self, course_name: str, grade: float):
        """Adds a grade for a specific course."""
        if course_name in self.courses:
            self.grades[course_name] = grade
        else:
            raise ValueError("Student is not enrolled in the course.")

    def get_gpa(self) -> float | None:
        """Calculates and returns the student's GPA."""
        if not self.grades:
            return None
        return sum(self.grades.values()) / len(self.grades)

    def __str__(self):
        """Returns a string representation of the Student object."""
        return f"Student Name: {self.name}, ID: {self.student_id}, Courses: {self.courses}"

