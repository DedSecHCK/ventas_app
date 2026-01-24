"""
Credito Repository
Handles all database operations for creditos
"""
from database.db_manager import db_manager
from database.models import Credito
from datetime import datetime

class CreditoRepository:
    """Repository for credito operations"""
    
    def get_all(self):
        """Get all creditos"""
        try:
            query = f"SELECT * FROM {Credito.TABLE_NAME} ORDER BY created_at DESC"
            rows = db_manager.execute_query(query)
            return [Credito.to_dict(row) for row in rows] if rows else []
        except Exception as e:
            print(f"Error getting all creditos: {e}")
            return []
    
    def get_by_id(self, credito_id):
        """Get credito by ID"""
        try:
            query = f"SELECT * FROM {Credito.TABLE_NAME} WHERE id = ?"
            rows = db_manager.execute_query(query, (credito_id,))
            return Credito.to_dict(rows[0]) if rows else None
        except Exception as e:
            print(f"Error getting credito by id: {e}")
            return None
    
    def get_by_cliente(self, cliente_id):
        """Get all creditos for a specific cliente"""
        try:
            query = f"SELECT * FROM {Credito.TABLE_NAME} WHERE cliente_id = ? ORDER BY created_at DESC"
            rows = db_manager.execute_query(query, (cliente_id,))
            return [Credito.to_dict(row) for row in rows] if rows else []
        except Exception as e:
            print(f"Error getting creditos by cliente: {e}")
            return []
    
    def create(self, data):
        """Create a new credito"""
        try:
            # Use current date if not provided
            fecha = data.get('fecha', datetime.now().strftime('%Y-%m-%d'))
            
            query = f"""
                INSERT INTO {Credito.TABLE_NAME}
                (cliente_id, fecha, monto, plazo, tasa_interes, saldo)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            params = (
                data.get('cliente_id'),
                fecha,
                data.get('monto'),
                data.get('plazo'),
                data.get('tasa_interes'),
                data.get('saldo', data.get('monto'))  # Default saldo = monto
            )
            credito_id = db_manager.execute_insert(query, params)
            if credito_id:
                return self.get_by_id(credito_id)
            return None
        except Exception as e:
            print(f"Error creating credito: {e}")
            return None
    
    def update(self, credito_id, data):
        """Update an existing credito"""
        try:
            query = f"""
                UPDATE {Credito.TABLE_NAME}
                SET cliente_id = ?, fecha = ?, monto = ?, 
                    plazo = ?, tasa_interes = ?, saldo = ?
                WHERE id = ?
            """
            params = (
                data.get('cliente_id'),
                data.get('fecha'),
                data.get('monto'),
                data.get('plazo'),
                data.get('tasa_interes'),
                data.get('saldo'),
                credito_id
            )
            success = db_manager.execute_update(query, params)
            return self.get_by_id(credito_id) if success else None
        except Exception as e:
            print(f"Error updating credito: {e}")
            return None
    
    def update_saldo(self, credito_id, nuevo_saldo):
        """Update only the saldo of a credito"""
        try:
            query = f"UPDATE {Credito.TABLE_NAME} SET saldo = ? WHERE id = ?"
            return db_manager.execute_update(query, (nuevo_saldo, credito_id))
        except Exception as e:
            print(f"Error updating saldo: {e}")
            return False
    
    def delete(self, credito_id):
        """Delete a credito"""
        try:
            query = f"DELETE FROM {Credito.TABLE_NAME} WHERE id = ?"
            return db_manager.execute_delete(query, (credito_id,))
        except Exception as e:
            print(f"Error deleting credito: {e}")
            return False

# Global instance
credito_repository = CreditoRepository()
