# create the student class

class Student(object):
    def __init__(self, fName, mName, lName, addressL1, addressL2, addressL3, addressPostCode, 
                 addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, contactDetParGar1, 
                 contactDetParGar2):
        
        if schoolSubjects is None:
            schoolSubjects = []

        self.fName = fName
        self.mName = mName
        self.lName = lName
        self.addressL1 = addressL1
        self.addressL2 = addressL2
        self.addressL3 = addressL3
        self.addressPostCode = addressPostCode
        self.addressCounty = addressCounty
        self.schoolYear = schoolYear
        self.schoolSubjects = schoolSubjects
        self.nameParGar1 = nameParGar1
        self.nameParGar2 = nameParGar2
        self.contactDetParGar1 = contactDetParGar1
        self.contactDetParGar2 = contactDetParGar2

    def __repr__(self):
        result = f"Here is a summary of the details for {self.fName} {self.mName} {self.lName}.\n"
        result += f"Address: {self.addressL1}, {self.addressL2}, {self.addressL3}, {self.addressPostCode}, {self.addressCounty}.\n"
        result += f"The student is in {self.schoolYear} and is studying {', '.join(self.schoolSubjects)}.\n"
        result += f"Parent/Guardian 1 is {self.nameParGar1} whose contact number is {self.contactDetParGar1}.\n" 
        result += f"Parent/Guardian 2 is {self.nameParGar2} whose contact number is {self.contactDetParGar2}.\n"
        return result
    
class MathStudent(Student):
    def __init__(self, fName, mName, lName, addressL1, addressL2, addressL3, addressPostCode, 
                 addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, 
                 contactDetParGar1, contactDetParGar2, mathLevel, mathClassNumber, 
                 mathTeacher, mathLastTestScore):
        
        # Initialize the parent class (Student) with the required parameters
        super().__init__(fName, mName, lName, addressL1, addressL2, addressL3, addressPostCode, 
                         addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, 
                         contactDetParGar1, contactDetParGar2)
        
        # Initialize the MathStudent specific attributes
        self.mathLevel = mathLevel
        self.mathClassNumber = mathClassNumber
        self.mathTeacher = mathTeacher
        self.mathLastTestScore = mathLastTestScore

    def add_math_details(self, level, class_number, teacher, last_test_score):
        self.mathLevel = level
        self.mathClassNumber = class_number
        self.mathTeacher = teacher
        self.mathLastTestScore = last_test_score
        if "Mathematics" not in self.schoolSubjects:
            self.schoolSubjects.append("Mathematics")

    def __repr__(self):
        return (#f"Details for Mathematics for the student {self.student.fName} {self.student.lName}:\n"
                f"Level: {self.mathLevel}, Class Number: {self.mathClassNumber}, "
                f"Teacher: {self.mathTeacher}, Last Test Score: {self.mathLastTestScore}.\n")

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
        if "English" not in self.schoolSubjects:
            self.schoolSubjects.append("English")

    def __repr__(self):
        return (f"Details for English for the student {self.fName} {self.lName}:\n"
                f"Level: {self.englishLevel}, Class Number: {self.englishClassNumber}, "
                f"Teacher: {self.englishTeacher}, Last Test Score: {self.englishLastTestScore}.\n")






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
        if "History" not in self.schoolSubjects:
            self.schoolSubjects.append("History")

    def __repr__(self):
        return (#f"Details for History for the student {self.fName} {self.lName}:\n"
                f"Level: {self.historyLevel}, Class Number: {self.historyClassNumber}, "
                f"Teacher: {self.historyTeacher}, Last Test Score: {self.historyLastTestScore}.\n")

