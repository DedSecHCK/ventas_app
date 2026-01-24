from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from database.db_manager import db_manager
from screens.login import LoginScreen
from screens.dashboard import DashboardScreen
from screens.mapa import MapaScreen
from screens.clientes import ClientesScreen
from screens.creditos import CreditosScreen
from screens.pagos import PagosScreen

class VentasApp(MDApp):
    def build(self):
        # Initialize database
        self.init_database()
        
        # Set theme
        self.theme_cls.primary_palette = "Blue"
        
        # Create screen manager
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(MapaScreen(name="mapa"))
        sm.add_widget(ClientesScreen(name="clientes"))
        sm.add_widget(CreditosScreen(name="creditos"))
        sm.add_widget(PagosScreen(name="pagos"))
        
        return sm
    
    def init_database(self):
        """Initialize SQLite database"""
        try:
            db_manager.connect()
            db_manager.create_tables()
            print("Database initialized successfully")
        except Exception as e:
            print(f"Error initializing database: {e}")
    
    def on_stop(self):
        """Called when app is closing"""
        try:
            db_manager.disconnect()
            print("Database connection closed")
        except Exception as e:
            print(f"Error closing database: {e}")

if __name__ == "__main__":
    VentasApp().run()
