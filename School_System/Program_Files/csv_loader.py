import csv
from student import Student
from subject import SubjectStudent
from employee import Teacher

def find_student_by_id(student_id, students):
    """Find a student by ID in a list of students"""
    for student in students:
        if student.studentID == student_id:
            return student
    return None

def find_employee_by_id(employee_id, employees):
    """Find an employee by ID in a list of employees"""
    for employee in employees:
        if employee.employeeID == employee_id:
            return employee
    return None

def load_students_from_csv(filename):
    """Load basic student data and return a list of Student objects"""
    students = []
    # Open and read CSV, create basic Student objects with core attributes
    # Return list of Student objects

    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Create a list of subjects if provided
                    subjects = []
                    if 'schoolSubjects' in row and row['schoolSubjects']:
                        subjects = [subj.strip() for subj in row['schoolSubjects'].split(',')]
                    
                    # Create empty subject_grades dictionary
                    subject_grades = {}
                    
                    # Convert age and postcode to integers
                    age = int(row.get('age', 0))
                    # postcode = int(row.get('addressPostCode', 0))
                    
                    # Convert contact details to integers if they exist
                    contact1 = int(row.get('contactDetParGar1', 0)) if row.get('contactDetParGar1') else 0
                    contact2 = int(row.get('contactDetParGar2', 0)) if row.get('contactDetParGar2') else 0
                    
                    # Create new student object
                    student = Student(
                        studentID=row.get('studentID', ''),
                        fName=row.get('fName', ''),
                        mName=row.get('mName', ''),
                        lName=row.get('lName', ''),
                        age=age,
                        addressL1=row.get('addressL1', ''),
                        addressL2=row.get('addressL2', ''),
                        addressL3=row.get('addressL3', ''),
                        addressPostCode=row.get('addressPostCode', ''),
                        addressCounty=row.get('addressCounty', ''),
                        schoolYear=row.get('schoolYear', ''),
                        schoolSubjects=subjects,
                        nameParGar1=row.get('nameParGar1', ''),
                        nameParGar2=row.get('nameParGar2', ''),
                        contactDetParGar1=contact1,
                        contactDetParGar2=contact2,
                        subject_grades=subject_grades
                    )
                    
                    students.append(student)
                except (ValueError, KeyError) as e:
                    print(f"Error processing student row: {e}")
                    continue
                    
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error reading from {filename}: {e}")
        
    print(f"Loaded {len(students)} students from {filename}")
    return students

def load_employees_from_csv(filename):
    """Load basic employee (teacher) data and return a list of Teacher objects"""
    employees = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:

                    emp_type = row.get('Type', '').strip().lower()
                    if not emp_type:
                        print(f"Skipping row with missing employee Type: {row}")
                        continue

                    # Common fields
                    employeeID = row.get('employeeID', '')
                    fName = row.get('fName', '')
                    mName = row.get('mName', '')
                    lName = row.get('lName', '')
                    dob = row.get('dob', '')
                    address = row.get('address', '')
                    contact_number = row.get('contact_number', '')
                    email = row.get('email', '')
                    start_date = row.get('start_date', '')

                    if emp_type == 'teacher':
                        subjects_raw = row.get('Subjects', '')
                        subjects = [s.strip() for s in subjects_raw.split(',')] if subjects_raw else []
                        
                        # YearsTeaching: Try to convert to int or default to 0
                        try:
                            years_teaching = int(row.get('YearsTeaching', 0))
                        except ValueError:
                            years_teaching = 0

                        emp = Teacher(employeeID, fName, lName, dob, address, contact_number, email, start_date,
                                      subjects=subjects, years_teaching=years_teaching)

                    elif emp_type == 'medic':
                        license_number = row.get('LicenseNumber', '')
                        office_location = row.get('OfficeLocation', '')
                        emp = Medic(employeeID, fName, lName, dob, address, contact_number, email, start_date,
                                    license_number=license_number, office_location=office_location)

                    elif emp_type == 'counselor':
                        cert_id = row.get('CertID', '')
                        specializations = row.get('Specializations', '').split(',') if row.get('Specializations') else []
                        specializations = [s.strip() for s in specializations]
                        emp = Counselor(employeeID, fName, lName, dob, address, contact_number, email, start_date,
                                        cert_id=cert_id, specializations=specializations)

                    elif emp_type == 'administrator':
                        department = row.get('Department', '')
                        office_hours = row.get('OfficeHours', '')
                        responsibilities = row.get('Responsibilities', '').split(',') if row.get('Responsibilities') else []
                        responsibilities = [r.strip() for r in responsibilities]
                        emp = Administrator(employeeID, fName, lName, dob, address, contact_number, email, start_date,
                                            department=department, office_hours=office_hours, responsibilities=responsibilities)

                    elif emp_type == 'principal':
                        office_number = row.get('OfficeNumber', '')
                        years_as_principal = int(row.get('YearsAsPrincipal', 0))
                        departments = row.get('Departments', '').split(',') if row.get('Departments') else []
                        departments = [d.strip() for d in departments]
                        emp = Principal(employeeID, fName, lName, dob, address, contact_number, email, start_date,
                                        office_number=office_number, years_as_principal=years_as_principal, departments=departments)

                    else:
                        print(f"Unknown employee type '{emp_type}' in row: {row}")
                        continue

                    employees.append(emp)

                except Exception as e:
                    print(f"Error processing employee row: {row}\n  → {e}")
                    continue

    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error reading from {filename}: {e}")

    print(f"Loaded {len(employees)} employees from {filename}")
    return employees



def load_math_grades_from_csv(filename, students):
    """Add math grades to existing students"""
    count = 0
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Find matching student by ID
                    student_id = row.get('studentID')
                    student = find_student_by_id(student_id, students)
                    
                    if student:
                        # Add Mathematics to student's subjects if not already present
                        if "Mathematics" not in student.schoolSubjects:
                            student.schoolSubjects.append("Mathematics")
                        
                        # If we have detailed grade data
                        if all(key in row for key in ['quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 'test1', 'test2', 'finalExam']):
                            # Store raw scores for calculation
                            quizzes = [
                                float(row.get('quiz1', 0)),
                                float(row.get('quiz2', 0)),
                                float(row.get('quiz3', 0)),
                                float(row.get('quiz4', 0)),
                                float(row.get('quiz5', 0))
                            ]
                            test1 = float(row.get('test1', 0))
                            test2 = float(row.get('test2', 0))
                            final_exam = float(row.get('finalExam', 0))
                            
                            # Store all grades in a list attribute
                            student.mathGrades = quizzes + [test1, test2, final_exam]
                            
                        # If we just have a test score
                        elif 'lastTestScore' in row:
                            test_score = float(row.get('lastTestScore', 0))
                            
                            # Create a SubjectStudent object for Mathematics
                            math_subject = SubjectStudent(
                                student=student,
                                subject_name="Mathematics",
                                subject_level=row.get('level', ''),
                                subject_class_number=row.get('classNumber', ''),
                                subject_teacher=row.get('teacher', ''),
                                last_test_score=test_score
                            )
                            
                            # Add direct math attributes for compatibility with older code
                            student.mathLastTestScore = test_score
                            student.mathGrade = test_score
                            
                            # Update subject_grades dictionary
                            student.subject_grades["Mathematics"] = test_score
                            
                        count += 1
                except (ValueError, KeyError) as e:
                    print(f"Error processing math grade row: {e}")
                    continue
                    
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error reading from {filename}: {e}")
        
    print(f"Updated {count} students with math grades from {filename}")
    return students

def load_english_grades_from_csv(filename, students):
    """Add english grades to existing students"""
    count = 0
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Find matching student by ID
                    student_id = row.get('studentID')
                    student = find_student_by_id(student_id, students)
                    
                    if student:
                        # Add English to student's subjects if not already present
                        if "English" not in student.schoolSubjects:
                            student.schoolSubjects.append("English")
                        
                        # If we have detailed grade data
                        if all(key in row for key in ['attendance', 'quiz1', 'quiz2', 'finalExam']):
                            # Store individual scores for calculation
                            student.englishAttendance = float(row.get('attendance', 0))
                            student.englishQuiz1 = float(row.get('quiz1', 0))
                            student.englishQuiz2 = float(row.get('quiz2', 0))
                            student.englishFinalExam = float(row.get('finalExam', 0))
                            
                        # If we just have a test score
                        elif 'lastTestScore' in row:
                            test_score = float(row.get('lastTestScore', 0))
                            
                            # Create a SubjectStudent object for English
                            english_subject = SubjectStudent(
                                student=student,
                                subject_name="English",
                                subject_level=row.get('level', ''),
                                subject_class_number=row.get('classNumber', ''),
                                subject_teacher=row.get('teacher', ''),
                                last_test_score=test_score
                            )
                            
                            # Add direct english attributes for compatibility with older code
                            student.englishLastTestScore = test_score
                            student.englishGrade = test_score
                            
                            # Update subject_grades dictionary
                            student.subject_grades["English"] = test_score
                            
                        count += 1
                except (ValueError, KeyError) as e:
                    print(f"Error processing English grade row: {e}")
                    continue
                    
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error reading from {filename}: {e}")
        
    print(f"Updated {count} students with English grades from {filename}")
    return students

def load_history_grades_from_csv(filename, students):
    """Add history grades to existing students"""
    count = 0
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Find matching student by ID
                    student_id = row.get('studentID')
                    student = find_student_by_id(student_id, students)
                    
                    if student:
                        # Add History to student's subjects if not already present
                        if "History" not in student.schoolSubjects:
                            student.schoolSubjects.append("History")
                        
                        # If we have detailed grade data
                        if all(key in row for key in ['attendance', 'project', 'exam1', 'exam2']):
                            # Store individual scores for calculation
                            student.historyAttendance = float(row.get('attendance', 0))
                            student.historyProject = float(row.get('project', 0))
                            student.historyExams = [
                                float(row.get('exam1', 0)),
                                float(row.get('exam2', 0))
                            ]
                            
                        # If we just have a test score
                        elif 'lastTestScore' in row:
                            test_score = float(row.get('lastTestScore', 0))
                            
                            # Create a SubjectStudent object for History
                            history_subject = SubjectStudent(
                                student=student,
                                subject_name="History",
                                subject_level=row.get('level', ''),
                                subject_class_number=row.get('classNumber', ''),
                                subject_teacher=row.get('teacher', ''),
                                last_test_score=test_score
                            )
                            
                            # Add direct history attributes for compatibility with older code
                            student.historyLastTestScore = test_score
                            student.historyGrade = test_score
                            
                            # Update subject_grades dictionary
                            student.subject_grades["History"] = test_score
                            
                        count += 1
                except (ValueError, KeyError) as e:
                    print(f"Error processing History grade row: {e}")
                    continue
                    
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error reading from {filename}: {e}")
        
    print(f"Updated {count} students with History grades from {filename}")
    return students

def load_all_data(student_file, math_file=None, english_file=None, history_file=None, employee_file=None):
    """Load all student data from CSV files"""
    # Load basic students first
    students = load_students_from_csv(student_file)
    
    # Load basic employees (teachers)
    employees = load_employees_from_csv(employee_file)

    # Add subject data to existing students
    if math_file:
        students = load_math_grades_from_csv(math_file, students)
    if english_file:
        students = load_english_grades_from_csv(english_file, students)
    if history_file:
        students = load_history_grades_from_csv(history_file, students)
        
    print(f"Loaded data for {len(students)} students and {len(employees)} employees in total")
    return students, employees