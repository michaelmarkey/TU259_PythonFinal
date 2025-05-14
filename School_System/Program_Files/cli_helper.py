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
)
from school import School
from grade_calculator import calculate_and_update_grades_for_students


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
    """Handles user login."""
    print("=== School Management System Login ===")
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    if USERS.get(username) == password:
        print("Login successful!\n")
        return True
    else:
        print("Invalid credentials. Exiting.")
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
        employees = load_employees_from_csv(paths['employees'])
        for emp in employees:
            if isinstance(emp, Teacher):
                school.register_teacher(emp)
            else:
                school.register_employee(emp)
        print(f"Registered {len(school.employees)} employees ({len(school.teachers)} teachers).\n")
    except Exception as e:
        print(f"Error loading employees: {e}")
        sys.exit(1)
    


    # Load grades
    try:
        load_math_grades_from_csv(paths['math'], list(school.students.values()))
        load_english_grades_from_csv(paths['english'], list(school.students.values()))
        load_history_grades_from_csv(paths['history'], list(school.students.values()))
    except Exception as e:
        print(f"Error loading grades: {e}")
        sys.exit(1)

    # Calculate final grades for all students to populate subject_grades fully
    calculate_and_update_grades_for_students(list(school.students.values()))

    return school


# def save_data(school):
#     """Save students, grades, and employees to CSV."""
#     try:
#         save_students_to_csv(STUDENT_CSV, school.students.values())
#         save_grades_to_csv(MATH_CSV, school.students.values(), 'Mathematics')
#         save_grades_to_csv(ENG_CSV, school.students.values(), 'English')
#         save_grades_to_csv(HIST_CSV, school.students.values(), 'History')
#         # TODO: Implement saving employees
#         print("Data saved successfully.\n")
#     except Exception as e:
#         print(f"Error saving data: {e}")
#         sys.exit(1)


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
        return repr(student)  # Using the __repr__ method for detailed output
    else:
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


def delete_student_cli(school: School, student_id: str = None) -> None:
    """
    Delete a student from the school (alias for remove for clarity).
    
    Args:
        school (School): The school instance.
        student_id (str, optional): The ID of the student to delete. If None, prompts for input.
    """
    remove_student_cli(school, student_id)


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


# New summary functions
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

def start_gui_from_cli(school_data):
    """Starts the graphical user interface for reports/summaries."""
    SchoolApp.school_data_from_cli = school_data  # Pass data to GUI (static variable)
    SchoolApp().run()

# Updated main menu to include summaries
def print_menu():
    print("=== Main Menu ===")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. View Graphical Reports/Summaries")  # Changed from Print Term Report
    print("0. Exit")


# Main entrypoint for both direct run and import
def main(school):  # main() now receives the school object
    if not login():
        sys.exit(1)
    # school = load_data()  # Removed: Data is loaded in main.py
    while True:
        print_menu()
        c = input("Option: ").strip()
        if c == '1':
            add_student_cli(school)
        elif c == '2':
            remove_student_cli(school)
        elif c == '3':
            view_student_cli(school)
        elif c == '4':
            update_student_cli(school)
        elif c == '5':
            delete_student_cli(school)
        elif c == '6':
            print("Launching Graphical Reports/Summaries...")
            start_gui_from_cli(school)
            print("Returning to CLI.")
        elif c == '0':
            print("Goodbye!")
            break
        else:
            print("⚠️ Invalid option.")

if __name__ == '__main__':
    main(load_data())  
    
    
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


# def print_report_cli(school: School) -> str:
#     """
#     Generate a term report for all students.
    
#     Args:
#         school (School): The school instance.
    
#     Returns:
#         str: A formatted string containing the term report.
#     """
#     report = "=== Term Report ===\n"
#     for student in school.get_all_students():
#         report += repr(student) + "\n"  # Assuming Student has a detailed __repr__
#     return report


# def summary_students_cli(school: School, return_summary: bool = False) -> Optional[str]:
#     """
#     Summarize student information.
    
#     Args:
#         school (School): The school instance.
#         return_summary (bool, optional): If True, returns the summary string. 
#                                          If False, prints the summary to the console.
    
#     Returns:
#         Optional[str]: A formatted string containing the student summary if `return_summary` is True, 
#                      None otherwise.
#     """

#     summary = "=== Student Summary ===\n"
#     summary += f"Total Students: {len(school.students)}\n\n"
#     for student in school.get_all_students():
#         summary += f"{student.studentID}: {student.fName} {student.lName}, Year {student.schoolYear}\n"
#     if return_summary:
#         return summary
#     else:
#         print(summary)
#         return None


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


# def summary_employees_cli(school: School, return_summary: bool = False) -> Optional[str]:
#     """
#     Summarize employee information.
    
#     Args:
#         school (School): The school instance.
#         return_summary (bool, optional): If True, returns the summary string. 
#                                          If False, prints the summary to the console.
    
#     Returns:
#         Optional[str]: A formatted string containing the employee summary if `return_summary` is True, 
#                      None otherwise.
#     """

#     summary = "=== Employee Summary ===\n"
#     summary += f"Total Employees: {len(school.employees)}\n\n"
#     for emp in school.get_all_employees():
#         summary += f"{emp.employeeID}: {emp.get_name()} ({emp.__class__.__name__})"
#         if isinstance(emp, Teacher):
#             summary += f" | Subjects: {', '.join(emp.subjects)}"
#         else:
#             years = emp.get_years_of_service()
#             info = f" | Years of Service: {years}"
#             summary += info
#         summary += "\n"

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


