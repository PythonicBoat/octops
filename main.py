# This file is final and shouldnt be changed
# Builder is used to generate all UI elements
# make use of the .kv files stored inside the screen folder
# This file simply builds the 
# Define window behaviours here such as size, transition



from kivy.config import Config 
Config.set('graphics', 'resizable', False) #prevents the window from being resizable

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
Window.borderless = False
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder

class MainScreen(Screen):
    pass

class MapScreen(Screen):
    pass

class SiteBScreen(Screen):
    pass

class SiteAScreen(Screen):
    pass

class DoorsScreen(Screen):
    pass

class SpawnScreen(Screen):
    pass

class Octops(App):

    def build(self):
        sm = ScreenManager()
        sm.transition = NoTransition()

        Builder.load_file('screens/main_screen.kv')
        Builder.load_file('screens/map_screen.kv')
        Builder.load_file('screens/siteb_screen.kv')
        Builder.load_file('screens/sitea_screen.kv')
        Builder.load_file('screens/doors_screen.kv')
        Builder.load_file('screens/spawn_screen.kv')    


        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(MapScreen(name='map'))
        sm.add_widget(SiteBScreen(name='siteb'))
        sm.add_widget(SiteAScreen(name='sitea'))
        sm.add_widget(DoorsScreen(name='doors'))
        sm.add_widget(SpawnScreen(name='spawn'))

        return sm
    
Octops().run()