"""
CP1404 Practical 7 - Kivy
Use Greeter example to create a pass or fail program
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class BoxLayoutDemo(App):
    def build(self):
        Window.size = (700, 300)
        self.title = "Pass or Fail"
        self.root = Builder.load_file('pass_or_fail.kv')
        return self.root

    def handle_grade(self):
        try:
            grade = float(self.root.ids.input_grade.text)
            if grade >= 90:
                self.root.ids.output_label.text = "High Distinction"
            elif grade >= 75:
                self.root.ids.output_label.text = "Distinction"
            elif grade >= 65:
                self.root.ids.output_label.text = "Credit"
            elif grade >= 50:
                self.root.ids.output_label.text = "Pass"
            else:
                self.root.ids.output_label.text = "Fail"
        except ValueError:
            self.root.ids.output_label.text = "Invalid grade"

    def handle_clear(self):
        self.root.ids.input_grade.text = ''
        self.root.ids.output_label.text = "Enter your grade"


BoxLayoutDemo().run()
