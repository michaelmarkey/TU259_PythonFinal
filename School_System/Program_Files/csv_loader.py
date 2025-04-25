import csv
from student import Student
from grade_calculator import calculate_math_grade, calculate_english_grade, calculate_history_grade
from pathlib import Path

def load_students_from_csv(filename):
    students = []
    file_path = Path(__file__).parent / "CSV_Files" / filename
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        for row in reader:
            fName, mName, lName, addressL1, addressL2, addressL3, addressPostCode, addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, contactDetParGar1, contactDetParGar2 = row
            schoolSubjects = schoolSubjects.split(',')  # Assuming schoolSubjects are comma-separated
            student = Student(fName, mName, lName, addressL1, addressL2, addressL3, addressPostCode, 
                              addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, 
                              contactDetParGar1, contactDetParGar2)
            students.append(student)
    return students

def load_maths_grades_from_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        for row in reader:
            fName, lName, *grades = row
            student = next((s for s in students if s.fName == fName and s.lName == lName), None)
            if student:
                # Extract the grades and prepare them
                quiz_grades = list(map(float, grades[:5]))  # First 5 entries are quiz grades
                test_grades = list(map(float, grades[5:7]))  # Next 2 are test grades
                final_exam_grade = float(grades[7])  # Last one is the final exam grade
                
                # Calculate math grade using the correct arguments: 5 quiz grades, 2 tests, and the final exam
                student.mathGrade = calculate_math_grade(quiz_grades, *test_grades, final_exam_grade)

def load_english_grades_from_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        for row in reader:
            fName, lName, attendance, quiz1, quiz2, final_exam = row
            student = next((s for s in students if s.fName == fName and s.lName == lName), None)
            if student:
                # Convert the string values to float
                attendance = float(attendance)
                quiz1 = float(quiz1)
                quiz2 = float(quiz2)
                final_exam = float(final_exam)

                # Calculate english grade and assign it to the student
                student.englishGrade = calculate_english_grade(attendance, [quiz1, quiz2], final_exam)

def load_history_grades_from_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if present
        for row in reader:
            fName, lName, attendance, project, exam1, exam2 = row
            student = next((s for s in students if s.fName == fName and s.lName == lName), None)
            if student:
                # Convert the string values to float
                attendance = float(attendance)
                project = float(project)
                exam1 = float(exam1)
                exam2 = float(exam2)

                # Calculate history grade and assign it to the student
                student.historyGrade = calculate_history_grade(attendance, project, [exam1, exam2])

# Save Functions
def save_students_to_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['fName', 'mName', 'lName', 'addressL1', 'addressL2', 'addressL3', 'addressPostCode',
                         'addressCounty', 'schoolYear', 'schoolSubjects', 'nameParGar1', 'nameParGar2',
                         'contactDetParGar1', 'contactDetParGar2'])
        for student in students:
            writer.writerow([student.fName, student.mName, student.lName, student.addressL1, student.addressL2, 
                             student.addressL3, student.addressPostCode, student.addressCounty, student.schoolYear, 
                             ','.join(student.schoolSubjects), student.nameParGar1, student.nameParGar2, 
                             student.contactDetParGar1, student.contactDetParGar2])

def save_maths_grades_to_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['fName', 'lName', 'quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'test1', 'test2', 'final_exam'])
        for student in students:
            writer.writerow([student.fName, student.lName] + student.mathGrades)

def save_english_grades_to_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['fName', 'lName', 'attendance', 'quiz1', 'quiz2', 'final_exam'])
        for student in students:
            writer.writerow([student.fName, student.lName, student.englishAttendance, student.englishQuiz1, 
                             student.englishQuiz2, student.englishFinalExam])

def save_history_grades_to_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['fName', 'lName', 'attendance', 'project', 'exam1', 'exam2'])
        for student in students:
            writer.writerow([student.fName, student.lName, student.historyAttendance, student.historyProject, 
                             student.historyExam1, student.historyExam2])
