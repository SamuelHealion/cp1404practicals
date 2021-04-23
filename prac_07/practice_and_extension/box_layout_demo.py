"""
CP1404 Practical 7 - Kivy
Change the Layout of the GUI for Practice and Extension
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class BoxLayoutDemo(App):
    def build(self):
        Window.size = (600, 300)
        self.title = "Greeter Program"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        # print('test')
        self.root.ids.output_label.text = 'Hello ' + self.root.ids.input_name.text

    def handle_clear(self):
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = "Enter your name"


BoxLayoutDemo().run()
