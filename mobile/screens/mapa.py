from kivy.uix.screenmanager import Screen
from services import gps
from repositories.cliente_repository import cliente_repository

class MapaScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.clientes = []
        self.current_location = None
        
    def on_enter(self):
        """Called when screen is displayed"""
        self.load_current_location()
        self.load_clientes()
        
    def load_current_location(self):
        """Get current GPS location"""
        try:
            self.current_location = gps.get_location()
            self.update_map()
            
            # Update location label if it exists
            if hasattr(self.ids, 'location_label'):
                self.ids.location_label.text = f"Ubicación actual: ({self.current_location['lat']:.4f}, {self.current_location['lon']:.4f})"
        except Exception as e:
            print(f"Error getting location: {e}")
        
    def load_clientes(self):
        """Load clients from local database to show on map"""
        try:
            self.clientes = cliente_repository.get_all()
            self.update_map()
        except Exception as e:
            print(f"Error loading clientes: {e}")
        
    def update_map(self):
        """Update map with markers"""
        # Implementation would update map widget with client locations
        # This requires a map library like kivy-garden.mapview
        # For now, just log the data
        print(f"Current location: {self.current_location}")
        print(f"Total clientes: {len(self.clientes)}")
        
    def go_back(self):
        """Navigate back to dashboard"""
        self.manager.current = "dashboard"