from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button


class DynamicLabels(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)

        self.names = ['Bob', 'Dave', 'Cat', 'Arthur', 'Oren', 'Mai']

    def build(self):
        """Build the KIVY GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()

        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.names:
            temp_button = Button(text=name, id=name)
            self.root.ids.entries_box.add_widget(temp_button)


if __name__ == '__main__':
    DynamicLabels().run()