import re

from kivymd.toast import toast
from kivymd.uix.screen import MDScreen

from Controller.firebasedb import FirebaseDatabase


class SignupScreen(MDScreen):
    def signup(self, fullname, email, password, kids, gender, phone):
        pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu)"
        # pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net|org)"
        if not fullname:
            toast("please enter your name")
        elif not email:
            toast("please enter your email")
        elif not password:
            toast("please enter your password")
        elif not kids:
            toast("How many kids have you?")
        elif not gender:
            toast("please enter your gender")
        elif not phone:
            toast("please enter your phone number")
        elif not fullname.isalpha():
            toast("only alphabets are allowed in a name")
        elif not re.search(pattern, email):
            toast("Please enter a valid email address")
        else:
            FirebaseDatabase().signup(fullname, email, password, kids, gender, phone)
