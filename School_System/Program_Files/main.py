from csv_loader import (
    load_students_from_csv,
    load_maths_grades_from_csv,
    load_english_grades_from_csv,
    load_history_grades_from_csv,
)
from school import School

def main():
    # Load students
    students = load_students_from_csv("students.csv")
    print(f"✅ Loaded {len(students)} students.\n")

    # Load grades
    load_maths_grades_from_csv("mathematics.csv", students)
    load_english_grades_from_csv("english.csv", students)
    load_history_grades_from_csv("history.csv", students)
    print("✅ All subject grades loaded.\n")

    # Create School instance
    school = School("Test High School", "1 Example Ave")

    # Add students to school
    for student in students:
        school.add_student(student)

    # Print school summary
    print("📘 School Overview:")
    print(school, "\n")

    # Print details for first 5 students
    print("📋 Sample Student Records:\n")
    for i, student in enumerate(students[:5], start=1):
        print(f"--- Student {i}: {student.fName} {student.lName} ---")
        print(student)  # Assumes __repr__ on Student includes grade info
        print("-" * 40)

if __name__ == "__main__":
    main()
