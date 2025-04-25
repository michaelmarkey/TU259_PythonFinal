from student import Student
from csv_loader import load_students_from_csv, load_maths_grades_from_csv, load_english_grades_from_csv, load_history_grades_from_csv

class MathStudent(Student):
    def __init__(self, fName, mName, lName, addressL1, addressL2, addressL3, addressPostCode, 
                 addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, 
                 contactDetParGar1, contactDetParGar2, mathLevel, mathClassNumber, 
                 mathTeacher, mathLastTestScore):
        
        super().__init__(fName, mName, lName, addressL1, addressL2, addressL3, addressPostCode, 
                         addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, 
                         contactDetParGar1, contactDetParGar2)
        
        self.mathLevel = mathLevel
        self.mathClassNumber = mathClassNumber
        self.mathTeacher = mathTeacher
        self.mathLastTestScore = mathLastTestScore        

    def add_math_details(self, level, class_number, teacher, last_test_score):
        self.mathLevel = level
        self.mathClassNumber = class_number
        self.mathTeacher = teacher
        self.mathLastTestScore = last_test_score
        self.mathGrade = last_test_score
        if "Mathematics" not in self.schoolSubjects:
            self.schoolSubjects.append("Mathematics")

    def __repr__(self):
        base = super().__repr__()  # This will call Student.__repr__()
        return (f"{base} | Math Level: {self.mathLevel}, "
                f"Class Number: {self.mathClassNumber}, "
                f"Teacher: {self.mathTeacher}, "
                f"Last Test Score: {self.mathLastTestScore}")

class EnglishStudent(Student):
    def __init__(self, fName, mName, lName, addressL1, addressL2, addressL3, addressPostCode, 
                 addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, 
                 contactDetParGar1, contactDetParGar2, englishLevel, englishClassNumber, 
                 englishTeacher, englishLastTestScore):
        
        super().__init__(fName, mName, lName, addressL1, addressL2, addressL3, addressPostCode, 
                         addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, 
                         contactDetParGar1, contactDetParGar2)
        
        self.englishLevel = englishLevel
        self.englishClassNumber = englishClassNumber
        self.englishTeacher = englishTeacher
        self.englishLastTestScore = englishLastTestScore
        
    def add_english_details(self, level, class_number, teacher, last_test_score):
        self.englishLevel = level
        self.englishClassNumber = class_number
        self.englishTeacher = teacher
        self.englishLastTestScore = last_test_score
        self.englishGrade = last_test_score
        if "English" not in self.schoolSubjects:
            self.schoolSubjects.append("English")

    def __repr__(self):
        base = super().__repr__()  # This will call Student.__repr__()
        return (f"{base} | English Level: {self.englishLevel}, "
                f"Class Number: {self.englishClassNumber}, "
                f"Teacher: {self.englishTeacher}, "
                f"Last Test Score: {self.englishLastTestScore}") 

class HistoryStudent(Student):
    def __init__(self, fName, mName, lName, addressL1, addressL2, addressL3, addressPostCode, 
                 addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, 
                 contactDetParGar1, contactDetParGar2, historyLevel, historyClassNumber, 
                 historyTeacher, historyLastTestScore):
        
        super().__init__(fName, mName, lName, addressL1, addressL2, addressL3, addressPostCode, 
                         addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, 
                         contactDetParGar1, contactDetParGar2)
        
        self.historyLevel = historyLevel
        self.historyClassNumber = historyClassNumber
        self.historyTeacher = historyTeacher
        self.historyLastTestScore = historyLastTestScore

    def add_history_details(self, level, class_number, teacher, last_test_score):
        self.historyLevel = level
        self.historyClassNumber = class_number
        self.historyTeacher = teacher
        self.historyLastTestScore = last_test_score
        self.historyGrade = last_test_score
        if "History" not in self.schoolSubjects:
            self.schoolSubjects.append("History")

    def __repr__(self):
        base = super().__repr__()  # This will call Student.__repr__()
        return (f"{base} | History Level: {self.historyLevel}, "
                f"Class Number: {self.historyClassNumber}, "
                f"Teacher: {self.historyTeacher}, "
                f"Last Test Score: {self.historyLastTestScore}")

# Function to load all students and their grades using the csv_loader functions
def load_all_data(student_file, maths_file, english_file, history_file):
    students = load_students_from_csv(student_file)  # Load the student details
    load_maths_grades_from_csv(maths_file, students)  # Load the math grades and assign them to students
    load_english_grades_from_csv(english_file, students)  # Load the English grades and assign them
    load_history_grades_from_csv(history_file, students)  # Load the history grades and assign them
    return students

# Function to list all students by subject
def list_students_by_subject(students, subject):
    return [student for student in students if subject in student.schoolSubjects]

# Helper function to print student details with their grades
def print_student_details(students):
    for student in students:
        print(f"{student.fName} {student.lName} - Year {student.schoolYear}")
        print(student)  # This will use the new __repr__ from above
        print("-" * 40)
