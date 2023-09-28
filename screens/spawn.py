from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.slider import Slider
import random

Builder.load_file('screenLayout/spawn_screen.kv')

class SpawnScreen(Screen):

    def check_slider_values(self):
        # Check if each slider value matches the corresponding random number
        print(self.ids.slide1.value)
        if ((self.ids.slide1.value < 80) and (self.ids.slide1.value > 70 )) and ((self.ids.slide2.value < 60)and ( self.ids.slide2.value > 50 )) and ((self.ids.slide3.value < 100) and (self.ids.slide3.value > 90 )):
            print("Mission successful!")
        else:
            print("Mission failed. Try again.")
