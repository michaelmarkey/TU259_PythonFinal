class Student(object):
    def __init__(self, studentID, fName, mName, lName, age, addressL1, addressL2, addressL3, addressPostCode, 
                 addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, contactDetParGar1, 
                 contactDetParGar2):
        
        if schoolSubjects is None:
            schoolSubjects = []

        self.studentID = studentID
        self.fName = fName
        self.mName = mName
        self.lName = lName
        self.age = age
        self.addressL1 = addressL1
        self.addressL2 = addressL2
        self.addressL3 = addressL3
        self.addressPostCode = addressPostCode
        self.addressCounty = addressCounty
        self.schoolYear = schoolYear
        # Force a copy of subjects, just in case the original list is passed externally and modified later.
        self.schoolSubjects = list(schoolSubjects) 
        self.nameParGar1 = nameParGar1
        self.nameParGar2 = nameParGar2
        self.contactDetParGar1 = contactDetParGar1
        self.contactDetParGar2 = contactDetParGar2
        

    def __repr__(self):
        # Readable output
        result = f"Student ID: {self.studentID}\n"
        result += f"Name: {self.fName} {self.mName} {self.lName}, Age: {self.age}\n"
        result += f"Address: {self.get_full_address()}\n"
        result += f"Subjects: {', '.join(self.schoolSubjects)}\n"
        result += f"Guardian 1: {self.nameParGar1} (Contact: {self.contactDetParGar1})\n"
        result += f"Guardian 2: {self.nameParGar2} (Contact: {self.contactDetParGar2})\n"
        return result

# Update methods

    def update_ID(self, new_studentID):
        if new_studentID is not None:
            self.studentID= new_studentID

    def update_name(self, new_fName=None, new_mName=None, new_lName=None): 
        if new_fName is not None:
            self.fName = new_fName  
        if new_mName is not None:
            self.mName = new_mName  
        if new_lName is not None:
            self.lName = new_lName 

    def update_address(self, new_addressL1=None, new_addressL2=None, new_addressL3=None, new_addressPostCode=None, new_addressCounty=None):  # new: update address fields
        if new_addressL1 is not None:
            self.addressL1 = new_addressL1  
        if new_addressL2 is not None:
            self.addressL2 = new_addressL2  
        if new_addressL3 is not None:
            self.addressL3 = new_addressL3  
        if new_addressPostCode is not None:
            self.addressPostCode = new_addressPostCode  
        if new_addressCounty is not None:
            self.addressCounty = new_addressCounty  

    def update_age(self, new_age):
        self.age = new_age

    def update_school_year(self, new_schoolYear):  # new: method to update school year
        self.schoolYear = new_schoolYear  # new: set new school year

    def add_subject(self, new_subject):  # new: add a subject to the student's list
        if new_subject not in self.schoolSubjects:
            self.schoolSubjects.append(new_subject)  # new: append new subject
    
    def update_subjects(self, new_subjects):
        """Replace all subjects with a new list."""
        self.schoolSubjects = list(new_subjects)

    def remove_subject(self, old_subject):  # new: remove a subject from the student's list
        if old_subject in self.schoolSubjects:
            self.schoolSubjects.remove(old_subject)  # new: remove existing subject

    def update_guardian_contact(self, guardian_number, new_name=None, new_contact=None):  # new: update guardian details
        if guardian_number == 1:
            if new_name is not None:
                self.nameParGar1 = new_name  # new: update guardian1 name
            if new_contact is not None:
                self.contactDetParGar1 = new_contact  # new: update guardian1 contact
        elif guardian_number == 2:
            if new_name is not None:
                self.nameParGar2 = new_name  # new: update guardian2 name
            if new_contact is not None:
                self.contactDetParGar2 = new_contact  # new: update guardian2 contact

# Data Access

    def get_full_student_data(self):
        """Return all of this student's data"""
        result = f"Student ID: {self.studentID}\n"
        result += f"Name: {self.fName} {self.mName} {self.lName}\n"
        result += f"Age: {self.age}\n"
        result += f"Address: {self.get_full_address()}\n"
        result += f"School Year: {self.schoolYear}\n"
        result += f"Subjects: {', '.join(self.schoolSubjects)}\n"
        result += f"Guardian 1: {self.nameParGar1} (Contact: {self.contactDetParGar1})\n"
        result += f"Guardian 2: {self.nameParGar2} (Contact: {self.contactDetParGar2})\n"
        return result
    
    def get_summary_student_data(self):
        """Return a summary of the student data"""
        result = f"Student ID: {self.studentID}\n"
        result += f"Name: {self.fName} {self.mName} {self.lName}\n"
        result += f"Age: {self.age}\n"
        return result

    
    def get_full_address(self):
        """Return the full address as a formatted string."""
        parts = [self.addressL1, self.addressL2, self.addressL3, self.addressPostCode, self.addressCounty]
        return ", ".join(part for part in parts if part)
    
    def get_guardian_info(self):
        """Return a readable format of guardian names and contact details."""
        result = f"Guardian 1: {self.nameParGar1} (Contact: {self.contactDetParGar1}\n"
        result += f"Guardian 2: {self.nameParGar2} (Contact: {self.contactDetParGar2}\n"
        return result

    def get_subjects(self):
        """Returns subjects the student is taking."""
        return ", ".join(self.schoolSubjects)
    
# Checks

    def is_full_name_available(self):
        """Check if student has both a first name and last name."""
        return bool(self.fName and self.lName)
    
    def is_address_complete(self):
        """Check if all address fields are filled."""
        fields = [self.addressL1, self.addressPostCode, self.addressCounty]
        return all(fields)
    
    def is_in_year(self, year):
        """Check if the student is in a particular school year."""
        return self.schoolYear == year
    
    def is_enrolled_in(self, subject):
        """Check if the student is enrolled in a particular subject."""
        return subject in self.schoolSubjects
    
    def is_guardian_contact_available(self, guardian_number):
        """Check if the selected guardian has contact details available."""
        if guardian_number == 1:
            return bool(self.contactDetParGar1)
        elif guardian_number == 2:
            return bool(self.contactDetParGar2)
        else:
            raise ValueError("guardian_number must be 1 or 2")
