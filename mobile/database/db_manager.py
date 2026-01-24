"""
Database Manager for Ventas App
Handles SQLite database connection and table creation
"""
import sqlite3
import os
from kivy.utils import platform

class DatabaseManager:
    """Manages SQLite database connection and operations"""
    
    def __init__(self, db_name="ventas.db"):
        self.db_name = db_name
        self.db_path = self._get_db_path()
        self.connection = None
        self.cursor = None
        
    def _get_db_path(self):
        """Get the appropriate database path based on platform"""
        if platform == 'android':
            from android.storage import app_storage_path
            # Store in app's internal storage
            db_dir = app_storage_path()
            db_path = os.path.join(db_dir, self.db_name)
        else:
            # For desktop testing
            db_path = self.db_name
            
        return db_path
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row  # Return rows as dictionaries
            self.cursor = self.connection.cursor()
            print(f"Database connected: {self.db_path}")
            return True
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return False
    
    def disconnect(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            print("Database disconnected")
    
    def create_tables(self):
        """Create all necessary tables"""
        try:
            # Clientes table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS clientes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    cedula TEXT UNIQUE NOT NULL,
                    telefono TEXT,
                    direccion TEXT,
                    email TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Creditos table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS creditos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_id INTEGER NOT NULL,
                    fecha TEXT NOT NULL,
                    monto REAL NOT NULL,
                    plazo INTEGER NOT NULL,
                    tasa_interes REAL NOT NULL,
                    saldo REAL NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (cliente_id) REFERENCES clientes (id) ON DELETE CASCADE
                )
            ''')
            
            # Pagos table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS pagos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    credito_id INTEGER NOT NULL,
                    fecha TEXT NOT NULL,
                    valor REAL NOT NULL,
                    lat REAL,
                    lon REAL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (credito_id) REFERENCES creditos (id) ON DELETE CASCADE
                )
            ''')
            
            self.connection.commit()
            print("Tables created successfully")
            return True
        except Exception as e:
            print(f"Error creating tables: {e}")
            return False
    
    def execute_query(self, query, params=None):
        """Execute a query and return results"""
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error executing query: {e}")
            return None
    
    def execute_insert(self, query, params):
        """Execute an insert query and return the last row id"""
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(f"Error executing insert: {e}")
            self.connection.rollback()
            return None
    
    def execute_update(self, query, params):
        """Execute an update query"""
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error executing update: {e}")
            self.connection.rollback()
            return False
    
    def execute_delete(self, query, params):
        """Execute a delete query"""
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error executing delete: {e}")
            self.connection.rollback()
            return False

# Global database instance
db_manager = DatabaseManager()
