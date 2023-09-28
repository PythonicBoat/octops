from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.slider import Slider
import random

Builder.load_file('screenLayout/spawn_screen.kv')

class SpawnScreen(Screen):
    def generate_random_numbers(self):
        # Generate 3 random numbers between 0 and 1
        random_numbers = [random.random() for _ in range(3)]
        return random_numbers

    def check_slider_values(self):
        random_numbers = self.generate_random_numbers()
        # Check if each slider value matches the corresponding random number
        print(round(self.ids.slide1.value, 2))
        print(round(0.8, 2))
        if round(self.ids.slide1.value, 2) == round(0.8, 2) and round(self.ids.slide2.value, 2) == round(0.6, 2) and round(self.ids.slide3.value, 2) == round(0.4, 2):
            print("Mission successful!")
        else:
            print("Mission failed. Try again.")
