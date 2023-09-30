from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from .screen_check import slider

Builder.load_file('screenLayout/spawn_screen.kv')

from .screen_check import set_spawn

class SpawnScreen(Screen):
    verified = False
    def slider_val_change(self):
        if not SpawnScreen.verified and ((self.ids.slide1.value < slider[0]+10) and (self.ids.slide1.value > slider[0]-10 )) and ((self.ids.slide2.value < slider[1]+10)and ( self.ids.slide2.value > slider[1]-10 )) and ((self.ids.slide3.value < slider[2]+10) and (self.ids.slide3.value > slider[2]-10 )):
            SpawnScreen.verified = True
            set_spawn()