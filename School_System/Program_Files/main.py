#!/usr/bin/env python3
#Need to update all this

"""
School Management System - Main Entry Point
This module initializes the school management system and provides the user
with options to run in either CLI mode or GUI mode.
"""

import sys
import os

# Get the directory containing main.py
main_dir = os.path.dirname(os.path.abspath(__file__))
garden_matplotlib_path = os.path.join(main_dir, 'garden.matplotlib')

# Add the parent directory to sys.path if it's not already there
parent_dir = os.path.dirname(garden_matplotlib_path)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import sys
import os
from pathlib import Path

# Import school classes
from school import School
from student import Student
from employee import Teacher, Principal, Medic, Administrator, Counselor

# Import the CLI helper functions
from cli_helper import (
    login,
    load_data,
    save_data_to_csv,
    crud_menu
)

# GUI needs to be imported but not used directly here
# It will be imported by cli_helper when needed
from gui import SchoolApp


def main():
    """
    Main entry point for the School Management System.
    Performs login, loads data, and launches the CLI interface.
    """
    # Print application header
    print("\n====================================================")
    print("     SCHOOL MANAGEMENT SYSTEM")
    print("====================================================")
    print("A complete solution for managing students and staff.")
    print("----------------------------------------------------\n")
    
    # Check if login is required (can be disabled during development)
    REQUIRE_LOGIN = True
    
    if REQUIRE_LOGIN:
        if not login():
            print("Login failed. Exiting application.")
            sys.exit(1)
    
    # Load school data
    try:
        school = load_data()
        print("\nData loaded successfully!")
        print(f"School: {school.name}")
        print(f"Students: {len(school.students)}")
        print(f"Employees: {len(school.employees)} (including {len(school.teachers)} teachers)")
        print("----------------------------------------------------")
    except Exception as e:
        print(f"Error loading school data: {e}")
        sys.exit(1)
    
    # Start the CRUD menu (which includes the option to launch the GUI)
    try:
        crud_menu(school)
    except KeyboardInterrupt:
        print("\nApplication terminated by user.")
    except Exception as e:
        print(f"Error in application: {e}")
    finally:
        # Ensure data is saved when exiting
        try:
            save_data_to_csv(school)
            print("Data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    print("\nThank you for using the School Management System!")


if __name__ == "__main__":
    main()


# # main.py
# from cli_helper import * # Import all functions from your helper file

# def main():
#     if login():
#         school = load_data()  # Load initial data
#         crud_menu(school)  # Or crud_menu(school) if you want the CRUD-only version
#         save_data_to_csv(school)  # Save data on exit

# if __name__ == "__main__":
#     main()

# # In your main.py file

# from cli_helper import main as run_cli, load_data # Assuming your CLI main is named run_cli
# from gui import SchoolManagementApp # Import your GUI App class
# import sys
# import os

# if __name__ == "__main__":
#     # Determine the base path
#     base_path = os.path.dirname(os.path.abspath(__file__))
#     csv_folder = os.path.join(base_path, "CSV_Files")  # Adjust if your folder is named differently
#     student_csv_path = os.path.join(csv_folder, "students.csv")  # Example path
#     # ... other CSV paths if needed ...

#     # --- Initial Interface Choice ---
#     interface_choice = input("Choose interface: (1) CLI, (2) GUI: ").strip()

#     if interface_choice == "1":
#         print("\nStarting CLI. To switch, restart the application.")
#         school = load_data() # Load data HERE for CLI
#         run_cli(school)  # Pass the schooadminl object to the CLI (make sure cli_helper's main accepts it)
#     elif interface_choice == "2":
#         print("\nStarting GUI. To switch, restart the application.")
#         school = load_data() # Load data HERE for GUI
#         app = SchoolManagementApp(school=school)  # Pass the school object to the GUI
#         app.run() # This starts the Kivy event loop
#     else:
#         print("Invalid choice. Please restart and select 1 or 2.")
#         sys.exit(1) # Exit if the choice is invalid

#!/usr/bin/env python3
# main.py - Entry point for School Management System

# import sys
# import cli_helper

# if __name__ == '__main__':
#     # If 'cli' argument provided, run interactive CLI
#     if len(sys.argv) > 1 and sys.argv[1].lower() == 'cli':
#         cli_helper.main()
#     else:
#         # Default to launching interactive CLI
#         cli_helper.main()

# #!/usr/bin/env python3
# # main.py - Test script for School Management System

# from school import School
# from student import Student
# from subject import SubjectStudent, create_subject_student
# from grade_calculator import calculate_and_update_grades_for_students, simple_grade_calculation
# from csv_loader import load_all_data
# from employee import Teacher  # Needed to check isinstance()

# def test_csv_loading():
#     """Test loading data from CSV files"""
#     print("\n" + "="*50)
#     print("TESTING CSV LOADING")
#     print("="*50)
    
#     # Create a school
#     sunnydale = School(
#         name="Sunnydale High School",
#         address="1630 Revello Drive, Sunnydale",
#         telephoneNumber="555-SUNNY",
#         subjects=["Mathematics", "English", "History"]
#     )
    
#     # Load all student and employee data from CSV files
#     students, employees = load_all_data(
#         student_file="students.csv",
#         employee_file="employees.csv",  # Add employee file
#         math_file="math_grades.csv",
#         english_file="english_grades.csv",
#         history_file="history_grades.csv"
#     )
    
#     # Register each student with the school
#     print("\n--- Registering CSV Students with School ---")
#     for student in students:
#         sunnydale.register_student(student)
    
#     print(f"School now has {len(sunnydale.students)} registered students")
    
#     # Register each employee or teacher with the school (if necessary)
#     print("\n--- Registering CSV Teachers with School ---")
#     for emp in employees:
#         if isinstance(emp, Teacher):
#             sunnydale.register_teacher(emp)
#         else:
#             sunnydale.register_employee(emp)
#     print(f"School now has {len(sunnydale.teachers)} registered teachers")
#     print(f"Total employees (including teachers): {len(sunnydale.employees)}")
    
#     print(f"School now has {len(sunnydale.teachers)} registered teachers")
    
#     # Apply the grade calculation for students
#     print("\n--- Calculating Final Grades for CSV Students ---")
#     calculate_and_update_grades_for_students(sunnydale.get_all_students())
    
#     # Display student information
#     print("\n--- CSV Student Information ---")
#     for student in sunnydale.get_all_students():
#         print(student.get_summary_student_data())
#         if hasattr(student, 'subject_grades') and student.subject_grades:
#             print("Subject Grades:")
#             for subject, grade in student.subject_grades.items():
#                 print(f"  {subject}: {grade}")
            
#             overall_avg = student.calculate_overall_average()
#             if overall_avg is not None:
#                 print(f"Overall Average: {overall_avg:.2f}")
        
#         print("-" * 40)
    
#     # Display teacher information
#     print("\n--- CSV Teacher Information ---")
#     for teacher in sunnydale.get_all_teachers():  # Assuming you have a method to get all teachers
#         print(f"Teacher: {teacher.fName} {teacher.lName} (ID: {teacher.employeeID})")
#         print(f"  Subjects: {', '.join(teacher.subjects)}")
#         print(f"  Years of Teaching: {teacher.years_teaching}")
#         print(f"  Contact: {teacher.contact_number}, {teacher.email}")
#         print("-" * 40)
    
#     # Test some school reporting methods
#     print("\n--- School Reports ---")
#     print("Students in Year 11:")
#     print(sunnydale.list_students_by_year(11))
    
#     print("Students taking History:")
#     print(sunnydale.list_students_by_subject("History"))
    
#     # Get average grade for each subject
#     print("\n--- Subject Average Grades ---")
#     for subject in ["Mathematics", "English", "History"]:
#         avg = sunnydale.get_average_grade(subject)
#         if avg is not None:
#             print(f"Average grade for {subject}: {avg}")
    
#     # Find students with specific criteria
#     print("\n--- Find Students by Name ---")
#     smith_students = sunnydale.find_students_by_name(last_name="Smith")
#     for student in smith_students:
#         print(f"Found: {student.fName} {student.lName} (ID: {student.studentID})")
    
#     return sunnydale

# def main():
#     """Main function to run the tests"""
#     print("\n" + "*"*70)
#     print("SCHOOL MANAGEMENT SYSTEM TEST SUITE")
#     print("*"*70)
    
#     # Test CSV loading
#     sunnydale = test_csv_loading()

#     print("\n" + "*"*70)
#     print("ALL TESTS COMPLETED")
#     print("*"*70)


# # This ensures main() gets called when you run the script
# if __name__ == "__main__":
#     main()


# def test_manual_creation():
#     """Test manually creating and manipulating objects"""
#     print("\n" + "="*50)
#     print("TESTING MANUAL OBJECT CREATION")
#     print("="*50)
    
#     # Create a school
#     print("\n--- Creating School ---")
#     greenwood = School(
#         name="Greenwood High School",
#         address="123 Education Lane, Learning City",
#         telephoneNumber="555-LEARN",
#         subjects=["Mathematics", "English", "History"]
#     )
#     print(greenwood)
    
#     # Create a few students
#     print("\n--- Creating Students ---")
#     alice = Student(
#         studentID="ST001",
#         fName="Alice",
#         mName="Jane",
#         lName="Smith",
#         age=16,
#         addressL1="456 Student Ave",
#         addressL2="Apt 3B",
#         addressL3="",
#         addressPostCode=54321,
#         addressCounty="Essex",
#         schoolYear="11",
#         schoolSubjects=["Mathematics", "English", "History"],
#         nameParGar1="Sarah Smith",
#         nameParGar2="John Smith",
#         contactDetParGar1=5551234567,
#         contactDetParGar2=5559876543,
#         subject_grades={}
#     )
    
#     bob = Student(
#         studentID="ST002",
#         fName="Bob",
#         mName="Thomas",
#         lName="Jones",
#         age=15,
#         addressL1="789 Pupil Street",
#         addressL2="",
#         addressL3="",
#         addressPostCode=65432,
#         addressCounty="Kent",
#         schoolYear="10",
#         schoolSubjects=["Mathematics", "History"],
#         nameParGar1="Mary Jones",
#         nameParGar2="Robert Jones",
#         contactDetParGar1=5552345678,
#         contactDetParGar2=5558765432,
#         subject_grades={}
#     )
    
#     # Register students with the school
#     print("\n--- Registering Students ---")
#     greenwood.register_student(alice)
#     greenwood.register_student(bob)
#     print(f"School now has {len(greenwood.students)} registered students")
    
#     # Add subject details for students
#     print("\n--- Adding Subject Details ---")
    
#     # Add Math details for Alice and Bob using SubjectStudent class
#     alice_math = create_subject_student(
#         student=alice,
#         subject_name="Mathematics",
#         level="Advanced",
#         class_number="M101",
#         teacher="Mr. Thompson",
#         last_test_score=92
#     )
    
#     bob_math = create_subject_student(
#         student=bob,
#         subject_name="Mathematics",
#         level="Standard",
#         class_number="M102", 
#         teacher="Ms. Parker",
#         last_test_score=85
#     )
    
#     # Add English for Alice only
#     alice_english = create_subject_student(
#         student=alice,
#         subject_name="English",
#         level="Advanced",
#         class_number="E201",
#         teacher="Mrs. Johnson",
#         last_test_score=88
#     )
    
#     # Add History for both
#     alice_history = create_subject_student(
#         student=alice,
#         subject_name="History",
#         level="Standard",
#         class_number="H302",
#         teacher="Ms. Wilson", 
#         last_test_score=90
#     )
    
#     bob_history = create_subject_student(
#         student=bob,
#         subject_name="History",
#         level="Standard",
#         class_number="H302",
#         teacher="Ms. Wilson",
#         last_test_score=78
#     )
    
#     # Apply simple grade calculation
#     print("\n--- Calculating Grades ---")
#     updated_students = simple_grade_calculation(greenwood.get_all_students())
    



    # Print student information with grades
#     print("\n--- Student Information with Grades ---")
#     for student in updated_students:
#         print(student.get_full_student_data())
#         if hasattr(student, 'subject_grades') and student.subject_grades:
#             print("Subject Grades:")
#             for subject, grade in student.subject_grades.items():
#                 print(f"  {subject}: {grade}")
            
#             overall_avg = student.calculate_overall_average()
#             if overall_avg is not None:
#                 print(f"Overall Average: {overall_avg:.2f}")
            
#         print("-" * 40)
    
#     # Test school methods
#     print("\n--- Testing School Methods ---")
#     print("Students in year 11:")
#     print(greenwood.list_students_by_year(11))
    
#     print("Students taking Mathematics:")
#     print(greenwood.list_students_by_subject("Mathematics"))
    
#     print("Finding student by ID:")
#     found_student = greenwood.find_student_by_id("ST001")
#     if found_student:
#         print(f"Found: {found_student.fName} {found_student.lName}")
    
#     print("Finding students by name:")
#     found_students = greenwood.find_students_by_name(first_name="Alice")
#     for student in found_students:
#         print(f"Found: {student.fName} {student.lName}")
    
#     # Test updating student information
#     print("\n--- Testing Student Update Methods ---")
#     bob.update_address(new_addressL1="999 New Address St")
#     bob.add_subject("English")
#     bob.update_guardian_contact(1, new_name="Margaret Jones", new_contact=5559998888)
    
#     print("Updated Bob's information:")
#     print(bob.get_full_student_data())
    
#     # Test removing a student
#     print("\n--- Testing Student Removal ---")
#     old_count = len(greenwood.students)
#     greenwood.remove_student("ST001")
#     new_count = len(greenwood.students)
#     print(f"Student count before: {old_count}, after: {new_count}")
    
#     return greenwood


# def test_csv_loading():
#     """Test loading data from CSV files"""
#     print("\n" + "="*50)
#     print("TESTING CSV LOADING")
#     print("="*50)
    
#     # Create a school
#     sunnydale = School(
#         name="Sunnydale High School",
#         address="1630 Revello Drive, Sunnydale",
#         telephoneNumber="555-SUNNY",
#         subjects=["Mathematics", "English", "History"]
#     )
    
#     # Load all student data from CSV files
#     students = load_all_data(
#         student_file="students.csv",
#         math_file="math_grades.csv",
#         english_file="english_grades.csv",
#         history_file="history_grades.csv"
#     )
    
#     # Register each student with the school
#     print("\n--- Registering CSV Students with School ---")
#     for student in students:
#         sunnydale.register_student(student)
    
#     print(f"School now has {len(sunnydale.students)} registered students")
    
#     # Apply the grade calculation
#     print("\n--- Calculating Final Grades for CSV Students ---")
#     calculate_and_update_grades_for_students(sunnydale.get_all_students())
    
#     # Display student information
#     print("\n--- CSV Student Information ---")
#     for student in sunnydale.get_all_students():
#         print(student.get_summary_student_data())
#         if hasattr(student, 'subject_grades') and student.subject_grades:
#             print("Subject Grades:")
#             for subject, grade in student.subject_grades.items():
#                 print(f"  {subject}: {grade}")
            
#             overall_avg = student.calculate_overall_average()
#             if overall_avg is not None:
#                 print(f"Overall Average: {overall_avg:.2f}")
        
#         print("-" * 40)
    
#     # Test some school reporting methods
#     print("\n--- School Reports ---")
#     print("Students in Year 11:")
#     print(sunnydale.list_students_by_year(11))
    
#     print("Students taking History:")
#     print(sunnydale.list_students_by_subject("History"))
    
#     # Get average grade for each subject
#     print("\n--- Subject Average Grades ---")
#     for subject in ["Mathematics", "English", "History"]:
#         avg = sunnydale.get_average_grade(subject)
#         if avg is not None:
#             print(f"Average grade for {subject}: {avg}")
    
#     # Find students with specific criteria
#     print("\n--- Find Students by Name ---")
#     smith_students = sunnydale.find_students_by_name(last_name="Smith")
#     for student in smith_students:
#         print(f"Found: {student.fName} {student.lName} (ID: {student.studentID})")
    
#     return sunnydale


# def main():
#     """Main function to run the tests"""
#     print("\n" + "*"*70)
#     print("SCHOOL MANAGEMENT SYSTEM TEST SUITE")
#     print("*"*70)
    
#     # Test manual creation and manipulation
#     school1 = test_manual_creation()
    
#     # Test CSV loading
#     school2 = test_csv_loading()
    
#     print("\n" + "*"*70)
#     print("ALL TESTS COMPLETED")
#     print("*"*70)


# if __name__ == "__main__":
#     main()



# import random
# import json

# # Generate student data
# def generate_student_data(n=20):
#     first_names = ["Andrew", "Jasmine", "Liam", "Olivia", "Noah", "Emma", "James", "Sophia", "Benjamin", "Isabella",
#                    "Lucas", "Mia", "Henry", "Charlotte", "Alexander", "Amelia", "Daniel", "Harper", "Matthew", "Evelyn"]
#     last_names = ["Smith", "Jones", "Brown", "Johnson", "Williams", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson"]
#     subjects = ["Mathematics", "English", "History"]

#     data = []

#     for i in range(n):
#         fName = first_names[i % len(first_names)]
#         lName = last_names[i % len(last_names)]
#         student_id = f"S{str(i+1).zfill(3)}"
#         school_subjects = random.sample(subjects, random.randint(1, 3))

#         assessments = {}
#         if "Mathematics" in school_subjects:
#             assessments["mathGrades"] = [round(random.uniform(50, 100), 1) for _ in range(8)]  # 5 quizzes, 2 tests, 1 final exam
#         if "English" in school_subjects:
#             assessments["englishAttendance"] = round(random.uniform(60, 100), 1)
#             assessments["englishQuiz1"] = round(random.uniform(50, 100), 1)
#             assessments["englishQuiz2"] = round(random.uniform(50, 100), 1)
#             assessments["englishFinalExam"] = round(random.uniform(50, 100), 1)
#         if "History" in school_subjects:
#             assessments["historyAttendance"] = round(random.uniform(60, 100), 1)
#             assessments["historyProject"] = round(random.uniform(50, 100), 1)
#             assessments["historyExams"] = [round(random.uniform(50, 100), 1), round(random.uniform(50, 100), 1)]

#         data.append({
#             "studentID": student_id,
#             "fName": fName,
#             "mName": f"{fName[0]}.",
#             "lName": lName,
#             "age": random.randint(14, 18),
#             "addressL1": f"{random.randint(1, 100)} Main Street",
#             "addressL2": "Townsville",
#             "addressL3": "North",
#             "addressPostCode": random.randint(10000, 99999),
#             "addressCounty": "Countyshire",
#             "schoolYear": f"Year {random.randint(9, 12)}",
#             "schoolSubjects": school_subjects,
#             "nameParGar1": f"Parent1 {fName}",
#             "nameParGar2": f"Parent2 {fName}",
#             "contactDetParGar1": random.randint(5000000000, 5999999999),
#             "contactDetParGar2": random.randint(6000000000, 6999999999),
#             "assessments": assessments
#         })

#     return data

# # Generate and store dataset
# student_dataset = generate_student_data()

# # --------------------------------------------
# # Print Summary 1: Student ID, Full Name, Subjects
# print("\n--- List of Students and Subjects Studied ---")
# for student in student_dataset:
#     full_name = f"{student['fName']} {student['lName']}"
#     print(f"ID: {student['studentID']}, Name: {full_name}, Subjects: {', '.join(student['schoolSubjects'])}")

# # --------------------------------------------
# # Print Summary 2: Student Grades Summary
# print("\n--- Continuous Assessment and Final Grades ---")
# for student in student_dataset:
#     full_name = f"{student['fName']} {student['lName']}"
#     print(f"\nStudent: {full_name} (ID: {student['studentID']})")
#     assessments = student["assessments"]
#     if "mathGrades" in assessments:
#         avg_math = round(sum(assessments["mathGrades"]) / len(assessments["mathGrades"]), 2)
#         print(f"  Math - Continuous Assessment Avg: {avg_math}")
#     if "englishQuiz1" in assessments:
#         cont_eng = round((assessments["englishQuiz1"] + assessments["englishQuiz2"]) / 2, 2)
#         final_eng = assessments["englishFinalExam"]
#         print(f"  English - Continuous: {cont_eng}, Final Exam: {final_eng}")
#     if "historyProject" in assessments:
#         cont_hist = assessments["historyProject"]
#         final_hist = round(sum(assessments["historyExams"]) / len(assessments["historyExams"]), 2)
#         print(f"  History - Project: {cont_hist}, Final Exam Avg: {final_hist}")

# # --------------------------------------------
# # Print Summary 3: Full breakdown per student, per subject, with assessment grades and averages
# print("\n--- Full Breakdown: Each Student, Each Subject, Continuous Grades & Averages ---")

# for student in student_dataset:
#     full_name = f"{student['fName']} {student['lName']}"
#     student_id = student['studentID']
#     assessments = student['assessments']
#     print(f"\n📘 Student: {full_name} (ID: {student_id})")
    
#     for subject in student["schoolSubjects"]:
#         print(f"\n  🔹 Subject: {subject}")
        
#         if subject == "Mathematics" and "mathGrades" in assessments:
#             grades = assessments["mathGrades"]
#             quizzes = grades[:5]  # First 5 are quizzes
#             test1, test2 = grades[5], grades[6]  # Test 1 & 2
#             final_exam = grades[7]  # Final exam
            
#             # Average math grade
#             avg_math = round(sum(grades) / len(grades), 2)
#             print(f"    Quizzes: {quizzes}")
#             print(f"    Test 1: {test1}")
#             print(f"    Test 2: {test2}")
#             print(f"    Final Exam: {final_exam}")
#             print(f"    ➤ Average: {avg_math}")
        
#         elif subject == "English":
#             if all(key in assessments for key in ["englishAttendance", "englishQuiz1", "englishQuiz2", "englishFinalExam"]):
#                 grades = [
#                     assessments["englishAttendance"],
#                     assessments["englishQuiz1"],
#                     assessments["englishQuiz2"],
#                     assessments["englishFinalExam"]
#                 ]
#                 labels = ["Attendance", "Quiz 1", "Quiz 2", "Final Exam"]
#                 weighted_average = (
#                     grades[0]*0.10 + grades[1]*0.15 + grades[2]*0.15 + grades[3]*0.60
#                 )
#                 for label, grade in zip(labels, grades):
#                     print(f"    {label}: {grade}")
#                 print(f"    ➤ Weighted Average: {round(weighted_average, 2)}")
        
#         elif subject == "History":
#             if all(key in assessments for key in ["historyAttendance", "historyProject", "historyExams"]):
#                 grades = [
#                     assessments["historyAttendance"],
#                     assessments["historyProject"],
#                     *assessments["historyExams"]
#                 ]
#                 labels = ["Attendance", "Project", "Exam 1", "Exam 2"]
#                 weighted_average = (
#                     grades[0]*0.10 + grades[1]*0.30 + grades[2]*0.30 + grades[3]*0.30
#                 )
#                 for label, grade in zip(labels, grades):
#                     print(f"    {label}: {grade}")
#                 print(f"    ➤ Weighted Average: {round(weighted_average, 2)}")


# from student import Student
# from subject import create_subject_student
# from grade_calculator import calculate_and_update_grades_for_students

# # -------------------------
# # Create Student Instances
# # -------------------------

# students = []

# student_data = [
#     {
#         'studentID': 'S001',
#         'fName': 'Andrew',
#         'mName': 'A.',
#         'lName': 'Smith',
#         'age': 17,
#         'addressL1': '12 Green Street',
#         'addressL2': 'Hightown',
#         'addressL3': 'West',
#         'addressPostCode': 48302,
#         'addressCounty': 'Countyshire',
#         'schoolYear': 'Year 10',
#         'schoolSubjects': ['English', 'History', 'Mathematics'],
#         'nameParGar1': 'Parent1 Andrew',
#         'nameParGar2': 'Parent2 Andrew',
#         'contactDetParGar1': 6595717523,
#         'contactDetParGar2': 7591665817,
#         'assessments': {
#             'mathGrades': [70.1, 84.9, 79.5, 90.8, 51.0, 52.6, 69.9, 79.8],
#             'englishAttendance': 71.3,
#             'englishQuiz1': 61.7,
#             'englishQuiz2': 70.5,
#             'englishFinalExam': 94.6,
#             'historyAttendance': 80.8,
#             'historyProject': 66.2,
#             'historyExams': [56.6, 65.9]
#         }
#     },
#     {
#         'studentID': 'S002',
#         'fName': 'Jasmine',
#         'mName': 'A.',
#         'lName': 'Jones',
#         'age': 15,
#         'addressL1': '12 Green Street',
#         'addressL2': 'Hightown',
#         'addressL3': 'West',
#         'addressPostCode': 89950,
#         'addressCounty': 'Countyshire',
#         'schoolYear': 'Year 11',
#         'schoolSubjects': ['English'],
#         'nameParGar1': 'Parent1 Jasmine',
#         'nameParGar2': 'Parent2 Jasmine',
#         'contactDetParGar1': 5934332577,
#         'contactDetParGar2': 9750022001,
#         'assessments': {
#             'englishAttendance': 78.9,
#             'englishQuiz1': 65.4,
#             'englishQuiz2': 80.2,
#             'englishFinalExam': 89.1
#         }
#     }
#     # Add remaining 18 students in same format here...
# ]

# # -------------------------
# # Convert to Student Objects
# # -------------------------
# for entry in student_data:
#     s = Student(
#         studentID=entry['studentID'],
#         fName=entry['fName'],
#         mName=entry['mName'],
#         lName=entry['lName'],
#         age=entry['age'],
#         addressL1=entry['addressL1'],
#         addressL2=entry['addressL2'],
#         addressL3=entry['addressL3'],
#         addressPostCode=entry['addressPostCode'],
#         addressCounty=entry['addressCounty'],
#         schoolYear=entry['schoolYear'],
#         schoolSubjects=entry['schoolSubjects'],
#         nameParGar1=entry['nameParGar1'],
#         nameParGar2=entry['nameParGar2'],
#         contactDetParGar1=entry['contactDetParGar1'],
#         contactDetParGar2=entry['contactDetParGar2']
#     )

#     # Attach assessments as attributes
#     for key, value in entry['assessments'].items():
#         setattr(s, key, value)

#     students.append(s)

# # -------------------------
# # Grade Calculation
# # -------------------------
# students = calculate_and_update_grades_for_students(students)

# # -------------------------
# # Print Student Grades
# # -------------------------
# for s in students:
#     print(f"\nStudent: {s.fName} {s.lName}")
#     for subject, grade in s.subject_grades.items():
#         print(f" - {subject}: {grade:.2f}")


# from student import Student
# from subject import create_subject_student
# import random

# first_names = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah", "Ian", "Jade",
#                "Kevin", "Laura", "Mike", "Nina", "Oscar", "Paula", "Quinn", "Rachel", "Sam", "Tina"]
# last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Lopez", "Clark"]

# subjects_available = ["English", "Mathematics", "History"]
# teachers = {
#     "English": ["Ms. Blake", "Mr. Knight"],
#     "Mathematics": ["Mr. Zhao", "Mrs. Newton"],
#     "History": ["Dr. Allen", "Ms. Ford"]
# }

# students = []
# subject_students = []

# for i in range(20):
#     fName = first_names[i]
#     lName = last_names[i % len(last_names)]
#     mName = chr(65 + i)  # A, B, ...
#     studentID = f"S{i+1:03d}"
#     age = random.randint(11, 17)
#     address = (f"{i+1} Main St", "Apt 1", "District", 10000 + i, "Countyshire")
#     schoolYear = f"Year {random.randint(7, 13)}"
#     guardian1 = f"Parent{i+1}A"
#     guardian2 = f"Parent{i+1}B"
#     contact1 = 1000000000 + i
#     contact2 = 2000000000 + i

#     # Randomly choose 1 to 3 subjects
#     num_subjects = random.choice([1, 2, 3])
#     selected_subjects = random.sample(subjects_available, num_subjects)

#     # Create student
#     student = Student(
#         studentID=studentID,
#         fName=fName,
#         mName=mName,
#         lName=lName,
#         age=age,
#         addressL1=address[0],
#         addressL2=address[1],
#         addressL3=address[2],
#         addressPostCode=address[3],
#         addressCounty=address[4],
#         schoolYear=schoolYear,
#         schoolSubjects=selected_subjects,
#         nameParGar1=guardian1,
#         nameParGar2=guardian2,
#         contactDetParGar1=contact1,
#         contactDetParGar2=contact2
#     )

#     # Add subject-specific data for each subject
#     for subj in selected_subjects:
#         level = random.choice(["Foundation", "Higher"])
#         class_number = random.randint(1, 5)
#         teacher = random.choice(teachers[subj])
#         test_score = round(random.uniform(50, 100), 2)
        
#         subject_data = create_subject_student(
#             student, subj, level, class_number, teacher, test_score
#         )
#         student.add_grade(subj, test_score)
#         subject_students.append(subject_data)

#     students.append(student)

# # Assumes: 
# # - 'students' is your list of Student instances
# # - 'subject_students' is your list of SubjectStudent instances from subject.py

# for student in students:
#     print(f"Student: {student.fName} {student.lName} (ID: {student.studentID})")
#     print(f"  Age: {student.age}")
#     print(f"  School Year: {student.schoolYear}")
#     print(f"  Enrolled Subjects: {', '.join(student.schoolSubjects)}")

#     # Find and print subject-specific details
#     print("  Subject Details:")
#     for subj in student.schoolSubjects:
#         # Filter for matching subject data for this student
#         matches = [s for s in subject_students if s.student == student and s.subject_name == subj]
#         for subject_data in matches:
#             print(f"    - {subject_data.subject_name}:")
#             print(f"        Level: {subject_data.subject_level}")
#             print(f"        Class Number: {subject_data.subject_class_number}")
#             print(f"        Teacher: {subject_data.subject_teacher}")
#             print(f"        Last Test Score: {subject_data.last_test_score}")
    
#     # Optionally print their overall average
#     avg = student.calculate_overall_average()
#     if avg is not None:
#         print(f"  Overall Average Grade: {avg:.2f}")
#     else:
#         print("  No grades available.")
    
#     print("-" * 60)


# ✅ Example: Show a few students with subject-specific data
# for student in students[:3]:
#     print(student.get_summary_student_data())
#     for subj in student.schoolSubjects:
#         details = [s for s in subject_students if s.student == student and s.subject_name == subj]
#         for d in details:
#             print("  ", d)
#     print("  Average Grade:", student.calculate_overall_average())
#     print("-" * 50)



# from student import Student
# import random

# first_names = ["Alice", "Bob", "Charlie", "Diana", "Edward", "Fiona", "George", "Hannah", "Ian", "Jade",
#                "Kevin", "Laura", "Mike", "Nina", "Oscar", "Paula", "Quinn", "Rachel", "Sam", "Tina"]
# last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Lopez", "Clark"]

# subjects = ["English", "Mathematics", "History"]
# students = []

# for i in range(20):
#     fName = first_names[i]
#     lName = last_names[i % len(last_names)]
#     mName = chr(65 + i)  # Middle initial like 'A', 'B', ...
#     studentID = f"S{i+1:03d}"
#     age = random.randint(11, 17)
#     address = (f"{i+1} Main St", "Apt 1", "District", 12345 + i, "Countyshire")
#     schoolYear = f"Year {random.randint(7, 13)}"
#     guardian1 = f"Parent{i+1}A"
#     guardian2 = f"Parent{i+1}B"
#     contact1 = 1000000000 + i
#     contact2 = 2000000000 + i

#     # Randomly choose 1 to 3 subjects
#     num_subjects = random.choice([1, 2, 3])
#     student_subjects = random.sample(subjects, num_subjects)

#     student = Student(
#         studentID=studentID,
#         fName=fName,
#         mName=mName,
#         lName=lName,
#         age=age,
#         addressL1=address[0],
#         addressL2=address[1],
#         addressL3=address[2],
#         addressPostCode=address[3],
#         addressCounty=address[4],
#         schoolYear=schoolYear,
#         schoolSubjects=student_subjects,
#         nameParGar1=guardian1,
#         nameParGar2=guardian2,
#         contactDetParGar1=contact1,
#         contactDetParGar2=contact2
#     )

#     students.append(student)

# # Example: Print subjects of each student
# for s in students:
#     print(f"{s.studentID}: {s.fName} {s.lName} - Subjects: {s.schoolSubjects}")



# from school import School
# from student import Student
# from subject import MathStudent, EnglishStudent, HistoryStudent
# from grade_calculator import calculate_and_update_grades_for_students, calculate_math_grade, calculate_english_grade, calculate_history_grade, simple_grade_calculation

# def main():
#     # 1. Create a school
#     print("Creating a new school...")
#     school = School(
#         name="Oakridge Academy",
#         address="123 Learning Lane, Edutown",
#         telephoneNumber="555-1234",
#         subjects=["Mathematics", "English", "History", "Science", "Art"]
#     )
#     school.update_school_year("2024-2025")
#     print(school)
#     print("-" * 50)

#     # 2. Create some students
#     print("\nCreating students...")
#     student1 = Student(
#         studentID="S001",
#         fName="John",
#         mName="David",
#         lName="Smith",
#         age=15,
#         addressL1="456 Student Road",
#         addressL2="Apartment 2B",
#         addressL3="",
#         addressPostCode=12345,
#         addressCounty="Lincoln County",
#         schoolYear="10",
#         schoolSubjects=["Science", "Art"],
#         nameParGar1="Jane Smith",
#         nameParGar2="Robert Smith",
#         contactDetParGar1=5551234,
#         contactDetParGar2=5555678,
#         subject_grades={"Science": 85, "Art": 92} 
#     )
    
#     # 3. Create subject-specific students
#     math_student = MathStudent(
#         studentID="S002",
#         fName="Emily",
#         mName="Rose",
#         lName="Johnson",
#         age=16,
#         addressL1="789 Education Ave",
#         addressL2="",
#         addressL3="",
#         addressPostCode=12346,
#         addressCounty="Lincoln County",
#         schoolYear="11",
#         schoolSubjects=["Science"],
#         nameParGar1="Michael Johnson",
#         nameParGar2="Sarah Johnson",
#         contactDetParGar1=5559876,
#         contactDetParGar2=5554321,
#         mathLevel="Advanced",
#         mathClassNumber=101,
#         mathTeacher="Dr. Newton",
#         mathLastTestScore=88
#     )
    
#     english_student = EnglishStudent(
#         studentID="S003",
#         fName="James",
#         mName="Alan",
#         lName="Brown",
#         age=15,
#         addressL1="321 Learning Street",
#         addressL2="",
#         addressL3="",
#         addressPostCode=12347,
#         addressCounty="Lincoln County",
#         schoolYear="10",
#         schoolSubjects=["Art", "Science"],
#         nameParGar1="David Brown",
#         nameParGar2="Lisa Brown",
#         contactDetParGar1=5558765,
#         contactDetParGar2=5552109,
#         englishLevel="Standard",
#         englishClassNumber=102,
#         englishTeacher="Ms. Austen",
#         englishLastTestScore=78
#     )
    
#     history_student = HistoryStudent(
#         studentID="S004",
#         fName="Sophia",
#         mName="Grace",
#         lName="Williams",
#         age=17,
#         addressL1="654 Scholar Way",
#         addressL2="",
#         addressL3="",
#         addressPostCode=12348,
#         addressCounty="Lincoln County",
#         schoolYear="12",
#         schoolSubjects=["Science", "Art"],
#         nameParGar1="Thomas Williams",
#         nameParGar2="Rebecca Williams",
#         contactDetParGar1=5553344,
#         contactDetParGar2=5556677,
#         historyLevel="Honors",
#         historyClassNumber=103,
#         historyTeacher="Mr. Historian",
#         historyLastTestScore=95
#     )
    
#     # Initialize subject_grades dictionary for each student if not exists
#     for student in [math_student, english_student, history_student]:
#         if not hasattr(student, 'subject_grades'):
#             student.subject_grades = {}
    
#     # 4. Register students with the school
#     print("\nRegistering students with the school...")
#     school.register_student(student1)
#     school.register_student(math_student)
#     school.register_student(english_student)
#     school.register_student(history_student)
    
#     # 5. Test student methods
#     print("\nTesting student methods...")
#     print("\nStudent Summary:")
#     print(student1.get_summary_student_data())
    
#     print("\nUpdating student details...")
#     student1.update_age(16)
#     student1.add_subject("Mathematics")
#     student1.add_grade("Mathematics", 80)
    
#     print("\nUpdated student data:")
#     print(student1.get_full_student_data())
    
#     # 6. Test school methods
#     print("\nTesting school methods...")
#     print("\nTotal students:", len(school.get_all_students()))
    
#     print("\nFinding student by ID (S002):")
#     found_student = school.find_student_by_id("S002")
#     if found_student:
#         print(found_student.get_summary_student_data())
    
#     print("\nFinding students by name (first name: Emily):")
#     name_results = school.find_students_by_name(first_name="Emily")
#     if name_results:
#         for student in name_results:
#             print(student.get_summary_student_data())
    
#     print("\nListing students by year (Year 10):")
#     print(school.list_students_by_year(10))
    
#     # 7. Test subject-specific features
#     print("\nTesting subject-specific features...")
    
#     # Option 1: Using simple_grade_calculation (just uses mathLastTestScore, etc.)
#     print("\nCalculating grades using simple method (using lastTestScore)...")
#     students = school.get_all_students()
#     updated_students = simple_grade_calculation(students)
    
#     print("\nCalculated grades:")
#     for student in updated_students:
#         name = f"{student.fName} {student.lName}"
#         if hasattr(student, 'mathGrade'):
#             print(f"{name} - Math Grade: {student.mathGrade}")
#         if hasattr(student, 'englishGrade'):
#             print(f"{name} - English Grade: {student.englishGrade}")
#         if hasattr(student, 'historyGrade'):
#             print(f"{name} - History Grade: {student.historyGrade}")
    
#     # Option 2: Setup additional attributes for detailed grade calculation
#     print("\nSetting up attributes for detailed grade calculation...")
    
#     # Add mathGrades (5 quizzes, test1, test2, final_exam)
#     math_student.mathGrades = [90, 85, 88, 92, 87, 85, 90, 88]
    
#     # Set up English attributes
#     english_student.englishAttendance = 95
#     english_student.englishQuiz1 = 82
#     english_student.englishQuiz2 = 88
#     english_student.englishFinalExam = 85
    
#     # Set up History attributes
#     history_student.historyAttendance = 98
#     history_student.historyProject = 94
#     history_student.historyExams = [90, 92]
    
#     # Calculate grades using the updated grade calculator
#     print("\nCalculating grades using detailed method...")
#     updated_students = calculate_and_update_grades_for_students(students)
    
#     print("\nUpdated calculated grades:")
#     for student in updated_students:
#         name = f"{student.fName} {student.lName}"
#         if hasattr(student, 'mathGrade'):
#             print(f"{name} - Math Grade: {student.mathGrade}")
#         if hasattr(student, 'englishGrade'):
#             print(f"{name} - English Grade: {student.englishGrade}")
#         if hasattr(student, 'historyGrade'):
#             print(f"{name} - History Grade: {student.historyGrade}")
    
#     # 8. Test average grade calculation
#     print("\nCalculating average grades by subject:")
#     math_avg = school.get_average_grade("Mathematics")
#     if math_avg:
#         print(f"Average Mathematics grade: {math_avg}")
    
#     english_avg = school.get_average_grade("English")
#     if english_avg:
#         print(f"Average English grade: {english_avg}")
    
#     history_avg = school.get_average_grade("History")
#     if history_avg:
#         print(f"Average History grade: {history_avg}")
    
#     # 9. Testing subject grading formulas directly
#     print("\nTesting grade calculation formulas directly:")
    
#     math_grade = calculate_math_grade([90, 85, 88, 92, 87], 85, 90, 88)
#     print(f"Calculated Math grade: {math_grade}")
    
#     english_grade = calculate_english_grade(95, [82, 88], 85)
#     print(f"Calculated English grade: {english_grade}")
    
#     history_grade = calculate_history_grade(98, 94, [90, 92])
#     print(f"Calculated History grade: {history_grade}")
    
#     # 10. Remove a student
#     print("\nRemoving a student...")
#     school.remove_student("S001")
#     print(f"Total students after removal: {len(school.get_all_students())}")
    
#     # 11. Test subject enrollments
#     print("\nStudents enrolled in Mathematics:")
#     print(school.list_students_by_subject("Mathematics"))

# if __name__ == "__main__":
#     main()



# from student import Student
# from school import School

# student1=Student("001", "Michael", "Joseph", "Markey", 42, "64 The Avenue", "Woodpark", "Ballinteer", 16, "Dublin", "6th", 
#                  ["English", "Maths"], "Dympna Markey", "Michael Markey", "012980884", "0875896936",
#                  {"History":76, "Maths":92})

# student2 = Student("002", "Mia", "Lee", "Johnson", 16, "49 Main Street", "Suburbia", "Dublin", 5, "Dublin", "4th", 
#                    ["History", "Maths"], "Alice Smith", "Mark Taylor", "012345601", "0871234501", 
#                    {"History": 75, "Maths": 80})

# student3 = Student("003", "Isabella", "Paul", "Martin", 15, "25 Main Street", "Suburbia", "Dublin", 8, "Dublin", "6th", 
#                    ["History", "English", "Maths"], "Diana Anderson", "Karen Johnson", "012345602", "0871234502", 
#                    {"History": 82, "English": 88, "Maths": 74})

# student4 = Student("004", "Lucas", "Marie", "Martin", 17, "69 Main Street", "Suburbia", "Dublin", 12, "Dublin", "1st", 
#                    ["History", "Maths", "English"], "Robert Brown", "Mark Taylor", "012345603", "0871234503", 
#                    {"History": 85, "Maths": 91, "English": 79})

# student5 = Student("005", "Noah", "Lee", "Thomas", 14, "29 Main Street", "Suburbia", "Dublin", 9, "Dublin", "1st", 
#                    ["Maths", "English"], "Diana Anderson", "Karen Johnson", "012345604", "0871234504", 
#                    {"Maths": 67, "English": 74})

# student6 = Student("006", "Olivia", "Ray", "Johnson", 18, "14 Main Street", "Suburbia", "Dublin", 4, "Dublin", "6th", 
#                    ["History", "Maths"], "Robert Brown", "Robert Brown", "012345605", "0871234505", 
#                    {"History": 68, "Maths": 85})

# student7 = Student("007", "Liam", "Jay", "Murphy", 13, "70 Oak Drive", "Greenfield", "Dublin", 16, "Dublin", "3rd", 
#                    ["English"], "Laura Murphy", "Kevin Murphy", "012345606", "0871234506", 
#                    {"English": 79})

# student8 = Student("008", "Emma", "Grace", "Walsh", 15, "88 Elm Road", "Cherrywood", "Dublin", 15, "Dublin", "4th", 
#                    ["History", "English"], "John Walsh", "Catherine Walsh", "012345607", "0871234507", 
#                    {"History": 92, "English": 85})

# student9 = Student("009", "Jack", "Ryan", "Kelly", 17, "19 Birch Lane", "Kilmainham", "Dublin", 10, "Dublin", "5th", 
#                    ["Maths"], "Sarah Kelly", "Sean Kelly", "012345608", "0871234508", 
#                    {"Maths": 72})

# student10 = Student("010", "Ava", "Skye", "Byrne", 14, "45 Cedar Park", "Crumlin", "Dublin", 12, "Dublin", "2nd", 
#                     ["English", "Maths"], "James Byrne", "Helen Byrne", "012345609", "0871234509", 
#                     {"English": 88, "Maths": 65})

# student11 = Student("011", "Ethan", "Max", "O'Brien", 16, "67 Pine Street", "Rathmines", "Dublin", 6, "Dublin", "4th", 
#                     ["English", "History"], "Mary O'Brien", "David O'Brien", "012345610", "0871234510", 
#                     {"English": 78, "History": 85})

# student12 = Student("012", "Sophia", "Rose", "Doyle", 15, "12 Willow Grove", "Sandyford", "Dublin", 18, "Dublin", "5th", 
#                     ["History"], "Karen Doyle", "Tom Doyle", "012345611", "0871234511", 
#                     {"History": 94})

# student13 = Student("013", "Daniel", "Lee", "Moore", 17, "33 Fir Street", "Donnybrook", "Dublin", 4, "Dublin", "6th", 
#                     ["Maths", "English"], "Claire Moore", "Brendan Moore", "012345612", "0871234512", 
#                     {"Maths": 78, "English": 83})

# student14 = Student("014", "Grace", "Lily", "O'Connor", 13, "20 Ash Close", "Drimnagh", "Dublin", 12, "Dublin", "1st", 
#                     ["English"], "Nora O'Connor", "James O'Connor", "012345613", "0871234513", 
#                     {"English": 90})

# student15 = Student("015", "Ben", "Alex", "Ryan", 18, "54 Maple Avenue", "Tallaght", "Dublin", 24, "Dublin", "6th", 
#                     ["Maths", "History", "English"], "Louise Ryan", "Chris Ryan", "012345614", "0871234514", 
#                     {"Maths": 75, "History": 80, "English": 89})

# student16 = Student("016", "Ella", "May", "Smith", 14, "18 Cherry Court", "Lucan", "Dublin", 22, "Dublin", "2nd", 
#                     ["History", "English"], "Jenny Smith", "Alan Smith", "012345615", "0871234515", 
#                     {"History": 85, "English": 82})

# student17 = Student("017", "James", "Finn", "Murray", 15, "72 Beech Drive", "Rathfarnham", "Dublin", 14, "Dublin", "3rd", 
#                     ["Maths"], "Rachel Murray", "Thomas Murray", "012345616", "0871234516", 
#                     {"Maths": 77})

# student18 = Student("018", "Chloe", "Hope", "Brady", 17, "36 Poplar Row", "Terenure", "Dublin", 6, "Dublin", "5th", 
#                     ["English", "Maths"], "Fiona Brady", "Stephen Brady", "012345617", "0871234517", 
#                     {"English": 83, "Maths": 78})

# student19 = Student("019", "Ryan", "Liam", "Kavanagh", 16, "90 Spruce Hill", "Clondalkin", "Dublin", 22, "Dublin", "4th", 
#                     ["History", "English", "Maths"], "Donna Kavanagh", "Greg Kavanagh", "012345618", "0871234518", 
#                     {"History": 80, "English": 86, "Maths": 77})

# student20 = Student("020", "Zoe", "Anne", "Nolan", 15, "7 Holly Way", "Portobello", "Dublin", 8, "Dublin", "3rd", 
#                     ["History"], "Aisling Nolan", "Brian Nolan", "012345619", "0871234519", 
#                     {"History": 90})


# students = [student1, student2, student3, student4, student5,student6, student7, student8, student9, student10, student11, student12, student13, student14, student15, student16, student17, student18, student19, student20]

# print(student1.calculate_overall_average())
# student1.add_grade("English", "75")
# print(student1.calculate_overall_average())

# school1 = School("Dublin High School", "123 School St, Dublin", "01-2345678", ["English", "Maths", "History"])

# for student in students:
#     school1.register_student(student)

# # for student in school1.get_all_students():
# #     print(student.get_summary_student_data())

# #print(school1.get_all_students())
# print(school1.get_student_by_id("015"))
# school1.remove_student("019")
# print(school1.find_student_by_id("018"))
# print(school1.find_students_by_name(first_name="Ryan", last_name="Kavanagh"))
# print(school1.list_students_by_subject("English"))
# print(school1.list_students_by_year("3rd"))

# #print(school1)

# school1.update_school_name("Dublin Low School")
# school1.update_school_address("456 School St, Dublin")
# school1.update_school_year("1984")
# school1.update_school_telephone("012980884")
# school1.update_school_subjects(["English", "Maths", "History"])
# school1.add_subject("Biology")
# school1.remove_subject("English")

#print(school1)



# student1 = Student("001", "Michael", "Joseph", "Markey", 42, "64 The Avenue", "Woodpark", "Ballinteer", 16, "Dublin", "6th", ["English", "Maths"], "Dympna Markey", "Michael Markey", "012980884", "0875896936")
# print(student1)

# student1.update_ID("002")
# student1.update_name("Michael", "James", "Markey")
# student1.update_address("67 The Avenue", "Woodpark", "Ballinteer", 16, "Dublin")
# student1.update_age(16)
# student1.update_school_year("5th")
# student1.add_subject("History")
# student1.remove_subject("English")
# student1.update_guardian_contact(1, "Cynthia Markey", "0872156598")
# print(student1)

# print(student1.get_full_student_data())
# print(student1.get_summary_student_data())
# print(student1.get_full_address())
# print(student1.get_guardian_info())
# print(student1.get_subjects())

# print(student1.is_full_name_available())
# print(student1.is_address_complete())
# print(student1.is_in_year("6th"))
# print(student1.is_enrolled_in("Maths"))
# print(student1.is_guardian_contact_available(1))




# What I'm testing

# Class – Student

# Attributes – self, studentID, fName, mName, lName, age, addressL1, addressL2, addressL3, addressPostCode, addressCounty, schoolYear, nameParGar1, nameParGar2, contactDetParGar1, contactDetParGar2

# Methods – 

# #update_and_add
# updateID, update_name, update_age, update_school_year, update_subjects , update_guardian_contact, add_subject, remove_subject, 

# #get
# get_full_student_data
# get_summary_student_data
# get_full_address
# get_guardian_info
# get_subjects

# #check
# is_ful_name_available
# is_address_complete
# is_in_year
# is_enrolled
# is_guardian_contact_available