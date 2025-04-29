import csv
from student import Student
from subject import MathStudent, EnglishStudent, HistoryStudent
from grade_calculator import calculate_math_grade, calculate_english_grade, calculate_history_grade
from pathlib import Path

def load_students_from_csv(filename):
    students = []
    file_path = Path(__file__).parent / "CSV_Files" / filename
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if present
            for row in reader:
                # Ensure we have enough columns
                if len(row) >= 16:  # Adding studentID and age
                    studentID, fName, mName, lName, age, addressL1, addressL2, addressL3, addressPostCode, addressCounty, schoolYear, schoolSubjects, nameParGar1, nameParGar2, contactDetParGar1, contactDetParGar2 = row[:16]
                    
                    # Convert age to integer and ensure schoolSubjects is a list
                    try:
                        age = int(age)
                    except ValueError:
                        age = 0  # Default age if conversion fails
                    
                    schoolSubjects = schoolSubjects.split(',') if schoolSubjects else []
                    
                    student = Student(studentID, fName, mName, lName, age, addressL1, addressL2, addressL3, 
                                      addressPostCode, addressCounty, schoolYear, schoolSubjects,
                                      nameParGar1, nameParGar2, contactDetParGar1, contactDetParGar2)
                    students.append(student)
                else:
                    print(f"Skipping row with insufficient data: {row}")
        return students
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"Error loading students: {e}")
        return []

def load_maths_grades_from_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if present
            for row in reader:
                if len(row) >= 10:  # studentID, fname, lname, 5 quizzes, 2 tests, 1 final
                    studentID, fName, lName, *grades = row  # First 3 columns are ID, first and last name
                    
                    # Find student by ID (primary key)
                    student = next((s for s in students if s.studentID == studentID), None)
                    
                    if student:
                        try:
                            # Convert all grade entries to float
                            math_grades = list(map(float, grades))
                            
                            # Store raw grades for future calculations
                            student.mathGrades = math_grades
                            
                            # Extract grades by type
                            quiz_grades = math_grades[:5]  # First 5 entries are quiz grades
                            test1, test2 = math_grades[5:7]  # Next 2 are test grades
                            final_exam = math_grades[7]     # Last one is the final exam
                            
                            # Calculate and store final grade
                            student.mathGrade = calculate_math_grade(quiz_grades, test1, test2, final_exam)
                            
                            # Check if this is a MathStudent or should be converted to one
                            if not isinstance(student, MathStudent):
                                # Default values for math-specific fields
                                mathLevel = "Standard"
                                mathClassNumber = "101"
                                mathTeacher = "TBD"
                                mathLastTestScore = student.mathGrade
                                
                                # Create new MathStudent with all existing data plus math-specific data
                                math_student = MathStudent(
                                    student.studentID, student.fName, student.mName, student.lName,
                                    student.age, student.addressL1, student.addressL2, student.addressL3,
                                    student.addressPostCode, student.addressCounty, student.schoolYear,
                                    student.schoolSubjects, student.nameParGar1, student.nameParGar2,
                                    student.contactDetParGar1, student.contactDetParGar2,
                                    mathLevel, mathClassNumber, mathTeacher, mathLastTestScore
                                )
                                
                                # Replace original student with math student in the list
                                students[students.index(student)] = math_student
                            
                        except (ValueError, IndexError) as e:
                            print(f"Error processing math grades for student {studentID}: {e}")
                    else:
                        print(f"No student found with ID {studentID}")
                else:
                    print(f"Skipping row with insufficient data: {row}")
        return students
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return students
    except Exception as e:
        print(f"Error loading math grades: {e}")
        return students

def load_english_grades_from_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if present
            for row in reader:
                if len(row) >= 6:  # studentID, fname, lname, attendance, quiz1, quiz2, final_exam
                    studentID, fName, lName, attendance, quiz1, quiz2, final_exam = row[:7]
                    
                    # Find student by ID
                    student = next((s for s in students if s.studentID == studentID), None)
                    
                    if student:
                        try:
                            # Convert string values to float
                            attendance = float(attendance)
                            quiz1 = float(quiz1)
                            quiz2 = float(quiz2)
                            final_exam = float(final_exam)
                            
                            # Store raw values for future calculations
                            student.englishAttendance = attendance
                            student.englishQuiz1 = quiz1
                            student.englishQuiz2 = quiz2
                            student.englishFinalExam = final_exam
                            
                            # Calculate and store English grade
                            student.englishGrade = calculate_english_grade(attendance, [quiz1, quiz2], final_exam)
                            
                            # Check if this is an EnglishStudent or should be converted to one
                            if not isinstance(student, EnglishStudent):
                                # Default values for English-specific fields
                                englishLevel = "Standard"
                                englishClassNumber = "101"
                                englishTeacher = "TBD"
                                englishLastTestScore = student.englishGrade
                                
                                # Get all current subject information to preserve math data if it exists
                                current_data = {
                                    "studentID": student.studentID,
                                    "fName": student.fName,
                                    "mName": student.mName,
                                    "lName": student.lName,
                                    "age": student.age,
                                    "addressL1": student.addressL1,
                                    "addressL2": student.addressL2,
                                    "addressL3": student.addressL3,
                                    "addressPostCode": student.addressPostCode,
                                    "addressCounty": student.addressCounty,
                                    "schoolYear": student.schoolYear,
                                    "schoolSubjects": student.schoolSubjects,
                                    "nameParGar1": student.nameParGar1,
                                    "nameParGar2": student.nameParGar2,
                                    "contactDetParGar1": student.contactDetParGar1,
                                    "contactDetParGar2": student.contactDetParGar2
                                }
                                
                                # Create new EnglishStudent with all existing data
                                english_student = EnglishStudent(
                                    **current_data,
                                    englishLevel=englishLevel, 
                                    englishClassNumber=englishClassNumber,
                                    englishTeacher=englishTeacher, 
                                    englishLastTestScore=englishLastTestScore
                                )
                                
                                # If the student was already a MathStudent, copy math-specific properties
                                if hasattr(student, 'mathGrade'):
                                    english_student.mathGrade = student.mathGrade
                                if hasattr(student, 'mathGrades'):
                                    english_student.mathGrades = student.mathGrades
                                
                                # Replace original student with english student in the list
                                students[students.index(student)] = english_student
                                
                        except (ValueError, IndexError) as e:
                            print(f"Error processing English grades for student {studentID}: {e}")
                    else:
                        print(f"No student found with ID {studentID}")
                else:
                    print(f"Skipping row with insufficient data: {row}")
        return students
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return students
    except Exception as e:
        print(f"Error loading English grades: {e}")
        return students

def load_history_grades_from_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row if present
            for row in reader:
                if len(row) >= 6:  # studentID, fname, lname, attendance, project, exam1, exam2
                    studentID, fName, lName, attendance, project, exam1, exam2 = row[:7]
                    
                    # Find student by ID
                    student = next((s for s in students if s.studentID == studentID), None)
                    
                    if student:
                        try:
                            # Convert string values to float
                            attendance = float(attendance)
                            project = float(project)
                            exam1 = float(exam1)
                            exam2 = float(exam2)
                            
                            # Store raw values for future calculations
                            student.historyAttendance = attendance
                            student.historyProject = project
                            student.historyExams = [exam1, exam2]
                            
                            # Calculate and store History grade
                            student.historyGrade = calculate_history_grade(attendance, project, [exam1, exam2])
                            
                            # Add subject if not already present
                            if "History" not in student.schoolSubjects:
                                student.schoolSubjects.append("History")
                            
                        except (ValueError, IndexError) as e:
                            print(f"Error processing History grades for student {studentID}: {e}")
                    else:
                        print(f"No student found with ID {studentID}")
                else:
                    print(f"Skipping row with insufficient data: {row}")
        return students
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return students
    except Exception as e:
        print(f"Error loading History grades: {e}")
        return students

# Save Functions
def save_students_to_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['studentID', 'fName', 'mName', 'lName', 'age', 'addressL1', 'addressL2', 'addressL3', 
                            'addressPostCode', 'addressCounty', 'schoolYear', 'schoolSubjects', 
                            'nameParGar1', 'nameParGar2', 'contactDetParGar1', 'contactDetParGar2'])
            
            for student in students:
                # Join subjects list into a comma-separated string
                subjects_str = ','.join(student.schoolSubjects) if student.schoolSubjects else ''
                
                writer.writerow([
                    student.studentID, student.fName, student.mName, student.lName, student.age,
                    student.addressL1, student.addressL2, student.addressL3, student.addressPostCode,
                    student.addressCounty, student.schoolYear, subjects_str,
                    student.nameParGar1, student.nameParGar2, student.contactDetParGar1, student.contactDetParGar2
                ])
        print(f"Successfully saved {len(students)} students to {filename}")
    except Exception as e:
        print(f"Error saving students: {e}")

def save_maths_grades_to_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['studentID', 'fName', 'lName', 'quiz1', 'quiz2', 'quiz3', 'quiz4', 'quiz5', 
                            'test1', 'test2', 'final_exam'])
            
            for student in students:
                # Only save data for students who have math grades
                if hasattr(student, 'mathGrades') and student.mathGrades:
                    writer.writerow([
                        student.studentID, student.fName, student.lName, 
                        *student.mathGrades  # Unpack all math grades
                    ])
        print(f"Successfully saved math grades to {filename}")
    except Exception as e:
        print(f"Error saving math grades: {e}")

def save_english_grades_to_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['studentID', 'fName', 'lName', 'attendance', 'quiz1', 'quiz2', 'final_exam'])
            
            for student in students:
                # Check if this student has English grades
                if (hasattr(student, 'englishAttendance') and hasattr(student, 'englishQuiz1') and
                    hasattr(student, 'englishQuiz2') and hasattr(student, 'englishFinalExam')):
                    
                    writer.writerow([
                        student.studentID, student.fName, student.lName,
                        student.englishAttendance, student.englishQuiz1, student.englishQuiz2,
                        student.englishFinalExam
                    ])
        print(f"Successfully saved English grades to {filename}")
    except Exception as e:
        print(f"Error saving English grades: {e}")

def save_history_grades_to_csv(filename, students):
    file_path = Path(__file__).parent / "CSV_Files" / filename
    try:
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['studentID', 'fName', 'lName', 'attendance', 'project', 'exam1', 'exam2'])
            
            for student in students:
                # Check if this student has History grades
                if (hasattr(student, 'historyAttendance') and hasattr(student, 'historyProject') and
                    hasattr(student, 'historyExams') and len(student.historyExams) >= 2):
                    
                    writer.writerow([
                        student.studentID, student.fName, student.lName,
                        student.historyAttendance, student.historyProject,
                        student.historyExams[0], student.historyExams[1]
                    ])
        print(f"Successfully saved History grades to {filename}")
    except Exception as e:
        print(f"Error saving History grades: {e}")

# Helper function to load all student data


def load_all_data(student_file, maths_file=None, english_file=None, history_file=None):
    """
    Load all student data from CSV files
    
    Args:
        student_file: Base student information CSV
        maths_file: Optional, CSV with mathematics grades
        english_file: Optional, CSV with English grades
        history_file: Optional, CSV with History grades
    
    Returns:
        List of Student objects (or subject-specific subclass instances)
    """
    students = load_students_from_csv(student_file)
    
    if maths_file:
        students = load_maths_grades_from_csv(maths_file, students)
    
    if english_file:
        students = load_english_grades_from_csv(english_file, students)
    
    if history_file:
        students = load_history_grades_from_csv(history_file, students)
    
    return students
