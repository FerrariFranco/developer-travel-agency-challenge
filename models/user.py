from models.product import Product


class User:
    """
    Representa un usuario de la agencia con presupuesto e historial de compras.
    """
    
    def __init__(self, name, budget):
        """
        Inicializa un usuario.
        
        Args:
            name (str): Nombre del usuario
            budget (float): Presupuesto inicial del usuario
        """
        self.name = name
        self.budget = budget
        self.initial_budget = budget  # Para tracking
        self.purchase_history = []
    
    def purchase_product(self, product, **kwargs):
        """
        Intenta comprar un producto.
        
        Args:
            product (Product): Producto a comprar
            **kwargs: Parámetros adicionales (ej: nights para alojamientos)
            
        Returns:
            bool: True si la compra fue exitosa, False si no hay fondos suficientes
        """
        # Validar que sea un Product
        if not isinstance(product, Product):
            print(f"✗ Error: {type(product).__name__} no es un producto válido")
            return False
        
        # Calcular precio según el tipo de producto
        try:
            # Si el producto necesita parámetros (como nights para alojamientos)
            if kwargs:
                price = product.calculate_price(**kwargs)
            else:
                price = product.calculate_price()
        except TypeError:
            # Si faltaron parámetros necesarios
            print(f"✗ Error: El producto requiere parámetros adicionales (ej: nights)")
            return False
        
        # Verificar si hay fondos suficientes
        if price <= self.budget:
            self.budget -= price
            self.purchase_history.append({
                'product': product,
                'price': price,
                'params': kwargs
            })
            print(f"✓ Compra exitosa: {product}")
            print(f"  Precio: ${price:,.0f}")
            print(f"  Presupuesto restante: ${self.budget:,.0f}")
            return True
        else:
            print(f"✗ Fondos insuficientes para comprar: {product}")
            print(f"  Precio: ${price:,.0f}")
            print(f"  Presupuesto disponible: ${self.budget:,.0f}")
            print(f"  Faltante: ${price - self.budget:,.0f}")
            return False
    
    def get_total_spent(self):
        """
        Calcula el total gastado por el usuario.
        
        Returns:
            float: Total gastado
        """
        return self.initial_budget - self.budget
    
    def get_purchase_count(self):
        """
        Retorna la cantidad de productos comprados.
        
        Returns:
            int: Cantidad de productos en el historial
        """
        return len(self.purchase_history)
    
    def can_afford(self, product, **kwargs):
        """
        Verifica si el usuario puede pagar un producto sin comprarlo.
        
        Args:
            product (Product): Producto a verificar
            **kwargs: Parámetros adicionales
            
        Returns:
            bool: True si puede pagarlo, False si no
        """
        try:
            if kwargs:
                price = product.calculate_price(**kwargs)
            else:
                price = product.calculate_price()
            return price <= self.budget
        except:
            return False
        
    def calculate_max_nights(self, accommodation):
        """Calcula el máximo de noches que puede pagar"""
        from models.complex import Complex
        
        if isinstance(accommodation, Complex):
            price_per_night = accommodation.calculate_price(1, units_to_rent=1)
        else:
            price_per_night = accommodation.calculate_price(1)
        
        if price_per_night > self.budget:
            return 0
        
        return int(self.budget // price_per_night)

    def show_affordable_products_max_nights(self, products):
        """Muestra productos con el máximo de noches para alojamientos"""
        from models.accommodation import Accommodation
        from models.complex import Complex
        
        print(f"Usuario: {self.name}")
        print(f"Presupuesto disponible: ${self.budget:,.0f}\n")
        print("Productos que puede comprar:")
        
        count = 0
        
        for product in products:
            if isinstance(product, Accommodation):
                max_nights = self.calculate_max_nights(product)
                
                if max_nights > 0:
                    if isinstance(product, Complex):
                        price = product.calculate_price(max_nights, units_to_rent=1)
                    else:
                        price = product.calculate_price(max_nights)
                    
                    print(f"  ✓ {product} (hasta {max_nights} noches) - ${price:,.0f}")
                    count += 1
            else:
                price = product.calculate_price()
                
                if price <= self.budget:
                    print(f"  ✓ {product} - ${price:,.0f}")
                    count += 1
        
        if count == 0:
            print("  ⚠ No hay productos disponibles con tu presupuesto actual")
        
        print(f"\nTotal de productos disponibles: {count}")
        return count
    
    def __str__(self):
        return f"Usuario: {self.name} - Presupuesto: ${self.budget:,.0f} - Compras: {len(self.purchase_history)}"