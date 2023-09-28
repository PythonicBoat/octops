from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader

Builder.load_file('screenLayout/sitea_screen.kv')
sound = SoundLoader.load('assets/audio/sitea_planted.wav')

from .screen_check import set_sitea
class SiteAScreen(Screen):
    pressed_buttons = []

    def show_overlay(self):
        self.ids.overlay.opacity = 0.5
        self.pressed_buttons = []

    def change_img(self, button, idOG):
        idOG_dynamic = f"{idOG}"
        widget = getattr(self.ids, idOG_dynamic, None)
        widget.source = "assets/img/symbols/off.png" if widget.source == "assets/img/symbols/on.png" else "assets/img/symbols/on.png"
        print(f"{idOG_dynamic}:{widget.source}")

    def check_product(self, instance, id):
        button_id = id  # Get the ID of the pressed button
        self.pressed_buttons.append(id)  # Add the ID to the list
        print(f'Button pressed: {button_id}')
        x = ""
        # Check if we have pressed 4 buttons
        if len(self.pressed_buttons) == 4:
            product = 1
            for button_id in self.pressed_buttons:
                # Multiply the button number to a product var
                product *= button_id

            if product == 70:
                x = "Valid"
                sound.play()
                self.show_overlay()
                set_sitea()
            else:
                x = "Invalid"

        if x == "Invalid":
            for button in self.pressed_buttons:
                widget = getattr(self.ids, f"{button}", None)
                widget.source = "assets/img/symbols/off.png"
            self.pressed_buttons = []

