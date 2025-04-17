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
        math = f"{self.mathGrade:.2f}" if hasattr(self, "mathGrade") else "N/A"
        english = f"{self.englishGrade:.2f}" if hasattr(self, "englishGrade") else "N/A"
        history = f"{self.historyGrade:.2f}" if hasattr(self, "historyGrade") else "N/A"

        return (f"{self.fName} {self.lName} | Year: {self.schoolYear} | "
                f"Math: {math}, English: {english}, History: {history}")
