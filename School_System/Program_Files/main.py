from student import Student
from school import School
from subject import MathStudent, EnglishStudent, HistoryStudent, list_students_by_subject, print_student_details
from grade_calculator import (
    calculate_math_grade,
    calculate_english_grade,
    calculate_history_grade,
    calculate_and_update_grades_for_students
)

# --- 1. Pure calculation function tests ---
print("\n=== Pure Function Tests ===")
# Math: 5 quizzes, 2 tests, 1 final
mq = [80, 85, 90, 75, 88]
mt1, mt2, mfe = 82, 87, 93
print("calculate_math_grade:", calculate_math_grade(mq, mt1, mt2, mfe))
# English: attendance, 2 quizzes, final
ea, eq1, eq2, efe = 90, 78, 82, 88
print("calculate_english_grade:", calculate_english_grade(ea, [eq1, eq2], efe))
# History: attendance, project, 2 exams
ha, hp, hexams = 92, 85, [80, 90]
print("calculate_history_grade:", calculate_history_grade(ha, hp, hexams))

# --- 2. Student class tests ---
stu = Student(
    "Test", "T", "Student",
    "1 Test Rd", "Suite 1", "City",
    "00001", "CountyX",
    10, ["Mathematics"], "ParentA", "ParentB", "111-1111", "222-2222"
)
print("\n=== Student Tests ===")
print("Initial:", stu)
stu.update_name(fName="Alice", lName="Wonder")
stu.update_address(addressL1="2 Example St", addressCounty="CountyY")
stu.update_school_year(11)
stu.add_subject("English")
stu.remove_subject("Mathematics")
stu.update_guardian_contact(1, name="New ParentA", contact="333-3333")
print("Modified:", stu)
print("Data tuple:", stu.get_student_data())

# --- 3. Subject classes tests ---
print("\n=== Subject Tests ===")
ms = MathStudent(
    "Bob","M","Math",
    "10 Calc Ave","","",
    "11111","CountM",
    12,["Mathematics"],"PA1","PA2","444-4444","555-5555",
    "Adv",201,"MrCalc",89
)
ms.add_math_details("Basic",202,"MsCalc",95)
print(ms)
es = EnglishStudent(
    "Eve","E","Lang",
    "20 Eng Rd","","",
    "22222","CountE",
    11,["English"],"PB1","PB2","666-6666","777-7777",
    "Std",301,"MsLang",78
)
es.add_english_details("Adv",302,"MrLang",88)
print(es)
hs = HistoryStudent(
    "Harry","H","Hist",
    "30 His St","","",
    "33333","CountH",
    10,["History"],"PC1","PC2","888-8888","999-9999",
    "Beg",401,"MrHist",74
)
hs.add_history_details("Int",402,"MsHist",84)
print(hs)
# Test list/print helpers
tlist = [ms, es, hs]
print("By subject 'Mathematics':", list_students_by_subject(tlist, "Mathematics"))
print_student_details(tlist)

# --- 4. Grade calculator on generic Students ---
print("\n=== calculate_and_update_grades_for_students ===")
# Build 4 generic students with full grade attributes
g1 = Student("G1","X","One","","","","","",9,["Mathematics","English","History"],"","","","")
g1.mathGrades = [80,85,90,75,88,82,87,93]
g1.englishAttendance, g1.englishQuiz1, g1.englishQuiz2, g1.englishFinalExam = 90,78,82,88
g1.historyAttendance, g1.historyProject, g1.historyExams = 92,85,[80,90]

g2 = Student("G2","X","Two","","","","","",10,["Mathematics","English","History"],"","","","")
g2.mathGrades = [70,75,80,65,60,70,75,80]
g2.englishAttendance, g2.englishQuiz1, g2.englishQuiz2, g2.englishFinalExam = 85,80,75,82
g2.historyAttendance, g2.historyProject, g2.historyExams = 88,80,[70,85]

g3 = Student("G3","X","Three","","","","","",11,["Mathematics","English","History"],"","","","")
g3.mathGrades = [100,100,100,100,100,100,100,100]
g3.englishAttendance, g3.englishQuiz1, g3.englishQuiz2, g3.englishFinalExam = 100,100,100,100
g3.historyAttendance, g3.historyProject, g3.historyExams = 100,100,[100,100]

g4 = Student("G4","X","Four","","","","","",12,["Mathematics","English","History"],"","","","")
g4.mathGrades = [50,55,60,45,40,50,55,60]
g4.englishAttendance, g4.englishQuiz1, g4.englishQuiz2, g4.englishFinalExam = 75,70,65,78
g4.historyAttendance, g4.historyProject, g4.historyExams = 80,70,[60,75]

all_g = calculate_and_update_grades_for_students([g1,g2,g3,g4])
for g in all_g:
    print(f"{g.fName} Grades -> Math: {g.mathGrade}, English: {g.englishGrade}, History: {g.historyGrade}")
    # Copy to final* for school usage
    if hasattr(g, 'mathGrade'): g.finalMathematicsGrade = g.mathGrade
    if hasattr(g, 'englishGrade'): g.finalEnglishGrade = g.englishGrade
    if hasattr(g, 'historyGrade'): g.finalHistoryGrade = g.historyGrade

# --- 5. School tests with all 10 students ---
print("\n=== School Tests ===")
# Combined list of 10 students: 3 specialized + 4 generic + 3 more specialized
all_students = tlist + all_g + [
    MathStudent("Extra","M","One","","","","","",10,["Mathematics"],"","","","","Adv",301,"Tchr",91),
    EnglishStudent("Extra","E","Two","","","","","",10,["English"],"","","","","Std",302,"Tchr",86),
    HistoryStudent("Extra","H","Three","","","","","",10,["History"],"","","","","Beg",303,"Tchr",79)
]

school2 = School("Test High","Addr","2025",["Mathematics","English","History"])
for s in all_students:
    school2.add_student(s)
print(school2)
print("Mathematics:", school2.list_students_by_subject("Mathematics"))
print("English:", school2.list_students_by_subject("English"))
print("History:", school2.list_students_by_subject("History"))
print("Avg Math:", school2.get_average_grade("Mathematics"))
print("Avg Eng:", school2.get_average_grade("English"))
print("Avg Hist:", school2.get_average_grade("History"))

# Update school info
school2.update_school_name("New High")
school2.update_school_address("New Addr")
school2.update_school_year(2026)
school2.update_school_subjects(["Mathematics","English","History","Science"])
print(school2)
