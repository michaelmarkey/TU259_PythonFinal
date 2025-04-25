from student import Student

class School:
    def __init__(self, name, address, school_year, subjects):
        self.name = name
        self.address = address
        self.school_year = school_year
        self.subjects = subjects
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
            # Check if 'schoolSubjects' is present in student object
            if 'schoolSubjects' in student.__dict__ and subject in student.schoolSubjects:
                result.append(f"{student.fName} {student.lName}")
        return result

    def get_average_grade(self, subject):
        total = 0
        count = 0

        if subject not in self.subjects:
            print(f"This subject ({subject}) is not offered at the school.")
            return None

        for student in self.students.values():
            # For each subject, try to pull the corresponding attribute; if it's missing, skip that student
            if subject == "Mathematics" and "Mathematics" in student.schoolSubjects:
                try:
                    grade = student.finalMathematicsGrade
                    total += grade
                    count += 1
                except AttributeError:
                    continue
            elif subject == "English" and "English" in student.schoolSubjects:
                try:
                    grade = student.finalEnglishGrade
                    total += grade
                    count += 1
                except AttributeError:
                    continue
            elif subject == "History" and "History" in student.schoolSubjects:
                try:
                    grade = student.finalHistoryGrade
                    total += grade
                    count += 1
                except AttributeError:
                    continue
            else:
                print("This subject is not given at the school")  # Unknown subject: you could raise an error or return None here
                return None

            

        # Compute average if we have any grades, otherwise None
        return round(total / count, 2) if count > 0 else None

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
        return (
            f"School Name: {self.name}\n"
            f"Address: {self.address}\n"
            f"Subjects Offered: {', '.join(self.subjects)}\n"
            f"Total Students Enrolled: {len(self.students)}"
        )

# Add your CRUD helpers for updating individual student attributes in a similar manner
# You may need to wire up these helpers into the CLI process based on user input.
