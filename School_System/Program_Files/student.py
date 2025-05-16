class Student(object):
    """This class is the base class for the students in the school system. 
     It stores and manages student information, including personal details """

    def __init__(self, studentID:str, fName:str, mName:str, lName:str, age:int, addressL1:str, addressL2:str, addressL3:str, addressPostCode:str, 
                 addressCounty:str, schoolYear:str, schoolSubjects:list, nameParGar1:str, nameParGar2:str, contactDetParGar1:int, contactDetParGar2:int,
                 subject_grades:dict = None):
        
        # Input validation
        if not studentID:
            raise ValueError("Student ID cannot be empty")
        if age < 0:
            raise ValueError("Age cannot be negative")
        
        if schoolSubjects is None:
            schoolSubjects = []
        
        if subject_grades is None:
            subject_grades = {}

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
        self.subject_grades = subject_grades  # Store the grades for each subject

    def __repr__(self):
        """Returns a formatted string with student information"""

        result = f"Student ID: {self.studentID}\n"
        result += f"Name: {self.fName} {self.mName} {self.lName}\n" 
        result += f"Age: {self.age}\n"
        result += f"Address: {self.addressL1} {self.addressL2} {self.addressL3} {self.addressPostCode} {self.addressCounty}\n"
        result += f"Subjects: {', '.join(self.schoolSubjects)}\n"
        result += f"Guardian 1: {self.nameParGar1} (Contact: {self.contactDetParGar1})\n"
        result += f"Guardian 2: {self.nameParGar2} (Contact: {self.contactDetParGar2})\n"
        return result

# Methods used to update student information

    def update_ID(self, new_studentID):
        """Update the student's ID if input is not empty"""

        if new_studentID is not None:
            self.studentID= new_studentID

    def update_name(self, new_fName:str=None, new_mName:str=None, new_lName:str=None): 
        """Update the student's name. Option here to only update individual parts of a student's name"""
        
        if new_fName is not None:
            self.fName = new_fName  
        if new_mName is not None:
            self.mName = new_mName  
        if new_lName is not None:
            self.lName = new_lName 

    def update_address(self, new_addressL1=None, new_addressL2=None, new_addressL3=None, new_addressPostCode=None, new_addressCounty=None):  # new: update address fields
        """Update the student's address. Option here to only update individual parts of a student's address"""

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
        """Update the student's age."""

        self.age = new_age

    def update_school_year(self, new_schoolYear):  
        """Update the student's school year."""

        self.schoolYear = new_schoolYear  

    def add_subject(self, new_subject):
        """Add a subject to the student's list if not already present."""


        if not new_subject:
            raise ValueError("Subject name cannot be empty")
        if new_subject not in self.schoolSubjects:
            self.schoolSubjects.append(new_subject)  # append new subject

    def remove_subject(self, old_subject):
        """Remove a subject to the student's list if present."""
        if old_subject in self.schoolSubjects:
            self.schoolSubjects.remove(old_subject)  

    def add_grade(self, subject, grade):
        """Add or upgrage a grade for a student"""

        try:
            grade_value = float(grade)
        except (ValueError, TypeError):
            raise TypeError("Grade must be a number")
        
        self.subject_grades[subject] = grade

    def calculate_overall_average(self):
        ''' Calculates the average grade across all subjects'''

        total = 0
        count = 0
        
        # Iterate through each subject in the list
        for subject in ['Mathematics', 'English', 'History']:
            if subject in self.subject_grades:
                total += float(self.subject_grades[subject])
                count += 1
        
        # Calculate and return the average, if there are any grades
        if count > 0:
            return total / count
        else:
            return None  # Return None if no grades are available
    
    def update_guardian_contact(self, guardian_number, new_name=None, new_contact=None):  
        """Update guardian details. Allows the user to fully or partially update."""

        if guardian_number == 1:
            if new_name is not None:
                self.nameParGar1 = new_name  # update guardian1 name
            if new_contact is not None:
                self.contactDetParGar1 = new_contact  # update guardian1 contact
        elif guardian_number == 2:
            if new_name is not None:
                self.nameParGar2 = new_name  # update guardian2 name
            if new_contact is not None:
                self.contactDetParGar2 = new_contact  # update guardian2 contact

# Data Access Methods

    def get_full_student_data(self):
        """Get all student data as a formatted string"""

        result = f"Student ID: {self.studentID}\n"
        result += f"Name: {self.fName} {self.mName} {self.lName}\n"
        result += f"Age: {self.age}\n"
        result += f"Address: {self.addressL1} {self.addressL2} {self.addressL3} {self.addressPostCode} {self.addressCounty}\n"
        result += f"School Year: {self.schoolYear}\n"
        result += f"Subjects: {', '.join(self.schoolSubjects)}\n"
        result += f"Guardian 1: {self.nameParGar1} (Contact: {self.contactDetParGar1})\n"
        result += f"Guardian 2: {self.nameParGar2} (Contact: {self.contactDetParGar2})\n"
        return result
    
    def get_summary_student_data(self):
        """Get a summary of student data"""

        result = f"Student ID: {self.studentID}\n"
        result += f"Name: {self.fName} {self.mName} {self.lName}\n"
        result += f"Age: {self.age}\n"
        return result


    def get_full_address(self):
        """Get the full address as a formatted string."""

        return f"Address: {self.addressL1} {self.addressL2} {self.addressL3} {self.addressPostCode} {self.addressCounty}\n"
    
    def get_guardian_info(self):
        """Get guardian information as a formatted string"""

        result = f"Guardian 1: {self.nameParGar1} (Contact: {self.contactDetParGar1})\n"
        result += f"Guardian 2: {self.nameParGar2} (Contact: {self.contactDetParGar2})\n"
        return result

    def get_subjects(self):
        """Get the student's subjects as a formatted string"""

        return f"Subjects: {', '.join(self.schoolSubjects)}\n"
    
# Check Methods

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
