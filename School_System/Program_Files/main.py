# Testing student, school, subject and grade_calculator classes together

# main.py - Enhanced test file for school system
from student import Student
from school import School
from subject import MathStudent, EnglishStudent, HistoryStudent
import grade_calculator

def main():
    # Create a school
    school = School(
        name="Springfield High School",
        address="123 Learning Lane, Springfield, SP12 3ED",
        telephoneNumber="01234 567890",
        subjects=["Mathematics", "English", "History"]
    )
    print(f"Created school: {school.name}")
    
    # Create 10 students with different details
    students = [
        Student(
            studentID="S001",
            fName="John", 
            mName="Robert", 
            lName="Smith", 
            age=15,
            addressL1="10 Oak Street", 
            addressL2="Greenville", 
            addressL3="", 
            addressPostCode="GR5 7TY", 
            addressCounty="Westshire",
            schoolYear=10, 
            schoolSubjects=[], 
            nameParGar1="Mary Smith", 
            nameParGar2="David Smith",
            contactDetParGar1="07700 900123", 
            contactDetParGar2="07700 900124"
        ),
        Student(
            studentID="S002",
            fName="Emma", 
            mName="Louise", 
            lName="Jones", 
            age=16,
            addressL1="25 Maple Avenue", 
            addressL2="Riverdale", 
            addressL3="", 
            addressPostCode="RD8 9PQ", 
            addressCounty="Eastshire",
            schoolYear=11, 
            schoolSubjects=[], 
            nameParGar1="Sarah Jones", 
            nameParGar2="Thomas Jones",
            contactDetParGar1="07700 900125", 
            contactDetParGar2="07700 900126"
        ),
        Student(
            studentID="S003",
            fName="Michael", 
            mName="James", 
            lName="Brown", 
            age=14,
            addressL1="5 Pine Road", 
            addressL2="Hilltown", 
            addressL3="", 
            addressPostCode="HT3 4LM", 
            addressCounty="Northshire",
            schoolYear=9, 
            schoolSubjects=[], 
            nameParGar1="Jennifer Brown", 
            nameParGar2="Richard Brown",
            contactDetParGar1="07700 900127", 
            contactDetParGar2="07700 900128"
        ),
        Student(
            studentID="S004",
            fName="Sophia", 
            mName="Grace", 
            lName="Wilson", 
            age=15,
            addressL1="17 Cedar Lane", 
            addressL2="Lakeside", 
            addressL3="", 
            addressPostCode="LS6 2FG", 
            addressCounty="Southshire",
            schoolYear=10, 
            schoolSubjects=[], 
            nameParGar1="Patricia Wilson", 
            nameParGar2="William Wilson",
            contactDetParGar1="07700 900129", 
            contactDetParGar2="07700 900130"
        ),
        Student(
            studentID="S005",
            fName="Olivia", 
            mName="Emily", 
            lName="Taylor", 
            age=16,
            addressL1="32 Birch Street", 
            addressL2="Mountainview", 
            addressL3="", 
            addressPostCode="MV9 1JK", 
            addressCounty="Westshire",
            schoolYear=11, 
            schoolSubjects=[], 
            nameParGar1="Elizabeth Taylor", 
            nameParGar2="Robert Taylor",
            contactDetParGar1="07700 900131", 
            contactDetParGar2="07700 900132"
        ),
        Student(
            studentID="S006",
            fName="Ethan", 
            mName="Daniel", 
            lName="Martin", 
            age=14,
            addressL1="8 Elm Road", 
            addressL2="Valleytown", 
            addressL3="", 
            addressPostCode="VT2 5HJ", 
            addressCounty="Eastshire",
            schoolYear=9, 
            schoolSubjects=[], 
            nameParGar1="Karen Martin", 
            nameParGar2="Christopher Martin",
            contactDetParGar1="07700 900133", 
            contactDetParGar2="07700 900134"
        ),
        Student(
            studentID="S007",
            fName="Ava", 
            mName="Charlotte", 
            lName="Anderson", 
            age=15,
            addressL1="14 Willow Avenue", 
            addressL2="Brookside", 
            addressL3="", 
            addressPostCode="BS7 6KL", 
            addressCounty="Northshire",
            schoolYear=10, 
            schoolSubjects=[], 
            nameParGar1="Michelle Anderson", 
            nameParGar2="Daniel Anderson",
            contactDetParGar1="07700 900135", 
            contactDetParGar2="07700 900136"
        ),
        Student(
            studentID="S008",
            fName="Noah", 
            mName="Thomas", 
            lName="Thompson", 
            age=16,
            addressL1="29 Sycamore Lane", 
            addressL2="Clifftop", 
            addressL3="", 
            addressPostCode="CT4 8NM", 
            addressCounty="Southshire",
            schoolYear=11, 
            schoolSubjects=[], 
            nameParGar1="Laura Thompson", 
            nameParGar2="James Thompson",
            contactDetParGar1="07700 900137", 
            contactDetParGar2="07700 900138"
        ),
        Student(
            studentID="S009",
            fName="Isabella", 
            mName="Sophia", 
            lName="Walker", 
            age=14,
            addressL1="3 Aspen Street", 
            addressL2="Meadowland", 
            addressL3="", 
            addressPostCode="ML1 3OP", 
            addressCounty="Westshire",
            schoolYear=9, 
            schoolSubjects=[], 
            nameParGar1="Emily Walker", 
            nameParGar2="Matthew Walker",
            contactDetParGar1="07700 900139", 
            contactDetParGar2="07700 900140"
        ),
        Student(
            studentID="S010",
            fName="Jacob", 
            mName="Alexander", 
            lName="White", 
            age=15,
            addressL1="22 Redwood Road", 
            addressL2="Seaside", 
            addressL3="", 
            addressPostCode="SS0 2QR", 
            addressCounty="Eastshire",
            schoolYear=10, 
            schoolSubjects=[], 
            nameParGar1="Samantha White", 
            nameParGar2="Andrew White",
            contactDetParGar1="07700 900141", 
            contactDetParGar2="07700 900142"
        )
    ]
    
    # Create subject-specific students
    math_students = []
    english_students = []
    history_students = []
    
    # Add students to the school and create subject-specific student objects
    print("\n=== Enrolling Students ===")
    for i, student in enumerate(students):
        # Add student to school
        school.add_student(student)
        
        # Math student creation
        math_level = "Advanced" if i % 3 == 0 else "Standard" if i % 3 == 1 else "Basic"
        math_class = f"M{(i % 3) + 1}"
        math_teacher = ["Mr. Newton", "Ms. Pascal", "Mr. Euler"][i % 3]
        math_score = 85 + (i % 3) * 5
        
        math_student = MathStudent(
            student.studentID, student.fName, student.mName, student.lName, 
            student.age, student.addressL1, student.addressL2, student.addressL3, 
            student.addressPostCode, student.addressCounty, student.schoolYear,
            student.schoolSubjects, student.nameParGar1, student.nameParGar2,
            student.contactDetParGar1, student.contactDetParGar2,
            math_level, math_class, math_teacher, math_score
        )
        math_students.append(math_student)
        
        # English student creation
        english_level = "Advanced" if i % 3 == 1 else "Standard" if i % 3 == 2 else "Basic"  
        english_class = f"E{(i % 3) + 1}"
        english_teacher = ["Ms. Austen", "Mr. Shakespeare", "Ms. Woolf"][i % 3]
        english_score = 80 + (i % 3) * 5
        
        english_student = EnglishStudent(
            student.studentID, student.fName, student.mName, student.lName, 
            student.age, student.addressL1, student.addressL2, student.addressL3, 
            student.addressPostCode, student.addressCounty, student.schoolYear,
            student.schoolSubjects, student.nameParGar1, student.nameParGar2,
            student.contactDetParGar1, student.contactDetParGar2,
            english_level, english_class, english_teacher, english_score
        )
        english_students.append(english_student)
        
        # History student creation
        history_level = "Advanced" if i % 3 == 2 else "Standard" if i % 3 == 0 else "Basic"
        history_class = f"H{(i % 3) + 1}"
        history_teacher = ["Dr. Churchill", "Ms. Victoria", "Mr. Tudor"][i % 3]
        history_score = 75 + (i % 3) * 5
        
        history_student = HistoryStudent(
            student.studentID, student.fName, student.mName, student.lName, 
            student.age, student.addressL1, student.addressL2, student.addressL3, 
            student.addressPostCode, student.addressCounty, student.schoolYear,
            student.schoolSubjects, student.nameParGar1, student.nameParGar2,
            student.contactDetParGar1, student.contactDetParGar2,
            history_level, history_class, history_teacher, history_score
        )
        history_students.append(history_student)
    
    # Update the subjects for students in the school
    for student_id in school.students:
        student = school.students[student_id]
        student.schoolSubjects = ["Mathematics", "English", "History"]

    # Print the school information
    print("\n=== School Information ===")
    print(school)
    
    # Add grade data to students for the grade calculator
    print("\n=== Adding Grade Data ===")
    for i, student in enumerate(students):
        # Add Mathematics raw grades
        student.mathGrades = [
            90 + i % 5,  # Quiz 1
            85 + i % 7,  # Quiz 2
            88 + i % 6,  # Quiz 3
            92 + i % 4,  # Quiz 4
            87 + i % 8,  # Quiz 5
            85 + i % 10,  # Test 1
            88 + i % 9,   # Test 2
            90 + i % 5    # Final Exam
        ]
        
        # Add English raw grades
        student.englishAttendance = 95 - i % 10
        student.englishQuiz1 = 85 + i % 10
        student.englishQuiz2 = 88 + i % 8
        student.englishFinalExam = 87 + i % 7
        
        # Add History raw grades
        student.historyAttendance = 92 - i % 8
        student.historyProject = 88 + i % 9
        student.historyExams = [85 + i % 10, 89 + i % 7]
        
        print(f"Added grade data for {student.fName} {student.lName}")
    
    # Calculate and update grades
    print("\n=== Calculating Grades ===")
    grade_calculator.calculate_and_update_grades_for_students(students)
    
    # Print student details with grades
    print("\n=== Student Grade Report ===")
    for student in students:
        print(f"\n{student.fName} {student.lName} - Year {student.schoolYear}")
        print(f"Mathematics Grade: {student.mathGrade:.2f}")
        print(f"English Grade: {student.englishGrade:.2f}")
        print(f"History Grade: {student.historyGrade:.2f}")
        print("-" * 40)
    
    # Test the school methods for listing students by subject
    print("\n=== Students Taking Mathematics ===")
    math_students_list = school.list_students_by_subject("Mathematics")
    print(math_students_list)
    
    print("\n=== Students Taking English ===")
    english_students_list = school.list_students_by_subject("English")
    print(english_students_list)
    
    print("\n=== Students Taking History ===")
    history_students_list = school.list_students_by_subject("History")
    print(history_students_list)
    
    # Calculate average grades
    # Note: The School's get_average_grade method expects the grades to be stored 
    # as finalMathematicsGrade, finalEnglishGrade, and finalHistoryGrade,
    # but our current structure uses mathGrade, englishGrade, and historyGrade.
    # Let's add these attributes for compatibility
    for student in students:
        student.finalMathematicsGrade = student.mathGrade
        student.finalEnglishGrade = student.englishGrade
        student.finalHistoryGrade = student.historyGrade
    
    math_avg = school.get_average_grade("Mathematics")
    english_avg = school.get_average_grade("English")
    history_avg = school.get_average_grade("History")
    
    print("\n=== School Average Grades ===")
    print(f"Mathematics Average: {math_avg}")
    print(f"English Average: {english_avg}")
    print(f"History Average: {history_avg}")

if __name__ == "__main__":
    main()

# # main.py - Test file for school system 1
# from student import Student
# from school import School
# from subject import MathStudent, EnglishStudent, HistoryStudent
# import grade_calculator

# def main():
#     print("\n=== SCHOOL SYSTEM TEST ===\n")
    
#     # Create a school
#     print("Creating school...")
#     woodland_high = School(
#         name="Woodland High School",
#         address="123 Forest Lane, Woodland, WD12 3AB",
#         telephoneNumber="01234 567890",
#         subjects=["Mathematics", "English", "History", "Physics", "Chemistry", "Biology", "Art", "Music"]
#     )
#     print(woodland_high)
#     print("-" * 50)
    
#     # Create regular students
#     print("\n=== CREATING REGULAR STUDENTS ===")
#     students = [
#         Student(
#             studentID="S001", 
#             fName="John", mName="Robert", lName="Smith",
#             age=16,
#             addressL1="10 Oak Street", addressL2="Oakville", addressL3="", 
#             addressPostCode="OA1 2BC", addressCounty="Oakshire",
#             schoolYear=11,
#             schoolSubjects=["Physics", "Chemistry"],
#             nameParGar1="Mary Smith", nameParGar2="David Smith",
#             contactDetParGar1="07777 123456", contactDetParGar2="07777 654321"
#         ),
#         Student(
#             studentID="S002", 
#             fName="Emily", mName="", lName="Johnson",
#             age=15,
#             addressL1="25 Maple Drive", addressL2="", addressL3="Mapletown", 
#             addressPostCode="MP3 4DE", addressCounty="Mapleshire",
#             schoolYear=10,
#             schoolSubjects=["Art", "Music"],
#             nameParGar1="Sarah Johnson", nameParGar2="",
#             contactDetParGar1="07777 222333", contactDetParGar2=""
#         )
#     ]
    
#     # Add students to school
#     for student in students:
#         woodland_high.add_student(student)
#         print(student.get_summary_student_data())
    
#     # Create subject-specific students
#     print("\n=== CREATING SUBJECT STUDENTS ===")
    
#     # Math students
#     math_students = [
#         MathStudent(
#             studentID="S003", 
#             fName="Alice", mName="Marie", lName="Williams",
#             age=17,
#             addressL1="5 Pine Close", addressL2="Pineville", addressL3="", 
#             addressPostCode="PN5 6FG", addressCounty="Pineshire",
#             schoolYear=12,
#             schoolSubjects=["Physics", "Chemistry"],
#             nameParGar1="Robert Williams", nameParGar2="Helen Williams",
#             contactDetParGar1="07777 333444", contactDetParGar2="07777 444555",
#             mathLevel="Advanced", mathClassNumber=2, mathTeacher="Mr. Thompson",
#             mathLastTestScore=92
#         ),
#         MathStudent(
#             studentID="S004", 
#             fName="Daniel", mName="", lName="Brown",
#             age=16,
#             addressL1="12 Cedar Road", addressL2="", addressL3="Cedartown", 
#             addressPostCode="CD7 8HI", addressCounty="Cedarshire",
#             schoolYear=11,
#             schoolSubjects=["Physics"],
#             nameParGar1="James Brown", nameParGar2="Linda Brown",
#             contactDetParGar1="07777 555666", contactDetParGar2="07777 666777",
#             mathLevel="Intermediate", mathClassNumber=3, mathTeacher="Mrs. Davis",
#             mathLastTestScore=85
#         )
#     ]
    
#     # English students
#     english_students = [
#         EnglishStudent(
#             studentID="S005", 
#             fName="Sophia", mName="Grace", lName="Taylor",
#             age=17,
#             addressL1="8 Elm Avenue", addressL2="Elmville", addressL3="", 
#             addressPostCode="EL9 0JK", addressCounty="Elmshire",
#             schoolYear=12,
#             schoolSubjects=["History", "Art"],
#             nameParGar1="Michael Taylor", nameParGar2="Catherine Taylor",
#             contactDetParGar1="07777 777888", contactDetParGar2="07777 888999",
#             englishLevel="Advanced", englishClassNumber=1, englishTeacher="Mr. Wilson",
#             englishLastTestScore=94
#         ),
#         EnglishStudent(
#             studentID="S006", 
#             fName="Oliver", mName="James", lName="Davies",
#             age=15,
#             addressL1="15 Birch Lane", addressL2="", addressL3="Birchtown", 
#             addressPostCode="BI1 2LM", addressCounty="Birchshire",
#             schoolYear=10,
#             schoolSubjects=["Music"],
#             nameParGar1="Thomas Davies", nameParGar2="Emma Davies",
#             contactDetParGar1="07777 999000", contactDetParGar2="07777 000111",
#             englishLevel="Intermediate", englishClassNumber=2, englishTeacher="Ms. Roberts",
#             englishLastTestScore=88
#         )
#     ]
    
#     # History students
#     history_students = [
#         HistoryStudent(
#             studentID="S007", 
#             fName="Charlotte", mName="Anne", lName="Evans",
#             age=16,
#             addressL1="22 Willow Street", addressL2="Willowville", addressL3="", 
#             addressPostCode="WI3 4NO", addressCounty="Willowshire",
#             schoolYear=11,
#             schoolSubjects=["English", "Art"],
#             nameParGar1="Richard Evans", nameParGar2="Patricia Evans",
#             contactDetParGar1="07777 111222", contactDetParGar2="07777 222333",
#             historyLevel="Advanced", historyClassNumber=1, historyTeacher="Mrs. Jackson",
#             historyLastTestScore=91
#         ),
#         HistoryStudent(
#             studentID="S008", 
#             fName="Jack", mName="", lName="Harris",
#             age=17,
#             addressL1="30 Aspen Way", addressL2="", addressL3="Aspentown", 
#             addressPostCode="AS5 6PQ", addressCounty="Aspenshire",
#             schoolYear=12,
#             schoolSubjects=["English", "Music"],
#             nameParGar1="Steven Harris", nameParGar2="Jennifer Harris",
#             contactDetParGar1="07777 333444", contactDetParGar2="07777 444555",
#             historyLevel="Advanced", historyClassNumber=2, historyTeacher="Mr. Parker",
#             historyLastTestScore=87
#         )
#     ]
    
#     # Add all subject students to the school
#     subject_students = math_students + english_students + history_students
#     for student in subject_students:
#         woodland_high.add_student(student)
#         print(f"Added {student.fName} {student.lName} ({student.studentID}) as a subject student")
    
#     # Test updating student information
#     print("\n=== TESTING UPDATE METHODS ===")
#     test_student = woodland_high.find_student_by_id("S001")
#     if test_student:
#         print(f"Before update: {test_student.get_summary_student_data()}")
#         test_student.update_name(new_fName="Johnny")
#         test_student.update_age(17)
#         test_student.add_subject("Mathematics")
#         print(f"After update: {test_student.get_summary_student_data()}")
#         print(f"Updated subjects: {test_student.get_subjects()}")
    
#     # Test subject-specific features
#     print("\n=== TESTING SUBJECT-SPECIFIC FEATURES ===")
    
#     # Set up raw grade data and calculate grades separately for each subject type
#     print("\nCalculating and updating grades...")
    
#     # Calculate Math grades only for Math students
#     for student in math_students:
#         # Set up raw math grades [quiz1, quiz2, quiz3, quiz4, quiz5, test1, test2, final]
#         student.mathGrades = [85, 90, 88, 92, 87, 89, 91, 94]
        
#         try:
#             quizzes = student.mathGrades[0:5]
#             test1, test2 = student.mathGrades[5], student.mathGrades[6]
#             final_exam = student.mathGrades[7]
#             student.mathGrade = grade_calculator.calculate_math_grade(quizzes, test1, test2, final_exam)
#         except Exception as e:
#             print(f"[Math] Could not calculate for {student.fName} {student.lName}: {e}")
    
#     # Calculate English grades only for English students  
#     for student in english_students:
#         student.englishAttendance = 95
#         student.englishQuiz1 = 88
#         student.englishQuiz2 = 92
#         student.englishFinalExam = 90
        
#         try:
#             attendance = student.englishAttendance
#             quizzes = [student.englishQuiz1, student.englishQuiz2]
#             final_exam = student.englishFinalExam
#             student.englishGrade = grade_calculator.calculate_english_grade(attendance, quizzes, final_exam)
#         except Exception as e:
#             print(f"[English] Could not calculate for {student.fName} {student.lName}: {e}")
    
#     # Calculate History grades only for History students
#     for student in history_students:
#         student.historyAttendance = 92
#         student.historyProject = 88
#         student.historyExams = [85, 90]
        
#         try:
#             attendance = student.historyAttendance
#             project = student.historyProject
#             exams = student.historyExams
#             student.historyGrade = grade_calculator.calculate_history_grade(attendance, project, exams)
#         except Exception as e:
#             print(f"[History] Could not calculate for {student.fName} {student.lName}: {e}")
    
#     # Display results
#     print("\n=== FINAL GRADES ===")
#     for student in math_students:
#         print(f"{student.fName} {student.lName} - Math Grade: {student.mathGrade}")
    
#     for student in english_students:
#         print(f"{student.fName} {student.lName} - English Grade: {student.englishGrade}")
    
#     for student in history_students:
#         print(f"{student.fName} {student.lName} - History Grade: {student.historyGrade}")
    
#     # Test school statistics methods
#     print("\n=== SCHOOL STATISTICS ===")
    
#     # List students by subject
#     print("\nStudents taking Mathematics:")
#     math_student_list = woodland_high.list_students_by_subject("Mathematics")
#     print(math_student_list)
    
#     print("\nStudents taking English:")
#     eng_student_list = woodland_high.list_students_by_subject("English")
#     print(eng_student_list)
    
#     print("\nStudents taking History:")
#     hist_student_list = woodland_high.list_students_by_subject("History")
#     print(hist_student_list)
    
#     print("\n=== SCHOOL SYSTEM TEST COMPLETE ===\n")

# if __name__ == "__main__":
#     main()

# # Testing grade_calculator

# # main.py

# # main.py

# from student import Student
# import grade_calculator as gc

# def test_pure_functions():
#     print("=== Testing Pure Calculation Functions ===\n")
    
#     # Math
#     quizzes = [100, 80, 90, 70, 85]
#     t1, t2, fe = 88, 92, 94
#     math_grade = gc.calculate_math_grade(quizzes, t1, t2, fe)
#     print(f"Math grade (quizzes={quizzes}, t1={t1}, t2={t2}, fe={fe}): {math_grade:.2f}")
    
#     # English
#     attendance = 95
#     eng_quizzes = [85, 90]
#     eng_fe = 88
#     english_grade = gc.calculate_english_grade(attendance, eng_quizzes, eng_fe)
#     print(f"English grade (att={attendance}, quizzes={eng_quizzes}, fe={eng_fe}): {english_grade:.2f}")
    
#     # History
#     hist_att = 90
#     project = 92
#     exams = [88, 94]
#     history_grade = gc.calculate_history_grade(hist_att, project, exams)
#     print(f"History grade (att={hist_att}, proj={project}, exams={exams}): {history_grade:.2f}")
#     print()


# def create_students():
#     """
#     Create 5 Student objects and attach raw-grade attributes
#     in the exact structure grade_calculator expects.
#     """
#     students = []
    
#     s1 = Student("S001", "John", "", "Doe", 16, "1 A St", "", "", "11111", "CountyX", "Year10",
#                  [], "Jane Doe", "Jack Doe", "123-456-7890", "098-765-4321")
#     s1.mathGrades = [80, 90, 85, 95, 100, 88, 92, 94]
#     s1.englishAttendance = 96
#     s1.englishQuiz1 = 89
#     s1.englishQuiz2 = 93
#     s1.englishFinalExam = 90
#     s1.historyAttendance = 94
#     s1.historyProject = 91
#     s1.historyExams = [88, 95]
#     students.append(s1)

#     s2 = Student("S002", "Alice", "B", "Smith", 17, "2 B Rd", "Unit 5", "", "22222", "CountyY", "Year11",
#                  [], "Ann Smith", "Bill Smith", "234-567-8901", "109-876-5432")
#     s2.mathGrades = [70, 75, 80, 85, 90, 78, 82, 88]
#     s2.englishAttendance = 88
#     s2.englishQuiz1 = 92
#     s2.englishQuiz2 = 85
#     s2.englishFinalExam = 87
#     s2.historyAttendance = 90
#     s2.historyProject = 89
#     s2.historyExams = [84, 90]
#     students.append(s2)

#     s3 = Student("S003", "Bob", "C", "Johnson", 15, "3 C Ave", "", "", "33333", "CountyZ", "Year9",
#                  [], "Carol Johnson", "Bob Johnson", "345-678-9012", "210-987-6543")
#     s3.mathGrades = [60, 65, 70, 75, 80, 68, 72, 78]
#     s3.englishAttendance = 92
#     s3.englishQuiz1 = 80
#     s3.englishQuiz2 = 82
#     s3.englishFinalExam = 85
#     s3.historyAttendance = 88
#     s3.historyProject = 85
#     s3.historyExams = [82, 88]
#     students.append(s3)

#     s4 = Student("S004", "Diana", "", "White", 16, "4 D Blvd", "Floor 2", "", "44444", "CountyW", "Year10",
#                  [], "Emily White", "Diana White", "456-789-0123", "321-098-7654")
#     s4.mathGrades = [90, 92, 94, 96, 98, 91, 93, 97]
#     s4.englishAttendance = 100
#     s4.englishQuiz1 = 95
#     s4.englishQuiz2 = 98
#     s4.englishFinalExam = 99
#     s4.historyAttendance = 97
#     s4.historyProject = 96
#     s4.historyExams = [94, 99]
#     students.append(s4)

#     s5 = Student("S005", "Eva", "D", "Green", 18, "5 E Ct", "", "", "55555", "CountyV", "Year12",
#                  [], "Frank Green", "Eva Green", "567-890-1234", "432-109-8765")
#     s5.mathGrades = [50, 55, 60, 65, 70, 58, 62, 68]
#     s5.englishAttendance = 85
#     s5.englishQuiz1 = 75
#     s5.englishQuiz2 = 78
#     s5.englishFinalExam = 80
#     s5.historyAttendance = 82
#     s5.historyProject = 80
#     s5.historyExams = [78, 84]
#     students.append(s5)

#     return students


# def test_batch_update(students):
#     print("=== Testing Batch Grade Update ===\n")
    
#     # Print before-update
#     for s in students:
#         print(f"{s.studentID} grades before:", end=" ")
#         # mathGrade
#         try:
#             print(f"{s.mathGrade:.2f}", end=" ")
#         except AttributeError:
#             print("None", end=" ")
#         # englishGrade
#         try:
#             print(f"{s.englishGrade:.2f}", end=" ")
#         except AttributeError:
#             print("None", end=" ")
#         # historyGrade
#         try:
#             print(f"{s.historyGrade:.2f}")
#         except AttributeError:
#             print("None")
    
#     # Perform batch update
#     gc.calculate_and_update_grades_for_students(students)
#     print()

#     # Print after-update
#     for s in students:
#         print(f"{s.studentID} grades after: ", end="")
#         # mathGrade
#         try:
#             print(f"{s.mathGrade:.2f}", end=" ")
#         except AttributeError:
#             print("None", end=" ")
#         # englishGrade
#         try:
#             print(f"{s.englishGrade:.2f}", end=" ")
#         except AttributeError:
#             print("None", end=" ")
#         # historyGrade
#         try:
#             print(f"{s.historyGrade:.2f}")
#         except AttributeError:
#             print("None")
#     print()


# def main():
#     test_pure_functions()
#     students = create_students()
#     test_batch_update(students)


# if __name__ == "__main__":
#     main()




# Testing interactions between student.py school.py and subject.py
# main.py

# from student import Student
# from school import School
# from subject import (
#     MathStudent,
#     EnglishStudent,
#     HistoryStudent,
#     print_student_details
# )

# def assign_final_grades(students):
#     """
#     The School.get_average_grade() method looks for attributes
#     finalMathematicsGrade, finalEnglishGrade, finalHistoryGrade—
#     so we inject them here from the existing last-test-score fields.
#     """
#     for s in students:
#         if hasattr(s, 'mathLastTestScore'):
#             s.finalMathematicsGrade = s.mathLastTestScore
#         if hasattr(s, 'englishLastTestScore'):
#             s.finalEnglishGrade = s.englishLastTestScore
#         if hasattr(s, 'historyLastTestScore'):
#             s.finalHistoryGrade = s.historyLastTestScore

# def main():
#     # --- 1. Create 10 students (4 Math, 3 English, 3 History) ---
#     students = [
#         MathStudent("S001", "John",  "A", "Doe",    15,
#             "123 Elm St",  "",  "", "AB12 3CD", "CountyA", "Year10", ["Mathematics"],
#             "Jane Doe", "Jack Doe", "123-456-789", "987-654-321",
#             mathLevel="Advanced", mathClassNumber="101", mathTeacher="Mr. Smith", mathLastTestScore=95
#         ),
#         EnglishStudent("S002", "Alice", "B", "Smith", 16,
#             "456 Oak St", "Apt 5", "", "XY45 6ZA", "CountyB", "Year11", ["English"],
#             "Ann Smith", "Bill Smith", "321-654-987", "654-321-987",
#             englishLevel="Intermediate", englishClassNumber="102", englishTeacher="Mrs. Johnson", englishLastTestScore=88
#         ),
#         HistoryStudent("S003", "Bob",   "C", "Johnson",17,
#             "789 Pine St","Suite 3","", "YZ12 8XD","CountyC", "Year12", ["History"],
#             "Carol Johnson","Bob's Dad","444-444-4444","555-555-5557",
#             historyLevel="Advanced", historyClassNumber="103", historyTeacher="Mr. Williams", historyLastTestScore=90
#         ),
#         MathStudent("S004", "Charlie","","Brown",  16,
#             "101 Maple St","Unit 5","","11223","CountyD","Year10", ["Mathematics","English"],
#             "David Brown","Eve Brown","111-222-3333","444-555-6666",
#             mathLevel="Beginner", mathClassNumber="104", mathTeacher="Mr. Black", mathLastTestScore=85
#         ),
#         EnglishStudent("S005", "Diana", "","White",  14,
#             "202 Birch St","","Apartment 8","22334","CountyE","Year 9", ["English","History"],
#             "Emily White","Diana's Dad","123-123-1234","987-987-9876",
#             englishLevel="Beginner", englishClassNumber="105", englishTeacher="Mrs. Brown", englishLastTestScore=75
#         ),
#         HistoryStudent("S006", "Eva",   "D","Green", 18,
#             "303 Cedar St","Floor 2","","33445","CountyF","Year12", ["History","English"],
#             "Frank Green","Eva's Mom","555-555-5558","555-555-5559",
#             historyLevel="Intermediate", historyClassNumber="106", historyTeacher="Mr. Clark", historyLastTestScore=92
#         ),
#         MathStudent("S007", "George", "","Adams",  15,
#             "404 Birchwood St","","Bungalow","44556","CountyG","Year10", ["Mathematics","English"],
#             "Helen Adams","George's Dad","777-777-7777","888-888-8888",
#             mathLevel="Advanced", mathClassNumber="107", mathTeacher="Mr. Lee", mathLastTestScore=89
#         ),
#         EnglishStudent("S008","Hannah","","Evans",  16,
#             "505 Aspen St","Floor 3","","55667","CountyH","Year11", ["English","History"],
#             "Isabel Evans","Hannah's Dad","999-999-9999","666-666-6666",
#             englishLevel="Intermediate", englishClassNumber="108", englishTeacher="Ms. Green", englishLastTestScore=81
#         ),
#         HistoryStudent("S009","Ivy",   "","Martin", 17,
#             "606 Fir St","Unit 7","","66778","CountyI","Year12", ["History","Mathematics"],
#             "Jack Martin","Ivy's Mom","222-333-4444","555-666-7777",
#             historyLevel="Advanced", historyClassNumber="109", historyTeacher="Mr. Harris", historyLastTestScore=93
#         ),
#         MathStudent("S010","Jack",   "","Moore",  15,
#             "707 Sequoia St","","Apartment 9","77889","CountyJ","Year10", ["Mathematics","History"],
#             "Karen Moore","Jack's Dad","333-444-5555","444-555-6666",
#             mathLevel="Intermediate", mathClassNumber="110", mathTeacher="Mr. Smith", mathLastTestScore=87
#         )
#     ]

#     # --- 2. Test Student (inherited) methods on the first student ---
#     s0 = students[0]
#     print("\n--- Student Base-Class Tests ---")
#     print("Original:\n", s0)
#     s0.update_ID("S001X")
#     print("After ID update:", s0.studentID)
#     s0.update_name(new_fName="JohnX", new_mName="Z", new_lName="DoeY")
#     print("After name update:\n", s0.get_summary_student_data())
#     s0.update_address(
#         new_addressL1="New Blvd", new_addressL2="Suite 100",
#         new_addressPostCode="00000", new_addressCounty="NewCounty"
#     )
#     print("After address update:", s0.get_full_address())
#     s0.update_age(16)
#     print("After age update:", s0.age)
#     s0.update_school_year("Year11")
#     print("After year update:", s0.schoolYear)
#     s0.add_subject("History")
#     print("After add_subject:", s0.get_subjects())
#     s0.update_subjects(["Mathematics","History","English"])
#     print("After update_subjects:", s0.get_subjects())
#     s0.remove_subject("English")
#     print("After remove_subject:", s0.get_subjects())
#     s0.update_guardian_contact(1, new_name="Guard1X", new_contact="111-111-1111")
#     s0.update_guardian_contact(2, new_name="Guard2X", new_contact="222-222-2222")
#     print("After guardian updates:\n", s0.get_guardian_info())
#     print("is_full_name_available:",    s0.is_full_name_available())
#     print("is_address_complete:",       s0.is_address_complete())
#     print("is_in_year('Year11'):",       s0.is_in_year("Year11"))
#     print("is_enrolled_in('History'):", s0.is_enrolled_in("History"))
#     print("is_guardian_contact_available(1):", s0.is_guardian_contact_available(1))
#     print("is_guardian_contact_available(2):", s0.is_guardian_contact_available(2))

#     # --- 3. Use the helper from subject.py ---
#     print("\n--- print_student_details (first 3 students) ---")
#     print_student_details(students[:3])

#     # --- 4. Inject final…Grade attributes so averages work ---
#     assign_final_grades(students)

#     # --- 5. Create a School and add all students ---
#     school = School(
#         name="Green Valley High",
#         address="123 School Rd, CountyA",
#         telephoneNumber="123-456-7890",
#         subjects=["Mathematics","English","History"]
#     )
#     for s in students:
#         school.add_student(s)

#     print("\n--- School After Adding 10 Students ---")
#     print(school)

#     # --- 6. School listings & averages ---
#     print("By subject → Math:",    school.list_students_by_subject("Mathematics"))
#     print("By subject → English:", school.list_students_by_subject("English"))
#     print("By subject → History:", school.list_students_by_subject("History"))

#     print("Average Mathematics grade:", school.get_average_grade("Mathematics"))
#     print("Average English grade:   ", school.get_average_grade("English"))
#     print("Average History grade:    ", school.get_average_grade("History"))

#     # --- 7. Test School updates and removals ---
#     school.update_school_name("Blue Valley High")
#     school.update_school_address("456 New Rd, CountyA")
#     school.update_school_year("Year2025")
#     school.update_school_subjects(["Art","Biology","Mathematics"])
#     print("\nAfter school updates:\n", school)

#     # Remove one student
#     school.remove_student(students[2])
#     print("\nAfter removing S003:\n", school)

#     # Find a student
#     found = school.find_student_by_id("S005")
#     print("\nFound S005 summary:\n", found.get_summary_student_data() if found else "Not Found")

#     # --- 8. Subject-specific detail-updating and __repr__ tests ---
#     print("\n--- Subject-Specific Detail Updates ---")
#     m = students[0]  # MathStudent
#     m.add_math_details("Expert", "201", "Dr. Euler", 100)
#     print("After add_math_details:\n", m)

#     e = students[1]  # EnglishStudent
#     e.add_english_details("Expert", "202", "Dr. Shakespeare", 95)
#     print("After add_english_details:\n", e)

#     h = students[2]  # HistoryStudent
#     h.add_history_details("Expert", "203", "Dr. Herodotus", 98)
#     print("After add_history_details:\n", h)


# if __name__ == "__main__":
#     main()


# Testing subject.py

# from subject import MathStudent, EnglishStudent, HistoryStudent

# def main():
#     # Sample Data for 10 students
#     students = [
#         MathStudent(1, 'Alice', '', 'Johnson', 16, '123 Main St', 'Apt 1', 'Springfield', '98765', 'County1', 11, ['Mathematics'], 'John Johnson', 'Jane Johnson', '555-1234', '555-5678', 'Advanced', 'MATH101', 'Mr. Smith', 92),
#         EnglishStudent(2, 'Bob', '', 'Williams', 15, '456 Elm St', 'Apt 2', 'Greenville', '54321', 'County2', 10, ['English'], 'Michael Williams', 'Emily Williams', '555-2345', '555-6789', 'Intermediate', 'ENG102', 'Mrs. Brown', 88),
#         HistoryStudent(3, 'Charlie', '', 'Davis', 16, '789 Oak St', 'Apt 3', 'Townsville', '11223', 'County3', 11, ['History'], 'David Davis', 'Alice Davis', '555-3456', '555-7890', 'Basic', 'HIS103', 'Mr. White', 85),
#         MathStudent(4, 'Diana', '', 'Martinez', 15, '321 Pine St', 'Apt 4', 'Hilltop', '22334', 'County4', 10, ['Mathematics'], 'Carlos Martinez', 'Sophia Martinez', '555-4567', '555-8901', 'Advanced', 'MATH104', 'Mr. Gray', 94),
#         EnglishStudent(5, 'Edward', '', 'Taylor', 14, '654 Maple St', 'Apt 5', 'Lakeside', '33445', 'County5', 9, ['English'], 'Matthew Taylor', 'Linda Taylor', '555-5678', '555-9012', 'Beginner', 'ENG105', 'Ms. Green', 76),
#         HistoryStudent(6, 'Fiona', '', 'Anderson', 17, '987 Birch St', 'Apt 6', 'Riverdale', '44556', 'County6', 12, ['History'], 'Benjamin Anderson', 'Sarah Anderson', '555-6789', '555-0123', 'Intermediate', 'HIS106', 'Mr. Black', 90),
#         MathStudent(7, 'George', '', 'Lee', 15, '321 Cedar St', 'Apt 7', 'Mountainview', '55667', 'County7', 10, ['Mathematics'], 'Daniel Lee', 'Natalie Lee', '555-7890', '555-1234', 'Intermediate', 'MATH107', 'Ms. White', 80),
#         EnglishStudent(8, 'Hannah', '', 'Lopez', 14, '234 Fir St', 'Apt 8', 'Woodland', '66778', 'County8', 9, ['English'], 'Anthony Lopez', 'Olivia Lopez', '555-8901', '555-2345', 'Advanced', 'ENG108', 'Mr. Blue', 93),
#         HistoryStudent(9, 'Ian', '', 'Gonzalez', 16, '876 Cedar St', 'Apt 9', 'Valleyview', '77889', 'County9', 11, ['History'], 'Samuel Gonzalez', 'Isabel Gonzalez', '555-9012', '555-3456', 'Advanced', 'HIS109', 'Ms. Yellow', 95),
#         MathStudent(10, 'Jack', '', 'Miller', 17, '432 Willow St', 'Apt 10', 'Greenfield', '88990', 'County10', 12, ['Mathematics'], 'Richard Miller', 'Barbara Miller', '555-0123', '555-4567', 'Beginner', 'MATH110', 'Mr. Red', 78)
#     ]

#     # Test Method and Attribute Access for each student
#     for student in students:
#         print(f"Testing {student.fName} {student.lName}:")
#         print(student)  # Test the __repr__ method
#         print(f"Student ID: {student.studentID}")
#         print(f"Name: {student.fName} {student.lName}")
#         print(f"Age: {student.age}")
#         print(f"School Year: {student.schoolYear}")
#         print(f"School Subjects: {student.schoolSubjects}")
#         print(f"Test Score: {student.mathLastTestScore if isinstance(student, MathStudent) else (student.englishLastTestScore if isinstance(student, EnglishStudent) else student.historyLastTestScore)}")
#         print(f"Grade: {student.mathGrade if isinstance(student, MathStudent) else (student.englishGrade if isinstance(student, EnglishStudent) else student.historyGrade)}")
        
#         # Add a subject to test subject addition
#         if isinstance(student, MathStudent):
#             student.add_math_details('Advanced', 'MATH115', 'Ms. Blue', 95)
#         elif isinstance(student, EnglishStudent):
#             student.add_english_details('Beginner', 'ENG110', 'Mr. Red', 79)
#         elif isinstance(student, HistoryStudent):
#             student.add_history_details('Intermediate', 'HIS112', 'Mr. Gray', 82)
        
#         print(f"Updated Test Score: {student.mathLastTestScore if isinstance(student, MathStudent) else (student.englishLastTestScore if isinstance(student, EnglishStudent) else student.historyLastTestScore)}")
#         print(f"Updated Grade: {student.mathGrade if isinstance(student, MathStudent) else (student.englishGrade if isinstance(student, EnglishStudent) else student.historyGrade)}")
        
#         print("=" * 50)
    
#     # Test listing students by subject
#     print("Listing students by subject: Mathematics")
#     math_students = [student for student in students if isinstance(student, MathStudent)]
#     for student in math_students:
#         print(student)

# if __name__ == "__main__":
#     main()




# Testing student.py and school.py

# Example test data with grades
# students_data = [
#     {
#         'studentID': 'S001',
#         'fName': 'Alice',
#         'mName': 'B',
#         'lName': 'Johnson',
#         'age': 16,
#         'addressL1': '123 Maple St',
#         'addressL2': 'Apt 5B',
#         'addressL3': '',
#         'addressPostCode': '12345',
#         'addressCounty': 'Lancashire',
#         'schoolYear': 11,
#         'schoolSubjects': ['English', 'Mathematics', 'History'],
#         'nameParGar1': 'Robert Johnson',
#         'nameParGar2': 'Susan Johnson',
#         'contactDetParGar1': '123-456-7890',
#         'contactDetParGar2': '098-765-4321',
#     },
#     {
#         'studentID': 'S002',
#         'fName': 'John',
#         'mName': 'A',
#         'lName': 'Smith',
#         'age': 17,
#         'addressL1': '456 Oak St',
#         'addressL2': '',
#         'addressL3': '',
#         'addressPostCode': '23456',
#         'addressCounty': 'Yorkshire',
#         'schoolYear': 12,
#         'schoolSubjects': ['English', 'Mathematics'],
#         'nameParGar1': 'David Smith',
#         'nameParGar2': 'Linda Smith',
#         'contactDetParGar1': '234-567-8901',
#         'contactDetParGar2': '987-654-3210',
#     },
#     {
#         'studentID': 'S003',
#         'fName': 'Emma',
#         'mName': 'C',
#         'lName': 'Brown',
#         'age': 15,
#         'addressL1': '789 Birch Rd',
#         'addressL2': 'Apt 7C',
#         'addressL3': '',
#         'addressPostCode': '34567',
#         'addressCounty': 'Cambridge',
#         'schoolYear': 10,
#         'schoolSubjects': ['English', 'Mathematics'],
#         'nameParGar1': 'William Brown',
#         'nameParGar2': 'Olivia Brown',
#         'contactDetParGar1': '345-678-9012',
#         'contactDetParGar2': '876-543-2109',
#     },
#     {
#         'studentID': 'S004',
#         'fName': 'Michael',
#         'mName': 'D',
#         'lName': 'Taylor',
#         'age': 14,
#         'addressL1': '101 Pine St',
#         'addressL2': 'Apt 3D',
#         'addressL3': '',
#         'addressPostCode': '45678',
#         'addressCounty': 'Bristol',
#         'schoolYear': 9,
#         'schoolSubjects': ['Mathematics', 'History'],
#         'nameParGar1': 'Joseph Taylor',
#         'nameParGar2': 'Evelyn Taylor',
#         'contactDetParGar1': '456-789-0123',
#         'contactDetParGar2': '765-432-1098',
#     },
#     {
#         'studentID': 'S005',
#         'fName': 'Sophia',
#         'mName': 'E',
#         'lName': 'Davis',
#         'age': 16,
#         'addressL1': '202 Cedar Ave',
#         'addressL2': '',
#         'addressL3': '',
#         'addressPostCode': '56789',
#         'addressCounty': 'Gloucestershire',
#         'schoolYear': 11,
#         'schoolSubjects': ['English', 'History'],
#         'nameParGar1': 'Charles Davis',
#         'nameParGar2': 'Megan Davis',
#         'contactDetParGar1': '567-890-1234',
#         'contactDetParGar2': '654-321-9870',
#     },
# ]

# # Create student objects using the data
# students = []
# for data in students_data:
#     student = Student(**data)  # Unpack data into the Student constructor
#     students.append(student)

# # Add grades for the students (directly in the School class)
# # Assuming we add the grades manually here
# grades = {
#     'S001': {'Mathematics': 88, 'English': 90, 'History': 85},
#     'S002': {'Mathematics': 92, 'English': 87},
#     'S003': {'Mathematics': 75, 'English': 80},
#     'S004': {'Mathematics': 85, 'History': 78},
#     'S005': {'English': 95, 'History': 89},
# }

# # Now you can use these students in the school system
# school = School("Sunshine High School", "789 School Rd, Cityville", "555-1234", ["English", "Mathematics", "History"])

# # Add students to the school
# for student in students:
#     school.add_student(student)

# # Example of calculating average grades using the grades data
# def calculate_average_grade(subject):
#     total = 0
#     count = 0
#     for student_id, student_grades in grades.items():
#         if subject in student_grades:
#             total += student_grades[subject]
#             count += 1
#     if count == 0:
#         return None
#     return total / count

# # Calculate average grades
# average_math = calculate_average_grade('Mathematics')
# average_english = calculate_average_grade('English')
# average_history = calculate_average_grade('History')

# # Print out the average grades
# print(f"Average Mathematics Grade: {average_math}")
# print(f"Average English Grade: {average_english}")
# print(f"Average History Grade: {average_history}")

# # Also testing student retrieval and information
# for student in students:
#     print(f"Details for {student.fName} {student.lName}:")
#     print(student.get_full_student_data())
#     print()


# Testing school.py

# from student import Student  # Import the Student class

# def main():
#     # Create a school
#     school = School(name="Springfield High", address="123 Elm Street", telephoneNumber="555-1234", subjects=["Mathematics", "English", "History"])

#     # Create students with grades for Mathematics, English, and History
#     student1 = Student(
#         studentID="S001", fName="John", mName="Paul", lName="Doe", age=15, 
#         addressL1="123 Main St", addressL2="Apt 4B", addressL3="Springfield", 
#         addressPostCode="12345", addressCounty="Somerset", schoolYear="2025", 
#         schoolSubjects=["Mathematics", "English"], nameParGar1="Mary Doe", 
#         nameParGar2="John Doe Sr.", contactDetParGar1="555-001", contactDetParGar2="555-002"
#     )
#     student1.finalMathematicsGrade = 88
#     student1.finalEnglishGrade = 92
#     student1.finalHistoryGrade = 85

#     student2 = Student(
#         studentID="S002", fName="Jane", mName="Elizabeth", lName="Smith", age=16, 
#         addressL1="456 Oak St", addressL2="Room 12", addressL3="Springfield", 
#         addressPostCode="12346", addressCounty="Somerset", schoolYear="2025", 
#         schoolSubjects=["Mathematics", "History"], nameParGar1="Patricia Smith", 
#         nameParGar2="Michael Smith", contactDetParGar1="555-003", contactDetParGar2="555-004"
#     )
#     student2.finalMathematicsGrade = 76
#     student2.finalEnglishGrade = 85
#     student2.finalHistoryGrade = 90

#     student3 = Student(
#         studentID="S003", fName="Alice", mName="Marie", lName="Johnson", age=15, 
#         addressL1="789 Pine St", addressL2="", addressL3="Springfield", 
#         addressPostCode="12347", addressCounty="Somerset", schoolYear="2025", 
#         schoolSubjects=["English", "History"], nameParGar1="Linda Johnson", 
#         nameParGar2="David Johnson", contactDetParGar1="555-005", contactDetParGar2="555-006"
#     )
#     student3.finalMathematicsGrade = 93
#     student3.finalEnglishGrade = 95
#     student3.finalHistoryGrade = 88

#     student4 = Student(
#         studentID="S004", fName="Bob", mName="David", lName="Brown", age=17, 
#         addressL1="123 Birch St", addressL2="Room 5", addressL3="Springfield", 
#         addressPostCode="12348", addressCounty="Somerset", schoolYear="2025", 
#         schoolSubjects=["Mathematics"], nameParGar1="Susan Brown", 
#         nameParGar2="William Brown", contactDetParGar1="555-007", contactDetParGar2="555-008"
#     )
#     student4.finalMathematicsGrade = 80
#     student4.finalEnglishGrade = 75
#     student4.finalHistoryGrade = 78

#     student5 = Student(
#         studentID="S005", fName="Charlie", mName="James", lName="Davis", age=16, 
#         addressL1="567 Cedar St", addressL2="Apt 2A", addressL3="Springfield", 
#         addressPostCode="12349", addressCounty="Somerset", schoolYear="2025", 
#         schoolSubjects=["English", "History"], nameParGar1="Alice Davis", 
#         nameParGar2="James Davis", contactDetParGar1="555-009", contactDetParGar2="555-010"
#     )
#     student5.finalMathematicsGrade = 88
#     student5.finalEnglishGrade = 92
#     student5.finalHistoryGrade = 85

#     # Test adding students
#     school.add_student(student1)
#     school.add_student(student2)
#     school.add_student(student3)
#     school.add_student(student4)
#     school.add_student(student5)

#     # Test finding student by ID
#     found_student = school.find_student_by_id("S003")
#     if found_student:
#         print(f"Found student: {found_student.fName} {found_student.lName}")

#     # Test listing students by subject
#     math_students = school.list_students_by_subject("Mathematics")
#     print(f"Students enrolled in Mathematics: {', '.join(math_students)}")

#     english_students = school.list_students_by_subject("English")
#     print(f"Students enrolled in English: {', '.join(english_students)}")

#     history_students = school.list_students_by_subject("History")
#     print(f"Students enrolled in History: {', '.join(history_students)}")

#     # Test getting average grades
#     avg_math = school.get_average_grade("Mathematics")
#     print(f"Average Mathematics grade: {avg_math}")

#     avg_english = school.get_average_grade("English")
#     print(f"Average English grade: {avg_english}")

#     avg_history = school.get_average_grade("History")
#     print(f"Average History grade: {avg_history}")

#     # Test removing a student
#     school.remove_student(student2)  # Removing student2
#     school.remove_student(student1)  # Removing student1

#     # Test updating school attributes
#     school.update_school_name("Sunset High")
#     school.update_school_address("456 Oak Avenue")
#     school.update_school_year("2026")
#     school.update_school_subjects(["Mathematics", "English", "History", "Science"])

#     # Test the __repr__ method (printed automatically)
#     print(school)

#     # Test removing a student who doesn't exist (will print an error)
#     school.remove_student(student2)

#     # Test updating school subjects
#     school.update_school_subjects(["Mathematics", "English", "History", "Art"])

#     # Test final output of school information
#     print(school)

#     # Test student methods
#     student1.update_age(16)
#     student1.update_address(new_addressL1="111 Maple St")
#     student1.add_subject("Science")
#     student1.update_guardian_contact(guardian_number=1, new_contact="555-011")
#     student1.remove_subject("Mathematics")
#     student1.update_subjects(["Mathematics", "English", "History"])

#     # Print the full student data for student1
#     print(student1.get_full_student_data())

#     # Check if student1 has a full name
#     print(f"Is student1's full name available? {student1.is_full_name_available()}")

#     # Check if student1's address is complete
#     print(f"Is student1's address complete? {student1.is_address_complete()}")

#     # Check if student1 is in year 2025
#     print(f"Is student1 in year 2025? {student1.is_in_year(2025)}")

#     # Check if student1 is enrolled in "History"
#     print(f"Is student1 enrolled in History? {student1.is_enrolled_in('History')}")

#     # Check if guardian 1 has contact details
#     print(f"Does student1's guardian 1 have contact? {student1.is_guardian_contact_available(guardian_number=1)}")

# if __name__ == "__main__":
#     main()




# Testing student.py

# def main():
#     # Creating 5 student instances with minimal formatting
#     student1 = Student(
#         studentID="S001",
#         fName="Aoife",
#         mName="Marie",
#         lName="O'Brien",
#         age=15,
#         addressL1="12 Oak Drive",
#         addressL2="Rathmines",
#         addressL3="Dublin 6",
#         addressPostCode="D06X5F4",
#         addressCounty="Dublin",
#         schoolYear=3,
#         schoolSubjects=["Maths", "English"],
#         nameParGar1="John O'Brien",
#         nameParGar2="Mary O'Brien",
#         contactDetParGar1="0871234567",
#         contactDetParGar2="0877654321"
#     )

#     student2 = Student(
#         studentID="S002",
#         fName="John",
#         mName="Paul",
#         lName="Smith",
#         age=17,
#         addressL1="56 Elm Street",
#         addressL2="Ballinteer",
#         addressL3="Dublin 16",
#         addressPostCode="D16P2H7",
#         addressCounty="Dublin",
#         schoolYear=5,
#         schoolSubjects=["Physics", "Chemistry"],
#         nameParGar1="David Smith",
#         nameParGar2="Sarah Smith",
#         contactDetParGar1="0879876543",
#         contactDetParGar2="0876543210"
#     )

#     student3 = Student(
#         studentID="S003",
#         fName="Sarah",
#         mName="Ellen",
#         lName="Doyle",
#         age=16,
#         addressL1="45 Maple Road",
#         addressL2="Greystones",
#         addressL3="Co. Wicklow",
#         addressPostCode="A63B1C2",
#         addressCounty="Wicklow",
#         schoolYear=4,
#         schoolSubjects=["Biology", "Geography"],
#         nameParGar1="Mark Doyle",
#         nameParGar2="Linda Doyle",
#         contactDetParGar1="0861237894",
#         contactDetParGar2="0869876543"
#     )

#     student4 = Student(
#         studentID="S004",
#         fName="David",
#         mName="Alexander",
#         lName="Jones",
#         age=18,
#         addressL1="21 Ashford Way",
#         addressL2="Terenure",
#         addressL3="Dublin 12",
#         addressPostCode="D12J1X8",
#         addressCounty="Dublin",
#         schoolYear=6,
#         schoolSubjects=["History", "Economics"],
#         nameParGar1="Brian Jones",
#         nameParGar2="Anna Jones",
#         contactDetParGar1="0854326789",
#         contactDetParGar2="0858765432"
#     )

#     student5 = Student(
#         studentID="S005",
#         fName="Emily",
#         mName="Grace",
#         lName="Taylor",
#         age=14,
#         addressL1="89 Birch Street",
#         addressL2="Clontarf",
#         addressL3="Dublin 3",
#         addressPostCode="D03V6L4",
#         addressCounty="Dublin",
#         schoolYear=2,
#         schoolSubjects=["Art", "Music"],
#         nameParGar1="Peter Taylor",
#         nameParGar2="Emma Taylor",
#         contactDetParGar1="0851234567",
#         contactDetParGar2="0859876543"
#     )

#     # List of all students
#     students = [student1, student2, student3, student4, student5]

#     for student in students:
#         # Test __repr__ method (prints a readable representation of the student)
#         print(student)

#         # Test get_full_student_data method
#         full_data = student.get_full_student_data()
#         print(full_data)

#         # Test get_summary_student_data method
#         summary_data = student.get_summary_student_data()
#         print(summary_data)

#         # Test update_ID method
#         student.update_ID(f"S{int(student.studentID[1:]) + 100}")
#         print(f"Updated Student ID: {student.studentID}")

#         # Test update_name method
#         student.update_name(new_fName="UpdatedFirst", new_lName="UpdatedLast")
#         print(f"Updated Name: {student.fName} {student.mName} {student.lName}")

#         # Test update_address method
#         student.update_address(new_addressL1="New Address Line 1", new_addressCounty="Updated County")
#         print(f"Updated Address: {student.get_full_address()}")

#         # Test update_age method
#         student.update_age(20)
#         print(f"Updated Age: {student.age}")

#         # Test update_school_year method
#         student.update_school_year(7)
#         print(f"Updated School Year: {student.schoolYear}")

#         # Test add_subject method
#         student.add_subject("New Subject")
#         print(f"Updated Subjects: {', '.join(student.schoolSubjects)}")

#         # Test remove_subject method
#         student.remove_subject("New Subject")
#         print(f"Updated Subjects after removal: {', '.join(student.schoolSubjects)}")

#         # Test update_guardian_contact method for both guardians
#         student.update_guardian_contact(guardian_number=1, new_name="Updated Guardian 1", new_contact="0871112233")
#         student.update_guardian_contact(guardian_number=2, new_name="Updated Guardian 2", new_contact="0874445566")
#         print(f"Updated Guardian Info: {student.get_guardian_info()}")

#         # Test is_full_name_available method
#         print(f"Is Full Name Available? {student.is_full_name_available()}")

#         # Test is_address_complete method
#         print(f"Is Address Complete? {student.is_address_complete()}")

#         # Test is_in_year method
#         print(f"Is Student in Year 6? {student.is_in_year(6)}")

#         # Test is_enrolled_in method
#         print(f"Is Student Enrolled in Physics? {student.is_enrolled_in('Physics')}")

#         # Test is_guardian_contact_available method
#         print(f"Is Guardian 1 Contact Available? {student.is_guardian_contact_available(guardian_number=1)}")

# if __name__ == "__main__":
#     main()
