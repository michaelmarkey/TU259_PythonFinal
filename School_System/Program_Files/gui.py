from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from typing import Dict, Any, List

# Import necessary functions from cli_helper
# Import necessary functions from cli_helper
from cli_helper import (
    load_data,
    add_student_cli,
    remove_student_cli,
    view_student_cli,
    update_student_cli,
    delete_student_cli,
    print_report_cli,
    summary_students_cli,
    summary_school_cli,
    summary_employees_cli,
    School,
)
from school import School
from employee import Employee, Teacher, Medic, Principal, Administrator, Counselor

class MainMenuScreen(Screen):
    def __init__(self, school, **kwargs):
        super().__init__(**kwargs)
        self.school = school
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        layout.add_widget(Label(text="Main Menu (GUI - Reports)", font_size=32, size_hint_y=None, height=50))  # Changed title

        menu_items = [
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

        layout.add_widget(Label(
            text="Use the command line to add/update student data.",
            size_hint_y=None, height=30
        ))

        self.add_widget(layout)

    def show_popup(self, title, message):
        content = BoxLayout(orientation='vertical')
        label = Label(text=message)
        back_button = Button(text="Back to Main Menu", size_hint_y=None, height=40)
        back_button.bind(on_release=lambda btn: self.manager.current == 'main' and popup.dismiss())
        content.add_widget(label)
        content.add_widget(back_button)
        popup = Popup(title=title, content=content, size_hint=(0.7, 0.5))
        popup.open()

    def show_scrollable_popup(self, title, content):
        layout = BoxLayout(orientation='vertical', size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))
        label = Label(text=content, size_hint_y=None, height=1000, font_size=16,
                      text_size=(600, None), halign='left', valign='top')
        label.bind(texture_size=label.setter('size'))
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(layout)
        popup = Popup(title=title, content=scroll_view, size_hint=(0.8, 0.8))
        popup.open()

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
        employee_summary = summary_employees_cli(self.school, return_summary=True)
        if employee_summary:
            self.show_scrollable_popup("Employee Summary", employee_summary)
        else:
            self.show_scrollable_popup("Employee Summary", "No employees found.")

    def exit_app(self, instance):
        App.get_running_app().stop()

class SchoolApp(App):
    def build(self):
        self.school = load_data()
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='main', school=self.school))
        return sm

if __name__ == '__main__':
    SchoolApp().run()

