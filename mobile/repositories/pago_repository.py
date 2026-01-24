"""
Pago Repository
Handles all database operations for pagos
"""
from database.db_manager import db_manager
from database.models import Pago
from datetime import datetime

class PagoRepository:
    """Repository for pago operations"""
    
    def get_all(self):
        """Get all pagos"""
        try:
            query = f"SELECT * FROM {Pago.TABLE_NAME} ORDER BY created_at DESC"
            rows = db_manager.execute_query(query)
            return [Pago.to_dict(row) for row in rows] if rows else []
        except Exception as e:
            print(f"Error getting all pagos: {e}")
            return []
    
    def get_by_id(self, pago_id):
        """Get pago by ID"""
        try:
            query = f"SELECT * FROM {Pago.TABLE_NAME} WHERE id = ?"
            rows = db_manager.execute_query(query, (pago_id,))
            return Pago.to_dict(rows[0]) if rows else None
        except Exception as e:
            print(f"Error getting pago by id: {e}")
            return None
    
    def get_by_credito(self, credito_id):
        """Get all pagos for a specific credito"""
        try:
            query = f"SELECT * FROM {Pago.TABLE_NAME} WHERE credito_id = ? ORDER BY created_at DESC"
            rows = db_manager.execute_query(query, (credito_id,))
            return [Pago.to_dict(row) for row in rows] if rows else []
        except Exception as e:
            print(f"Error getting pagos by credito: {e}")
            return []
    
    def create(self, data):
        """Create a new pago"""
        try:
            # Use current date if not provided
            fecha = data.get('fecha', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            
            query = f"""
                INSERT INTO {Pago.TABLE_NAME}
                (credito_id, fecha, valor, lat, lon)
                VALUES (?, ?, ?, ?, ?)
            """
            params = (
                data.get('credito_id'),
                fecha,
                data.get('valor'),
                data.get('lat', 0.0),
                data.get('lon', 0.0)
            )
            pago_id = db_manager.execute_insert(query, params)
            if pago_id:
                return self.get_by_id(pago_id)
            return None
        except Exception as e:
            print(f"Error creating pago: {e}")
            return None
    
    def delete(self, pago_id):
        """Delete a pago"""
        try:
            query = f"DELETE FROM {Pago.TABLE_NAME} WHERE id = ?"
            return db_manager.execute_delete(query, (pago_id,))
        except Exception as e:
            print(f"Error deleting pago: {e}")
            return False
    
    def get_total_by_credito(self, credito_id):
        """Get total amount paid for a credito"""
        try:
            query = f"SELECT SUM(valor) as total FROM {Pago.TABLE_NAME} WHERE credito_id = ?"
            rows = db_manager.execute_query(query, (credito_id,))
            if rows and rows[0]['total']:
                return float(rows[0]['total'])
            return 0.0
        except Exception as e:
            print(f"Error getting total pagos: {e}")
            return 0.0

# Global instance
pago_repository = PagoRepository()
