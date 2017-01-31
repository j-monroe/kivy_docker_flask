from kivy.app import App
from kivy.utils import platform
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.clock import Clock #clock to schedule the game update
from kivy.storage.jsonstore import JsonStore
from os.path import join
import random
import requests
from kivy.logger import Logger


class ImageButton(ButtonBehavior, Image):
    pass

class AppScreen(FloatLayout):
    app = ObjectProperty(None)

class MenuScreen(AppScreen):
    def __init__(self,app):
        super(MenuScreen, self).__init__()
        self.app = app

    def run(self):
        pass

    def make_request(self,place):
        url = "http://104.236.145.84:5000/clothing?place={}".format(place)
        request = requests.get(url)
        if request.ok:
            #return(request.text)
            response = request.json()
            self.response_text = response['coat']
            Logger.info('log: response text is: '+ self.response_text)
            self.ids.printing_area.text = self.response_text


presentation = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):
        self.request = ""
        self.url = ""
        self.response_text = ""
        self.screens = {}
        self.screens['menu'] = MenuScreen(self)
        self.root = FloatLayout()

        self.open_screen('menu')
        return self.root



    def open_screen(self,name):
        self.root.clear_widgets()
        self.root.add_widget(self.screens[name])
        self.screens[name].run()

if __name__ == '__main__':
    MainApp().run()