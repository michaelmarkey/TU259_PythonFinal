from student import Student

class MathStudent(Student):
    def __init__(self, studentID, fName, mName, lName, age, addressL1, addressL2, addressL3, addressPostCode, 
                 addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, contactDetParGar1, 
                 contactDetParGar2, mathLevel, mathClassNumber, mathTeacher, mathLastTestScore):
        
        super().__init__(studentID, fName, mName, lName, age, addressL1, addressL2, addressL3, addressPostCode, 
                 addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, contactDetParGar1, 
                 contactDetParGar2)
        
        self.mathLevel = mathLevel
        self.mathClassNumber = mathClassNumber
        self.mathTeacher = mathTeacher
        self.mathLastTestScore = mathLastTestScore
        self.mathGrade = mathLastTestScore     

        if "Mathematics" not in self.schoolSubjects:
            self.schoolSubjects.append("Mathematics")

    def add_math_details(self, level, class_number, teacher, last_test_score):
        self.mathLevel = level
        self.mathClassNumber = class_number
        self.mathTeacher = teacher
        self.mathLastTestScore = last_test_score
        self.mathGrade = last_test_score

    def __repr__(self):
        base = super().__repr__()  # This will call Student.__repr__()
        return (f"{base} | Math Level: {self.mathLevel}, "
                f"Class Number: {self.mathClassNumber}, "
                f"Teacher: {self.mathTeacher}, "
                f"Last Test Score: {self.mathLastTestScore}")

class EnglishStudent(Student):
    def __init__(self, studentID, fName, mName, lName, age, addressL1, addressL2, addressL3, addressPostCode, 
                 addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, contactDetParGar1, 
                 contactDetParGar2, englishLevel, englishClassNumber, englishTeacher, englishLastTestScore):
        
        super().__init__(studentID, fName, mName, lName, age, addressL1, addressL2, addressL3, addressPostCode, 
                 addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, contactDetParGar1, 
                 contactDetParGar2)
        
        self.englishLevel = englishLevel
        self.englishClassNumber = englishClassNumber
        self.englishTeacher = englishTeacher
        self.englishLastTestScore = englishLastTestScore
        self.englishGrade = englishLastTestScore
        
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
    def __init__(self, studentID, fName, mName, lName, age, addressL1, addressL2, addressL3, addressPostCode, 
                 addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, contactDetParGar1, 
                 contactDetParGar2, historyLevel, historyClassNumber, historyTeacher, historyLastTestScore):
        
        super().__init__(studentID, fName, mName, lName, age, addressL1, addressL2, addressL3, addressPostCode, 
                 addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, contactDetParGar1, 
                 contactDetParGar2)
        
        self.historyLevel = historyLevel
        self.historyClassNumber = historyClassNumber
        self.historyTeacher = historyTeacher
        self.historyLastTestScore = historyLastTestScore
        self.historyGrade = historyLastTestScore

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

# Helper function to print student details with their grades
def print_student_details(students):
    for student in students:
        print(f"{student.fName} {student.lName} - Year {student.schoolYear}")
        print(student)  # This will use the new __repr__ from above
        print("-" * 40)
