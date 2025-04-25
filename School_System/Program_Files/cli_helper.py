import sys
import getpass
from student import Student  # Only import Student from student.py
from subject import MathStudent, HistoryStudent, EnglishStudent  # Import MathStudent, HistoryStudent, and EnglishStudent from subject.py
from csv_loader import load_students_from_csv, load_maths_grades_from_csv, \
    load_english_grades_from_csv, load_history_grades_from_csv
from csv_loader import save_students_to_csv, save_maths_grades_to_csv, \
    save_english_grades_to_csv, save_history_grades_to_csv
from school import School
import os
from pathlib import Path

# === Configuration & Data Files ===
STUDENT_CSV = 'students.csv'
MATH_CSV = 'mathematics.csv'
ENG_CSV = 'english.csv'
HIST_CSV = 'history.csv'

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

    student_file_path = Path(__file__).parent / "CSV_Files" / 'students.csv'
    math_file_path = Path(__file__).parent / "CSV_Files" / 'mathematics.csv'
    english_file_path = Path(__file__).parent / "CSV_Files" / 'english.csv'
    history_file_path = Path(__file__).parent / "CSV_Files" / 'history.csv'

    school_year = "2025"  # or any value you'd like to use
    subjects = ["Math", "English", "History"]  # example list of subjects
    school = School("My School", "123 Main St", school_year, subjects)
    
    # Load students from CSV and categorize them
    try:
        students = load_students_from_csv(STUDENT_CSV)
    except FileNotFoundError:
        print("Error: Student CSV file not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error loading students: {e}")
        sys.exit(1)

    for student in students:
        if 'Math' in student.schoolSubjects:
            math_student = MathStudent(*student.get_student_data())
            school.add_student(math_student)
        elif 'History' in student.schoolSubjects:
            history_student = HistoryStudent(*student.get_student_data())
            school.add_student(history_student)
        elif 'English' in student.schoolSubjects:
            english_student = EnglishStudent(*student.get_student_data())
            school.add_student(english_student)

    try:
        load_maths_grades_from_csv(MATH_CSV, school.students)
        load_english_grades_from_csv(ENG_CSV, school.students)
        load_history_grades_from_csv(HIST_CSV, school.students)
    except FileNotFoundError as e:
        print(f"Error loading grades from file: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
        
    return school


def save_data(school):
    try:
        save_students_to_csv(STUDENT_CSV, school.students.values())
        save_maths_grades_to_csv(MATH_CSV, school.students.values())
        save_english_grades_to_csv(ENG_CSV, school.students.values())
        save_history_grades_to_csv(HIST_CSV, school.students.values())
        print("Data saved successfully.\n")
    except Exception as e:
        print(f"Error saving data: {e}")
        sys.exit(1)


def print_menu():
    print("=== Main Menu ===")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. View Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Print Term Report")
    print("7. Save & Exit")


def add_student_cli(school):
    print("--- Add Student ---")
    fName = input("First Name: ")
    lName = input("Last Name: ")
    year = input("School Year: ")
    subjects = input("Subjects (comma separated, e.g., Math, History): ").split(',')
    student = Student(fName, "", lName, "", "", "", "", "", year, subjects, "", "", "", "")
    
    # Add specific student categories
    if 'Math' in subjects:
        student = MathStudent(fName, "", lName, "", "", "", "", "", year, subjects, "", "", "", "")
    elif 'History' in subjects:
        student = HistoryStudent(fName, "", lName, "", "", "", "", "", year, subjects, "", "", "", "")
    elif 'English' in subjects:
        student = EnglishStudent(fName, "", lName, "", "", "", "", "", year, subjects, "", "", "", "")
    
    school.add_student(student)


def remove_student_cli(school):
    print("--- Remove Student ---")
    fName = input("First Name: ")
    lName = input("Last Name: ")
    student = school.find_student_by_name(fName, lName)
    if student:
        school.remove_student(student)
    else:
        print("Student not found.")


def view_student_cli(school):
    print("--- View Student ---")
    fName = input("First Name: ")
    lName = input("Last Name: ")
    student = school.find_student_by_name(fName, lName)
    if student:
        print(student)
    else:
        print("Student not found.")


def update_student_cli(school):
    print("--- Update Student ---")
    fName = input("First Name of student to update: ").strip()
    lName = input("Last Name of student to update: ").strip()
    student = school.find_student_by_name(fName, lName)
    if not student:
        print("Student not found.\n")
        return

    # Sub-menu for which field to update
    print("What would you like to update?")
    print("1. Name")
    print("2. Address")
    print("3. School Year")
    print("4. Subjects")
    print("5. Guardian Contact")
    choice = input("Select an option: ").strip()

    if choice == '1':
        # Update Name
        new_first = input(f"New First Name (current: {student.fName}): ").strip() or None
        new_middle = input(f"New Middle Name (current: {student.mName}): ").strip() or None
        new_last = input(f"New Last Name (current: {student.lName}): ").strip() or None
        student.update_name(fName=new_first, mName=new_middle, lName=new_last)
        print(f"✅ Updated Name: {student.fName} {student.mName} {student.lName}\n")

    elif choice == '2':
        # Update Address
        new_a1 = input(f"New Address Line 1 (current: {student.addressL1}): ").strip() or None
        new_a2 = input(f"New Address Line 2 (current: {student.addressL2}): ").strip() or None
        new_a3 = input(f"New Address Line 3 (current: {student.addressL3}): ").strip() or None
        new_pc = input(f"New Post Code (current: {student.addressPostCode}): ").strip() or None
        new_ct = input(f"New County (current: {student.addressCounty}): ").strip() or None
        student.update_address(addressL1=new_a1, addressL2=new_a2, addressL3=new_a3,
                               addressPostCode=new_pc, addressCounty=new_ct)
        print(f"✅ Updated Address: {student.addressL1}, {student.addressL2}, {student.addressL3}, {student.addressPostCode}, {student.addressCounty}\n")

    elif choice == '3':
        # Update School Year
        new_year = input(f"New School Year (current: {student.schoolYear}): ").strip()
        if new_year:
            student.update_school_year(new_year)
            print(f"✅ Updated School Year: {student.schoolYear}\n")

    elif choice == '4':
        # Update Subjects
        print("a. Add Subject")
        print("b. Remove Subject")
        sub_choice = input("Choose action: ").strip().lower()
        subject = input("Subject name: ").strip()
        if sub_choice == 'a':
            student.add_subject(subject)
            print(f"✅ Added Subject: {subject}\n")
        elif sub_choice == 'b':
            student.remove_subject(subject)
            print(f"✅ Removed Subject: {subject}\n")

    elif choice == '5':
        # Update Guardian Contact
        g_num = input("Guardian to update (1 or 2): ").strip()
        name = input("New Guardian Name (leave blank to skip): ").strip() or None
        contact = input("New Guardian Contact (leave blank to skip): ").strip() or None
        if g_num in ('1','2'):
            student.update_guardian_contact(int(g_num), name=name, contact=contact)
            print(f"✅ Updated Guardian {g_num}: Name={getattr(student, 'nameParGar'+g_num)}, Contact={getattr(student, 'contactDetParGar'+g_num)}\n")
        else:
            print("Invalid guardian number.\n")

    else:
        print("Invalid choice.\n")


def delete_student_cli(school):
    print("--- Delete Student ---")
    view_student_cli(school)
    confirm = input("Type 'yes' to confirm deletion: ").strip().lower()
    if confirm == 'yes':
        remove_student_cli(school)


def print_report_cli(school):
    print("--- Term Report ---")
    subject = input("Subject (Mathematics/English/History): ").strip()
    avg = school.get_average_grade(subject)
    print(f"Average {subject} grade: {avg}\n")
    students = school.list_students_by_subject(subject)
    print(f"Students taking {subject}:")
    for name in students:
        print(" - ", name)
    print()


def main():
    if not login():
        sys.exit(1)
    school = load_data()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1': add_student_cli(school)
        elif choice == '2': remove_student_cli(school)
        elif choice == '3': view_student_cli(school)
        elif choice == '4': update_student_cli(school)
        elif choice == '5': delete_student_cli(school)
        elif choice == '6': print_report_cli(school)
        elif choice == '7':
            save_data(school)
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

if __name__ == '__main__':
    main()
