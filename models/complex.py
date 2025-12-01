from models.accommodation import Accommodation
from constants import DISCOUNT_PER_UNIT_COMPLEX, MAX_DISCOUNT_COMPLEX


class Complex(Accommodation):
    """
    Representa un complejo compuesto por varias casas.
    
    Reglas de descuento:
    - Si se alquilan todas las unidades: 10% de descuento por cada unidad
    - Descuento máximo acumulado: 50%
    - Si se alquila solo una unidad: se cobra como casa normal (sin descuento)
    """  
    
    def __init__(self, address, houses):
        """
        Inicializa un complejo.
        
        Args:
            address (str): Dirección del complejo
            houses (list): Lista de objetos House que componen el complejo
            
        Raises:
            ValueError: Si houses está vacía o contiene elementos que no son House
        """
        super().__init__(address)
        
        if len(houses) < 2:
            raise ValueError("El complejo debe tener al menos 2 casas (varias unidades)")
        
        self.houses = houses
        self.total_units = len(houses)
    
    def calculate_price(self, nights, units_to_rent=1):
        """
        Calcula el precio del complejo según las unidades alquiladas.
        
        Args:
            nights (int): Cantidad de noches
            units_to_rent (int): Cantidad de unidades a alquilar (por defecto 1)
            
        Returns:
            float: Precio total con descuentos aplicados si corresponde
        """
        if units_to_rent < 1 or units_to_rent > self.total_units:
            raise ValueError(f"Debe alquilar entre 1 y {self.total_units} unidades")
        
        if units_to_rent == 1:
            return self.houses[0].calculate_price(nights)
        
        if units_to_rent == self.total_units:
            return self._calculate_with_discount(nights, units_to_rent)
        
        total = 0
        for i in range(units_to_rent):
            total += self.houses[i].calculate_price(nights)
        return total
    
    def _calculate_with_discount(self, nights, units_to_rent):
        """
        Calcula el precio con descuento cuando se alquilan todas las unidades.
        
        Args:
            nights (int): Cantidad de noches
            units_to_rent (int): Cantidad de unidades a alquilar
            
        Returns:
            float: Precio total con descuento aplicado
        """
        base_price = sum(house.calculate_price(nights) for house in self.houses)
        
        discount_percentage = min(units_to_rent * DISCOUNT_PER_UNIT_COMPLEX, MAX_DISCOUNT_COMPLEX)
        
        final_price = base_price * (1 - discount_percentage)
        
        return final_price
    
    def get_discount_info(self, units_to_rent):
        """
        Obtiene información sobre el descuento aplicable.
        
        Args:
            units_to_rent (int): Cantidad de unidades a alquilar
            
        Returns:
            dict: Información del descuento (porcentaje y si aplica)
        """
        if units_to_rent == self.total_units:
            discount = min(units_to_rent * DISCOUNT_PER_UNIT_COMPLEX, MAX_DISCOUNT_COMPLEX)
            return {
                'applies': True,
                'percentage': discount * 100,
                'description': f'{int(discount * 100)}% de descuento'
            }
        return {
            'applies': False,
            'percentage': 0,
            'description': 'Sin descuento'
        }
    
    def __str__(self):
        return f"Complejo con {self.total_units} unidades en {self.address}"