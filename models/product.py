from abc import ABC, abstractmethod


class Product(ABC):
    """
    Clase abstracta base para todos los productos de la agencia.
    """
    
    @abstractmethod
    def calculate_price(self):
        """
        Calcula y retorna el precio del producto.
        """
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__}"