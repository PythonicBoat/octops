from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.slider import Slider
import random
from .screen_check import slider

Builder.load_file('screenLayout/spawn_screen.kv')

from .screen_check import set_spawn

class SpawnScreen(Screen):

    def check_slider_values(self):
        # Check if each slider value matches the corresponding random number
        print(self.ids.slide1.value)
        x=slider[0]
        y=slider[1]
        z=slider[2]
        if ((self.ids.slide1.value < x) and (self.ids.slide1.value > x-10 )) and ((self.ids.slide2.value < y)and ( self.ids.slide2.value > y-10 )) and ((self.ids.slide3.value < z) and (self.ids.slide3.value > z-10 )):
            print("Mission successful!")
        else:
            print("Mission failed. Try again.")