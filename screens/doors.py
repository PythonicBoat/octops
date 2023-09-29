from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from .screen_check import passcode, set_doors

Builder.load_file('screenLayout/doors_screen.kv')
sound = SoundLoader.load('assets/audio/doors_roger.wav')

class DoorsScreen(Screen):
    verified = False

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

    def verify(self):
        code = ""
        code = self.ids.label_1.text + self.ids.label_2.text + self.ids.label_3.text + self.ids.label_4.text
        print(code)
        if passcode == int(code):
            return True

    def verify_btn_press(self):
        if not DoorsScreen.verified and DoorsScreen.verify(self):
            DoorsScreen.verified = True
            self.ids.splash_bg.source = 'assets/img/doors_splash_after.png'
            set_doors()
            sound.play()