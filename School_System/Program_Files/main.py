from student import Student
from school import School

student1=Student("001", "Michael", "Joseph", "Markey", 42, "64 The Avenue", "Woodpark", "Ballinteer", 16, "Dublin", "6th", 
                 ["English", "Maths"], "Dympna Markey", "Michael Markey", "012980884", "0875896936",
                 {"History":76, "Maths":92})

student2 = Student("002", "Mia", "Lee", "Johnson", 16, "49 Main Street", "Suburbia", "Dublin", 5, "Dublin", "4th", 
                   ["History", "Maths"], "Alice Smith", "Mark Taylor", "012345601", "0871234501", 
                   {"History": 75, "Maths": 80})

student3 = Student("003", "Isabella", "Paul", "Martin", 15, "25 Main Street", "Suburbia", "Dublin", 8, "Dublin", "6th", 
                   ["History", "English", "Maths"], "Diana Anderson", "Karen Johnson", "012345602", "0871234502", 
                   {"History": 82, "English": 88, "Maths": 74})

student4 = Student("004", "Lucas", "Marie", "Martin", 17, "69 Main Street", "Suburbia", "Dublin", 12, "Dublin", "1st", 
                   ["History", "Maths", "English"], "Robert Brown", "Mark Taylor", "012345603", "0871234503", 
                   {"History": 85, "Maths": 91, "English": 79})

student5 = Student("005", "Noah", "Lee", "Thomas", 14, "29 Main Street", "Suburbia", "Dublin", 9, "Dublin", "1st", 
                   ["Maths", "English"], "Diana Anderson", "Karen Johnson", "012345604", "0871234504", 
                   {"Maths": 67, "English": 74})

student6 = Student("006", "Olivia", "Ray", "Johnson", 18, "14 Main Street", "Suburbia", "Dublin", 4, "Dublin", "6th", 
                   ["History", "Maths"], "Robert Brown", "Robert Brown", "012345605", "0871234505", 
                   {"History": 68, "Maths": 85})

student7 = Student("007", "Liam", "Jay", "Murphy", 13, "70 Oak Drive", "Greenfield", "Dublin", 16, "Dublin", "3rd", 
                   ["English"], "Laura Murphy", "Kevin Murphy", "012345606", "0871234506", 
                   {"English": 79})

student8 = Student("008", "Emma", "Grace", "Walsh", 15, "88 Elm Road", "Cherrywood", "Dublin", 15, "Dublin", "4th", 
                   ["History", "English"], "John Walsh", "Catherine Walsh", "012345607", "0871234507", 
                   {"History": 92, "English": 85})

student9 = Student("009", "Jack", "Ryan", "Kelly", 17, "19 Birch Lane", "Kilmainham", "Dublin", 10, "Dublin", "5th", 
                   ["Maths"], "Sarah Kelly", "Sean Kelly", "012345608", "0871234508", 
                   {"Maths": 72})

student10 = Student("010", "Ava", "Skye", "Byrne", 14, "45 Cedar Park", "Crumlin", "Dublin", 12, "Dublin", "2nd", 
                    ["English", "Maths"], "James Byrne", "Helen Byrne", "012345609", "0871234509", 
                    {"English": 88, "Maths": 65})

student11 = Student("011", "Ethan", "Max", "O'Brien", 16, "67 Pine Street", "Rathmines", "Dublin", 6, "Dublin", "4th", 
                    ["English", "History"], "Mary O'Brien", "David O'Brien", "012345610", "0871234510", 
                    {"English": 78, "History": 85})

student12 = Student("012", "Sophia", "Rose", "Doyle", 15, "12 Willow Grove", "Sandyford", "Dublin", 18, "Dublin", "5th", 
                    ["History"], "Karen Doyle", "Tom Doyle", "012345611", "0871234511", 
                    {"History": 94})

student13 = Student("013", "Daniel", "Lee", "Moore", 17, "33 Fir Street", "Donnybrook", "Dublin", 4, "Dublin", "6th", 
                    ["Maths", "English"], "Claire Moore", "Brendan Moore", "012345612", "0871234512", 
                    {"Maths": 78, "English": 83})

student14 = Student("014", "Grace", "Lily", "O'Connor", 13, "20 Ash Close", "Drimnagh", "Dublin", 12, "Dublin", "1st", 
                    ["English"], "Nora O'Connor", "James O'Connor", "012345613", "0871234513", 
                    {"English": 90})

student15 = Student("015", "Ben", "Alex", "Ryan", 18, "54 Maple Avenue", "Tallaght", "Dublin", 24, "Dublin", "6th", 
                    ["Maths", "History", "English"], "Louise Ryan", "Chris Ryan", "012345614", "0871234514", 
                    {"Maths": 75, "History": 80, "English": 89})

student16 = Student("016", "Ella", "May", "Smith", 14, "18 Cherry Court", "Lucan", "Dublin", 22, "Dublin", "2nd", 
                    ["History", "English"], "Jenny Smith", "Alan Smith", "012345615", "0871234515", 
                    {"History": 85, "English": 82})

student17 = Student("017", "James", "Finn", "Murray", 15, "72 Beech Drive", "Rathfarnham", "Dublin", 14, "Dublin", "3rd", 
                    ["Maths"], "Rachel Murray", "Thomas Murray", "012345616", "0871234516", 
                    {"Maths": 77})

student18 = Student("018", "Chloe", "Hope", "Brady", 17, "36 Poplar Row", "Terenure", "Dublin", 6, "Dublin", "5th", 
                    ["English", "Maths"], "Fiona Brady", "Stephen Brady", "012345617", "0871234517", 
                    {"English": 83, "Maths": 78})

student19 = Student("019", "Ryan", "Liam", "Kavanagh", 16, "90 Spruce Hill", "Clondalkin", "Dublin", 22, "Dublin", "4th", 
                    ["History", "English", "Maths"], "Donna Kavanagh", "Greg Kavanagh", "012345618", "0871234518", 
                    {"History": 80, "English": 86, "Maths": 77})

student20 = Student("020", "Zoe", "Anne", "Nolan", 15, "7 Holly Way", "Portobello", "Dublin", 8, "Dublin", "3rd", 
                    ["History"], "Aisling Nolan", "Brian Nolan", "012345619", "0871234519", 
                    {"History": 90})


students = [student1, student2, student3, student4, student5,student6, student7, student8, student9, student10, student11, student12, student13, student14, student15, student16, student17, student18, student19, student20]

print(student1.calculate_overall_average())
student1.add_grade("English", "75")
print(student1.calculate_overall_average())

school1 = School("Dublin High School", "123 School St, Dublin", "01-2345678", ["English", "Maths", "History"])

for student in students:
    school1.register_student(student)

# for student in school1.get_all_students():
#     print(student.get_summary_student_data())

#print(school1.get_all_students())
print(school1.get_student_by_id("015"))
school1.remove_student("019")
print(school1.find_student_by_id("018"))
print(school1.find_students_by_name(first_name="Ryan", last_name="Kavanagh"))
print(school1.list_students_by_subject("English"))
print(school1.list_students_by_year("3rd"))

#print(school1)

school1.update_school_name("Dublin Low School")
school1.update_school_address("456 School St, Dublin")
school1.update_school_year("1984")
school1.update_school_telephone("012980884")
school1.update_school_subjects(["English", "Maths", "History"])
school1.add_subject("Biology")
school1.remove_subject("English")

#print(school1)



# student1 = Student("001", "Michael", "Joseph", "Markey", 42, "64 The Avenue", "Woodpark", "Ballinteer", 16, "Dublin", "6th", ["English", "Maths"], "Dympna Markey", "Michael Markey", "012980884", "0875896936")
# print(student1)

# student1.update_ID("002")
# student1.update_name("Michael", "James", "Markey")
# student1.update_address("67 The Avenue", "Woodpark", "Ballinteer", 16, "Dublin")
# student1.update_age(16)
# student1.update_school_year("5th")
# student1.add_subject("History")
# student1.remove_subject("English")
# student1.update_guardian_contact(1, "Cynthia Markey", "0872156598")
# print(student1)

# print(student1.get_full_student_data())
# print(student1.get_summary_student_data())
# print(student1.get_full_address())
# print(student1.get_guardian_info())
# print(student1.get_subjects())

# print(student1.is_full_name_available())
# print(student1.is_address_complete())
# print(student1.is_in_year("6th"))
# print(student1.is_enrolled_in("Maths"))
# print(student1.is_guardian_contact_available(1))




# What I'm testing

# Class – Student

# Attributes – self, studentID, fName, mName, lName, age, addressL1, addressL2, addressL3, addressPostCode, addressCounty, schoolYear, nameParGar1, nameParGar2, contactDetParGar1, contactDetParGar2

# Methods – 

# #update_and_add
# updateID, update_name, update_age, update_school_year, update_subjects , update_guardian_contact, add_subject, remove_subject, 

# #get
# get_full_student_data
# get_summary_student_data
# get_full_address
# get_guardian_info
# get_subjects

# #check
# is_ful_name_available
# is_address_complete
# is_in_year
# is_enrolled
# is_guardian_contact_available