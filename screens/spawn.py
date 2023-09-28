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

    def check_slider_values(self, slider1_value, slider2_value, slider3_value):
        random_numbers = self.generate_random_numbers()

        # Check if each slider value matches the corresponding random number
        if round(slider1_value, 2) == round(random_numbers[0], 2) and \
           round(slider2_value, 2) == round(random_numbers[1], 2) and \
           round(slider3_value, 2) == round(random_numbers[2], 2):
            print("Mission successful!")
        else:
            print("Mission failed. Try again.")

