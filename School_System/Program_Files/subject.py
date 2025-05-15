# subject.py

from student import Student

# Define a class for each subject, where grade and subject-specific data are stored
class SubjectStudent:
    def __init__(self, student, subject_name, subject_level, subject_class_number, subject_teacher, last_test_score):
        self.student = student  # Link back to the Student object
        self.subject_name = subject_name
        self.subject_level = subject_level
        self.subject_class_number = subject_class_number
        self.subject_teacher = subject_teacher
        self.last_test_score = last_test_score
        self.grade = last_test_score  # This is the grade in the subject

        if subject_name not in self.student.schoolSubjects:
            self.student.schoolSubjects.append(subject_name)

    def add_details(self, level, class_number, teacher, last_test_score):
        """Add or update subject-specific details."""
        self.subject_level = level
        self.subject_class_number = class_number
        self.subject_teacher = teacher
        self.last_test_score = last_test_score
        self.grade = last_test_score

    def __repr__(self):
        return (f"{self.student.fName} {self.student.lName} | "
                f"{self.subject_name} Level: {self.subject_level}, "
                f"Class: {self.subject_class_number}, "
                f"Teacher: {self.subject_teacher.get_name() if self.subject_teacher else 'No teacher assigned'}, "
                f"Last Test Score: {self.last_test_score}")

# Helper function to create a SubjectStudent object for a specific subject - useful for future subjects
def create_subject_student(student, subject_name, level, class_number, teacher, last_test_score):
    return SubjectStudent(student, subject_name, level, class_number, teacher, last_test_score)


