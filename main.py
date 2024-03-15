import random
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.layout import Layout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.widget import Widget
from kivy.properties import StringProperty, ObjectProperty
Builder.load_file('design.kv')
class MainApp(App):


    def build(self):
        # crate the screen manager
        sm =ScreenManager()
        sm.add_widget(StartScreen(name = 'start'))
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        return sm


class StartScreen(Screen):
    pass
class MenuScreen(Screen):
    pass
class FirstScreen(Screen):
    name_label_text = StringProperty()
    def question_label_text(self, *args):
        question = str(open("text.txt","r").read())
        self.name_label_text = question
        # main_label.text = question
        return question
    def change_text(self):
        self.name_label_text = str(open("text.txt","r").read())
class SecondScreen(Screen):
    pass

if __name__ == '__main__':
    app = MainApp()
    app.run()