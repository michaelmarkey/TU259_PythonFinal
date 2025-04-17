from csv_loader import load_students_from_csv

def main():
    student_records = load_students_from_csv("input_file.csv")

    print("\n")
    for math_stu, eng_stu, hist_stu in student_records:
        # Print base student info (only once)
        print(math_stu.__class__.__base__.__repr__(math_stu))

        # Print subject-specific details
        print(f"\nDetails for Mathematics for {math_stu.fName} {math_stu.lName}:")
        print(f"Level: {math_stu.mathLevel}, Class: {math_stu.mathClassNumber}, Teacher: {math_stu.mathTeacher}, Score: {math_stu.mathLastTestScore}")

        print(f"\nDetails for English for {eng_stu.fName} {eng_stu.lName}:")
        print(f"Level: {eng_stu.englishLevel}, Class: {eng_stu.englishClassNumber}, Teacher: {eng_stu.englishTeacher}, Score: {eng_stu.englishLastTestScore}")

        print(f"\nDetails for History for {hist_stu.fName} {hist_stu.lName}:")
        print(f"Level: {hist_stu.historyLevel}, Class: {hist_stu.historyClassNumber}, Teacher: {hist_stu.historyTeacher}, Score: {hist_stu.historyLastTestScore}")

        print("\n" + "-"*60 + "\n")

if __name__ == "__main__":
    main()
