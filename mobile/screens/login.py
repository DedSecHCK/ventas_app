from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def on_enter(self):
        """Called when screen is displayed"""
        pass
        
    def login(self):
        """Handle login button press"""
        # Get username and password from KV file widgets
        username = self.ids.username.text
        password = self.ids.password.text
        
        # Simple validation (in production, validate against backend)
        if username and password:
            self.manager.current = "dashboard"
        else:
            # Show error message
            pass