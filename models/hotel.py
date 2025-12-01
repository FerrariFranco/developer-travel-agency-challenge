from models.accommodation import Accommodation
from constants import PRICE_PER_HOTEL_STAR

class Hotel(Accommodation):
    """
    Representa un hotel con nombre y clasificación por estrellas.
    """
    
    def __init__(self, address, name, stars):
        """
        Inicializa un hotel.
        
        Args:
            address (str): Dirección del hotel
            name (str): Nombre del hotel
            stars (int): Clasificación por estrellas (1-5)
        """
        super().__init__(address)
        self.name = name
        self.stars = stars
    
    def calculate_price(self, nights):
        """
        Calcula el precio del hotel.
        Fórmula: estrellas * $10,000 * noches
        
        Args:
            nights (int): Cantidad de noches
            
        Returns:
            float: Precio total del hotel
        """
        return self.stars * PRICE_PER_HOTEL_STAR * nights
    
    def __str__(self):
        return f"Hotel {self.name} ({self.stars}★) en {self.address}"