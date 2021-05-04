"""
CP1404 Practical 7 - Kivy
Practice a dynamic widget layout
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ['Sam', 'Lindsay', 'Bobby', 'John', 'Jane']


class DynamicLabelsApp(App):
    """Dynamic creation of widget layout."""
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from the names list and add them to the GUI."""
        for name in NAMES:
            temp_label = Label(text=name)
            self.root.ids.entries_label.add_widget(temp_label)


DynamicLabelsApp().run()
