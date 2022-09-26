from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.label import MDLabel

class SentMessage(MDLabel):
    message = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Roboto-Bold"
    font_size = 17


class ReceivedMessage(MDLabel):
    message = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    font_name = "Roboto-Bold"
    font_size = 17


class ChatScreen(MDScreen):
    name = StringProperty()

    def goto_chat_screen(self):
        self.manager.get_screen(
            "home_screen").ids['nav'].switch_tab("screen 2")
        self.manager.current = "home_screen"

    def send(self):
        message = self.ids['message_box'].text
        self.ids.chat_list.add_widget(SentMessage(
            message=f"{message.strip()}", size_hint_x=.5, halign="center"))
        print("sent")
        self.ids['message_box'].text = ""

        greetings = ['hi', 'hey', 'good morning', 'good evening', 'good night']
        for greeting in greetings:
            if message == greeting:
                response = greeting
                self.ids.chat_list.add_widget(ReceivedMessage(
                    message=greeting, size_hint_x=.5, halign="center"))
                print("recieved")
        else:
            self.ids.chat_list.add_widget(ReceivedMessage(
                message=message, size_hint_x=.5, halign="center"))
            print("recieved")

