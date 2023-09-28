from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader


Builder.load_file('screenLayout/sitea_screen.kv')
sound = SoundLoader.load('assets/audio/sitea_planted.wav')


class SiteAScreen(Screen):
    pressed_buttons = []

    def change_img(self, button, idOG):
        idOG_dynamic = f"{idOG}"
        widget = getattr(self.ids, idOG_dynamic, None)
        widget.source = "assets/img/symbols/off.png" if widget.source == f"assets/img/symbols/on.png" else f"assets/img/symbols/on.png"

    def check_product(self, instance, id):
        button_id = id  # Get the ID of the pressed button
        self.pressed_buttons.append(id)  # Add the ID to the list
        print(f'Button pressed: {button_id}')

        # Check if we have pressed 4 buttons
        if len(self.pressed_buttons) == 4:
            product = 1
            for button_id in self.pressed_buttons:
                # Extract the button number from the ID
                product *= button_id

            if product == 70:
                print("Valid")
                sound.play()
            else:
                print("Invalid")
            self.pressed_buttons = []  # Reset the list for the next set of button presses


