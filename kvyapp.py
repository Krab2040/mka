from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import  ScreenManager, Screen

class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main',text='Назад', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal
class MainScr(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        v_layout = BoxLayout(orientation='vertical', padding=8,spacing=8)
        h_layout = BoxLayout()
        txt = Label(text='Выбери экран')
        self.btn_1 = ScrButton(self, direction='down',goal='first', text='1')
        self.btn_2 = ScrButton(self, direction='left', goal='second', text='2')
        self.btn_3 = ScrButton(self, direction='right', goal='third', text='3')
        self.btn_4 = ScrButton(self, direction='up', goal='fourth', text='4')

        v_layout.add_widget(self.btn_1)
        v_layout.add_widget(self.btn_2)
        v_layout.add_widget(self.btn_3)
        v_layout.add_widget(self.btn_4)

        h_layout.add_widget(txt)
        h_layout.add_widget(v_layout)
        self.add_widget(h_layout)

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn_back = ScrButton(self, direction='down', goal='main', text='Назад', size_hint=(0.5, 1))
        v_layout = BoxLayout(orientation='vertical')
        v_layout.add_widget(self.btn_back)
        self.add_widget(v_layout)

class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn_back = ScrButton(self, direction='left', goal='main', text='Назад', size_hint=(0.5, 1))
        v_layout = BoxLayout(orientation='vertical')
        v_layout.add_widget(self.btn_back)
        self.add_widget(v_layout)

class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn_back = ScrButton(self, direction='right', goal='main', text='Назад', size_hint=(0.5, 1))
        v_layout = BoxLayout(orientation='vertical')
        v_layout.add_widget(self.btn_back)
        self.add_widget(v_layout)

class FourhtScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.btn_back = ScrButton(self, direction='up', goal='main', text='Назад', size_hint=(0.5, 1))
        v_layout = BoxLayout(orientation='vertical')
        v_layout.add_widget(self.btn_back)
        self.add_widget(v_layout)


class MyApp(App):
    def build(self):
        scr_manager = ScreenManager()
        scr_manager.add_widget(MainScr(name='main'))
        scr_manager.add_widget(FirstScr(name='first'))
        scr_manager.add_widget(SecondScr(name='second'))
        scr_manager.add_widget(ThirdScr(name='third'))
        scr_manager.add_widget(FourhtScr(name='fourth'))
        return scr_manager



MyApp().run()
print('ыввфывыф')