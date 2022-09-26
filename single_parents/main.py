# from kaki.app import App
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang.builder import Builder
from kivy.properties import StringProperty
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDCustomBottomSheet
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.transition import MDSwapTransition
from PIL import ImageGrab

from Controller.chats import ChatScreen
from Controller.first import FirstScreen
from Controller.login import LoginScreen
from Controller.mainscreen import Feeds, HomeScreen
from Controller.signup import SignupScreen

# TODO: You may know an easier way to get the size of a computer display.
resolution = ImageGrab.grab().size

if platform == "linux" or platform == "win" or platform == "macosx":
    Window.size = (350, 720)
    Window.top = 0
    Window.left = resolution[0] - Window.width


class WindowManager(ScreenManager):
    pass


# class Singla(App, MDApp):
#     CLASSES = {
#         # "FirstScreen": "Controller/first",
#         # "Signup": "Controller/signup",
#         # "Login": "Controller/login",
#         "HomeScreen": "Controller/mainscreen",
#     }

#     AUTORELOADER_PATHS = [
#         (".", {"recursive": True}),
#     ]

#     KV_FILES = [
#         'Views/first.kv',
#         # 'Views/signup.kv',
#         # 'Views/login.kv',
#         'Views/mainscreen.kv',
#         'Views/chats.kv',
#     ]

#     def build_app(self, *args):
#         print("Autoreload")
class Singla(MDApp):
    def build(self):
        self.wm = WindowManager()
        # self.wm = WindowManager(transition=MDSwapTransition())
        self.theme_cls.material_style = "M3"
        # self.kv_directory = "Views"
        Builder.load_file("Views/first.kv")
        Builder.load_file("Views/signup.kv")
        Builder.load_file("Views/login.kv")
        Builder.load_file("Views/mainscreen.kv")
        Builder.load_file("Views/chats.kv")

        screens = [
            # HomeScreen(name="home_screen"),
            # SignupScreen(name="signup_screen"),
            # FirstScreen(),
            LoginScreen(name="login_screen"),
            SignupScreen(name="signup_screen"),
            ChatScreen(name="chat_screen"),
            HomeScreen(name="home_screen"),
            FirstScreen()
            # Home(name="home")
        ]

        for screen in screens:
            self.wm.add_widget(screen)
        self.wm.get_screen('home_screen').ids['nav'].switch_tab("screen 1")
        return self.wm

    def show_sheet(self):
        global bottom_sheet
        bottom_sheet = Factory.CustomSheet()
        # bottom_sheet.rate = rate
        # bottom_sheet.image = image
        # bottom_sheet.price = price
        self.custom_sheet = MDCustomBottomSheet(screen=bottom_sheet)
        self.custom_sheet.open()
        print(self.wm.ids)

    def publish(self, post):
        global bottom_sheet
        # post = self.wm.get_screen(bottom_sheet).ids['post'].text
        if post:
            self.wm.get_screen('home_screen').ids['nav'].switch_tab("screen 1")
            self.wm.get_screen('home_screen').ids['container'].add_widget(
                Feeds(pic="assets/img/pic.png", text=post, name="Bobo", date_time="today"))
            self.custom_sheet.dismiss()
        else:
            toast("You've not written anything")

    def update_name(self,name):
        # name = self.wm.get_screen('home_screen').ids['chat_card'].text

        self.wm.get_screen('chat_screen').ids['name'].text = name

Singla().run()
# class Singla(MDApp):

#     def build(self):

#         # Create a list of all screen, loop through it and add it to the screenmanager
#         # and return the screenmanager.
#         self.wm = WindowManager()

#         screens = [
#             FirstScreen()
#             # Home(name="home")
#         ]

#         for screen in screens:
#             self.wm.add_widget(screen)

#         return self.wm


# if __name__ == "__main__":
#     Singla().run()
