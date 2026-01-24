"""
Database Models
Defines the structure of database tables
"""

class Cliente:
    """Cliente model"""
    TABLE_NAME = "clientes"
    
    @staticmethod
    def to_dict(row):
        """Convert database row to dictionary"""
        if row is None:
            return None
        return {
            'id': row['id'],
            'nombre': row['nombre'],
            'apellido': row['apellido'],
            'cedula': row['cedula'],
            'telefono': row['telefono'],
            'direccion': row['direccion'],
            'email': row['email'],
            'created_at': row['created_at']
        }

class Credito:
    """Credito model"""
    TABLE_NAME = "creditos"
    
    @staticmethod
    def to_dict(row):
        """Convert database row to dictionary"""
        if row is None:
            return None
        return {
            'id': row['id'],
            'cliente_id': row['cliente_id'],
            'fecha': row['fecha'],
            'monto': row['monto'],
            'plazo': row['plazo'],
            'tasa_interes': row['tasa_interes'],
            'saldo': row['saldo'],
            'created_at': row['created_at']
        }

class Pago:
    """Pago model"""
    TABLE_NAME = "pagos"
    
    @staticmethod
    def to_dict(row):
        """Convert database row to dictionary"""
        if row is None:
            return None
        return {
            'id': row['id'],
            'credito_id': row['credito_id'],
            'fecha': row['fecha'],
            'valor': row['valor'],
            'lat': row['lat'],
            'lon': row['lon'],
            'created_at': row['created_at']
        }
