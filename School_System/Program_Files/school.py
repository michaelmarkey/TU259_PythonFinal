class School:
    def __init__(self, name, address, telephoneNumber, subjects):
        self.name = name
        self.address = address
        self.telephoneNumber = telephoneNumber
        self.subjects = subjects
        self.students = {}

    def add_student(self, student):
        key = student.studentID  # Use studentID as the key
        if not key or not isinstance(key, str):
            print(f"Invalid student ID {key}.")
            return
        if key not in self.students:
            self.students[key] = student
            print(f"Added {student.fName} {student.lName} to the school.")
        else:
            print(f"Student with ID {student.studentID} already exists.")

    def remove_student(self, student):
        key = student.studentID  # Use studentID as the key
        if key in self.students:
            del self.students[key]
            print(f"Removed {student.fName} {student.lName} from the school.")
        else:
            print(f"Student with ID {student.studentID} not found.")

    def find_student_by_id(self, student_id):
        student = self.students.get(student_id, None)
        if student is None:
            print(f"Student with ID {student_id} not found.")
        return student

    def list_students_by_subject(self, subject):
        result = []
        for student in self.students.values():
            if subject in student.schoolSubjects:
                result.append(f"{student.fName} {student.lName}")
        return result

    def get_average_grade(self, subject):
        total = 0
        count = 0

        if subject == "Mathematics":
            for student in self.students.values():
                try:
                    total += student.finalMathematicsGrade
                    count += 1
                except:
                    continue

        elif subject == "English":
            for student in self.students.values():
                try:
                    total += student.finalEnglishGrade
                    count += 1
                except:
                    continue

        elif subject == "History":
            for student in self.students.values():
                try:
                    total += student.finalHistoryGrade
                    count += 1
                except:
                    continue

        else:
            print(f"This subject ({subject}) is not offered at the school.")
            return None

        if count == 0:
            print(f"No grades available for {subject}.")
            return None

        return round(total / count, 2)

    # Updated helper methods for School class
    def update_school_name(self, name=None):  # new: method to update school name
        if name is not None:
            self.name = name  # new: update school name
        print(f"Updated school name to: {self.name}")

    def update_school_address(self, address=None):  # new: method to update school address
        if address is not None:
            self.address = address  # new: update school address
        print(f"Updated school address to: {self.address}")

    def update_school_year(self, school_year=None):  # new: method to update school year
        if school_year is not None:
            self.school_year = school_year  # new: update school year
        print(f"Updated school year to: {self.school_year}")

    def update_school_subjects(self, subjects=None):  # new: method to update school subjects
        if subjects is not None:
            self.subjects = subjects  # new: update school subjects
        print(f"Updated school subjects to: {', '.join(self.subjects)}")

    def __repr__(self):
        student_ids = ', '.join(self.students.keys())
        return (
            f"School Name: {self.name}\n"
            f"Address: {self.address}\n"
            f"Subjects Offered: {', '.join(self.subjects)}\n"
            f"Total Students Enrolled: {len(self.students)}\n"
            f"Student IDs: {student_ids}\n"
        )

