"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
Amrita Khatri
Started: 15/11/2024
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometresApp(App):
    """Miles to Kilometres Converter App"""

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (300, 200)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_conversion(self):
        """Convert miles to kilometres."""
        try:
            miles = float(self.root.ids.input_miles.text)
            kilometres = miles * 1.60934
            self.root.ids.output_label.text = f"{kilometres:.3f} km"
        except ValueError:
            self.root.ids.output_label.text = "0.0 km"

    def handle_increment(self, change):
        """Increment or decrement miles by 1."""
        try:
            miles = float(self.root.ids.input_miles.text) + change
        except ValueError:
            miles = change
        self.root.ids.input_miles.text = str(miles)
        self.handle_conversion()


MilesToKilometresApp().run()
