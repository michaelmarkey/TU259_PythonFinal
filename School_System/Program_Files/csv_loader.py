
def load_students_from_csv(filename):
    """Load basic student data and return a list of Student objects"""
    students = []
    # Open and read CSV, create basic Student objects with core attributes
    # Return list of Student objects
    return students

def load_math_grades_from_csv(filename, students):
    """Add math grades to existing students"""
    # Open and read CSV
    for row in math_data:
        # Find matching student by ID
        student = find_student_by_id(row['studentID'], students)
        if student:
            # Simply add math attributes to existing student
            student.add_math_grades(quiz_grades=[quiz1, quiz2...], 
                                   test_grades=[test1, test2], 
                                   final_exam=final)
            # Update student subjects list if needed
            if "Mathematics" not in student.schoolSubjects:
                student.schoolSubjects.append("Mathematics")
    return students

def load_english_grades_from_csv(filename, students):
    """Add english grades to existing students"""
    # Similar to math grades, but for English attributes
    # No object type conversion, just add data
    return students

def load_history_grades_from_csv(filename, students):
    """Add history grades to existing students"""
    # Similar to math grades, but for History attributes
    # No object type conversion, just add data
    return students

def load_all_data(student_file, math_file=None, english_file=None, history_file=None):
    """Load all student data from CSV files"""
    # Load basic students first
    students = load_students_from_csv(student_file)
    
    # Add subject data to existing students
    if math_file:
        students = load_math_grades_from_csv(math_file, students)
    if english_file:
        students = load_english_grades_from_csv(english_file, students)
    if history_file:
        students = load_history_grades_from_csv(history_file, students)
        
    return students