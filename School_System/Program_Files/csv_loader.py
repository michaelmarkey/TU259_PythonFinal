import csv
from student_classes import MathStudent, EnglishStudent, HistoryStudent, Student

def load_students_from_csv(filename):
    students = []

    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Base student info
            student = Student(
                fName=row['fName'],
                mName=row['mName'],
                lName=row['lName'],
                addressL1=row['addressL1'],
                addressL2=row['addressL2'],
                addressL3=row['addressL3'],
                addressPostCode=row['addressPostCode'],
                addressCounty=row['addressCounty'],
                schoolYear=row['schoolYear'],
                schoolSubjects=row['schoolSubjects'].split(", "),  # Split by comma to get list of subjects
                nameParGar1=row['nameParGar1'],
                nameParGar2=row['nameParGar2'],
                contactDetParGar1=row['contactDetParGar1'],
                contactDetParGar2=row['contactDetParGar2']
            )

            # Subject-specific info
            math_student = MathStudent(
                fName=row['fName'],
                mName=row['mName'],
                lName=row['lName'],
                addressL1=row['addressL1'],
                addressL2=row['addressL2'],
                addressL3=row['addressL3'],
                addressPostCode=row['addressPostCode'],
                addressCounty=row['addressCounty'],
                schoolYear=row['schoolYear'],
                schoolSubjects=row['schoolSubjects'].split(", "),
                nameParGar1=row['nameParGar1'],
                nameParGar2=row['nameParGar2'],
                contactDetParGar1=row['contactDetParGar1'],
                contactDetParGar2=row['contactDetParGar2'],
                mathLevel=row['mathLevel'],
                mathClassNumber=row['mathClassNumber'],
                mathTeacher=row['mathTeacher'],
                mathLastTestScore=row['mathLastTestScore']
            )

            english_student = EnglishStudent(
                fName=row['fName'],
                mName=row['mName'],
                lName=row['lName'],
                addressL1=row['addressL1'],
                addressL2=row['addressL2'],
                addressL3=row['addressL3'],
                addressPostCode=row['addressPostCode'],
                addressCounty=row['addressCounty'],
                schoolYear=row['schoolYear'],
                schoolSubjects=row['schoolSubjects'].split(", "),
                nameParGar1=row['nameParGar1'],
                nameParGar2=row['nameParGar2'],
                contactDetParGar1=row['contactDetParGar1'],
                contactDetParGar2=row['contactDetParGar2'],
                englishLevel=row['englishLevel'],
                englishClassNumber=row['englishClassNumber'],
                englishTeacher=row['englishTeacher'],
                englishLastTestScore=row['englishLastTestScore']
            )

            history_student = HistoryStudent(
                fName=row['fName'],
                mName=row['mName'],
                lName=row['lName'],
                addressL1=row['addressL1'],
                addressL2=row['addressL2'],
                addressL3=row['addressL3'],
                addressPostCode=row['addressPostCode'],
                addressCounty=row['addressCounty'],
                schoolYear=row['schoolYear'],
                schoolSubjects=row['schoolSubjects'].split(", "),
                nameParGar1=row['nameParGar1'],
                nameParGar2=row['nameParGar2'],
                contactDetParGar1=row['contactDetParGar1'],
                contactDetParGar2=row['contactDetParGar2'],
                historyLevel=row['historyLevel'],
                historyClassNumber=row['historyClassNumber'],
                historyTeacher=row['historyTeacher'],
                historyLastTestScore=row['historyLastTestScore']
            )

            students.append((math_student, english_student, history_student))

    return students
