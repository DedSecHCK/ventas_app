from kivy.uix.screenmanager import Screen
from kivymd.uix.list import MDList, ThreeLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from repositories.pago_repository import pago_repository
from repositories.credito_repository import credito_repository
from services import gps

class PagosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pagos = []
        self.dialog = None
        
    def on_enter(self):
        """Called when screen is displayed"""
        self.load_pagos()
        
    def load_pagos(self):
        """Load payments from local database"""
        try:
            self.pagos = pago_repository.get_all()
            self.update_list()
        except Exception as e:
            print(f"Error loading pagos: {e}")
        
    def update_list(self):
        """Update the list view with payments"""
        if hasattr(self.ids, 'pagos_list'):
            self.ids.pagos_list.clear_widgets()
            for pago in self.pagos:
                item = ThreeLineListItem(
                    text=f"Crédito ID: {pago.get('credito_id', 'N/A')}",
                    secondary_text=f"Valor: ${pago.get('valor', 0):.2f} - Fecha: {pago.get('fecha', 'N/A')}",
                    tertiary_text=f"Ubicación: ({pago.get('lat', 0):.4f}, {pago.get('lon', 0):.4f})"
                )
                self.ids.pagos_list.add_widget(item)
    
    def show_add_dialog(self):
        """Show dialog to add new payment with GPS location"""
        from widgets.pago_modal import PagoModal
        modal = PagoModal(callback=self.load_pagos)
        modal.show()
        
    def go_back(self):
        """Navigate back to dashboard"""
        self.manager.current = "dashboard"
