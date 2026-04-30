from kivy.uix.screenmanager import Screen
from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from repositories.cliente_repository import cliente_repository

class ClientesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.clientes = []
        self.dialog = None
        
    def on_enter(self):
        """Called when screen is displayed"""
        self.load_clientes()
        
    def load_clientes(self):
        """Load clients from local database"""
        try:
            self.clientes = cliente_repository.get_all()
            self.update_list()
        except Exception as e:
            print(f"Error loading clientes: {e}")
        
    def update_list(self):
        """Update the list view with clients"""
        if hasattr(self.ids, 'clientes_list'):
            self.ids.clientes_list.clear_widgets()
            for cliente in self.clientes:
                item = TwoLineListItem(
                    text=f"{cliente.get('nombre', '')} {cliente.get('apellido', '')}",
                    secondary_text=f"Cédula: {cliente.get('cedula', '')} - Tel: {cliente.get('telefono', '')}"
                )
                self.ids.clientes_list.add_widget(item)
    
    def show_add_dialog(self):
        """Show dialog to add new client"""
    
        content = MDBoxLayout(
            orientation="vertical",
            spacing=15,
            size_hint_y=None,
            height=400
        )
        
        self.nombre_field = MDTextField(hint_text="Nombre", required=True)
        self.apellido_field = MDTextField(hint_text="Apellido", required=True)
        self.cedula_field = MDTextField(hint_text="Cédula", required=True)
        self.telefono_field = MDTextField(hint_text="Teléfono")
        self.direccion_field = MDTextField(hint_text="Dirección")
        self.email_field = MDTextField(hint_text="Email")
        
        content.add_widget(self.nombre_field)
        content.add_widget(self.apellido_field)
        content.add_widget(self.cedula_field)
        content.add_widget(self.telefono_field)
        content.add_widget(self.direccion_field)
        content.add_widget(self.email_field)
        
        self.dialog = MDDialog(
            title="Agregar Cliente",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(text="CANCELAR", on_release=self.close_dialog),
                MDRaisedButton(text="GUARDAR", on_release=self.save_cliente)
            ]
        )
        self.dialog.open()
        
    def close_dialog(self, *args):
        """Close the dialog"""
        if self.dialog:
            self.dialog.dismiss()
            
    def save_cliente(self, *args):
        """Save new client to local database"""
        try:
            
            if not self.nombre_field.text or not self.apellido_field.text or not self.cedula_field.text:
                print("Error: Nombre, apellido y cédula son requeridos")
                return
            
            
            cliente_data = {
                'nombre': self.nombre_field.text,
                'apellido': self.apellido_field.text,
                'cedula': self.cedula_field.text,
                'telefono': self.telefono_field.text,
                'direccion': self.direccion_field.text,
                'email': self.email_field.text
            }
            
            
            result = cliente_repository.create(cliente_data)
            if result:
                print(f"Cliente guardado: {result}")
                self.close_dialog()
                self.load_clientes()
            else:
                print("Error al guardar cliente")
        except Exception as e:
            print(f"Error saving cliente: {e}")
        
    def go_back(self):
        """Navigate back to dashboard"""
        self.manager.current = "dashboard"
