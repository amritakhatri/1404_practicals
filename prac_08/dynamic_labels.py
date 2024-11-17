"""
CP1404/CP5632 Practical
Dynamic Labels Example
Amrita Khatri
Started: 17/11/2024
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """ Create dynamic labels from a list of names and display them in a BoxLayout """

    def build(self):
        """ Build the app and dynamically add labels """
        self.names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']  # List of names
        self.root = Builder.load_file('dynamic_labels.kv')  # Load the kv file
        for name in self.names:
            temp_label = Label(text=name)  # Create a label for each name
            self.root.ids.main.add_widget(temp_label)  # Add label to BoxLayout
        return self.root


if __name__ == '__main__':
    DynamicLabelsApp().run()
