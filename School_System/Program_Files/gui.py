#Need to explain all this

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
from kivy.core.window import Window
from kivy.properties import ObjectProperty

from school import School 
from employee import Employee, Teacher, Medic, Principal, Administrator, Counselor


class ScrollableLabel(BoxLayout):
    """A scrollable label that properly handles text size and scrolling"""
    
    def __init__(self, **kwargs):
        super(ScrollableLabel, self).__init__(orientation='vertical', **kwargs)
        self.scroll_view = ScrollView()
        self.label = Label(
            size_hint_y=None,
            markup=True,
            halign='left',
            valign='top'
        )
        # Make sure the label size updates correctly
        self.label.bind(size=self._update_label_height)
        self.scroll_view.add_widget(self.label)
        self.add_widget(self.scroll_view)
    
    def _update_label_height(self, instance, value):
        # Update label height to enable proper scrolling
        self.label.text_size = (self.width, None)
        self.label.texture_update()
        self.label.height = self.label.texture_size[1]
    
    def set_text(self, text):
        self.label.text = text
        # Force text size update
        Clock.schedule_once(lambda dt: self._update_label_height(None, None), 0.1)


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
            ("0. Return to CLI", self.return_to_cli),
        ]

        for text, callback in menu_items:
            button = Button(text=text, on_press=callback,
                            size_hint_y=None, height=50)
            layout.add_widget(button)

        self.add_widget(layout)

    def show_scrollable_popup(self, title, text):
        """Display a properly scrollable popup with the given text."""
        # Create BoxLayout to hold content
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Create our custom scrollable label
        scrollable_content = ScrollableLabel()
        scrollable_content.set_text(text)
        
        # Add scrollable content to layout
        content.add_widget(scrollable_content)
        
        # Create close button
        close_btn = Button(
            text='Close', 
            size_hint_y=None, 
            height=50
        )
        
        # Add close button to layout
        content.add_widget(close_btn)
        
        # Create popup
        popup = Popup(
            title=title,
            content=content,
            size_hint=(0.9, 0.9)
        )
        
        # Connect close button
        close_btn.bind(on_release=popup.dismiss)
        
        # Open the popup
        popup.open()

    def async_print_report(self, instance):
        """Run print_report_cli in a separate thread and display the result."""
        threading.Thread(target=self.run_print_report, daemon=True).start()

    def run_print_report(self):
        """Helper function to run print_report_cli and update the GUI."""
        from cli_helper import print_report_cli, summary_students_cli, summary_school_cli, summary_employees_cli
        report_text = print_report_cli(self.school)
        Clock.schedule_once(
            lambda dt: self.show_scrollable_popup("Term Report", report_text))

    def async_summary_students(self, instance):
        """Run summary_students_cli in a separate thread."""
        threading.Thread(target=self.run_summary_students, daemon=True).start()

    def run_summary_students(self):
        """Helper function to run summary_students_cli and update the GUI."""
        from cli_helper import print_report_cli, summary_students_cli, summary_school_cli, summary_employees_cli
        summary_text = summary_students_cli(self.school, return_summary=True)
        Clock.schedule_once(
            lambda dt: self.show_scrollable_popup("Student Summary", summary_text))

    def async_summary_school(self, instance):
        """Run summary_school_cli in a separate thread."""
        threading.Thread(target=self.run_summary_school, daemon=True).start()

    def run_summary_school(self):
        """Helper function to run summary_school_cli and update the GUI."""
        from cli_helper import print_report_cli, summary_students_cli, summary_school_cli, summary_employees_cli
        summary_text = summary_school_cli(self.school, return_summary=True)
        Clock.schedule_once(
            lambda dt: self.show_scrollable_popup("School Summary", summary_text))

    def async_summary_employees(self, instance):
        """Run summary_employees_cli in a separate thread."""
        threading.Thread(target=self.run_summary_employees, daemon=True).start()

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


class SchoolApp(App):
    school = ObjectProperty(None)
    
    def __init__(self, school=None, **kwargs):
        super().__init__(**kwargs)
        self.school = school
        print(f"GUI App: SchoolApp initialized with school: {self.school}")
        # Store app instance for easy access
        SchoolApp.instance = self
        
    def build(self):
        print("GUI App: build method called")
        self.sm = ScreenManager()
        main_screen = MainMenuScreen(name='main', school=self.school)
        self.sm.add_widget(main_screen)
        print(f"GUI App: MainMenuScreen added to ScreenManager: {main_screen}")
        return self.sm

    def on_stop(self):
        print("GUI App: on_stop called")
        # Any cleanup code here
        
    @staticmethod
    def launch_gui(school):
        """Static method to launch or relaunch the GUI"""
        if hasattr(SchoolApp, 'instance') and SchoolApp.instance:
            # If app instance exists but is stopped
            if not SchoolApp.instance.root:
                print("GUI App: Relaunching existing app instance")
                SchoolApp.instance.school = school
                SchoolApp.instance.run()
            else:
                print("GUI App: App is already running")
        else:
            # Create new app instance
            print("GUI App: Creating new app instance")
            app = SchoolApp(school=school)
            app.run()


# Helper function for CLI to open the GUI
def open_gui(school):
    """Function to open the GUI from the CLI"""
    # This should be called from your CLI module
    SchoolApp.launch_gui(school)


if __name__ == '__main__':
    # For testing only
    from school import School
    test_school = School("Test School")
    SchoolApp(school=test_school).run()
