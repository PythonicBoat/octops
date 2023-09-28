from kivy.animation import Animation
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.core.audio import SoundLoader
from kivy.clock import Clock

Builder.load_file('screenLayout/siteb_screen.kv')
sound = SoundLoader.load('assets/audio/siteb_defused.wav')

class SiteBScreen(Screen):
    @staticmethod
    def Delay(delay):
        return Animation(duration=delay)
    
    def defuse_btn_press(self):

        Animation(color= (1,1,1,1), duration=0.5).start(self.ids.defuse_img)
        Animation(color=(0,0,0,0.6), duration=0).start(self.ids.overlay_black)

        octocat_icon = self.Delay(0.5) + Animation(color=(1,1,1,1), pos= (dp(0), dp(0)), duration=0.2, t='out_quad')
        octocat_icon.start(self.ids.octocat_icon)
        
        text_bubble = self.Delay(1) + Animation(color=(1,1,1,1), pos= (dp(233), dp(154)), duration=0.2, t='out_quad')
        text_bubble.start(self.ids.octocat_prompt)

        Clock.schedule_once(lambda dt:sound.play(), 0.7)