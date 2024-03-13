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
from kivy.properties import StringProperty
Builder.load_string("""
<StartScreen>:
    FloatLayout:
        orientation: 'vertical'
        padding:20
        canvas:
            Color:
                rgba: 1, .3, .8, .5
        Label:
            text: 'Hello'
            pos_hint:{'center_x': .5, 'center_y': .7}
        Button:
            text: 'Start'
            size_hint: 0.5, 0.2
            pos_hint:{'center_x': .5, 'center_y': .3}
            on_press: root.manager.current = 'menu'
<MenuScreen>
    BoxLayout:
        Label:
            text: 'You can choose your vibe'
        Button:
            text: 'first'
            on_press: 
                root.manager.current = 'first'
                root.manager.transition.direction = 'left'
            
        Button:
            text: 'second'
            on_press: 
                root.manager.current = 'second'
                root.manager.transition.direction = 'left'
<FirstScreen>
    BoxLayout:
        size:root.size
        Label:
            id:label1
            text: 'lddldlld'
        Button:
            id: button_question
            text: 'next question'
            
        Button:
            text: 'change vibe'
            on_press: 
                root.manager.current = 'menu'
                root.manager.transition.direction = 'right'

<SecondScreen>
    BoxLayout:
        Label:
            text: 'Второй вайб'
            
        Button:
            text: 'change vibe'
            on_press: 
                root.manager.current = 'menu'
                root.manager.transition.direction = 'right'
""")
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
    pass
class SecondScreen(Screen):
    pass

if __name__ == '__main__':
    app = MainApp()
    app.run()