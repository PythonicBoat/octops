from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
import webbrowser

Builder.load_file('screenLayout/main_screen.kv')

sound = SoundLoader.load('assets/audio/main_gogo.wav')
if sound:
    print("Sound found at %s" % sound.source)
    sound.play()

class MainScreen(Screen):
    def website(self):
        webbrowser.open('http://www.youtube.com')