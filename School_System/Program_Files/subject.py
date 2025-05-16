from student import Student
from employee import Employee

class SubjectStudent:
    """This covers a student's enrollment in a specific subject.
    
    We stores here subject-specific information for a student, including
    the subject details, teacher, grades, and test scores. It maintains a
    link to the associated Student object."""

    def __init__(self, student, subject_name, subject_level, subject_class_number, subject_teacher, last_test_score):
        
        # Input validation without raising exceptions to maintain compatibility
        if not isinstance(student, Student):
            print(f"Warning: Expected Student object, got {type(student).__name__}")
            
        if not subject_name:
            print("Warning: Subject name should not be empty")
        
        self.student = student  # Link back to the Student object
        self.subject_name = subject_name
        self.subject_level = subject_level
        self.subject_class_number = subject_class_number
        self.subject_teacher = subject_teacher

        # Handle potential non-numeric scores gracefully
        try:
            self.last_test_score = float(last_test_score)
        except (ValueError, TypeError):
            print(f"Warning: Invalid test score '{last_test_score}', defaulting to 0")
            self.last_test_score = 0

        
        self.grade = last_test_score  # This is the grade in the subject

        # Add subject to student's subject list if not already present
        if hasattr(self.student, 'schoolSubjects'):
            if subject_name not in self.student.schoolSubjects:
                self.student.schoolSubjects.append(subject_name)
        else:
            print("Warning: Student object does not have schoolSubjects attribute")


    def add_details(self, level, class_number, teacher, last_test_score):
        """Add or update subject-specific details."""

        self.subject_level = level
        self.subject_class_number = class_number
        self.subject_teacher = teacher
        
        # Handle potential non-numeric scores gracefully
        try:
            self.last_test_score = float(last_test_score)
        except (ValueError, TypeError):
            print(f"Warning: Invalid test score '{last_test_score}', not updating score")
        else:
            self.grade = self.last_test_score

    def __repr__(self):
        """Returns a string representation of the SubjectStudent"""

        teacher_name = self.subject_teacher.get_name() if isinstance(self.subject_teacher, Employee) else 'No teacher assigned'
        return (f"{self.student.fName} {self.student.lName} | "
                f"{self.subject_name} Level: {self.subject_level}, "
                f"Class: {self.subject_class_number}, "
                f"Teacher: {self.subject_teacher.get_name() if self.subject_teacher else 'No teacher assigned'}, "
                f"Last Test Score: {self.last_test_score}")

    def create_subject_student(student, subject_name, level, class_number, teacher, last_test_score):
        """Create a SubjectStudent object for a specific subject. This helper function creates and 
        returns a new SubjectStudent instance, which is useful for creating different subject enrollments."""
        
        return SubjectStudent(student, subject_name, level, class_number, teacher, last_test_score)


