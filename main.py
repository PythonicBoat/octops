# This file is final and shouldnt be changed
# Builder is used to generate all UI elements
# make use of the .kv files stored inside the screen folder
# This file simply builds the 
# Define window behaviours here such as size, transition

#------------------------Imports-------------------------#

from kivy.config import Config 
Config.set('kivy','window_icon','assets/img/main_mascot.png') #setting this is enough for taskbar icon as well it will show up when it is built
Config.set('graphics', 'resizable', False)
from kivy.app import App
from kivy.core.window import Window

from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

#---------------------Screen Imports---------------------#

from screens.main import MainScreen
from screens.map import MapScreen
from screens.sitea import SiteAScreen
from screens.siteb import SiteBScreen
from screens.doors import DoorsScreen
from screens.spawn import SpawnScreen
from screens.map import MapScreen

#---------------------Screen Imports---------------------#

Window.size = (600,600)
Window.borderless = False
class Octops(App):

    def build(self):
        sm = ScreenManager()
        sm.transition = NoTransition()

        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(MapScreen(name='map'))
        sm.add_widget(SiteBScreen(name='siteb'))
        sm.add_widget(SiteAScreen(name='sitea'))
        sm.add_widget(DoorsScreen(name='doors'))
        sm.add_widget(SpawnScreen(name='spawn'))

        return sm
 
Octops().run()