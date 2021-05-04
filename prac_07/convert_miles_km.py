"""
CP1404 Practical 7 - Kivy
Program to convert miles to kilometers using a GUI built in Kivy
"""

from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.core.window import Window

KILOMETERS_PER_MILE = 1.60934


class MilesToKmApp(App):
    """Main program - Kivy app to convert miles to kilometers."""
    kilometers = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, increment):
        """Change miles based on buttons in GUI."""
        valid_input = self.check_valid_input()
        result = valid_input + increment
        self.root.ids.miles.text = str(result)

    def calculate_kilometers(self):
        """Convert miles to kilometers."""
        valid_input = self.check_valid_input()
        result = valid_input * KILOMETERS_PER_MILE
        self.kilometers = str(result)

    def check_valid_input(self):
        """Check for valid input for the conversion from miles to kilometers."""
        try:
            result = float(self.root.ids.miles.text)
            return result
        except ValueError:
            return 0


MilesToKmApp().run()
