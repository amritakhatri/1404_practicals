from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyKivyApp(App):
    def build(self):
        return MyBoxLayout()

class MyBoxLayout(BoxLayout):
    pass  # The layout is defined in the .kv file

if __name__ == "__main__":
    MyKivyApp().run()
