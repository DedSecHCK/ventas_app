from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from services import gps
from repositories.pago_repository import pago_repository
from repositories.credito_repository import credito_repository

class PagoModal:
    """Modal dialog for registering payments"""
    
    def __init__(self, callback=None):
        self.callback = callback
        self.dialog = None
        self.location = None
        
    def show(self):
        """Show the payment modal"""
        # Get current GPS location
        self.location = gps.get_location()
        
        # Create content layout
        content = MDBoxLayout(
            orientation="vertical",
            spacing=20,
            size_hint_y=None,
            height=300
        )
        
        # Credit ID field
        self.credito_field = MDTextField(
            hint_text="ID del Crédito",
            required=True,
            input_filter="int"
        )
        content.add_widget(self.credito_field)
        
        # Amount field
        self.valor_field = MDTextField(
            hint_text="Valor del Pago",
            required=True,
            input_filter="float"
        )
        content.add_widget(self.valor_field)
        
        # Location display
        location_label = MDLabel(
            text=f"Ubicación: ({self.location['lat']:.4f}, {self.location['lon']:.4f})",
            size_hint_y=None,
            height=30
        )
        content.add_widget(location_label)
        
        # Create dialog
        self.dialog = MDDialog(
            title="Registrar Pago",
            type="custom",
            content_cls=content,
            buttons=[
                MDFlatButton(
                    text="CANCELAR",
                    on_release=self.close
                ),
                MDRaisedButton(
                    text="GUARDAR",
                    on_release=self.save_pago
                )
            ]
        )
        
        self.dialog.open()
        
    def close(self, *args):
        """Close the modal"""
        if self.dialog:
            self.dialog.dismiss()
            
    def save_pago(self, *args):
        """Save the payment to local database"""
        # Validate fields
        if not self.credito_field.text or not self.valor_field.text:
            print("Error: Todos los campos son requeridos")
            return
            
        try:
            credito_id = int(self.credito_field.text)
            valor = float(self.valor_field.text)
            
            # Verify credito exists
            credito = credito_repository.get_by_id(credito_id)
            if not credito:
                print(f"Error: Crédito {credito_id} no encontrado")
                return
            
            # Prepare payment data
            pago_data = {
                "credito_id": credito_id,
                "valor": valor,
                "lat": self.location["lat"],
                "lon": self.location["lon"]
            }
            
            # Save to local database
            result = pago_repository.create(pago_data)
            if result:
                print(f"Pago guardado: {result}")
                
                # Update credito saldo
                nuevo_saldo = credito['saldo'] - valor
                credito_repository.update_saldo(credito_id, nuevo_saldo)
                print(f"Saldo actualizado: {nuevo_saldo}")
                
                # Call callback if provided
                if self.callback:
                    self.callback()
            else:
                print("Error al guardar pago")
                
        except ValueError as e:
            print(f"Error en los valores ingresados: {e}")
        except Exception as e:
            print(f"Error guardando pago: {e}")
            
        # Close dialog
        self.close()
