"""
Repositories package initialization
"""
from .cliente_repository import cliente_repository
from .credito_repository import credito_repository
from .pago_repository import pago_repository

__all__ = ['cliente_repository', 'credito_repository', 'pago_repository']
