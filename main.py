# main.py

import time

#from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.svg import Svg
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd import images_path
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

from layout_helper import loginscreen_helper
from database import DataBase
from cborder import myWebsocketClient

Window.size = (360,600)

class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class HelloScreen(Screen):
    def loginbtn(self):
        if db.validate(self.username.text, self.password.text):
            #MainWindow.current = self.email.text
            self.reset()
            screen = Builder.load_string(MainScreen)
            return screen
            #sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.username.text = ""
        self.password.text = ""


class MainScreen(Screen):
    n = ObjectProperty(None)
    #created = ObjectProperty(None)
    email = ObjectProperty(None)
    product = ObjectProperty(None)
    spotpr = ObjectProperty(None)
    current = ""
    wsClient = myWebsocketClient()    
    

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        #self.created.text = "Created On: " + created
        self.product.text = "Product: " #+ wsClient.msg["type"]
        self.spotpr.text = "Spot Price: " #+ wsClient.msg["price"]
        self.wsClient.start()
         #print(wsClient.url, wsClient.products)
        while (sm.current == "main" or time.elaps):
            print (wsClient)
        #time.sleep(1)
        wsClient.close()



class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(0.75, 0.75))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


#kv = Builder.load_file("my.kv")
#sm = WindowManager()
db = DataBase("users.txt")

#wsClient.start()

#screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main")]
#for screen in screens:
#    sm.add_widget(screen)

#sm.current = "login"
#wsClient.close()

# The ScreenManager controls moving between screens
screen_manager = ScreenManager()
   
# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(HelloScreen(name ="hello_user"))

class TradeStationApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"

        screen = Builder.load_string(loginscreen_helper)
        return screen

if __name__ == "__main__":
    TradeStationApp().run()