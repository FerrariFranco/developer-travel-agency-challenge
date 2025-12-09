from models.product import Product


class Package(Product):
    """
    Representa un paquete turístico compuesto por múltiples productos.
    Puede contener vuelos, alojamientos e incluso otros paquetes.
    El precio total es la suma de todos los productos incluidos.
    """
    
    def __init__(self, name, description=""):
        """
        Inicializa un paquete.
        
        Args:
            name (str): Nombre del paquete
            description (str): Descripción opcional del paquete
        """
        self.name = name
        self.description = description
        self.products = []
    
    def add_product(self, product):
        """
        Agrega un producto al paquete.
        
        Args:
            product (Product): Producto a agregar (Flight, Accommodation, Package, etc.)
            
        Raises:
            TypeError: Si el producto no es una instancia de Product
        """
        if not isinstance(product, Product):
            raise TypeError(f"Solo se pueden agregar productos. Recibido: {type(product).__name__}")
        
        self.products.append(product)
    
    def remove_product(self, product):
        """
        Remueve un producto del paquete.
        
        Args:
            product (Product): Producto a remover
            
        Returns:
            bool: True si se removió, False si no estaba en el paquete
        """
        try:
            self.products.remove(product)
            return True
        except ValueError:
            return False
    
    def calculate_price(self, **kwargs):
        """
        Calcula el precio total del paquete.
        Es la suma de los precios de todos los productos incluidos.
        
        Args:
            **kwargs: Parámetros variables que se pueden pasar a productos específicos
                     (por ejemplo, nights para alojamientos)
        
        Returns:
            float: Precio total del paquete
            
        Note:
            Para alojamientos, debes especificar 'nights' en kwargs.
            Ejemplo: package.calculate_price(nights=5)
        """
        total = 0
        
        for product in self.products:
            if hasattr(product, 'airline'):
                total += product.calculate_price()
            elif hasattr(product, 'address'): 
                nights = kwargs.get('nights', 1)
                total += product.calculate_price(nights)
            elif isinstance(product, Package):
                total += product.calculate_price(**kwargs)
            else:
                total += product.calculate_price()
        
        return total
    
    def __str__(self):
        products_summary = f"{len(self.products)} producto(s)"
        if self.description:
            return f"Paquete '{self.name}': {self.description} - {products_summary}"
        return f"Paquete '{self.name}' - {products_summary}"