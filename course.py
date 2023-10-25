from professor import Professor
from enroll import Enroll

class Course:
    def __init__(self, name, code, min_, max_, professor: Professor):
        self.name = name
        self.code = code
        self.min_students = min_
        self.max_students = max_
        self.professors = []
        self.enrollments = []

        if isinstance(professor, Professor):
            self.professors.append(professor)
        elif isinstance(professor, list):
            for entry in professor:
                if not isinstance(entry, Professor):
                    raise Exception("Invalid professor...")
            self.professors = professor
        else:
            raise Exception("Invalid professor...")
        
    def add_professor(self, professor: Professor):
        if not isinstance(professor, Professor):
            raise Exception("Invalid professor...")

        self.professors.append(professor)

    def add_enrollment(self, enroll: Enroll):
        if not isinstance(enroll, Enroll):
            raise Exception("Invalid enrollment...")
        
        if len(self.enrollments) == self.max_students:
            raise Exception("Course is full, can't enroll anymore students!")
        
        self.enrollments.append(enroll)


    def is_cancelled(self):
        return len(self.enrollments) <= self.min_students
    