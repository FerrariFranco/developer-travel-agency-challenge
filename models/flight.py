from datetime import datetime
from models.product import Product


class Flight(Product):
    """
    Representa un vuelo con información de fechas y aerolínea.
    """
    
    def __init__(self, departure_date, return_date, airline, price):
        """
        Inicializa un vuelo.
        
        Args:
            departure_date (str): Fecha de salida en formato 'YYYY-MM-DD'
            return_date (str): Fecha de regreso en formato 'YYYY-MM-DD' o None para solo ida
            airline (str): Nombre de la aerolínea
            price (float): Precio del vuelo
        """
        self.departure_date = departure_date
        self.return_date = return_date
        self.airline = airline
        self.price = price
    
    def calculate_price(self):
        """
        Calcula el precio del vuelo.
        
        Returns:
            float: Precio del vuelo
        """
        return self.price
    
    def is_round_trip(self):
        """
        Verifica si es un vuelo de ida y vuelta.
        
        Returns:
            bool: True si tiene fecha de regreso, False si es solo ida
        """
        return self.return_date is not None
    
    def __str__(self):
        trip_type = "ida y vuelta" if self.is_round_trip() else "solo ida"
        if self.return_date:
            return f"Vuelo {self.airline} ({self.departure_date} - {self.return_date}) - {trip_type}"
        else:
            return f"Vuelo {self.airline} ({self.departure_date}) - {trip_type}"