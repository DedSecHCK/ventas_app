from kivy.uix.screenmanager import Screen
from kivymd.uix.list import MDList, ThreeLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from repositories.credito_repository import credito_repository
from repositories.cliente_repository import cliente_repository

class CreditosScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.creditos = []
        self.dialog = None
        
    def on_enter(self):
        """Called when screen is displayed"""
        self.load_creditos()
        
    def load_creditos(self):
        """Load credits from local database"""
        try:
            self.creditos = credito_repository.get_all()
            self.update_list()
        except Exception as e:
            print(f"Error loading creditos: {e}")
        
    def update_list(self):
        """Update the list view with credits"""
        if hasattr(self.ids, 'creditos_list'):
            self.ids.creditos_list.clear_widgets()
            for credito in self.creditos:
                # Get client name
                cliente = cliente_repository.get_by_id(credito.get('cliente_id'))
                cliente_nombre = f"{cliente.get('nombre', '')} {cliente.get('apellido', '')}" if cliente else "N/A"
                
                item = ThreeLineListItem(
                    text=f"Cliente: {cliente_nombre}",
                    secondary_text=f"Monto: ${credito.get('monto', 0):.2f} - Plazo: {credito.get('plazo', 0)} meses",
                    tertiary_text=f"Saldo: ${credito.get('saldo', 0):.2f} - Tasa: {credito.get('tasa_interes', 0)}%"
                )
                self.ids.creditos_list.add_widget(item)
    
    def show_add_dialog(self):
        """Show dialog to add new credit"""
        # Create form content
        content = MDBoxLayout(
            orientation="vertical",
            spacing=15,
            size_hint_y=None,
            height=350
        )
        
        self.cliente_id_field = MDTextField(hint_text="ID del Cliente", required=True, input_filter="int")
        self.monto_field = MDTextField(hint_text="Monto", required=True, input_filter="float")
        self.plazo_field = MDTextField(hint_text="Plazo (meses)", required=True, input_filter="int")
        self.tasa_field = MDTextField(hint_text="Tasa de Interés (%)", required=True, input_filter="float")
        
        content.add_widget(self.cliente_id_field)
        content.add_widget(self.monto_field)
        content.add_widget(self.plazo_field)
        content.add_widget(self.tasa_field)
        
        self.dialog = MDDialog(
            title="Agregar Crédito",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(text="CANCELAR", on_release=self.close_dialog),
                MDRaisedButton(text="GUARDAR", on_release=self.save_credito)
            ]
        )
        self.dialog.open()
        
    def close_dialog(self, *args):
        """Close the dialog"""
        if self.dialog:
            self.dialog.dismiss()
            
    def save_credito(self, *args):
        """Save new credit to local database"""
        try:
            # Validate required fields
            if not self.cliente_id_field.text or not self.monto_field.text or not self.plazo_field.text or not self.tasa_field.text:
                print("Error: Todos los campos son requeridos")
                return
            
            # Create credito data
            monto = float(self.monto_field.text)
            credito_data = {
                'cliente_id': int(self.cliente_id_field.text),
                'monto': monto,
                'plazo': int(self.plazo_field.text),
                'tasa_interes': float(self.tasa_field.text),
                'saldo': monto  # Initial saldo equals monto
            }
            
            # Save to database
            result = credito_repository.create(credito_data)
            if result:
                print(f"Crédito guardado: {result}")
                self.close_dialog()
                self.load_creditos()
            else:
                print("Error al guardar crédito")
        except Exception as e:
            print(f"Error saving credito: {e}")
        
    def go_back(self):
        """Navigate back to dashboard"""
        self.manager.current = "dashboard"
