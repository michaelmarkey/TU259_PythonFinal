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
        try:
            math = f"{self.mathGrade:.2f}" if self.mathGrade is not None else "N/A"
        except:
            math = "N/A"

        try:
            english = f"{self.englishGrade:.2f}" if self.englishGrade is not None else "N/A"
        except:
            english = "N/A"

        try:
            history = f"{self.historyGrade:.2f}" if self.historyGrade is not None else "N/A"
        except:
            history = "N/A"

        return (f"{self.fName} {self.lName} | Year: {self.schoolYear} | "
                f"Address: {self.addressL1}, {self.addressL2}, {self.addressL3}, "
                f"{self.addressPostCode}, {self.addressCounty} | "
                f"Subjects: {', '.join(self.schoolSubjects)} | "
                f"Math: {math}, English: {english}, History: {history}")


    def update_name(self, fName=None, mName=None, lName=None):  # new: method to update name fields
        if fName is not None:
            self.fName = fName  # new: update first name
        if mName is not None:
            self.mName = mName  # new: update middle name
        if lName is not None:
            self.lName = lName  # new: update last name

    def update_address(self, addressL1=None, addressL2=None, addressL3=None, addressPostCode=None, addressCounty=None):  # new: update address fields
        if addressL1 is not None:
            self.addressL1 = addressL1  # new: update address line 1
        if addressL2 is not None:
            self.addressL2 = addressL2  # new: update address line 2
        if addressL3 is not None:
            self.addressL3 = addressL3  # new: update address line 3
        if addressPostCode is not None:
            self.addressPostCode = addressPostCode  # new: update postal code
        if addressCounty is not None:
            self.addressCounty = addressCounty  # new: update county

    def update_school_year(self, schoolYear):  # new: method to update school year
        self.schoolYear = schoolYear  # new: set new school year

    def add_subject(self, subject):  # new: add a subject to the student's list
        if subject not in self.schoolSubjects:
            self.schoolSubjects.append(subject)  # new: append new subject

    def remove_subject(self, subject):  # new: remove a subject from the student's list
        if subject in self.schoolSubjects:
            self.schoolSubjects.remove(subject)  # new: remove existing subject

    def update_guardian_contact(self, guardian_number, name=None, contact=None):  # new: update guardian details
        if guardian_number == 1:
            if name is not None:
                self.nameParGar1 = name  # new: update guardian1 name
            if contact is not None:
                self.contactDetParGar1 = contact  # new: update guardian1 contact
        elif guardian_number == 2:
            if name is not None:
                self.nameParGar2 = name  # new: update guardian2 name
            if contact is not None:
                self.contactDetParGar2 = contact  # new: update guardian2 contact

    def get_student_data(self):
            """
            Return all of this student's base‐class init arguments,
            in the exact order expected by MathStudent/EnglishStudent/HistoryStudent.
            """
            return (
                self.fName,
                self.mName,
                self.lName,
                self.addressL1,
                self.addressL2,
                self.addressL3,
                self.addressPostCode,
                self.addressCounty,
                self.schoolYear,
                self.schoolSubjects,
                self.nameParGar1,
                self.nameParGar2,
                self.contactDetParGar1,
                self.contactDetParGar2,
            )