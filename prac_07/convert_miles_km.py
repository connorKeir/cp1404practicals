"""
CP1404 practical 07 - GUI program to convert miles to kilometres
Connor Keir
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.60934


class MilesToKmApp(App):
    result = StringProperty()

    def build(self):
        self.title = 'Convert Miles to Kilometres'
        self.root = Builder.load_file('convert_miles_km.kv')
        self.result = '54.717'
        return self.root

    def handle_calculate(self):
        value = self.check_input()
        self.result = str(value * MILES_TO_KM)

    def handle_change(self, increment):
        change = self.check_input() + increment
        self.root.ids.user_input.text = str(change)
        self.handle_calculate()

    def check_input(self):
        try:
            test_value = float(self.root.ids.user_input.text)
            return test_value
        except ValueError:
            return 0


MilesToKmApp().run()
