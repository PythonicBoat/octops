from kivy.animation import Animation
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from .screen_check import passcode, get_spawn, get_doors, get_sitea

Builder.load_file('screenLayout/siteb_screen.kv')
sound = SoundLoader.load('assets/audio/siteb_defused.wav')

class SiteBScreen(Screen):
    defused = False
    @staticmethod
    def Delay(delay):
        return Animation(duration=delay)

    def on_enter(self):
        if get_spawn() and get_sitea() and get_doors() and not SiteBScreen.defused:
            self.ids.defuse_img.color = (1,1,1,1)

    def defuse_btn_press(self):
        if get_sitea() and get_doors() and get_spawn() and not SiteBScreen.defused:
            SiteBScreen.defused = True
            Animation(color= (1,1,1,0.5), duration=0.5).start(self.ids.defuse_img)

            self.ids.overlay_black.opacity = 0.6

            octocat_icon = self.Delay(0.5) + Animation(color=(1,1,1,1), pos= (dp(0), dp(0)), duration=0.2, t='out_quad')
            octocat_icon.start(self.ids.octocat_icon)
            
            text_bubble = self.Delay(1) + Animation(color=(1,1,1,1), pos= (dp(233), dp(154)), duration=0.2, t='out_quad')
            text_bubble.start(self.ids.octocat_prompt)

            Clock.schedule_once(lambda dt:sound.play(), 0.7)

        else:
            return