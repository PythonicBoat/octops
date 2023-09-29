from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.slider import Slider

Builder.load_file('screenLayout/spawn_screen.kv')

from .screen_check import set_spawn

class SpawnScreen(Screen):

    def check_slider_values(self):
        if ((self.ids.slide1.value < 80) and (self.ids.slide1.value > 70 )) and ((self.ids.slide2.value < 60)and ( self.ids.slide2.value > 50 )) and ((self.ids.slide3.value < 100) and (self.ids.slide3.value > 90 )):
            set_spawn()

#values are 75 55 95