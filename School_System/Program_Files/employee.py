# employee.py

from datetime import datetime

class Employee:
    def __init__(self, employeeID, fName, lName, dob, address, contact_number, email, start_date):
        self.employeeID = employeeID
        self.fName = fName
        self.lName = lName
        self.dob = dob  # Format: "YYYY-MM-DD"
        self.address = address
        self.contact_number = contact_number
        self.email = email
        #Avoides issues with input in CSV files
        if isinstance(start_date, str):
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d")  # stored as datetime object
        else:
            self.start_date = start_date

    #Methods common to all employees

    def get_name(self):
        return f"{self.fName} {self.lName}"

    def get_contact_info(self):
        return f"Email: {self.email}, Phone: {self.contact_number}"

    def get_years_of_service(self):
        today = datetime.today()
        return today.year - self.start_date.year - ((today.month, today.day) < (self.start_date.month, self.start_date.day))

    def __repr__(self):
        return f"{self.get_name()} (ID: {self.employeeID})"


class Teacher(Employee):
    def __init__(self, employeeID, fName, lName, dob, address, contact_number, email, start_date, subjects=None, years_teaching=0):
        super().__init__(employeeID, fName, lName, dob, address, contact_number, email, start_date)
        self.subjects = subjects or []
        self.years_teaching = years_teaching
        self.schedule = {}

    def get_name(self):
        return f"{self.fName} {self.lName}"
    
    def assign_grade(self, student, subject, grade):
        student.add_grade(subject, grade)

    def get_teaching_schedule(self):
        return self.schedule

    def set_teaching_schedule(self, subject, time_slot):
        self.schedule[subject] = time_slot

    def assign_subject(self, subject):
        """ Assign this teacher to a subject """
        if subject not in self.subjects:
            self.subjects.append(subject)

    def __repr__(self):
        return f"{self.get_name()} (ID: {self.employeeID}, Subjects: {', '.join([subj.name for subj in self.subjects])})"

    


class Principal(Employee):
    def __init__(self, employeeID, fName, lName, dob, address, contact_number, email, start_date, office_number, years_as_principal, departments=None):
        super().__init__(employeeID, fName, lName, dob, address, contact_number, email, start_date)
        self.office_number = office_number
        self.years_as_principal = years_as_principal
        self.departments = departments or []

    def evaluate_teacher(self, teacher, feedback):
        return f"Evaluated {teacher.get_name()}: {feedback}"

    def get_school_summary(self, school):
        return repr(school)


class Medic(Employee):
    def __init__(self, employeeID, fName, lName, dob, address, contact_number, email, start_date, license_number, office_location):
        super().__init__(employeeID, fName, lName, dob, address, contact_number, email, start_date)
        self.license_number = license_number
        self.office_location = office_location
        self.emergency_contacts = {}

    def record_incident(self, student, incident):
        print(f"Recorded incident for {student.get_name()}: {incident}")

    def get_medical_summary(self):
        return f"Medic {self.get_name()}, License: {self.license_number}"

    def alert_guardian(self, student):
        print(f"Alert sent to {student.nameParGar1} ({student.contactDetParGar1}) and {student.nameParGar2} ({student.contactDetParGar2})")


class Administrator(Employee):
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


class Counselor(Employee):
    def __init__(self, employeeID, fName, lName, dob, address, contact_number, email, start_date, cert_id, specializations=None):
        super().__init__(employeeID, fName, lName, dob, address, contact_number, email, start_date)
        self.cert_id = cert_id
        self.specializations = specializations or []
        self.student_notes = {}

    def schedule_session(self, student, time):
        return f"Session with {student.get_name()} scheduled at {time}"

    def log_note(self, student, note):
        if student.studentID not in self.student_notes:
            self.student_notes[student.studentID] = []
        self.student_notes[student.studentID].append(note)

    def recommend_course(self, student, course):
        return f"Recommended course '{course}' for {student.get_name()}"
