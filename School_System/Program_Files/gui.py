from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

# Import necessary functions from cli_helper
from cli_helper import load_data, add_student_cli, remove_student_cli, view_student_cli, update_student_cli, delete_student_cli, print_report_cli, summary_students_cli, summary_school_cli, summary_employees_cli
from school import School
from employee import Employee, Teacher, Medic, Principal, Administrator, Counselor

class MainMenuScreen(Screen):
    def __init__(self, school, **kwargs):
        super().__init__(**kwargs)
        self.school = school
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        layout.add_widget(Label(text="Main Menu", font_size=32, size_hint_y=None, height=50))

        menu_items = [
            ("1. Add Student", self.add_student),
            ("2. Remove Student", self.remove_student),
            ("3. View Student", self.view_student),
            ("4. Update Student", self.update_student),
            ("5. Delete Student", self.delete_student),
            ("6. Print Term Report", self.print_report),
            ("7. Student Summary", self.summary_students),
            ("8. School Summary", self.summary_school),
            ("9. Employee Summary", self.summary_employees),
            ("0. Exit", self.exit_app)
        ]

        for text, callback in menu_items:
            btn = Button(text=text, size_hint_y=None, height=40)
            btn.bind(on_release=callback)
            layout.add_widget(btn)

        self.add_widget(layout)

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(0.6, 0.4))
        popup.open()
    
    def show_scrollable_popup(self, title, content):
        # Create a scrollable layout
        layout = BoxLayout(orientation='vertical', size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # Create a Label with the content (multi-line support)
        label = Label(text=content, size_hint_y=None, height=1000, font_size=16, text_size=(600, None), halign='left', valign='top')
        label.bind(texture_size=label.setter('size'))  # auto-size based on content
        layout.add_widget(label)

        # Add it to a scrollview
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(layout)

        # Put the scrollview into a popup
        popup = Popup(title=title, content=scroll_view, size_hint=(0.8, 0.8))
        popup.open()


    def add_student(self, instance):
        add_student_cli(self.school)
        self.show_popup("Success", "Student added successfully!")

    def remove_student(self, instance):
        remove_student_cli(self.school)
        self.show_popup("Success", "Student removed successfully!")

    def view_student(self, instance):
        view_student_cli(self.school)
        self.show_popup("Success", "Student displayed successfully!")

    def update_student(self, instance):
        update_student_cli(self.school)
        self.show_popup("Success", "Student updated successfully!")

    def delete_student(self, instance):
        delete_student_cli(self.school)
        self.show_popup("Success", "Student deleted successfully!")

    def print_report(self, instance):
        report_content = print_report_cli(self.school, return_summary=True)        
        self.show_scrollable_popup("Term Report", report_content)

    def summary_students(self, instance):
        student_summary = summary_students_cli(self.school, return_summary=True)
        self.show_scrollable_popup("Student Summary", student_summary)

    def summary_school(self, instance):
        school_summary = summary_school_cli(self.school, return_summary=True)
        self.show_scrollable_popup("School Summary", school_summary)

    def summary_employees(self, instance):
        # Get the employee summary as a string from summary_employees_cli
        employee_summary = summary_employees_cli(self.school, return_summary=True)
        
        # Show the summary in a scrollable pop-up
        if employee_summary:
            self.show_scrollable_popup("Employee Summary", employee_summary)
        else:
            self.show_scrollable_popup("Employee Summary", "No employees found.")

    def exit_app(self, instance):
        App.get_running_app().stop()

class SchoolApp(App):
    def build(self):
        # Assuming the load_data function returns a populated school instance
        self.school = load_data()  # Load the school data as before
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='main', school=self.school))
        return sm

if __name__ == '__main__':
    SchoolApp().run()


# # gui.py
# import kivy

# from kivy.app import App
# from kivy.uix.screenmanager import ScreenManager, Screen
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.popup import Popup
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput

# from main import cli_helper  # Import your CLI logic
# from cli_helper import load_data
# from student import Student

# class MainMenuScreen(Screen):
#     def __init__(self, school, **kwargs):
#         super().__init__(**kwargs)
#         self.school = school
#         layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

#         layout.add_widget(Label(text="Main Menu", font_size=32, size_hint_y=None, height=50))

#         menu_items = [
#         ("1. Add Student", self.add_student),
#         # ("2. Remove Student", self.remove_student),
#         # ("3. View Student Info", self.view_individual_student),
#         # ("4. Update Student", self.update_student),
#         # ("5. Delete Student", self.delete_student),
#         # ("6. Print Term Report", self.print_report),
#         ("7. Student Summary", self.student_summary),
#         ("8. School Summary", self.school_summary),
#         ("9. Employee Summary", self.employee_summary),
#         ("Exit", self.exit_app)
#         ]

#         for text, callback in menu_items:
#             btn = Button(text=text, size_hint_y=None, height=40)
#             btn.bind(on_release=callback)
#             layout.add_widget(btn)

#         self.add_widget(layout)

#     def show_popup(self, title, message):
#         popup = Popup(title=title,
#                       content=ScrollView(size_hint=(1, 1),
#                                          content=Label(text=message, size_hint_y=None)),
#                       size_hint=(0.9, 0.9))
#         popup.open()

#     def add_student(self, instance):
#         self.manager.current = 'add_student'  # Switch to the AddStudentScreen

#     def view_student(self, instance):
#         students = self.school.students.values()
#         info = "\n".join([f"{s.studentID}: {s.fName} {s.lName}" for s in students])
#         self.show_popup("Students", info)

#     def student_summary(self, instance):
#         self.show_popup("Student Summary", f"Total students: {len(self.school.students)}")

#     def school_summary(self, instance):
#         self.show_popup("School Info", f"{self.school.name}\n{self.school.address}")

#     def employee_summary(self, instance):
#         self.show_popup("Employees", f"{len(self.school.employees)} employees")

#     def exit_app(self, instance):
#         App.get_running_app().stop()

# class SchoolApp(App):
#     def build(self):
#         self.school = load_data()
#         sm = ScreenManager()
#         sm.add_widget(MainMenuScreen(name='main', school=self.school))
#         # Add the MainMenuScreen and AddStudentScreen to the ScreenManager
#         sm.add_widget(MainMenuScreen(name='main', school=self.school))
#         sm.add_widget(AddStudentScreen(name='add_student', school=self.school))
#         return sm



# class AddStudentScreen(Screen):
#     def __init__(self, school, **kwargs):
#         super().__init__(**kwargs)
#         self.school = school
#         layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

#         layout.add_widget(Label(text="Add Student", font_size=32, size_hint_y=None, height=50))

#         # Create a GridLayout for the form fields
#         form_layout = GridLayout(cols=2, size_hint_y=None, height=500, spacing=10)

#         # Add form fields for student information
#         self.fields = {
#             "Student ID": TextInput(),
#             "First Name": TextInput(),
#             "Middle Name": TextInput(),
#             "Last Name": TextInput(),
#             "Age": TextInput(),
#             "Address Line 1": TextInput(),
#             "Address Line 2": TextInput(),
#             "Address Line 3": TextInput(),
#             "Postcode": TextInput(),
#             "County": TextInput(),
#             "School Year": TextInput(),
#             "Subjects (comma-separated)": TextInput(),
#             "Guardian 1 Name": TextInput(),
#             "Guardian 1 Contact": TextInput(),
#             "Guardian 2 Name": TextInput(),
#             "Guardian 2 Contact": TextInput(),
#         }

#         for label, input_field in self.fields.items():
#             form_layout.add_widget(Label(text=label))
#             form_layout.add_widget(input_field)

#         layout.add_widget(form_layout)

#         # Add the Submit button
#         submit_button = Button(text="Submit", size_hint_y=None, height=50)
#         submit_button.bind(on_release=self.submit_form)
#         layout.add_widget(submit_button)

#         self.add_widget(layout)

#     def submit_form(self, instance):
#         """Submit the form and create the student"""
#         # Collect data from the form
#         student_data = {label: field.text for label, field in self.fields.items()}
        
#         # Ensure all fields are filled
#         if any(value == '' for value in student_data.values()):
#             self.show_popup("Error", "Please fill in all fields.")
#             return
        
#         # Create the student object
#         student = Student(
#             studentID=student_data["Student ID"],
#             fName=student_data["First Name"],
#             mName=student_data["Middle Name"],
#             lName=student_data["Last Name"],
#             age=int(student_data["Age"]),
#             addressL1=student_data["Address Line 1"],
#             addressL2=student_data["Address Line 2"],
#             addressL3=student_data["Address Line 3"],
#             addressPostCode=student_data["Postcode"],
#             addressCounty=student_data["County"],
#             schoolYear=student_data["School Year"],
#             schoolSubjects=student_data["Subjects (comma-separated)"].split(","),
#             nameParGar1=student_data["Guardian 1 Name"],
#             contactDetParGar1=student_data["Guardian 1 Contact"],
#             nameParGar2=student_data["Guardian 2 Name"],
#             contactDetParGar2=student_data["Guardian 2 Contact"]
#         )

#         # Register the student in the school
#         self.school.register_student(student)
        
#         # Show success message
#         self.show_popup("Success", f"Student {student.studentID} added successfully!")
        
#         # Clear the form or return to the main menu
#         self.manager.current = 'main'

#     def show_popup(self, title, message):
#         popup = Popup(title=title,
#                       content=Label(text=message),
#                       size_hint=(0.7, 0.5))
#         popup.open()




# if __name__ == '__main__':
#     SchoolApp().run()
