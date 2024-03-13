from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.layout import Layout
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_string("""
<StartScreen>:
    BoxLayout:
        Label:
            text: 'Hello'
        Button:
            text: 'Start'
            on_press: root.manager.current = 'menu'
<MenuScreen>
    BoxLayout:
        Label:
            text: 'You can choose your vibe'
        Button:
            text: 'first'
            on_press: root.manager.current = 'first'
        Button:
            text: 'second'
            on_press: root.manager.current = 'second'
<FirstScreen>
    BoxLayout:
        Label:
            text: 'You can choose your vibe'
        Button:
            text: 'change vibe'
            on_press: root.manager.current = 'menu'

<SecondScreen>
    BoxLayout:
        Label:
            text: 'You can choose your vibe'
        Button:
            text: 'change vibe'
            on_press: root.manager.current = 'menu'
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