# grade_calculator.py

def get_full_name():
    while True:
        try:
            name = input("Enter the student's full name: ").strip()
            first, last = name.split()
            return first, last
        except ValueError:
            print("Please enter both first and last name separated by a space.")

def get_valid_grade(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# -------------------------------
# 1) Pure calculation functions (no I/O)
# -------------------------------

def calculate_math_grade(quizzes, test1, test2, final_exam):
    """quizzes: list of 5 floats; test1, test2, final_exam: floats"""
    quiz_avg = sum(quizzes) / len(quizzes)
    return quiz_avg * 0.15 + test1 * 0.15 + test2 * 0.15 + final_exam * 0.55

def calculate_english_grade(attendance, quizzes, final_exam):
    """quizzes: list of 2 floats"""
    return attendance * 0.1 + quizzes[0] * 0.15 + quizzes[1] * 0.15 + final_exam * 0.6

def calculate_history_grade(attendance, project, exams):
    """exams: list of 2 floats"""
    return attendance * 0.1 + project * 0.3 + exams[0] * 0.3 + exams[1] * 0.3

# -------------------------------
# 2) Interactive wrappers (for CLI use)
# -------------------------------

def input_math_grade():
    first, last = get_full_name()
    quizzes = [get_valid_grade(f"Grade for quiz {i}? ") for i in range(1, 6)]
    t1 = get_valid_grade("Grade for test 1? ")
    t2 = get_valid_grade("Grade for test 2? ")
    fe = get_valid_grade("Grade for final exam? ")
    grade = calculate_math_grade(quizzes, t1, t2, fe)
    print(f"\n{first} {last} — Mathematics final grade: {grade:.2f}\n")
    return grade

def input_english_grade():
    first, last = get_full_name()
    att = get_valid_grade("Attendance grade? ")
    fe = get_valid_grade("Final exam grade? ")
    quizzes = [get_valid_grade(f"Grade for quiz {i}? ") for i in range(1, 3)]
    grade = calculate_english_grade(att, quizzes, fe)
    print(f"\n{first} {last} — English final grade: {grade:.2f}\n")
    return grade

def input_history_grade():
    first, last = get_full_name()
    att = get_valid_grade("Attendance grade? ")
    proj = get_valid_grade("Project grade? ")
    exams = [get_valid_grade(f"Grade for exam {i}? ") for i in range(1, 3)]
    grade = calculate_history_grade(att, proj, exams)
    print(f"\n{first} {last} — History final grade: {grade:.2f}\n")
    return grade

# -------------------------------
# 3) CLI entry point
# -------------------------------

def main():
    print("\nGrade Calculator")
    print("Options: Mathematics, English, History")
    sub = input("Subject: ").strip().lower()
    if sub == "mathematics":
        input_math_grade()
    elif sub == "english":
        input_english_grade()
    elif sub == "history":
        input_history_grade()
    else:
        print("Unknown subject.")

if __name__ == "__main__":
    while True:
        main()
        if input("Again? (yes/no): ").strip().lower() != "yes":
            break
