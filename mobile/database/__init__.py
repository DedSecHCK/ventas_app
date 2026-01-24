"""
Database package initialization
"""
from .db_manager import db_manager
from .models import Cliente, Credito, Pago

__all__ = ['db_manager', 'Cliente', 'Credito', 'Pago']
