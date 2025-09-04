import os
import random
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty, ObjectProperty
from kivy.config import Config

# Настройка для headless режима (Docker)
Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '768')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

# Отключение проблемных провайдеров ввода для headless режима
os.environ['KIVY_WINDOW'] = 'sdl2'
os.environ['KIVY_GL_BACKEND'] = 'gl'

Builder.load_file('design.kv.txt')

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

        question = 'вопросик '
        self.name_label_text = question
        # main_label.text = question
        return self.name_label_text
    def change_text(self):
        try:
            with open("text_first_vibe.txt", encoding="utf8") as file:
                content = file.read()
            questions = content.split(';\n')
            # Убираем пустые строки
            questions = [q.strip() for q in questions if q.strip()]
            if questions:
                random_offset = random.randrange(0, len(questions))
                self.lbl.text = questions[random_offset]
            else:
                self.lbl.text = "Вопросы не найдены"
        except FileNotFoundError:
            self.lbl.text = "Файл с вопросами не найден"
        except Exception as e:
            self.lbl.text = f"Ошибка: {str(e)}"

class SecondScreen(Screen):
    name_label_text = StringProperty()

    def question_label_text(self, *args):
        question = 'вопросик '
        self.name_label_text = question
        # main_label.text = question
        return self.name_label_text

    def change_text(self):
        try:
            with open("text_second_vibe.txt", encoding="utf8") as file:
                content = file.read()
            questions = content.split(';\n')
            # Убираем пустые строки
            questions = [q.strip() for q in questions if q.strip()]
            if questions:
                random_offset = random.randrange(0, len(questions))
                self.lbl.text = questions[random_offset]
            else:
                self.lbl.text = "Вопросы не найдены"
        except FileNotFoundError:
            self.lbl.text = "Файл с вопросами не найден"
        except Exception as e:
            self.lbl.text = f"Ошибка: {str(e)}"
if __name__ == '__main__':
    app = MainApp()
    app.run()