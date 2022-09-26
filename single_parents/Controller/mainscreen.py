from kivymd.uix.screen import MDScreen
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.toast import toast
from kivymd.uix.list import TwoLineAvatarListItem
from kivymd.uix.selectioncontrol import MDSwitch
# from kivymd.uix.bottomnavigation import MDBottomNavigation
# from kivymd.utils.cropimage import crop_image

class Options(MDBoxLayout):
    pass

class Feeds(MDFloatLayout, FakeRectangularElevationBehavior):
    pic = StringProperty()
    text = StringProperty()
    name = StringProperty()
    date_time = StringProperty()

class ChatsCard(MDFloatLayout, TwoLineAvatarListItem, FakeRectangularElevationBehavior):
    image = StringProperty()
    name = StringProperty()
    last_msg = StringProperty()

class HomeScreen(MDScreen):
    def publish(self):
        post = self.ids['post'].text
        if post:
            Feeds(pic="assets/img/pic.png", text=post, name="Bobo", date_time="today")
        else:
            toast("You've not written anything.png")

    def logout(self):
        self.manager.current = "login_screen"