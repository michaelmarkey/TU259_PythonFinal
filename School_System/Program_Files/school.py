from student import Student

class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address

        self.students = {}

    def add_student(self, student):
        key = (student.fName, student.lName)
        if key not in self.students:
            self.students[key] = student
            print(f"Added {student.fName} {student.lName} to the school.")
        else:
            print("Student already exists.")

    def remove_student(self, student):
        key = (student.fName, student.lName)
        if key in self.students:
            del self.students[key]
            print(f"Removed {student.fName} {student.lName} from the school.")
        else:
            print("Student not found.")

    def find_student_by_name(self, first_name, last_name):
        return self.students.get((first_name, last_name), None)

    def list_students_by_subject(self, subject):
        result = []
        for student in self.students.values():
            if hasattr(student, 'schoolSubjects') and subject in student.schoolSubjects:
                result.append(f"{student.fName} {student.lName}")
        return result

    def get_average_grade(self, subject):
        total = 0
        count = 0

        for student in self.students.values():
            grade_attr = f"final{subject}Grade"  # e.g., finalMathematicsGrade
            if hasattr(student, grade_attr):
                total += getattr(student, grade_attr)
                count += 1

        return round(total / count, 2) if count > 0 else None
    
    def __repr__(self):
        return (
            f"School Name: {self.name}\n"
            f"Address: {self.address}\n"
            f"Subjects Offered: English, Mathematics, History\n"
            f"Total Students Enrolled: {len(self.students)}"
        )
