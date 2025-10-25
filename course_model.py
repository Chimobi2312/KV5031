
from dataclasses import dataclass, field
from typing import Dict, Set, List

@dataclass(frozen=True)
class Lecturer:
    lid: str
    name: str

@dataclass(frozen=True)
class Student:
    sid: str
    name: str

@dataclass(frozen=True)
class Module:
    code: str
    title: str

class Course:
    """Course is the single source of truth for relationships."""

    def __init__(self, cid: str, title: str):
        self.cid = cid
        self.title = title
        self.modules: Dict[str, Module] = {}
        self.students: Dict[str, Student] = {}
        self.lecturers: Dict[str, Lecturer] = {}
        self._roster: Dict[str, Set[str]] = {}

    def add_module(self, m: Module) -> None:
        self.modules[m.code] = m
        self._roster.setdefault(m.code, set())

    def add_student(self, s: Student) -> None:
        self.students[s.sid] = s

    def add_lecturer(self, l: Lecturer) -> None:
        self.lecturers[l.lid] = l

    def enrol(self, sid: str, module_code: str) -> None:
        if sid not in self.students:
            raise KeyError(f"Unknown student: {sid}")
        if module_code not in self.modules:
            raise KeyError(f"Unknown module: {module_code}")
        self._roster[module_code].add(sid)

    def students_in_module(self, module_code: str) -> List[Student]:
        return [self.students[sid] for sid in self._roster.get(module_code, set())]

    def modules_for_student(self, sid: str) -> List[Module]:
        codes = [code for code, sids in self._roster.items() if sid in sids]
        return [self.modules[c] for c in codes]


class OnlineCourse(Course):
    """A subclass of Course for online courses."""

    def add_student(self, s: Student, online_access_code: str) -> None:
        """Adds a student to the online course with an access code."""
        super().add_student(s)
        print(f"Student {s.name} has been granted online access with code {online_access_code}")


# --- Example usage

# Create a course
course = Course("CS-BSc", "BSc Computer Science")

# Create an online course
online_course = OnlineCourse("CS-MSc-Online", "MSc Computer Science (Online)")

# Add a student to the regular course
course.add_student(Student("S001", "Raphael"))

# Add a student to the online course
online_course.add_student(Student("S002", "Eze"), "XYZ123")

