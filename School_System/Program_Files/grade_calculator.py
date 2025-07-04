# Grade calculation logic for Mathematics, English, and History. 
# This module provides functions to calculate final grades for students
# in different subjects based on various assessment components.



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



def calculate_and_update_grades_for_students(students):
    """
    Calcuates grade for each subject. Checks to make sure grades exist or not before starting calculations.
    Returns a list of students with updated grade information
    """
    
    for student in students:
        
        for student in students:
          if not hasattr(student, "subject_grades"):
            student.subject_grades = {}  # Initialize if missing

        # Mathematics
        try:
          if hasattr(student, 'mathLastTestScore'):
            student.mathGrade = student.mathLastTestScore
            # Add to subject_grades dictionary
            student.subject_grades["Mathematics"] = student.mathGrade
            print(f"Math grade updated for {student.fName}: {student.mathGrade}")

          elif hasattr(student, 'mathGrades') and student.mathGrades:
                raw = student.mathGrades
                quizzes = raw[0:5]
                test1, test2 = raw[5], raw[6]
                final_exam = raw[7]
                student.mathGrade = calculate_math_grade(quizzes, test1, test2, final_exam)
                student.subject_grades["Mathematics"] = student.mathGrade
          else:
            print(f"Warning: Not enough data to calculate Math grade for {student.fName} {student.lName}")

        except (ValueError, TypeError) as e:
          print(f"Error calculating Math grade for {student.fName} {student.lName}: {e}")

    
        # English
        try:
          if hasattr(student, 'englishLastTestScore'):
            student.englishGrade = student.englishLastTestScore
            # Add to subject_grades dictionary
            student.subject_grades["English"] = student.englishGrade
            print(f"English grade updated for {student.fName}: {student.englishGrade}")
        
          elif (hasattr(student, 'englishAttendance') and hasattr(student, 'englishQuiz1') and 
                hasattr(student, 'englishQuiz2') and hasattr(student, 'englishFinalExam')):
            attendance = student.englishAttendance
            quizzes = [student.englishQuiz1, student.englishQuiz2]
            final_exam = student.englishFinalExam
            student.englishGrade = calculate_english_grade(attendance, quizzes, final_exam)
            student.subject_grades["English"] = student.englishGrade
            print(f"[English] Could not calculate for {student.fName} {student.lName}: {e}")
          else:
            print(f"Warning: Not enough data to calculate English grade for {student.fName} {student.lName}")
        except (ValueError, TypeError) as e:
          print(f"Error calculating English grade for {student.fName} {student.lName}: {e}")




        # History
        try:
            if hasattr(student, 'historyLastTestScore'):
              student.historyGrade = student.historyLastTestScore
              # Add to subject_grades dictionary
              student.subject_grades["History"] = student.historyGrade
              print(f"History grade updated for {student.fName}: {student.historyGrade}")

            elif (hasattr(student, 'historyAttendance') and hasattr(student, 'historyProject') and 
              hasattr(student, 'historyExams')):
              attendance = student.historyAttendance
              project = student.historyProject
              exams = student.historyExams
              student.historyGrade = calculate_history_grade(attendance, project, exams)
              student.subject_grades["History"] = student.historyGrade
              print(f"[History] Could not calculate for {student.fName} {student.lName}: {e}")
            else:
                print(f"Warning: Not enough data to calculate History grade for {student.fName} {student.lName}")
        except (ValueError, TypeError) as e:
            print(f"Error calculating History grade for {student.fName} {student.lName}: {e}")
    
    return students


#Maybe should be in student.py?
def simple_grade_calculation(students):
  """
  A simpler version that just uses the lastTestScore values as grades.
  Returns a list of students with updated grades
  """

  for student in students:
      # Ensure student has a subject_grades dictionary
      if not hasattr(student, 'subject_grades'):
          student.subject_grades = {}
          
      try:
          if hasattr(student, 'mathLastTestScore'):
            student.mathGrade = student.mathLastTestScore
            student.subject_grades["Mathematics"] = student.mathGrade
          
          if hasattr(student, 'englishLastTestScore'):
            student.englishGrade = student.englishLastTestScore
            student.subject_grades["English"] = student.englishGrade
          
          if hasattr(student, 'historyLastTestScore'):
            student.historyGrade = student.historyLastTestScore
            student.subject_grades["History"] = student.historyGrade
      
      except (ValueError, TypeError) as e:
            print(f"Error in simple grade calculation for {student.fName} {student.lName}: {e}")
            
  return students



