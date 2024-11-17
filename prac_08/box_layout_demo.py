from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutDemoApp(App):
    """Main application for BoxLayout Demo."""

    def build(self):
        return BoxLayout()

    def handle_greet(self):
        """Handles the greeting event."""
        input_name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello, {input_name}!"

    def handle_clear(self):
        """Clears the input and output fields."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


if __name__ == '__main__':
    BoxLayoutDemoApp().run()
