from student import Student
from school import School

def test_school():
    # Test 1: Create a school
    school = School(name="Greenwood Academy", address="789 Oak Rd, Greenwood", school_year=2025, subjects=["Mathematics", "English", "History"])
    print("\nSchool created:")
    print(school)
    
    # Test 2: Create students with different combinations of subjects
    student1 = Student(fName="John", mName="Doe", lName="Smith", 
                       addressL1="123 Main St", addressL2="Apt 4B", addressL3="Springfield", 
                       addressPostCode="12345", addressCounty="Springfield", schoolYear=10,
                       schoolSubjects=["Mathematics", "English", "History"], 
                       nameParGar1="Jane Smith", nameParGar2="Jake Smith", 
                       contactDetParGar1="555-1234", contactDetParGar2="555-5678")
    
    student2 = Student(fName="Alice", mName="Marie", lName="Johnson", 
                       addressL1="456 Elm St", addressL2=None, addressL3=None, 
                       addressPostCode="54321", addressCounty="Greenville", schoolYear=11,
                       schoolSubjects=["English", "History"], 
                       nameParGar1="Emily Johnson", nameParGar2="Mark Johnson", 
                       contactDetParGar1="555-8765", contactDetParGar2="555-4321")
    
    student3 = Student(fName="Michael", mName="James", lName="Brown", 
                       addressL1="789 Pine St", addressL2="Apt 2A", addressL3="Downtown", 
                       addressPostCode="98765", addressCounty="Pinehill", schoolYear=9,
                       schoolSubjects=["Mathematics", "History"], 
                       nameParGar1="Sarah Brown", nameParGar2="William Brown", 
                       contactDetParGar1="555-3333", contactDetParGar2="555-4444")
    
    student4 = Student(fName="Sophia", mName="Grace", lName="Davis", 
                       addressL1="101 Maple St", addressL2=None, addressL3=None, 
                       addressPostCode="67890", addressCounty="Maplewood", schoolYear=12,
                       schoolSubjects=["Mathematics", "English"], 
                       nameParGar1="Laura Davis", nameParGar2="Chris Davis", 
                       contactDetParGar1="555-5555", contactDetParGar2="555-6666")
    
    student5 = Student(fName="David", mName="Lee", lName="Miller", 
                       addressL1="202 Oak St", addressL2="Suite 3B", addressL3="Hillside", 
                       addressPostCode="11223", addressCounty="Hillside", schoolYear=11,
                       schoolSubjects=["History"], 
                       nameParGar1="Tina Miller", nameParGar2="Richard Miller", 
                       contactDetParGar1="555-7777", contactDetParGar2="555-8888")
    
    # Test 3: Add students to the school
    school.add_student(student1)
    school.add_student(student2)
    school.add_student(student3)
    school.add_student(student4)
    school.add_student(student5)
    
    # Test 4: Try adding a student that already exists
    school.add_student(student1)  # This should print a message about the student already existing.

    # Test 5: Remove a student from the school
    school.remove_student(student2)  # Removing Alice Johnson
    school.remove_student(student5)  # Removing David Miller

    # Test 6: Try removing a student who does not exist
    school.remove_student(student2)  # This should print a "not found" message because Alice was already removed.

    # Test 7: Find a student by name
    found_student = school.find_student_by_name("Michael", "Brown")
    if found_student:
        print("\nFound student:", found_student)
    else:
        print("\nStudent not found.")

    found_student = school.find_student_by_name("Alice", "Johnson")  # Should not be found (removed)
    if found_student:
        print("\nFound student:", found_student)
    else:
        print("\nStudent not found.")

    # Test 8: List students by subject
    students_in_english = school.list_students_by_subject("English")
    print("\nStudents taking English:", students_in_english)

    students_in_mathematics = school.list_students_by_subject("Mathematics")
    print("\nStudents taking Mathematics:", students_in_mathematics)

    students_in_history = school.list_students_by_subject("History")
    print("\nStudents taking History:", students_in_history)

    # Test 9: Get average grade for Mathematics
    student1.finalMathematicsGrade = 85
    student3.finalMathematicsGrade = 90
    average_math_grade = school.get_average_grade("Mathematics")
    print("\nAverage Mathematics grade:", average_math_grade)

    # Test 10: Get average grade for History
    student1.finalHistoryGrade = 88
    student3.finalHistoryGrade = 92
    student4.finalHistoryGrade = 95
    average_history_grade = school.get_average_grade("History")
    print("\nAverage History grade:", average_history_grade)

    # Test 11: Get average grade for a subject with no grades (e.g., English)
    average_english_grade = school.get_average_grade("English")
    print("\nAverage English grade (should be None):", average_english_grade)

    # Test 12: Update school details
    school.update_school_name("Pinehill Academy")
    school.update_school_address("500 Pine Rd, Pinehill")
    school.update_school_year(2026)
    school.update_school_subjects(["Mathematics", "English", "History", "Geography"])

    # Test 13: Check the updated school details
    print("\nUpdated school details:")
    print(school)

    # Test 14: School's representation
    print("\nSchool's full representation:")
    print(school)

if __name__ == "__main__":
    test_school()
