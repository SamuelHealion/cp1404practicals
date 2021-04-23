"""
CP1404 Practical 7 - Kivy
Practice and Extension
Creating a GUI for the temperature conversion program from week 1
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty


class TemperaturesApp(App):
    """Main program to convert temperatures using Kivy as the GUI."""
    converted_temperature = StringProperty()

    def build(self):
        """Build the GUI"""
        self.title = "Temperature Converter"
        self.root = Builder.load_file('temperatures.kv')
        return self.root

    def handle_increment(self, value):
        temperature = self.get_valid_temperature()
        result = temperature + value
        self.root.ids.input_temperature.text = str(result)

    def change_conversion(self):
        """Change which conversion is currently being used."""
        if self.root.ids.conversion_type.text == 'Celsius to Fahrenheit':
            self.root.ids.conversion_type.text = 'Fahrenheit to Celsius'
        else:
            self.root.ids.conversion_type.text = 'Celsius to Fahrenheit'
        self.convert_temperature()

    def get_valid_temperature(self):
        try:
            temperature = float(self.root.ids.input_temperature.text)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input"
            temperature = 0.0
        return temperature

    def convert_temperature(self):
        temperature = self.get_valid_temperature()
        if self.root.ids.conversion_type.text == 'Fahrenheit to Celsius':
            converted_temperature = (temperature - 32) * 5 / 9
        else:
            converted_temperature = temperature * 9 / 5 + 32
        self.root.ids.output_label.text = str(converted_temperature)


TemperaturesApp().run()
