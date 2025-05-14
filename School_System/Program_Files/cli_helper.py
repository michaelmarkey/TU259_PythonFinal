import sys
import getpass
from pathlib import Path

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

def login():
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
    except FileNotFoundError:
        print("Error: Student CSV file not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading students: {e}")
        sys.exit(1)

    # Register students into school
    for student in students:
        school.register_student(student)
    print(f"Registered {len(school.students)} students.")

    # Load employees
    try:
        employees = load_employees_from_csv(paths['employees'])
    except Exception as e:
        print(f"Error loading employees: {e}")
        sys.exit(1)
    for emp in employees:
        if isinstance(emp, Teacher):
            school.register_teacher(emp)
        else:
            school.register_employee(emp)
    print(f"Registered {len(school.employees)} employees ({len(school.teachers)} teachers).\n")


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


def save_data(school):
    """Save students, grades, and employees to CSV."""
    try:
        save_students_to_csv(STUDENT_CSV, school.students.values())
        save_grades_to_csv(MATH_CSV, school.students.values(), 'Mathematics')
        save_grades_to_csv(ENG_CSV, school.students.values(), 'English')
        save_grades_to_csv(HIST_CSV, school.students.values(), 'History')
        # TODO: Implement saving employees
        print("Data saved successfully.\n")
    except Exception as e:
        print(f"Error saving data: {e}")
        sys.exit(1)


def add_student_cli(school):
    print("--- Add Student ---")
    sid = input("Student ID: ").strip()
    fName = input("First Name: ").strip()
    mName = input("Middle Name (optional): ").strip()
    lName = input("Last Name: ").strip()
    age = int(input("Age: ").strip() or 0)
    addr1 = input("Address Line 1: ").strip()
    addr2 = input("Address Line 2 (optional): ").strip()
    addr3 = input("Address Line 3 (optional): ").strip()
    postcode = input("Post Code: ").strip()
    county = input("County: ").strip()
    year = input("School Year: ").strip()
    subjects = [s.strip() for s in input("Subjects (comma-separated): ").split(',') if s.strip()]
    par1 = input("Guardian 1 Name: ").strip()
    contact1 = input("Guardian 1 Contact: ").strip()
    par2 = input("Guardian 2 Name: ").strip()
    contact2 = input("Guardian 2 Contact: ").strip()

    student = Student(
        studentID=sid, fName=fName, mName=mName, lName=lName,
        age=age, addressL1=addr1, addressL2=addr2, addressL3=addr3,
        addressPostCode=postcode, addressCounty=county,
        schoolYear=year, schoolSubjects=subjects,
        nameParGar1=par1, contactDetParGar1=contact1,
        nameParGar2=par2, contactDetParGar2=contact2
    )

    school.register_student(student)
    print(f"✅ Added Student: {sid} - {fName} {lName}\n")


def remove_student_cli(school):
    print("--- Remove Student ---")
    sid = input("Student ID to remove: ").strip()
    student = school.get_student_by_id(sid)
    if student:
        school.remove_student(sid)
        print(f"✅ Removed Student ID {sid}\n")
    else:
        print("⚠️ Student not found.\n")


def view_student_cli(school):
    print("--- View Student ---")
    sid = input("Student ID to view: ").strip()
    student = school.get_student_by_id(sid)
    if student:
        print(student.get_full_student_data())
        if student.subject_grades:
            print("Subject Grades:")
            for subj, grade in student.subject_grades.items():
                print(f"  {subj}: {grade}")
            avg = student.calculate_overall_average()
            if avg is not None:
                print(f"Overall Average: {avg:.2f}\n")
    else:
        print("⚠️ Student not found.\n")


def update_student_cli(school):
    print("--- Update Student ---")
    sid = input("Student ID to update: ").strip()
    student = school.get_student_by_id(sid)
    if not student:
        print("⚠️ Student not found.\n")
        return

    print("1. Name | 2. Address | 3. Year | 4. Subjects | 5. Guardian")
    choice = input("Select field to update: ").strip()

    if choice == '1':
        nf = input(f"First Name ({student.fName}): ").strip() or None
        nm = input(f"Middle Name ({student.mName}): ").strip() or None
        nl = input(f"Last Name ({student.lName}): ").strip() or None
        student.update_name(new_fName=nf, new_mName=nm, new_lName=nl)
    elif choice == '2':
        a1 = input(f"Address1 ({student.addressL1}): ").strip() or None
        a2 = input(f"Address2 ({student.addressL2}): ").strip() or None
        a3 = input(f"Address3 ({student.addressL3}): ").strip() or None
        pc = input(f"PostCode ({student.addressPostCode}): ").strip() or None
        ct = input(f"County ({student.addressCounty}): ").strip() or None
        student.update_address(a1, a2, a3, pc, ct)
    elif choice == '3':
        ny = input(f"School Year ({student.schoolYear}): ").strip()
        student.update_school_year(ny)
    elif choice == '4':
        s = input("Add or Remove (a/r): ").strip().lower()
        sub = input("Subject: ").strip()
        if s=='a': student.add_subject(sub)
        else: student.remove_subject(sub)
    elif choice == '5':
        gn = input("Guardian# (1/2): ").strip()
        name = input("Name: ").strip() or None
        contact = input("Contact: ").strip() or None
        student.update_guardian_contact(int(gn), new_name=name, new_contact=contact)
    print("✅ Update complete.\n")


def delete_student_cli(school):
    """Delete a student after confirmation."""
    print("--- Delete Student ---")
    sid = input("Student ID to delete: ").strip()
    student = school.get_student_by_id(sid)
    if not student:
        print("⚠️ Student not found.\n")
        return
    print(student.get_full_student_data())
    confirm = input("Type 'yes' to confirm deletion: ").strip().lower()
    if confirm == 'yes':
        school.remove_student(sid)
        print(f"✅ Deleted Student ID {sid}\n")
    else:
        print("❌ Deletion cancelled.\n")


def print_report_cli(school, return_summary=False):
    subject = "Mathematics"  # Default subject for GUI, or parameterize if needed
    avg = school.get_average_grade(subject)
    report = f"--- Term Report: {subject} ---\n"
    report += f"Average Grade: {avg}\n"
    report += school.list_students_by_subject(subject)
    
    if return_summary:
        return report
    else:
        print(report)

# New summary functions
def summary_students_cli(school, return_summary=False):
    students = school.get_all_students()
    summary = "--- Student Population Summary ---\n"
    summary += f"Total Students: {len(students)}\n"
    for student in students:
        info = student.get_summary_student_data().strip().splitlines()
        subjects = ', '.join(student.schoolSubjects)
        avg = student.calculate_overall_average()
        summary += f"{info[0]} | Subjects: {subjects} | Avg: {avg if avg is not None else 'N/A'}\n"
    
    if return_summary:
        return summary
    else:
        print(summary)


def summary_school_cli(school, return_summary=False):
    summary = "--- School Information ---\n"
    summary += repr(school) + "\n"
    
    if return_summary:
        return summary
    else:
        print(summary)


def summary_employees_cli(school, return_summary=False):
    """Print or return a summary for all employees"""
    employees = school.get_all_employees()
    if not employees:
        result = "No employees found.\n"
    
    summary = "--- Employee Summary ---\n"
    summary += f"Total Employees: {len(employees)}\n"

    for emp in employees:
        role = emp.__class__.__name__
        info = f"ID: {emp.employeeID} | Name: {emp.get_name()} | Role: {role}"
        if isinstance(emp, Teacher):
            subjects = ', '.join(emp.subjects)
            info += f" | Subjects: {subjects} | Years Teaching: {emp.years_teaching}"
        else:
            years = emp.get_years_of_service()
            info += f" | Years of Service: {years}"
        summary += f"{info}\n"

    return summary if return_summary else None



# Updated main menu to include summaries
def print_menu():
    print("=== Main Menu ===")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Print Term Report")
    print("7. Student Summary")
    print("8. School Summary")
    print("9. Employee Summary")
    print("0. Exit")

# Main entrypoint for both direct run and import

def main():
    if not login():
        sys.exit(1)
    school = load_data()
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
            print_report_cli(school)
        elif c == '7':
            summary_students_cli(school)
        elif c == '8':
            summary_school_cli(school)
        elif c == '9':
            summary_employees_cli(school)
        elif c == '0':
            print("Goodbye!")
            break
        else:
            print("⚠️ Invalid option.")

if __name__ == '__main__':
    main()


