from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton

class DashboardScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def on_enter(self):
        """Called when screen is displayed"""
        # Load statistics or refresh data
        pass
        
    def navigate_to(self, screen_name):
        """Navigate to specified screen"""
        self.manager.current = screen_name
        
    def logout(self):
        """Handle logout"""
        self.manager.current = "login"