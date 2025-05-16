# This module defines the School class, which manages students, employees,
# and subjects.

from student import Student
from employee import Employee, Teacher

class School:
    """Represents a school."""

    def __init__(self, name, address, telephoneNumber, subjects):
        
        if not isinstance(name, str):
            raise TypeError("School name must be a string")
        if not isinstance(address, str):
            raise TypeError("School address must be a string")
        if not isinstance(telephoneNumber, str):
            raise TypeError("School telephone number must be a string")

        self.name = name
        self.address = address
        self.telephoneNumber = telephoneNumber
        self.subjects = subjects if subjects else []
        self.school_year = None  # Added school_year property
        self.students = {}
        self.teachers = {}     # employeeID -> Teacher object
        self.employees = {}  # Track all employees

    #Student methods

    def register_student(self, student):
        """Registers a student in the school"""

        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be registered.")
        if student.studentID in self.students:
            raise ValueError(f"Student with ID {student.studentID} already exists.")
        self.students[student.studentID] = student    
    
    def get_all_students(self):
        """Returns a list of all the students in the school"""

        return list(self.students.values())
    
    def get_student_by_id(self, student_id):
        """ Retrieves a student by their ID"""

        if not isinstance(student_id, str):
            raise TypeError("Student ID must be a string.")
        return self.students.get(student_id)

    def remove_student(self, student_id):
        """Remove a student by their ID"""
        
        if isinstance(student_id, str):
            if student_id not in self.students:
                raise ValueError(f"Student with ID {student_id} not found.")
            student = self.students.pop(student_id)
            print(f"Removed {student.fName} {student.lName} from the school.")
        elif isinstance(student_id, Student):
            if student_id.studentID not in self.students:
                raise ValueError(f"Student with ID {student_id.studentID} not found.")
            del self.students[student_id.studentID]
            print(f"Removed {student_id.fName} {student_id.lName} from the school.")
        else:
            raise TypeError("student_id must be a string or a Student object.")

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


    #List different types of students


    def list_students_by_subject(self, subject):
        """Get a list of students enrolled in a specific subject"""

        if not isinstance(subject, str):
            raise TypeError("Subject must be a string.")

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



    #Employee methods

    def get_all_teachers(self):
        """Returns a list of all teachers in the school"""

        return list(self.teachers.values())

    def get_all_employees(self):
        """Returns a list of all employees in the school"""

        return list(self.employees.values())

    def register_employee(self, employee):
        """Registers a non-teacher employee"""

        if not isinstance(employee, Employee):
            raise TypeError("Only Employee objects can be registered.")
        if employee.employeeID in self.employees:
            raise ValueError(f"Employee with ID {employee.employeeID} already exists.")

        self.employees[employee.employeeID] = employee

    def register_teacher(self, teacher):
        """Registers a teacher, and also adds to employees list"""

        if not isinstance(teacher, Teacher):
            raise TypeError("Only Teacher objects can be registered.")
        if teacher.employeeID in self.employees:
            raise ValueError(f"Employee with ID {teacher.employeeID} already exists.")

        self.teachers[teacher.employeeID] = teacher
        self.employees[teacher.employeeID] = teacher

    def hire_employee(self, employee):
        """Hires an employee for the school"""

        if not isinstance(employee, Employee):
            raise TypeError("Only Employee objects can be hired.")
        if employee.employeeID in self.employees:
            raise ValueError(f"Employee with ID {employee.employeeID} already exists.")

        self.employees[employee.employeeID] = employee
        print(f"Hired {employee.get_name()} ({employee.__class__.__name__})")

    def get_employee_by_id(self, emp_id):
        """Retrieves an employee by their ID"""

        if not isinstance(emp_id, str):
            raise TypeError("Employee ID must be a string.")
        return self.employees.get(emp_id)

    def fire_employee(self, emp_id):
        "Fires an employee from the school"

        if not isinstance(emp_id, str):
            raise TypeError("Employee ID must be a string.")
        if emp_id not in self.employees:
            raise ValueError(f"Employee with ID {emp_id} not found.")

        emp = self.employees.pop(emp_id)
        print(f"Fired {emp.get_name()}")

    def list_employees_by_role(self, role_name):
        """List employees by their role"""

        if not isinstance(role_name, str):
            raise TypeError("Role name must be a string.")
        return [emp for emp in self.employees.values() if emp.__class__.__name__.lower() == role_name.lower()]
    

    #List Employees by type


    def get_average_grade(self, subject):
        """Calculate the average grade across students for a specific subject"""

        if not isinstance(subject, str):
            raise TypeError("Subject must be a string.")

        total = 0
        count = 0
        
        for student in self.students.values():
            if hasattr(student, "subject_grades") and subject in student.subject_grades:
                total += student.subject_grades[subject]
                count += 1

        if count == 0:
            print(f"No grades available for {subject}.")
            return None

        return round(total / count, 2)

    # Updated helper methods for School class
    
    def update_school_name(self, name=None):
        """Update the school's name"""

        if not isinstance(name, str):
            raise TypeError("School name must be a string.")
        self.name = name
        print(f"Updated school name to: {self.name}")
    
    def update_school_address(self, address=None):
        """Update the school's address"""

        if not isinstance(address, str):
            raise TypeError("School address must be a string.")
        self.address = address
        print(f"Updated school address to: {self.address}")
    
    def update_school_year(self, school_year=None):
        """Update the school year"""

        if not isinstance(school_year, str):
            raise TypeError("School year must be a string.")
        self.school_year = school_year
        print(f"Updated school year to: {self.school_year}")
    
    def update_school_telephone(self, telephone=None):
        """Update the school's telephone number"""
        
        if not isinstance(telephone, str):
            raise TypeError("School telephone number must be a string.")
        self.telephone_number = telephone
        print(f"Updated school telephone to: {self.telephone_number}")
    
    def update_school_subjects(self, subjects=None):
        """Update the list of subjects offered by the school"""

        if not isinstance(subjects, list) or not all(isinstance(subject, str) for subject in subjects):
            raise TypeError("Subjects must be a list of strings.")
        self.subjects = subjects
        print(f"Updated school subjects to: {', '.join(self.subjects)}")

    def add_subject(self, subject):
        """Add a new subject to the school's offerings"""
        
        if not isinstance(subject, str):
            raise TypeError("Subject must be a string.")
        if subject in self.subjects:
            raise ValueError(f"{subject} is already offered at this school")
        self.subjects.append(subject)
        print(f"Added {subject} to school subjects")
    
    def remove_subject(self, subject):
        """Remove a subject from the school's offerings"""

        if not isinstance(subject, str):
            raise TypeError("Subject must be a string.")
        if subject not in self.subjects:
            raise ValueError(f"{subject} is not offered at this school")
        self.subjects.remove(subject)
        print(f"Removed {subject} from school subjects")
    
    def __repr__(self):
        """Returns a formatted string representing the School object"""

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

