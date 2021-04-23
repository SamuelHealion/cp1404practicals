"""
CP1404 Practical 7 - Kivy
Practice creating dynamic buttons by taking names and ages from a text file then adding them to the GUI
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button

INPUT_FILE = 'names_ages.txt'


class DynamicNameAgeApp(App):
    """Main program - Kivy app to practice dynamic widget creation."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        """Get details from names_ages.txt file."""
        self.name_to_age = {}
        in_file = open(INPUT_FILE, 'r')
        for name in in_file:
            new_name = name.split(',')
            self.name_to_age[new_name[0]] = new_name[1]
        in_file.close()

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Names with Ages"
        self.root = Builder.load_file('dynamic_names_ages.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.name_to_age:
            temp_button = Button(text=name)
            temp_button.bind(on_press=self.press_entry)
            self.root.ids.dynamic_layout.add_widget(temp_button)

    def press_entry(self, instance):
        """Handle pressing entry buttons."""
        name = instance.text
        self.root.ids.output_label.text = '{} is {} years old'.format(name, self.name_to_age[name])


DynamicNameAgeApp().run()
