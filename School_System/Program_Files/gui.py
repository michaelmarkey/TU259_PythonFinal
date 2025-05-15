from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from typing import Dict, Any, List
import threading
from kivy.clock import Clock
import sys
import os


# from cli_helper import print_report_cli, summary_employees_cli, summary_school_cli, summary_students_cli
from school import School  # Assuming School, Employee, etc., are in these files
from employee import Employee, Teacher, Medic, Principal, Administrator, Counselor


class MainMenuScreen(Screen):
    def __init__(self, school, **kwargs):
        super().__init__(**kwargs)
        self.school = school
        print(f"GUI: MainMenuScreen initialized with school: {self.school}")
        if self.school and hasattr(self.school, 'students') and hasattr(self.school, 'employees'):
            print(
                f"GUI: School object contains {len(self.school.students)} students and {len(self.school.employees)} employees.")
        else:
            print(
                "GUI: School object is either None or missing 'students' or 'employees' attributes!")

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        layout.add_widget(Label(
            text="Main Menu (GUI - Reports & Return)", font_size=32, size_hint_y=None, height=50))

        menu_items = [
            ("1. Print Term Report", self.async_print_report),
            ("2. Student Summary", self.async_summary_students),
            ("3. School Summary", self.async_summary_school),
            ("4. Employee Summary", self.async_summary_employees),
            ("0. Return to CLI", self.return_to_cli),  # Add this
        ]

        for text, callback in menu_items:
            button = Button(text=text, on_press=callback,
                            size_hint_y=None, height=50)
            layout.add_widget(button)

        self.add_widget(layout)

    def show_scrollable_popup(self, title, text):
        """Display a scrollable popup with the given text."""
        # Create a ScrollView to handle potentially long text
        scroll_view = ScrollView()
        # Create a Label to display the text.  Use markup if needed.
        text_label = Label(text=text, markup=True,
                           text_size=(None, None), halign='left', valign='top')
        # Add the Label to the ScrollView
        scroll_view.add_widget(text_label)

        # Create a BoxLayout to hold the ScrollView and a close button
        content = BoxLayout(orientation='vertical')
        content.add_widget(scroll_view)

        # Create a Popup to display the ScrollView
        popup = Popup(title=title,
                      content=content,
                      size_hint=(0.8, 0.8))
        content.add_widget(
            Button(text='Close', size_hint_y=None, height=50, on_release=popup.dismiss))  # Added a close button
        popup.open()

    def async_print_report(self, instance):
        """Run print_report_cli in a separate thread and display the result."""
        threading.Thread(target=self.run_print_report).start()

    def run_print_report(self):
        """Helper function to run print_report_cli and update the GUI."""
        from cli_helper import print_report_cli, summary_students_cli, summary_school_cli, summary_employees_cli
        report_text = print_report_cli(self.school)
        Clock.schedule_once(
            lambda dt: self.show_scrollable_popup("Term Report", report_text))

    def async_summary_students(self, instance):
        """Run summary_students_cli in a separate thread."""
        threading.Thread(target=self.run_summary_students).start()

    def run_summary_students(self):
        """Helper function to run summary_students_cli and update the GUI."""
        from cli_helper import print_report_cli, summary_students_cli, summary_school_cli, summary_employees_cli
        summary_text = summary_students_cli(self.school, return_summary=True)
        Clock.schedule_once(
            lambda dt: self.show_scrollable_popup("Student Summary", summary_text))

    def async_summary_school(self, instance):
        """Run summary_school_cli in a separate thread."""
        threading.Thread(target=self.run_summary_school).start()

    def run_summary_school(self):
        """Helper function to run summary_school_cli and update the GUI."""
        from cli_helper import print_report_cli, summary_students_cli, summary_school_cli, summary_employees_cli
        summary_text = summary_school_cli(self.school, return_summary=True)
        Clock.schedule_once(
            lambda dt: self.show_scrollable_popup("School Summary", summary_text))

    def async_summary_employees(self, instance):
        """Run summary_employees_cli in a separate thread."""
        threading.Thread(target=self.run_summary_employees).start()

    def run_summary_employees(self):
        """Helper function to run summary_employees_cli and update the GUI."""
        from cli_helper import print_report_cli, summary_students_cli, summary_school_cli, summary_employees_cli
        employee_summary = summary_employees_cli(self.school, return_summary=True)
        Clock.schedule_once(
            lambda dt: self.show_scrollable_popup("Employee Summary", employee_summary))

    def return_to_cli(self, instance):
        """Return to the command-line interface (CLI)."""
        print("GUI: Return to CLI button pressed")
        App.get_running_app().stop()
        print("GUI: App stopped")
        return

class SchoolApp(App):
    def __init__(self, school=None, **kwargs):
        super().__init__(**kwargs)
        self.school = school
        print(f"GUI App: SchoolApp initialized with school: {self.school}")

    def build(self):
        print("GUI App: build method called")
        sm = ScreenManager()
        main_screen = MainMenuScreen(name='main', school=self.school)
        sm.add_widget(main_screen)
        print(
            f"GUI App: MainMenuScreen added to ScreenManager: {main_screen}")
        return sm

    def on_stop(self):
        print("GUI App on_stop") # Add this


if __name__ == '__main__':
    # No direct instantiation here.  The CLI will create the School and pass it in.
    # from cli_helper import School, Student, Employee
    # test_school = School()
    # test_school.add_student(Student("John", "Doe", "S123"))
    # test_school.add_employee(Employee("Jane", "Smith", "E456"))
    SchoolApp().run()
