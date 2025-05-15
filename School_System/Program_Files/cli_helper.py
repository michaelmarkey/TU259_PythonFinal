import csv
import os
import sys
import getpass
from pathlib import Path
from gui import SchoolApp  # Import SchoolApp here
from kivy.base import runTouchApp  # Import runTouchApp
from typing import Optional, Dict, Any

from student import Student 
from subject import SubjectStudent, create_subject_student
from employee import Teacher, Principal, Medic, Administrator, Counselor
from csv_loader import (
    load_students_from_csv,
    load_math_grades_from_csv,
    load_english_grades_from_csv,
    load_history_grades_from_csv,
    load_employees_from_csv,
    find_student_by_id,
    find_employee_by_id,
)
from school import School
from grade_calculator import calculate_and_update_grades_for_students
import getpass

# === Configuration & Data Files ===
STUDENT_CSV = 'students.csv'
MATH_CSV = 'math_grades.csv'
ENG_CSV = 'english_grades.csv'
HIST_CSV = 'history_grades.csv'
EMPLOYEE_CSV = 'employees.csv'


# === Simple User Store (for demo) ===
USERS = {
    'admin': 'password123',
    # add more usernames/passwords as needed
}

def login() -> bool:
    """Handles user login with 5 attempts."""
    print("=== School Management System Login ===")
    
    max_attempts = 5
    attempts = 0
    
    while attempts < max_attempts:
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        
        if USERS.get(username) == password:
            print("Login successful!\n")
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            
            if remaining > 0:
                print(f"Invalid credentials. {remaining} attempts remaining.")
            else:
                print("Maximum login attempts reached. Exiting.")
                
    return False


def load_data():

    """
    Load students, grades, and employees from CSV files and register them in a School instance.
    """

    base = Path(__file__).parent / "CSV_Files"
    paths = {
        'students': base / STUDENT_CSV,
        'math': base / MATH_CSV,
        'english': base / ENG_CSV,
        'history': base / HIST_CSV,
        'employees': base / EMPLOYEE_CSV,
    }

    school = School(
        name="My School",
        address="123 Main St",
        telephoneNumber="000-000-0000",
        subjects=["Mathematics", "English", "History"]
    )
    
    # Load students from CSV and categorize them
    try:
        students = load_students_from_csv(paths['students'])
        # Register students into school
        for student in students:
            school.register_student(student)
        print(f"Registered {len(school.students)} students.")
    except FileNotFoundError:
        print("Error: Student CSV file not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading students: {e}")
        sys.exit(1)

    # Load employees
    try:
        print(f"Loading employees from: {paths['employees']}")  # Debug: Print path
        employees = load_employees_from_csv(paths['employees'])
        print(f"Loaded {len(employees)} employees from CSV.") # Debug: Print num employees
        for emp in employees:
            print(f"Registering employee: {emp}") # Debug: Print each employee
            if isinstance(emp, Teacher):
                school.register_teacher(emp)
                print(f"Registered as teacher: {emp}")  # Debug: Check if registered as teacher
            else:
                school.register_employee(emp)
                print(f"Registered as employee: {emp}") # Debug: Check if registered as employee
        print(f"Registered {len(school.employees)} employees ({len(school.teachers)} teachers).\n")
    except Exception as e:
        print(f"Error loading employees: {e}")
        print(f"Exception Details: {e.__class__}, {e}") #show exception type
        sys.exit(1)
    


    # Load grades
    try:
        load_math_grades_from_csv(paths['math'], list(school.students.values()))
        load_english_grades_from_csv(paths['english'], list(school.students.values()))
        load_history_grades_from_csv(paths['history'], list(school.students.values()))
        print("Loaded grades.")
    except Exception as e:
        print(f"Error loading grades: {e}")
        sys.exit(1)

    # Calculate final grades for all students to populate subject_grades fully
    calculate_and_update_grades_for_students(list(school.students.values()))
    print("Calculated student grades.")

    return school

#Save into different files?

def save_data_to_csv(school: School):
    """Save students, grades, and employees to CSV files."""
    import csv
    
    base = Path(__file__).parent / "CSV_Files"
    
    # Save students to CSV
    try:
        with open(base / STUDENT_CSV, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['studentID', 'fName', 'mName', 'lName', 'age', 
                         'addressL1', 'addressL2', 'addressL3', 'addressPostCode', 'addressCounty',
                         'schoolYear', 'schoolSubjects', 'nameParGar1', 'contactDetParGar1', 
                         'nameParGar2', 'contactDetParGar2']
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for student in school.get_all_students():
                writer.writerow({
                    'studentID': student.studentID,
                    'fName': student.fName,
                    'mName': student.mName,
                    'lName': student.lName,
                    'age': student.age,
                    'addressL1': student.addressL1,
                    'addressL2': student.addressL2,
                    'addressL3': student.addressL3,
                    'addressPostCode': student.addressPostCode,
                    'addressCounty': student.addressCounty,
                    'schoolYear': student.schoolYear,
                    'schoolSubjects': ','.join(student.schoolSubjects),
                    'nameParGar1': student.nameParGar1,
                    'contactDetParGar1': student.contactDetParGar1,
                    'nameParGar2': student.nameParGar2,
                    'contactDetParGar2': student.contactDetParGar2
                })
        print(f"Saved {len(school.students)} students to {STUDENT_CSV}")
    except Exception as e:
        print(f"Error saving students to CSV: {e}")
    
    # Save grades to CSV files
    try:
        # Math grades
        with open(base / MATH_CSV, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['studentID', 'lastTestScore', 'level', 'classNumber', 'teacher']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for student in school.get_all_students():
                if "Mathematics" in student.subject_grades:
                    writer.writerow({
                        'studentID': student.studentID,
                        'lastTestScore': student.subject_grades.get("Mathematics", 0),
                        'level': 'Standard',  # Default values
                        'classNumber': '101',
                        'teacher': 'Unknown'
                    })
        
        # English grades
        with open(base / ENG_CSV, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['studentID', 'lastTestScore', 'level', 'classNumber', 'teacher']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for student in school.get_all_students():
                if "English" in student.subject_grades:
                    writer.writerow({
                        'studentID': student.studentID,
                        'lastTestScore': student.subject_grades.get("English", 0),
                        'level': 'Standard',  # Default values
                        'classNumber': '102',
                        'teacher': 'Unknown'
                    })
        
        # History grades
        with open(base / HIST_CSV, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['studentID', 'lastTestScore', 'level', 'classNumber', 'teacher']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for student in school.get_all_students():
                if "History" in student.subject_grades:
                    writer.writerow({
                        'studentID': student.studentID,
                        'lastTestScore': student.subject_grades.get("History", 0),
                        'level': 'Standard',  # Default values
                        'classNumber': '103',
                        'teacher': 'Unknown'
                    })
        print(f"Saved grades for subjects to CSV files")
    except Exception as e:
        print(f"Error saving grades to CSV: {e}")
    
    # Save employees to CSV
    try:
        with open(base / EMPLOYEE_CSV, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['employeeID', 'Type', 'fName', 'lName', 'dob', 'address', 'contact_number', 
                         'email', 'start_date', 'Subjects', 'YearsTeaching']
            
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for employee in school.get_all_employees():
                emp_data = {
                    'employeeID': employee.employeeID,
                    'fName': employee.fName,
                    'lName': employee.lName,
                    'dob': employee.dob,
                    'address': employee.address,
                    'contact_number': employee.contact_number,
                    'email': employee.email,
                    'start_date': employee.start_date.strftime("%Y-%m-%d")
                }
                
                # Set type-specific fields
                if isinstance(employee, Teacher):
                    emp_data['Type'] = 'Teacher'
                    emp_data['Subjects'] = ','.join(employee.subjects)
                    emp_data['YearsTeaching'] = employee.years_teaching
                elif isinstance(employee, Principal):
                    emp_data['Type'] = 'Principal'
                elif isinstance(employee, Medic):
                    emp_data['Type'] = 'Medic'
                elif isinstance(employee, Administrator):
                    emp_data['Type'] = 'Administrator'
                elif isinstance(employee, Counselor):
                    emp_data['Type'] = 'Counselor'
            
                writer.writerow(emp_data)
        print(f"Saved {len(school.employees)} employees to {EMPLOYEE_CSV}")
    except Exception as e:
        print(f"Error saving employees to CSV: {e}")

# Needs to be closed? Return something?


def add_student_cli(school: School, student_data: Optional[Dict[str, Any]] = None) -> None:
    """
    Add a new student to the school.
    
    Args:
        school (School): The school instance.
        student_data (dict, optional): Student data. If None, prompts for input.
    """
    if not student_data:
        print("\n--- Add New Student ---")
        student_data = {
            "studentID": input("Student ID: "),
            "fName": input("First Name: "),
            "mName": input("Middle Name: "),
            "lName": input("Last Name: "),
            "age": int(input("Age: ")),
            "addressL1": input("Address Line 1: "),
            "addressL2": input("Address Line 2: "),
            "addressL3": input("Address Line 3: "),
            "addressPostCode": input("Postcode: "),
            "addressCounty": input("County: "),
            "schoolYear": input("School Year: "),
            "schoolSubjects": [
                subject.strip() for subject in input("Subjects (comma-separated): ").split(",")
            ],
            "nameParGar1": input("Guardian 1 Name: "),
            "contactDetParGar1": int(input("Guardian 1 Contact: ")),
            "nameParGar2": input("Guardian 2 Name: "),
            "contactDetParGar2": int(input("Guardian 2 Contact: ")),
        }

    try:
        new_student = Student(**student_data)
        school.register_student(new_student)
        print(f"Student {new_student.fName} {new_student.lName} added successfully.")
    except Exception as e:
        print(f"Error adding student: {e}")


def remove_student_cli(school: School, student_id: str = None) -> None:
    """
    Remove a student from the school.
    
    Args:
        school (School): The school instance.
        student_id (str, optional): The ID of the student to remove. If None, prompts for input.
    """
    if not student_id:
        student_id = input("Enter Student ID to remove: ")
    try:
        school.remove_student(student_id)
        print(f"Student with ID {student_id} removed successfully.")
    except Exception as e:
        print(f"Error removing student: {e}")


def view_student_cli(school: School, student_id: str = None) -> str:
    """
    View a student's details.
    
    Args:
        school (School): The school instance.
        student_id (str, optional): The ID of the student to view. If None, prompts for input.
    
    Returns:
        str: A formatted string containing the student's details.
    """
    if not student_id:
        student_id = input("Enter Student ID to view: ")
    student = school.get_student_by_id(student_id)
    if student:
        # Calculate the average grade
        avg_grade = student.calculate_overall_average()
        result = student.get_full_student_data()
        result += "\nGrades:\n"
        for subject, grade in student.subject_grades.items():
            result += f"{subject}: {grade}\n"
        
        if avg_grade is not None:
            result += f"\nOverall Average Grade: {avg_grade:.2f}\n"
        
        print(result)
        return result
    else:
        print(f"Student with ID {student_id} not found.")
        return f"Student with ID {student_id} not found."



def update_student_cli(school: School, student_id: str = None, updates: Dict[str, Any] = None) -> None:
    """
    Update a student's details.
    
    Args:
        school (School): The school instance.
        student_id (str, optional): The ID of the student to update. If None, prompts for input.
        updates (dict, optional): A dictionary of updates. If None, prompts for input.
    """

    if not student_id:
        student_id = input("Enter Student ID to update: ")
    student = school.get_student_by_id(student_id)

    if not student:
        print(f"Student with ID {student_id} not found.")
        return

    if not updates:
        print("\n--- Update Student Details ---")
        updates = {}
        for field in [
            "fName",
            "mName",
            "lName",
            "age",
            "addressL1",
            "addressL2",
            "addressL3",
            "addressPostCode",
            "addressCounty",
            "schoolYear",
            "schoolSubjects",
            "nameParGar1",
            "contactDetParGar1",
            "nameParGar2",
            "contactDetParGar2",
        ]:
            value = input(f"Enter new {field} (or leave blank to keep current): ")
            if value:
                updates[field] = value
        if updates.get("schoolSubjects"):
            updates["schoolSubjects"] = [
                subject.strip() for subject in updates["schoolSubjects"].split(",")
            ]
        if updates.get("age"):
            updates["age"] = int(updates["age"])
        if updates.get("contactDetParGar1"):
            updates["contactDetParGar1"] = int(updates["contactDetParGar1"])
        if updates.get("contactDetParGar2"):
            updates["contactDetParGar2"] = int(updates["contactDetParGar2"])

    for key, value in updates.items():
        setattr(student, key, value)
    print("Student details updated successfully.")

def update_student_grades_cli(school: School) -> None:
    """Update a student's grades for one or more subjects."""
    student_id = input("Enter Student ID to update grades: ")
    student = school.get_student_by_id(student_id)
    
    if not student:
        print(f"Student with ID {student_id} not found.")
        return
    
    print(f"Updating grades for {student.fName} {student.lName}")
    print("Available subjects:", ", ".join(school.subjects))
    
    subject = input("Enter subject name to update (Mathematics, English, History): ")
    if subject not in school.subjects:
        print(f"Invalid subject name. Must be one of: {', '.join(school.subjects)}")
        return
    
    try:
        grade = float(input(f"Enter new grade for {subject}: "))
        student.add_grade(subject, grade)
        print(f"Updated {subject} grade to {grade} for {student.fName} {student.lName}")
    except ValueError:
        print("Invalid grade value. Please enter a numeric value.")

def delete_student_cli(school: School, student_id: str = None) -> None:
    """
    Delete a student from the school (alias for remove for clarity).
    
    Args:
        school (School): The school instance.
        student_id (str, optional): The ID of the student to delete. If None, prompts for input.
    """
    remove_student_cli(school, student_id)


def search_students_cli(school: School) -> None:
    """Search for students by name, year, or subject"""
    print("\n--- Search Students ---")
    print("1. Search by Name")
    print("2. Search by School Year")
    print("3. Search by Subject")
    
    search_option = input("Select search option: ")
    
    if search_option == "1":
        name = input("Enter name (first or last): ").lower()
        matches = []
        
        for student in school.get_all_students():
            if name in student.fName.lower() or name in student.lName.lower():
                matches.append(student)
    
    elif search_option == "2":
        year = input("Enter school year: ")
        matches = []
        
        for student in school.get_all_students():
            if student.is_in_year(year):
                matches.append(student)
    
    elif search_option == "3":
        subject = input("Enter subject: ")
        matches = []
        
        for student in school.get_all_students():
            if student.is_enrolled_in(subject):
                matches.append(student)
    
    else:
        print("Invalid option")
        return
    
    # Display results
    if matches:
        print(f"\nFound {len(matches)} matches:")
        for student in matches:
            print(f"ID: {student.studentID}, Name: {student.fName} {student.lName}, Year: {student.schoolYear}")
    else:
        print("No matches found")





# === Employee Management Functions ===

def add_employee_cli(school: School) -> None:
    """Add a new employee to the school."""
    print("\n--- Add New Employee ---")
    
    print("Select employee type:")
    print("1. Teacher")
    print("2. Principal")
    print("3. Medic")
    print("4. Administrator")
    print("5. Counselor")
    
    emp_type_choice = input("Option: ")
    
    # Collect common fields
    employee_data = {
        "employeeID": input("Employee ID: "),
        "fName": input("First Name: "),
        "lName": input("Last Name: "),
        "dob": input("Date of Birth (YYYY-MM-DD): "),
        "address": input("Address: "),
        "contact_number": input("Contact Number: "),
        "email": input("Email: "),
        "start_date": input("Start Date (YYYY-MM-DD): ")
    }
    
    try:
        if emp_type_choice == "1":  # Teacher
            subjects = [s.strip() for s in input("Subjects (comma-separated): ").split(",") if s.strip()]
            years_teaching = int(input("Years of Teaching Experience: "))
            
            employee = Teacher(
                **employee_data,
                subjects=subjects,
                years_teaching=years_teaching
            )
            school.register_teacher(employee)
            
        elif emp_type_choice == "2":  # Principal
            office_number = input("Office Number: ")
            years_as_principal = int(input("Years as Principal: "))
            departments = [d.strip() for d in input("Departments (comma-separated): ").split(",") if d.strip()]
            
            employee = Principal(
                **employee_data,
                office_number=office_number,
                years_as_principal=years_as_principal,
                departments=departments
            )
            school.register_employee(employee)
            
        elif emp_type_choice == "3":  # Medic
            license_number = input("License Number: ")
            office_location = input("Office Location: ")
            
            employee = Medic(
                **employee_data,
                license_number=license_number,
                office_location=office_location
            )
            school.register_employee(employee)
            
        elif emp_type_choice == "4":  # Administrator
            department = input("Department: ")
            office_hours = input("Office Hours: ")
            responsibilities = [r.strip() for r in input("Responsibilities (comma-separated): ").split(",") if r.strip()]
            
            employee = Administrator(
                **employee_data,
                department=department,
                office_hours=office_hours,
                responsibilities=responsibilities
            )
            school.register_employee(employee)
            
        elif emp_type_choice == "5":  # Counselor
            cert_id = input("Certification ID: ")
            specializations = [s.strip() for s in input("Specializations (comma-separated): ").split(",") if s.strip()]
            
            employee = Counselor(
                **employee_data,
                cert_id=cert_id,
                specializations=specializations
            )
            school.register_employee(employee)
            
        else:
            print("Invalid employee type")
            return
            
        print(f"Employee {employee.fName} {employee.lName} added successfully.")
    except Exception as e:
        print(f"Error adding employee: {e}")


def view_employee_cli(school: School) -> None:
    """View an employee's details."""
    employee_id = input("Enter Employee ID to view: ")
    employee = find_employee_by_id(employee_id, school.get_all_employees())
    
    if not employee:
        print(f"Employee with ID {employee_id} not found.")
        return
    
    # Display basic info for all employees
    print(f"\nEmployee ID: {employee.employeeID}")
    print(f"Name: {employee.get_name()}")
    print(f"Contact: {employee.get_contact_info()}")
    print(f"Years of Service: {employee.get_years_of_service()}")
    
    # Display specific info based on employee type
    if isinstance(employee, Teacher):
        print(f"Type: Teacher")
        print(f"Subjects: {', '.join(employee.subjects)}")
        print(f"Years Teaching: {employee.years_teaching}")
    
    elif isinstance(employee, Principal):
        print(f"Type: Principal")
        print(f"Office Number: {employee.office_number}")
        print(f"Years as Principal: {employee.years_as_principal}")
        print(f"Departments: {', '.join(employee.departments)}")
    
    elif isinstance(employee, Medic):
        print(f"Type: Medic")
        print(f"License Number: {employee.license_number}")
        print(f"Office Location: {employee.office_location}")
    
    elif isinstance(employee, Administrator):
        print(f"Type: Administrator")
        print(f"Department: {employee.department}")
        print(f"Office Hours: {employee.office_hours}")
        print(f"Responsibilities: {', '.join(employee.responsibilities)}")
    
    elif isinstance(employee, Counselor):
        print(f"Type: Counselor")
        print(f"Certification ID: {employee.cert_id}")
        print(f"Specializations: {', '.join(employee.specializations)}")


def update_employee_cli(school: School) -> None:
    """Update an employee's details."""
    employee_id = input("Enter Employee ID to update: ")
    employees = school.get_all_employees()
    employee = find_employee_by_id(employee_id, employees)
    
    if not employee:
        print(f"Employee with ID {employee_id} not found.")
        return
    
    print(f"Updating details for {employee.get_name()}")
    
    # Update common fields
    common_fields = {
        "fName": "First Name",
        "lName": "Last Name",
        "address": "Address",
        "contact_number": "Contact Number",
        "email": "Email"
    }
    
    updates = {}
    for field, display_name in common_fields.items():
        value = input(f"Enter new {display_name} (or leave blank to keep current): ")
        if value:
            updates[field] = value
    
    # Update specific fields based on employee type
    if isinstance(employee, Teacher):
        subjects = input("Enter new subjects (comma-separated, or leave blank to keep current): ")
        if subjects:
            employee.subjects = [s.strip() for s in subjects.split(",") if s.strip()]
            
        years_teaching = input("Enter new years of teaching experience (or leave blank to keep current): ")
        if years_teaching:
            employee.years_teaching = int(years_teaching)
    
    elif isinstance(employee, Principal):
        office_number = input("Enter new office number (or leave blank to keep current): ")
        if office_number:
            employee.office_number = office_number
            
        years_as_principal = input("Enter new years as principal (or leave blank to keep current): ")
        if years_as_principal:
            employee.years_as_principal = int(years_as_principal)
    
    elif isinstance(employee, Medic):
        license_number = input("Enter new license number (or leave blank to keep current): ")
        if license_number:
            employee.license_number = license_number
            
        office_location = input("Enter new office location (or leave blank to keep current): ")
        if office_location:
            employee.office_location = office_location
    
    elif isinstance(employee, Administrator):
        department = input("Enter new department (or leave blank to keep current): ")
        if department:
            employee.department = department
            
        office_hours = input("Enter new office hours (or leave blank to keep current): ")
        if office_hours:
            employee.office_hours = office_hours
            
        responsibilities = input("Enter new responsibilities (comma-separated, or leave blank to keep current): ")
        if responsibilities:
            employee.responsibilities = [r.strip() for r in responsibilities.split(",") if r.strip()]
    
    elif isinstance(employee, Counselor):
        cert_id = input("Enter new certification ID (or leave blank to keep current): ")
        if cert_id:
            employee.cert_id = cert_id
            
        specializations = input("Enter new specializations (comma-separated, or leave blank to keep current): ")
        if specializations:
            employee.specializations = [s.strip() for s in specializations.split(",") if s.strip()]
    
    # Apply common updates
    for field, value in updates.items():
        setattr(employee, field, value)
    
    print("Employee details updated successfully.")


def remove_employee_cli(school: School) -> None:
    """Remove an employee from the school."""
    employee_id = input("Enter Employee ID to remove: ")
    
    # Check if the employee exists first
    employee = None
    for emp in school.get_all_employees():
        if emp.employeeID == employee_id:
            employee = emp
            break
    
    if not employee:
        print(f"Employee with ID {employee_id} not found.")
        return
    
    try:
        if isinstance(employee, Teacher):
            school.teachers = {k: v for k, v in school.teachers.items() if v.employeeID != employee_id}
        
        # Remove from employees dictionary
        school.employees = {k: v for k, v in school.employees.items() if v.employeeID != employee_id}
        
        print(f"Employee with ID {employee_id} removed successfully.")
    except Exception as e:
        print(f"Error removing employee: {e}")


#Summary functions, used in gui.py

def print_report_cli(school: School) -> str:
    """
    Generate a term report for all students.
    
    Args:
        school (School): The school instance.
    
    Returns:
        str: A formatted string containing the term report.
    """
    report = "=== Term Report ===\n"
    for student in school.get_all_students():
        report += repr(student) + "\n"  # Assuming Student has a detailed __repr__
    return report


def summary_students_cli(school: School, return_summary: bool = False) -> Optional[str]:
    """
    Summarize student information.
    
    Args:
        school (School): The school instance.
        return_summary (bool, optional): If True, returns the summary string. 
                                         If False, prints the summary to the console.
    
    Returns:
        Optional[str]: A formatted string containing the student summary if `return_summary` is True, 
                     None otherwise.
    """

    summary = "=== Student Summary ===\n"
    summary += f"Total Students: {len(school.students)}\n\n"
    for student in school.get_all_students():
        summary += f"{student.studentID}: {student.fName} {student.lName}, Year {student.schoolYear}\n"
    if return_summary:
        return summary
    else:
        print(summary)
        return None

def summary_school_cli(school: School, return_summary: bool = False) -> Optional[str]:
    """
    Summarize school information.
    
    Args:
        school (School): The school instance.
        return_summary (bool, optional): If True, returns the summary string. 
                                         If False, prints the summary to the console.
    
    Returns:
        Optional[str]: A formatted string containing the school summary if `return_summary` is True, 
                     None otherwise.
    """
    summary = "=== School Summary ===\n"
    summary += f"School Name: {school.name}\n"
    summary += f"Address: {school.address}\n"
    summary += f"Telephone Number: {school.telephoneNumber}\n"
    summary += f"Total Students: {len(school.students)}\n"
    summary += f"Total Employees: {len(school.employees)} ({len(school.teachers)} teachers)\n"
    summary += f"Subjects Offered: {', '.join(school.subjects)}\n"
    if return_summary:
        return summary
    else:
        print(summary)
        return None

def summary_employees_cli(school: School, return_summary: bool = False) -> Optional[str]:
    """
    Summarize employee information.
    
    Args:
        school (School): The school instance.
        return_summary (bool, optional): If True, returns the summary string. 
                                         If False, prints the summary to the console.
    
    Returns:
        Optional[str]: A formatted string containing the employee summary if `return_summary` is True, 
                     None otherwise.
    """

    summary = "=== Employee Summary ===\n"
    summary += f"Total Employees: {len(school.employees)}\n\n"
    for emp in school.get_all_employees():
        summary += f"{emp.employeeID}: {emp.get_name()} ({emp.__class__.__name__})"
        if isinstance(emp, Teacher):
            summary += f" | Subjects: {', '.join(emp.subjects)}"
        else:
            years = emp.get_years_of_service()
            info = f" | Years of Service: {years}"
            summary += info
        summary += "\n"

    if return_summary:
        return summary
    else:
        print(summary)
        return None

def crud_menu(school: School):
    """Main CLI loop for CRUD operations with GUI launch option."""
    while True:
        print("\n=== School Management System (CRUD & GUI) ===")
        print("1. Student Management")
        print("2. Employee Management")
        print("3. Save Data to CSV")
        print("4. Launch GUI (Reports & Summaries)")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            student_crud_menu(school)
        elif choice == "2":
            employee_crud_menu(school)
        elif choice == "3":
            save_data_to_csv(school)
        elif choice == "4":
            try:
                from gui import SchoolApp
                from kivy.core.window import Window
                Window.size = (800, 600) # Set initial window size (optional)
                app = SchoolApp(school=school)
                app.run()
                print("\nReturning to CLI...") # Message after GUI closes
            except ImportError:
                print("GUI functionality not available. Please ensure the 'gui.py' file and Kivy are installed.")
            except Exception as e:
                print(f"An error occurred while launching the GUI: {e}")
        elif choice == "5":
            print("Exiting School Management System.")
            break
        else:
            print("Invalid choice. Please try again.")



def student_crud_menu(school: School):
    """Student CRUD submenu."""
    while True:
        print("\n=== Student Management (CRUD) ===")
        print("1. Add Student")
        print("2. View Student Details")
        print("3. Update Student Details")
        print("4. Remove Student")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student_cli(school)
        elif choice == "2":
            view_student_cli(school)
        elif choice == "3":
            update_student_cli(school)
        elif choice == "4":
            remove_student_cli(school)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def employee_crud_menu(school: School):
    """Employee CRUD submenu."""
    while True:
        print("\n=== Employee Management (CRUD) ===")
        print("1. Add Employee")
        print("2. View Employee Details")
        print("3. Update Employee Details")
        print("4. Remove Employee")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee_cli(school)
        elif choice == "2":
            view_employee_cli(school)
        elif choice == "3":
            update_employee_cli(school)
        elif choice == "4":
            remove_employee_cli(school)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


#Incomplete function here
def main():
    if not login():
        sys.exit(1)

    school = load_data()  # Load data first

    while True:
        print("\nSchool Management System")
        print("1. List Students")
        print("2. Add Student")
        print("3. ... (other CLI options)")
        print("4. Launch GUI")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            # ... your CLI logic for listing students ...
            pass
        elif choice == '2':
            # ... your CLI logic for adding students ...
            pass
        elif choice == '3':
            # ... other CLI options ...
            pass
        elif choice == '4':
            print("Launching GUI...")
            #  --- DEBUGGING ---
            print("--- Employee Data Before GUI Launch ---")
            if school.employees:
                print(f"Number of employees: {len(school.employees)}")
                for emp in school.employees:
                    print(f"  - {emp.fName} {emp.lName} (ID: {emp.employeeID})")
            else:
                print("No employees in school.employees!")
            #  --- END DEBUGGING ---
            app = SchoolApp(school=school)
            runTouchApp()
            break
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

#  This ensures main() only runs when the script is executed directly
if __name__ == "__main__":
    main()





# def start_gui_from_cli(school_data):
#     """Starts the graphical user interface for reports/summaries."""
#     SchoolApp.school_data_from_cli = school_data  # Pass data to GUI (static variable)
#     SchoolApp().run()

# Updated main menu to include summaries
# def print_menu():
#     print("=== Main Menu ===")
#     print("1. Add Student")
#     print("2. Remove Student")
#     print("3. View Student")
#     print("4. Update Student")
#     print("5. Delete Student")
#     print("6. View Graphical Reports/Summaries")  # Changed from Print Term Report
#     print("0. Exit")


# # Main entrypoint for both direct run and import
# def main(school):  # main() now receives the school object
#     if not login():
#         sys.exit(1)
#     # school = load_data()  # Removed: Data is loaded in main.py
#     while True:
#         print_menu()
#         c = input("Option: ").strip()
#         if c == '1':
#             add_student_cli(school)
#         elif c == '2':
#             remove_student_cli(school)
#         elif c == '3':
#             view_student_cli(school)
#         elif c == '4':
#             update_student_cli(school)
#         elif c == '5':
#             delete_student_cli(school)
#         elif c == '6':
#             print("Launching Graphical Reports/Summaries...")
#             start_gui_from_cli(school)
#             print("Returning to CLI.")
#         elif c == '0':
#             print("Goodbye!")
#             break
#         else:
#             print("⚠️ Invalid option.")

# if __name__ == '__main__':
#     main(load_data())  
    
    
    # Call main() with loaded data when run directly

#     Query successful

# OK, here's a review and update of your cli_helper.py and gui.py files to better integrate all the functionalities and ensure they're GUI-friendly.

# I. Updated cli_helper.py
# Python

# import sys
# import getpass
# from pathlib import Path
# from typing import List, Dict, Any, Optional

# from student import Student
# from subject import SubjectStudent, create_subject_student
# from employee import Teacher, Principal, Medic, Administrator, Counselor
# from csv_loader import (
#     load_students_from_csv,
#     load_math_grades_from_csv,
#     load_english_grades_from_csv,
#     load_history_grades_from_csv,
#     load_employees_from_csv,
# )
# from school import School
# from grade_calculator import calculate_and_update_grades_for_students


# # === Configuration & Data Files ===
# STUDENT_CSV = "students.csv"
# MATH_CSV = "math_grades.csv"
# ENG_CSV = "english_grades.csv"
# HIST_CSV = "history_grades.csv"
# EMPLOYEE_CSV = "employees.csv"


# # === Simple User Store (for demo) ===
# USERS = {
#     "admin": "password123",
#     # add more usernames/passwords as needed
# }


# def login() -> bool:
#     """Handles user login."""
#     print("=== School Management System Login ===")
#     username = input("Username: ")
#     password = getpass.getpass("Password: ")
#     if USERS.get(username) == password:
#         print("Login successful!\n")
#         return True
#     else:
#         print("Invalid credentials. Exiting.")
#         return False


# def load_data() -> School:
#     """
#     Load students, grades, and employees from CSV files and register them in a School instance.
#     """

#     base = Path(__file__).parent / "CSV_Files"
#     paths = {
#         "students": base / STUDENT_CSV,
#         "math": base / MATH_CSV,
#         "english": base / ENG_CSV,
#         "history": base / HIST_CSV,
#         "employees": base / EMPLOYEE_CSV,
#     }

#     school = School(
#         name="My School",
#         address="123 Main St",
#         telephoneNumber="000-000-0000",
#         subjects=["Mathematics", "English", "History"],
#     )

#     # Load students from CSV
#     try:
#         students = load_students_from_csv(paths["students"])
#         for student in students:
#             school.register_student(student)
#         print(f"Registered {len(school.students)} students.")
#     except FileNotFoundError:
#         print("Error: Student CSV file not found.")
#         sys.exit(1)
#     except Exception as e:
#         print(f"Error loading students: {e}")
#         sys.exit(1)

#     # Load employees
#     try:
#         employees = load_employees_from_csv(paths["employees"])
#         for emp in employees:
#             if isinstance(emp, Teacher):
#                 school.register_teacher(emp)
#             else:
#                 school.register_employee(emp)
#         print(f"Registered {len(school.employees)} employees ({len(school.teachers)} teachers).\n")
#     except Exception as e:
#         print(f"Error loading employees: {e}")
#         sys.exit(1)

#     # Load grades
#     try:
#         if paths["math"].exists():
#             load_math_grades_from_csv(paths["math"], list(school.students.values()))
#         if paths["english"].exists():
#             load_english_grades_from_csv(paths["english"], list(school.students.values()))
#         if paths["history"].exists():
#             load_history_grades_from_csv(paths["history"], list(school.students.values()))
#     except Exception as e:
#         print(f"Error loading grades: {e}")
#         sys.exit(1)

#     calculate_and_update_grades_for_students(list(school.students.values()))
#     return school


# def save_data(school: School) -> None:
#     """Save students, grades, and employees to CSV."""
#     # Implementation needed (left as placeholder)
#     print("Save data functionality not implemented yet.")


# def add_student_cli(school: School, student_data: Optional[Dict[str, Any]] = None) -> None:
#     """
#     Add a new student to the school.
    
#     Args:
#         school (School): The school instance.
#         student_data (dict, optional): Student data. If None, prompts for input.
#     """

#     if not student_data:
#         print("\n--- Add New Student ---")
#         student_data = {
#             "studentID": input("Student ID: "),
#             "fName": input("First Name: "),
#             "mName": input("Middle Name: "),
#             "lName": input("Last Name: "),
#             "age": int(input("Age: ")),
#             "addressL1": input("Address Line 1: "),
#             "addressL2": input("Address Line 2: "),
#             "addressL3": input("Address Line 3: "),
#             "addressPostCode": input("Postcode: "),
#             "addressCounty": input("County: "),
#             "schoolYear": input("School Year: "),
#             "schoolSubjects": [
#                 subject.strip() for subject in input("Subjects (comma-separated): ").split(",")
#             ],
#             "nameParGar1": input("Guardian 1 Name: "),
#             "contactDetParGar1": int(input("Guardian 1 Contact: ")),
#             "nameParGar2": input("Guardian 2 Name: "),
#             "contactDetParGar2": int(input("Guardian 2 Contact: ")),
#         }

#     try:
#         new_student = Student(**student_data)
#         school.register_student(new_student)
#         print(f"Student {new_student.fName} {new_student.lName} added successfully.")
#     except Exception as e:
#         print(f"Error adding student: {e}")


# def remove_student_cli(school: School, student_id: str = None) -> None:
#     """
#     Remove a student from the school.
    
#     Args:
#         school (School): The school instance.
#         student_id (str, optional): The ID of the student to remove. If None, prompts for input.
#     """
#     if not student_id:
#         student_id = input("Enter Student ID to remove: ")
#     try:
#         school.remove_student(student_id)
#     except Exception as e:
#         print(f"Error removing student: {e}")


# def view_student_cli(school: School, student_id: str = None) -> str:
#     """
#     View a student's details.
    
#     Args:
#         school (School): The school instance.
#         student_id (str, optional): The ID of the student to view. If None, prompts for input.
    
#     Returns:
#         str: A formatted string containing the student's details.
#     """

#     if not student_id:
#         student_id = input("Enter Student ID to view: ")
#     student = school.get_student_by_id(student_id)
#     if student:
#         return repr(student)  # Using the __repr__ method for detailed output
#     else:
#         return f"Student with ID {student_id} not found."


# def update_student_cli(school: School, student_id: str = None, updates: Dict[str, Any] = None) -> None:
#     """
#     Update a student's details.
    
#     Args:
#         school (School): The school instance.
#         student_id (str, optional): The ID of the student to update. If None, prompts for input.
#         updates (dict, optional): A dictionary of updates. If None, prompts for input.
#     """

#     if not student_id:
#         student_id = input("Enter Student ID to update: ")
#     student = school.get_student_by_id(student_id)

#     if not student:
#         print(f"Student with ID {student_id} not found.")
#         return

#     if not updates:
#         print("\n--- Update Student Details ---")
#         updates = {}
#         for field in [
#             "fName",
#             "mName",
#             "lName",
#             "age",
#             "addressL1",
#             "addressL2",
#             "addressL3",
#             "addressPostCode",
#             "addressCounty",
#             "schoolYear",
#             "schoolSubjects",
#             "nameParGar1",
#             "contactDetParGar1",
#             "nameParGar2",
#             "contactDetParGar2",
#         ]:
#             value = input(f"Enter new {field} (or leave blank to keep current): ")
#             if value:
#                 updates[field] = value
#         if updates.get("schoolSubjects"):
#             updates["schoolSubjects"] = [
#                 subject.strip() for subject in updates["schoolSubjects"].split(",")
#             ]
#         if updates.get("age"):
#             updates["age"] = int(updates["age"])
#         if updates.get("contactDetParGar1"):
#             updates["contactDetParGar1"] = int(updates["contactDetParGar1"])
#         if updates.get("contactDetParGar2"):
#             updates["contactDetParGar2"] = int(updates["contactDetParGar2"])

#     for key, value in updates.items():
#         setattr(student, key, value)
#     print("Student details updated successfully.")


# def delete_student_cli(school: School, student_id: str = None) -> None:
#     """
#     Delete a student from the school (alias for remove for clarity).
    
#     Args:
#         school (School): The school instance.
#         student_id (str, optional): The ID of the student to delete. If None, prompts for input.
#     """
#     remove_student_cli(school, student_id)







# def summary_school_cli(school: School, return_summary: bool = False) -> Optional[str]:
#     """
#     Summarize school information.
    
#     Args:
#         school (School): The school instance.
#         return_summary (bool, optional): If True, returns the summary string. 
#                                          If False, prints the summary to the console.
    
#     Returns:
#         Optional[str]: A formatted string containing the school summary if `return_summary` is True, 
#                      None otherwise.
#     """
#     summary = "=== School Summary ===\n"
#     summary += f"School Name: {school.name}\n"
#     summary += f"Address: {school.address}\n"
#     summary += f"Telephone Number: {school.telephoneNumber}\n"
#     summary += f"Total Students: {len(school.students)}\n"
#     summary += f"Total Employees: {len(school.employees)} ({len(school.teachers)} teachers)\n"
#     summary += f"Subjects Offered: {', '.join(school.subjects)}\n"
#     if return_summary:
#         return summary
#     else:
#         print(summary)
#         return None






# # Updated main menu to include summaries
# def print_menu():
#     print("=== Main Menu ===")
#     print("1. Add Student")
#     print("2. Remove Student")
#     print("3. View Student")
#     print("4. Update Student")
#     print("5. Delete Student")
#     print("6. Print Term Report")
#     print("7. Student Summary")
#     print("8. School Summary")
#     print("9. Employee Summary")
#     print("0. Exit")


# # Main entrypoint for both direct run and import
# def main():
#     if not login():
#         sys.exit(1)
#     school = load_data()
#     while True:
#         print_menu()
#         c = input("Option: ").strip()
#         if c == "1":
#             add_student_cli(school)
#         elif c == "2":
#             remove_student_cli(school)
#         elif c == "3":
#             print(view_student_cli(school))
#         elif c == "4":
#             update_student_cli(school)
#         elif c == "5":
#             delete_student_cli(school)
#         elif c == "6":
#             print(print_report_cli(school))
#         elif c == "7":
#             summary_students_cli(school)
#         elif c == "8":
#             summary_school_cli(school)
#         elif c == "9":
#             summary_employees_cli(school)
#         elif c == "0":
#             break
#         else:
#             print("Invalid option. Try again.")


# if __name__ == "__main__":
#     main()


