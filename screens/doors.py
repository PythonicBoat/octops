from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader

Builder.load_file('screenLayout/doors_screen.kv')

class DoorsScreen(Screen):

    def increment_value(self, label_index):
        if(int(label_index.text) == 9):
            label_index.text = "0"
        else:
            label_index.text = f"{int(label_index.text) + 1}"
    
    def decrement_value(self, label_index):
        if(int(label_index.text) == 0):
            label_index.text = "9"
        else:
            label_index.text = f"{int(label_index.text) - 1}"    

    

