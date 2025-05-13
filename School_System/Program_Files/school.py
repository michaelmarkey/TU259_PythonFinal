class School:
    def __init__(self, name, address, telephoneNumber, subjects):
        self.name = name
        self.address = address
        self.telephoneNumber = telephoneNumber
        self.subjects = subjects if subjects else []
        self.students = {}
        self.teachers = {}     # employeeID -> Teacher object
        self.school_year = None  # Added school_year property
        self.employees = {}  # New: Track all employees

    #Student methods

    def register_student(self, student):
        # Add student to the school's student list using student ID as the key
        self.students[student.studentID] = student

    def register_teacher(self, teacher):
        """Registers a teacher, and also adds to employees list"""
        self.teachers[teacher.employeeID] = teacher
        self.employees[teacher.employeeID] = teacher

    def register_employee(self, employee):
        """Registers a non-teacher employee"""
        self.employees[employee.employeeID] = employee

    def get_all_students(self):
        # Return a list of all students
        return list(self.students.values())
    
    def get_all_teachers(self):
        return list(self.teachers.values())

    def get_all_employees(self):
        return list(self.employees.values())

    def get_student_by_id(self, student_id):
        # Return a student by their ID
        return self.students.get(student_id)

    def remove_student(self, student_id):
        """Remove a student by their ID"""
        if isinstance(student_id, str):
            # If given a string ID
            if student_id in self.students:
                student = self.students[student_id]
                del self.students[student_id]
                print(f"Removed {student.fName} {student.lName} from the school.")
            else:
                print(f"Student with ID {student_id} not found.")
        else:
            # If given a student object
            key = getattr(student_id, 'studentID', None)
            if key and key in self.students:
                del self.students[key]
                print(f"Removed {student_id.fName} {student_id.lName} from the school.")
            else:
                print(f"Student not found.")

    def find_student_by_id(self, student_id):
        """Find a student by their ID"""
        student = self.students.get(student_id, None)
        if student is None:
            print(f"Student with ID {student_id} not found.")
        return student
    
    def find_students_by_name(self, first_name=None, last_name=None):
        """Find students by first name, last name, or both"""
        results = []
        
        for student in self.students.values():
            # If both first and last name are provided, check both
            if first_name and last_name:
                if student.fName.lower() == first_name.lower() and student.lName.lower() == last_name.lower():
                    results.append(student)
            # If only first name is provided
            elif first_name:
                if student.fName.lower() == first_name.lower():
                    results.append(student)
            # If only last name is provided
            elif last_name:
                if student.lName.lower() == last_name.lower():
                    results.append(student)
        
        return results 

    #Employee methods

    def hire_employee(self, employee):
        self.employees[employee.employeeID] = employee
        print(f"Hired {employee.get_name()} ({employee.__class__.__name__})")

    def get_employee_by_id(self, emp_id):
        return self.employees.get(emp_id)

    def get_all_employees(self):
        return list(self.employees.values())

    def fire_employee(self, emp_id):
        if emp_id in self.employees:
            emp = self.employees.pop(emp_id)
            print(f"Fired {emp.get_name()}")
        else:
            print(f"Employee with ID {emp_id} not found.")

    def list_employees_by_role(self, role_name):
        return [emp for emp in self.employees.values() if emp.__class__.__name__.lower() == role_name.lower()]


    #List different types of students


    def list_students_by_subject(self, subject):
        """Get a list of students enrolled in a specific subject"""
        result = []
        for student in self.students.values():
            if subject in student.subject_grades:  # Check if the subject exists in the subject_grades dictionary
                result.append(f"{student.fName} {student.lName} (ID: {student.studentID})")
        return f"Students doing this subject are: {result}\n"


    def list_students_by_year(self, year):
        """Get a list of students in a specific school year"""
        result = []
        for student in self.students.values():
            if student.schoolYear == str(year):  # Convert year to string for comparison
                result.append(f"{student.fName} {student.lName} (ID: {student.studentID})")
        return f"Students in this year are: {result}\n"
    
    #List Employees by type

    def list_employees_by_role(self, role_name):
        return [emp for emp in self.employees.values() if emp.__class__.__name__.lower() == role_name.lower()]


    def get_average_grade(self, subject):
        """Calculate the average grade for a specific subject"""
        total = 0
        count = 0
        
        if subject == "Mathematics":
            for student in self.students.values():
                if hasattr(student, 'mathGrade'):
                    total += student.mathGrade
                    count += 1
        elif subject == "English":
            for student in self.students.values():
                if hasattr(student, 'englishGrade'):
                    total += student.englishGrade
                    count += 1
        elif subject == "History":
            for student in self.students.values():
                if hasattr(student, 'historyGrade'):
                    total += student.historyGrade
                    count += 1
        else:
            print(f"This subject ({subject}) is not currently supported for grade calculation.")
            return None
        
        if count == 0:
            print(f"No grades available for {subject}.")
            return None
        
        return round(total / count, 2)

    # Updated helper methods for School class
    def update_school_name(self, name=None):
        """Update the school name"""
        if name is not None:
            self.name = name
            print(f"Updated school name to: {self.name}")
    
    def update_school_address(self, address=None):
        """Update the school address"""
        if address is not None:
            self.address = address
            print(f"Updated school address to: {self.address}")
    
    def update_school_year(self, school_year=None):
        """Update the school year"""
        if school_year is not None:
            self.school_year = school_year
            print(f"Updated school year to: {self.school_year}")
    
    def update_school_telephone(self, telephone=None):
        """Update the school telephone number"""
        if telephone is not None:
            self.telephoneNumber = telephone
            print(f"Updated school telephone to: {self.telephoneNumber}")
    
    def update_school_subjects(self, subjects=None):
        """Update the list of subjects offered by the school"""
        if subjects is not None:
            self.subjects = subjects
            print(f"Updated school subjects to: {', '.join(self.subjects)}")

    def add_subject(self, subject):
        """Add a new subject to the school's offerings"""
        if subject not in self.subjects:
            self.subjects.append(subject)
            print(f"Added {subject} to school subjects")
        else:
            print(f"{subject} is already offered at this school")
    
    def remove_subject(self, subject):
        """Remove a subject from the school's offerings"""
        if subject in self.subjects:
            self.subjects.remove(subject)
            print(f"Removed {subject} from school subjects")
        else:
            print(f"{subject} is not offered at this school")
    
    def __repr__(self):
        """String representation of the School object"""
        student_ids = ', '.join(self.students.keys()) if self.students else "None"
        employee_ids = ', '.join(self.employees.keys()) if self.employees else "None"
        return (
            f"School Name: {self.name}\n"
            f"Address: {self.address}\n"
            f"Telephone: {self.telephoneNumber}\n"
            f"School Year: {self.school_year or 'Not set'}\n"
            f"Subjects Offered: {', '.join(self.subjects)}\n"
            f"Total Students Enrolled: {len(self.students)}\n"
            f"Student IDs: {student_ids}\n"
            f"Total Employees: {len(self.employees)}\n"
            f"Employee IDs: {employee_ids}\n"
        )

