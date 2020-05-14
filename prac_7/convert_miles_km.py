from kivy.app import App
from kivy.lang import Builder
from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '250')
#Config.write()


FACTOR = 1.60934


class MilesConverterApp(App):
    """ DISTANCE CONVERTER APP """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "DISTANCE CONVERTER"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate_mi(self):
        """Handle calculation"""
        value = self.get_value()
        result = value / FACTOR
        self.root.ids.output_label.text = str(result)

    def handle_calculate_km(self):
        """Handle calculation"""
        value = self.get_value()
        result = value * FACTOR
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """UP/DOWN button press"""
        value = self.get_value() + increment
        self.root.ids.input_distance.text = str(value)

    def get_value(self):
        """Get text input from text entry widget"""
        try:
            value = float(self.root.ids.input_distance.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()