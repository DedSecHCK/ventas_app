from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.uix.boxlayout import BoxLayout

class ClienteCard(MDCard):
    """Custom card widget to display client information"""
    
    def __init__(self, cliente_data, **kwargs):
        super().__init__(**kwargs)
        self.cliente_data = cliente_data
        self.orientation = "vertical"
        self.padding = 15
        self.spacing = 10
        self.size_hint_y = None
        self.height = 120
        self.elevation = 3
        
        # Create layout
        self.build_card()
        
    def build_card(self):
        """Build the card UI"""
        # Name label
        name_label = MDLabel(
            text=f"{self.cliente_data.get('nombre', '')} {self.cliente_data.get('apellido', '')}",
            font_style="H6",
            size_hint_y=None,
            height=30
        )
        self.add_widget(name_label)
        
        # Info label
        info_label = MDLabel(
            text=f"Cédula: {self.cliente_data.get('cedula', 'N/A')}",
            size_hint_y=None,
            height=20
        )
        self.add_widget(info_label)
        
        # Contact label
        contact_label = MDLabel(
            text=f"Tel: {self.cliente_data.get('telefono', 'N/A')} | Email: {self.cliente_data.get('email', 'N/A')}",
            size_hint_y=None,
            height=20
        )
        self.add_widget(contact_label)
        
        # Action buttons
        button_layout = BoxLayout(
            size_hint_y=None,
            height=40,
            spacing=10
        )
        
        view_btn = MDIconButton(
            icon="eye",
            on_release=self.view_details
        )
        button_layout.add_widget(view_btn)
        
        edit_btn = MDIconButton(
            icon="pencil",
            on_release=self.edit_cliente
        )
        button_layout.add_widget(edit_btn)
        
        self.add_widget(button_layout)
        
    def view_details(self, *args):
        """View client details"""
        print(f"Viewing details for: {self.cliente_data}")
        
    def edit_cliente(self, *args):
        """Edit client information"""
        print(f"Editing: {self.cliente_data}")
