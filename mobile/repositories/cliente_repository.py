"""
Cliente Repository
Handles all database operations for clientes
"""
from database.db_manager import db_manager
from database.models import Cliente
from datetime import datetime

class ClienteRepository:
    """Repository for cliente operations"""
    
    def get_all(self):
        """Get all clientes"""
        try:
            query = f"SELECT * FROM {Cliente.TABLE_NAME} ORDER BY created_at DESC"
            rows = db_manager.execute_query(query)
            return [Cliente.to_dict(row) for row in rows] if rows else []
        except Exception as e:
            print(f"Error getting all clientes: {e}")
            return []
    
    def get_by_id(self, cliente_id):
        """Get cliente by ID"""
        try:
            query = f"SELECT * FROM {Cliente.TABLE_NAME} WHERE id = ?"
            rows = db_manager.execute_query(query, (cliente_id,))
            return Cliente.to_dict(rows[0]) if rows else None
        except Exception as e:
            print(f"Error getting cliente by id: {e}")
            return None
    
    def get_by_cedula(self, cedula):
        """Get cliente by cedula"""
        try:
            query = f"SELECT * FROM {Cliente.TABLE_NAME} WHERE cedula = ?"
            rows = db_manager.execute_query(query, (cedula,))
            return Cliente.to_dict(rows[0]) if rows else None
        except Exception as e:
            print(f"Error getting cliente by cedula: {e}")
            return None
    
    def create(self, data):
        """Create a new cliente"""
        try:
            query = f"""
                INSERT INTO {Cliente.TABLE_NAME} 
                (nombre, apellido, cedula, telefono, direccion, email)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            params = (
                data.get('nombre'),
                data.get('apellido'),
                data.get('cedula'),
                data.get('telefono', ''),
                data.get('direccion', ''),
                data.get('email', '')
            )
            cliente_id = db_manager.execute_insert(query, params)
            if cliente_id:
                return self.get_by_id(cliente_id)
            return None
        except Exception as e:
            print(f"Error creating cliente: {e}")
            return None
    
    def update(self, cliente_id, data):
        """Update an existing cliente"""
        try:
            query = f"""
                UPDATE {Cliente.TABLE_NAME}
                SET nombre = ?, apellido = ?, cedula = ?, 
                    telefono = ?, direccion = ?, email = ?
                WHERE id = ?
            """
            params = (
                data.get('nombre'),
                data.get('apellido'),
                data.get('cedula'),
                data.get('telefono', ''),
                data.get('direccion', ''),
                data.get('email', ''),
                cliente_id
            )
            success = db_manager.execute_update(query, params)
            return self.get_by_id(cliente_id) if success else None
        except Exception as e:
            print(f"Error updating cliente: {e}")
            return None
    
    def delete(self, cliente_id):
        """Delete a cliente"""
        try:
            query = f"DELETE FROM {Cliente.TABLE_NAME} WHERE id = ?"
            return db_manager.execute_delete(query, (cliente_id,))
        except Exception as e:
            print(f"Error deleting cliente: {e}")
            return False
    
    def search(self, search_term):
        """Search clientes by name, apellido, or cedula"""
        try:
            query = f"""
                SELECT * FROM {Cliente.TABLE_NAME}
                WHERE nombre LIKE ? OR apellido LIKE ? OR cedula LIKE ?
                ORDER BY created_at DESC
            """
            search_pattern = f"%{search_term}%"
            rows = db_manager.execute_query(query, (search_pattern, search_pattern, search_pattern))
            return [Cliente.to_dict(row) for row in rows] if rows else []
        except Exception as e:
            print(f"Error searching clientes: {e}")
            return []

# Global instance
cliente_repository = ClienteRepository()
