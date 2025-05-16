#This module defines classes for representing employees in a school system,
# including general employees, teachers, principals, medics, administrators,
# and counselors.

from datetime import datetime

class Employee:
    """ Base class for all employees in the school."""

    def __init__(self, employeeID, fName, lName, dob, address, contact_number, email, start_date):
        
        if not all([employeeID, fName, lName, dob, address, contact_number, email]):
            raise ValueError("Employee details cannot be empty")
        
        self.employeeID = employeeID
        self.fName = fName
        self.lName = lName
        self.dob = dob  # Format: "YYYY-MM-DD"
        self.address = address
        self.contact_number = contact_number
        self.email = email
        
        #Avoids issues with input in CSV files
        if isinstance(start_date, str):
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d")  # stored as datetime object
        else:
            self.start_date = start_date

    #Methods common to all employees

    def get_name(self):
        """Returns the full name of the employee"""

        return f"{self.fName} {self.lName}"

    def get_contact_info(self):
        """Returns the contact details of the employee"""

        return f"Email: {self.email}, Phone: {self.contact_number}"

    def get_years_of_service(self):
        """Calcuates the number of years of service of the employee"""

        today = datetime.today()
        return today.year - self.start_date.year - ((today.month, today.day) < (self.start_date.month, self.start_date.day))

    def __repr__(self):
        """Returns a string representation of the employee"""
        return f"{self.get_name()} (ID: {self.employeeID})"


class Teacher(Employee):
    """Represents a teacher in the school"""
    
    def __init__(self, employeeID, fName, lName, dob, address, contact_number, email, start_date, subjects=None, years_teaching=0):
        super().__init__(employeeID, fName, lName, dob, address, contact_number, email, start_date)
        self.subjects = subjects or []
        self.years_teaching = years_teaching
        self.schedule = {}

    def get_name(self):
        """Returns the full name of the teacher"""

        return f"{self.fName} {self.lName}"
    
    def assign_grade(self, student, subject, grade):
        """Assigns a grade to a student for a specific subject, checks to make sure it is the right format and in the right range"""

        if not isinstance(grade, float):
            raise TypeError("Grade must be a float")
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100")
        student.add_grade(subject, grade)

    def get_teaching_schedule(self):
        """Returns the teaching schecude of the teacher."""

        return self.schedule

    def set_teaching_schedule(self, subject, time_slot):
        """Sets the time slot for the teacher."""

        self.schedule[subject] = time_slot

    def assign_subject(self, subject):
        """ Assign this teacher to a subject """

        if subject not in self.subjects:
            self.subjects.append(subject)

    def __repr__(self):
        """Returns a string representation of the Teacher object"""

        return f"{self.get_name()} (ID: {self.employeeID}, Subjects: {', '.join([subj.name for subj in self.subjects])})"


class Principal(Employee):
    """Represents a principal in the school"""

    def __init__(self, employeeID, fName, lName, dob, address, contact_number, email, start_date, office_number, years_as_principal, departments=None):
        super().__init__(employeeID, fName, lName, dob, address, contact_number, email, start_date)
        self.office_number = office_number
        self.years_as_principal = years_as_principal
        self.departments = departments or []

    def evaluate_teacher(self, teacher, feedback):
        """Evaluates a teacher and provides feedback."""

        return f"Evaluated {teacher.get_name()}: {feedback}"

    def get_school_summary(self, school):
        """Returns a summary of the school"""

        return repr(school)
    
    def __repr__(self):
        """Returns a string representation of the Principal object"""

        return f"{self.get_name()} (ID: {self.employeeID}, Office: {self.office_number}, Years as Principal: {self.years_as_principal}, Departments: {self.departments})"


class Medic(Employee):
    """Represents a medic in the school"""

    def __init__(self, employeeID, fName, lName, dob, address, contact_number, email, start_date, license_number, office_location):
        super().__init__(employeeID, fName, lName, dob, address, contact_number, email, start_date)
        self.license_number = license_number
        self.office_location = office_location
        self.emergency_contacts = {}

    def record_incident(self, student, incident):
        """Records a medical incident for a student"""

        print(f"Recorded incident for {student.get_name()}: {incident}")

    def get_medical_summary(self):
        """Returns a medical summary of the medic"""

        return f"Medic {self.get_name()}, License: {self.license_number}"

    def alert_guardian(self, student):
        """Alerts the guardian of a student"""
        
        try:
            print(
                f"Alert sent to {student.nameParGar1} ({student.contactDetParGar1}) and {student.nameParGar2} ({student.contactDetParGar2})")
        except AttributeError as e:
            raise AttributeError(f"Student object is missing guardian information: {e}")

    def __repr__(self):
        """Returns a string representation of the Medic object"""

        return f"{self.get_name()} (ID: {self.employeeID}, License: {self.license_number}, Office: {self.office_location})"

class Administrator(Employee):
    """Represents an administrator in the school"""

    def __init__(self, employeeID, fName, lName, dob, address, contact_number, email, start_date, department, office_hours, responsibilities=None):
        super().__init__(employeeID, fName, lName, dob, address, contact_number, email, start_date)
        self.department = department
        self.office_hours = office_hours
        self.responsibilities = responsibilities or []

    def enroll_student(self, school, student):
        school.register_student(student)

    def schedule_meeting(self, with_whom, time):
        return f"Meeting with {with_whom} scheduled at {time}"

    def generate_report(self):
        return f"{self.get_name()}'s Report: Responsibilities - {', '.join(self.responsibilities)}"

    def __repr__(self):
        """Returns a string representation of the Administrator object"""

        return f"{self.get_name()} (ID: {self.employeeID}, Department: {self.department}, Office Hours: {self.office_hours}, Responsibilities: {self.responsibilities})"


class Counselor(Employee):
    """Represents a counselor in the school"""

    def __init__(self, employeeID, fName, lName, dob, address, contact_number, email, start_date, cert_id, specializations=None):
        super().__init__(employeeID, fName, lName, dob, address, contact_number, email, start_date)
        self.cert_id = cert_id
        self.specializations = specializations or []
        self.student_notes = {}

    def schedule_session(self, student, time):
        """Note when a session is scheduled with a specific student"""

        return f"Session with {student.get_name()} scheduled at {time}"

    def log_note(self, student, note):
        """Update notes"""

        if student.studentID not in self.student_notes:
            self.student_notes[student.studentID] = []
        self.student_notes[student.studentID].append(note)

    def recommend_course(self, student, course):
        """Returns what course was recommended for a particular student"""

        return f"Recommended course '{course}' for {student.get_name()}"
    
    def __repr__(self):
        """Returns a string representation of the Counselor object"""

        return f"{self.get_name()} (ID: {self.employeeID}, Specialization: {self.specialization}, Certification ID: {self.cert_id})"