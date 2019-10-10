

import kivy, os
import callme

kivy.require('1.7.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.image import Image


class SLRGui(BoxLayout):
    id1 = StringProperty()

    def __init__(self):
        super(SLRGui, self).__init__()
        self.id1 = 'data'
        self.img = 'pict.jpg'
    def compt(self):

        try:
            callme.primer()
            self.id1= 'done'
        except Exception:
            self.display.text = 'error'


class SLRGuiApp(App):
    title = 'SLR'
    icon = 'pict.jpeg'

    def build(self):
        return SLRGui()


if __name__ in ('__main__', '__android__'):
    SLRGuiApp().run()
