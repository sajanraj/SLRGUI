from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen,FadeTransition
from kivy.uix.filechooser import FileChooser
from kivy.lang import Builder

import STest
import os
class Mainscrn(ScreenManager):
    pass

class FullImage(FloatLayout):
    cancel = ObjectProperty(None)
    pass


class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(Screen):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_live(self):
        STest.slrlive()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        print(path, filename)
        with open(os.path.join(path, filename[0])) as stream:
            # self.text_input.text = stream.read()
            self.text_input.text = filename[0]

        self.dismiss_popup()
        pred = STest.slrtest(filename[0])
        self.source = filename[0]
        self.id = str(pred)

    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()

    pass


class SLRGui(Screen):
    id1 = StringProperty()

    pass


presentation = Builder.load_file("editor.kv")


class Editor(App):
    id1 = StringProperty()

    def __init__(self):
        super(Editor, self).__init__()
        self.source = "pict.jpg"
        self.id = "image"



    def build(self):
        return presentation


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)

if __name__ == '__main__':
    Editor().run()
