from abc import abstractmethod
from models.product import Product


class Accommodation(Product):
    """
    Clase base abstracta para todos los tipos de alojamiento.
    """
    
    def __init__(self, address):
        """
        Inicializa un alojamiento.
        
        Args:
            address (str): Dirección del alojamiento
        """
        self.address = address
    
    @abstractmethod
    def calculate_price(self, nights):
        """
        Calcula el precio del alojamiento según la cantidad de noches.
        
        Args:
            nights (int): Cantidad de noches
            
        Returns:
            float: Precio total del alojamiento
        """
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} en {self.address}"