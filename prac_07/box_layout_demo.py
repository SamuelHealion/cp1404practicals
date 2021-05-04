"""
CP1404 Practical 7 - Kivy
Basic program that takes a users name and greets them using a GUI built in Kivy
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Main program - Kivy app to greet a user."""
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Take the input name and print to the label widget."""
        print('test')
        self.root.ids.output_label.text = 'Hello ' + self.root.ids.input_name.text

    def handle_clear(self):
        """Clear the input name and reset the label widget."""
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()
