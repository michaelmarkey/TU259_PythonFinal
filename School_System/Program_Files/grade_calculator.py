# Grade calculation logic for Mathematics, English, and History.
# This module provides:
#  1. Pure functions to compute a single final grade given raw scores.
#  2. A batch updater to pull raw grade fields off student objects,
#     compute each subject’s final grade, and write it back to them.


# -------------------------------
# 1) Pure calculation functions (no I/O)
# -------------------------------

def calculate_math_grade(quizzes, test1, test2, final_exam):
    """
    Calculate a Math final grade on a 100-point scale.
    
    Weighting:
      - Quiz average (5 quizzes): 15% total
      - Test 1: 15%
      - Test 2: 15%
      - Final exam: 55%
    
    Parameters:
      quizzes     List[float] of length 5
      test1       float
      test2       float
      final_exam  float
    
    Returns:
      float: final grade
    """
    if len(quizzes) != 5:
        raise ValueError("Expected 5 quiz scores for calculate_math_grade()")
    quiz_avg = sum(quizzes) / 5
    return quiz_avg * 0.15 + test1 * 0.15 + test2 * 0.15 + final_exam * 0.55


def calculate_english_grade(attendance, quizzes, final_exam):
    """
    Calculate an English final grade on a 100-point scale.
    
    Weighting:
      - Attendance: 10%
      - Quiz 1: 15%
      - Quiz 2: 15%
      - Final exam: 60%
    
    Parameters:
      attendance  float
      quizzes     List[float] of length 2
      final_exam  float
    
    Returns:
      float: final grade
    """
    if len(quizzes) != 2:
        raise ValueError("Expected 2 quiz scores for calculate_english_grade()")
    return (attendance * 0.10 +
            quizzes[0] * 0.15 +
            quizzes[1] * 0.15 +
            final_exam * 0.60)


def calculate_history_grade(attendance, project, exams):
    """
    Calculate a History final grade on a 100-point scale.
    
    Weighting:
      - Attendance: 10%
      - Project: 30%
      - Exam 1: 30%
      - Exam 2: 30%
    
    Parameters:
      attendance  float
      project     float
      exams       List[float] of length 2
    
    Returns:
      float: final grade
    """
    if len(exams) != 2:
        raise ValueError("Expected 2 exam scores for calculate_history_grade()")
    return (attendance * 0.10 +
            project * 0.30 +
            exams[0] * 0.30 +
            exams[1] * 0.30)


# -------------------------------
# 2) Batch update for student objects
# -------------------------------

def calculate_and_update_grades_for_students(students):
    """
    For each student in `students`, compute and assign:
      - student.mathGrade
      - student.englishGrade
      - student.historyGrade
    
    Expects each student object to have raw-grade attributes:
      - mathGrades : List[float] of length ≥ 8,
                      where:
                        quizzes = [:5],
                        test1   = [5],
                        test2   = [6],
                        final   = [7]
      - englishAttendance : float
      - englishQuiz1      : float
      - englishQuiz2      : float
      - englishFinalExam  : float
      - historyAttendance : float
      - historyProject    : float
      - historyExams      : List[float] of length ≥ 2
    
    Any missing or malformed data will be caught and reported;
    the subject grade for the sutdent will simply be skipped.
    
    Returns:
      List of students (same objects, mutated in place).
    """
    for student in students:
        # Mathematics
        try:
            raw = student.mathGrades
            quizzes    = raw[0:5]
            test1, test2 = raw[5], raw[6]
            final_exam  = raw[7]
            student.mathGrade = calculate_math_grade(quizzes, test1, test2, final_exam)
        except Exception as e:
            print(f"[Math] Could not calculate for {student.fName} {student.lName}: {e}")

        # English
        try:
            attendance = student.englishAttendance
            quizzes    = [student.englishQuiz1, student.englishQuiz2]
            final_exam = student.englishFinalExam
            student.englishGrade = calculate_english_grade(attendance, quizzes, final_exam)
        except Exception as e:
            print(f"[English] Could not calculate for {student.fName} {student.lName}: {e}")

        # History
        try:
            attendance = student.historyAttendance
            project    = student.historyProject
            exams      = student.historyExams
            student.historyGrade = calculate_history_grade(attendance, project, exams)
        except Exception as e:
            print(f"[History] Could not calculate for {student.fName} {student.lName}: {e}")

    return students



# # -------------------------------
# # 1) Pure calculation functions (no I/O)
# # -------------------------------

# def calculate_math_grade(quizzes, test1, test2, final_exam):
#     """quizzes: list of 5 floats; test1, test2, final_exam: floats"""
#     quiz_avg = sum(quizzes) / len(quizzes)
#     return quiz_avg * 0.15 + test1 * 0.15 + test2 * 0.15 + final_exam * 0.55

# def calculate_english_grade(attendance, quizzes, final_exam):
#     """quizzes: list of 2 floats"""
#     return attendance * 0.1 + quizzes[0] * 0.15 + quizzes[1] * 0.15 + final_exam * 0.6

# def calculate_history_grade(attendance, project, exams):
#     """exams: list of 2 floats"""
#     return attendance * 0.1 + project * 0.3 + exams[0] * 0.3 + exams[1] * 0.3

# # -------------------------------
# # 2) Grade Calculation for Students
# # -------------------------------

# def calculate_and_update_grades_for_students(students):
#     """
#     Calculates and updates grades for all students based on their stored information.
#     This function will iterate through all students, compute grades for each subject, 
#     and assign the calculated grades to the respective fields of the student objects.
#     """
#     for student in students:
#         try:
#             # Calculate and update Mathematics grade
#             quiz_grades = student.mathGrades[:5]
#             test1, test2 = student.mathGrades[5], student.mathGrades[6]
#             final_exam = student.mathGrades[7]
#             student.mathGrade = calculate_math_grade(quiz_grades, test1, test2, final_exam)
#         except (AttributeError, IndexError) as e:
#             print(f"Error processing Mathematics grades for {student.fName} {student.lName}: {e}")

#         try:
#             # Calculate and update English grade
#             attendance = student.englishAttendance
#             quizzes = [student.englishQuiz1, student.englishQuiz2]
#             final_exam = student.englishFinalExam
#             student.englishGrade = calculate_english_grade(attendance, quizzes, final_exam)
#         except (AttributeError, IndexError) as e:
#             print(f"Error processing English grades for {student.fName} {student.lName}: {e}")

#         try:
#             # Calculate and update History grade
#             attendance = student.historyAttendance
#             project = student.historyProject
#             exams = student.historyExams
#             student.historyGrade = calculate_history_grade(attendance, project, exams)
#         except (AttributeError, IndexError) as e:
#             print(f"Error processing History grades for {student.fName} {student.lName}: {e}")
    
#     return students

# # def get_valid_grade(prompt):
# #     while True:
# #         try:
# #             return float(input(prompt))
# #         except ValueError:
# #             print("Please enter a valid number.")

# # def get_full_name():
# #     while True:
# #         try:
# #             name = input("Enter the student's full name: ").strip()
# #             first, last = name.split()
# #             return first, last
# #         except ValueError:
# #             print("Please enter both first and last name separated by a space.")
            
# # def input_math_grade():
# #     first, last = get_full_name()
# #     quizzes = [get_valid_grade(f"Grade for quiz {i}? ") for i in range(1, 6)]
# #     t1 = get_valid_grade("Grade for test 1? ")
# #     t2 = get_valid_grade("Grade for test 2? ")
# #     fe = get_valid_grade("Grade for final exam? ")
# #     grade = calculate_math_grade(quizzes, t1, t2, fe)
# #     print(f"\n{first} {last} — Mathematics final grade: {grade:.2f}\n")
# #     return grade

# # def input_english_grade():
# #     first, last = get_full_name()
# #     att = get_valid_grade("Attendance grade? ")
# #     fe = get_valid_grade("Final exam grade? ")
# #     quizzes = [get_valid_grade(f"Grade for quiz {i}? ") for i in range(1, 3)]
# #     grade = calculate_english_grade(att, quizzes, fe)
# #     print(f"\n{first} {last} — English final grade: {grade:.2f}\n")
# #     return grade

# # def input_history_grade():
# #     first, last = get_full_name()
# #     att = get_valid_grade("Attendance grade? ")
# #     proj = get_valid_grade("Project grade? ")
# #     exams = [get_valid_grade(f"Grade for exam {i}? ") for i in range(1, 3)]
# #     grade = calculate_history_grade(att, proj, exams)
# #     print(f"\n{first} {last} — History final grade: {grade:.2f}\n")
# #     return grade
