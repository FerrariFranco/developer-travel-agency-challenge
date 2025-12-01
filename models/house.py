from models.accommodation import Accommodation


class House(Accommodation):
    """
    Representa una casa o departamento.
    Precios por noche:
    - Monoambiente (1): $15,000
    - Entre 2 y 4 ambientes: $30,000
    - Más de 4 ambientes: $50,000
    """
    
    def __init__(self, address, rooms):
        """
        Inicializa una casa.
        
        Args:
            address (str): Dirección de la casa
            rooms (int): Cantidad de ambientes
        """
        super().__init__(address)
        self.rooms = rooms
    
    def calculate_price(self, nights):
        """
        Calcula el precio de la casa según cantidad de ambientes y noches.
        
        Args:
            nights (int): Cantidad de noches
            
        Returns:
            float: Precio total de la casa
        """
        price_per_night = self._get_price_per_night()
        return price_per_night * nights
    
    def _get_price_per_night(self):
        """
        Determina el precio por noche según la cantidad de ambientes.
        
        Returns:
            int: Precio por noche
        """
        if self.rooms == 1:
            return 15000 
        elif 2 <= self.rooms <= 4:
            return 30000 
        else: 
            return 50000
    
    def __str__(self):
        room_type = "Monoambiente" if self.rooms == 1 else f"Casa de {self.rooms} ambientes"
        return f"{room_type} en {self.address}"