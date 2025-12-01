from models.flight import Flight
from models.hotel import Hotel
from models.house import House
from models.complex import Complex
from models.package import Package
from models.user import User


def print_separator(title=""):
    """Imprime un separador visual"""
    if title:
        print(f"\n{'='*60}")
        print(f"  {title}")
        print(f"{'='*60}")
    else:
        print(f"{'='*60}")


def main():
    print_separator("SISTEMA DE AGENCIA DE VIAJES - DEMO")
    
    print_separator("1. CREACIÓN DE PRODUCTOS")
    
    vuelo1 = Flight("2025-01-15", "2025-01-20", "Aerolíneas Argentinas", 120000)
    vuelo2 = Flight("2025-02-10", None, "LATAM", 80000)  # Solo ida
    print(f"✓ {vuelo1}")
    print(f"  Precio: ${vuelo1.calculate_price():,.0f}")
    print(f"✓ {vuelo2}")
    print(f"  Precio: ${vuelo2.calculate_price():,.0f}")
    
    hotel1 = Hotel("Av. Corrientes 1234", "Hotel Plaza", 4)
    hotel2 = Hotel("Calle Florida 567", "Grand Hotel", 5)
    print(f"\n✓ {hotel1}")
    print(f"  Precio por 3 noches: ${hotel1.calculate_price(3):,.0f}")
    print(f"✓ {hotel2}")
    print(f"  Precio por 3 noches: ${hotel2.calculate_price(3):,.0f}")
    
    monoambiente = House("Av. Santa Fe 890", 1)
    casa_mediana = House("Calle Rivadavia 456", 3)
    casa_grande = House("Av. Libertador 789", 5)
    print(f"\n✓ {monoambiente}")
    print(f"  Precio por 2 noches: ${monoambiente.calculate_price(2):,.0f}")
    print(f"✓ {casa_mediana}")
    print(f"  Precio por 2 noches: ${casa_mediana.calculate_price(2):,.0f}")
    print(f"✓ {casa_grande}")
    print(f"  Precio por 2 noches: ${casa_grande.calculate_price(2):,.0f}")
    
    complejo = Complex("Barrio Cerrado Las Palmas", [
        House("Unidad 1", 2),
        House("Unidad 2", 3),
        House("Unidad 3", 2)
    ])
    print(f"\n✓ {complejo}")
    print(f"  Alquilar 1 casa por 5 noches: ${complejo.calculate_price(5, units_to_rent=1):,.0f}")
    print(f"  Alquilar 3 casas por 5 noches: ${complejo.calculate_price(5, units_to_rent=3):,.0f}")
    discount_info = complejo.get_discount_info(3)
    print(f"  Descuento aplicado: {discount_info['description']}")
    
    paquete = Package("Vacaciones en Buenos Aires", "Paquete todo incluido")
    paquete.add_product(vuelo1)
    paquete.add_product(hotel1)
    print(f"\n✓ {paquete}")
    print(f"  Precio total (5 noches): ${paquete.calculate_price(nights=5):,.0f}")
    
    print_separator("2. USUARIOS Y COMPRAS")
    
    user1 = User("Juan Pérez", 500000)
    user2 = User("María López", 150000)
    user3 = User("Carlos Gómez", 80000)
    
    print(f"✓ Usuario creado: {user1.name}")
    print(f"  Presupuesto inicial: ${user1.budget:,.0f}\n")
    
    print("--- Compras de Juan Pérez ---")
    user1.purchase_product(vuelo1)
    user1.purchase_product(hotel1, nights=5)
    user1.purchase_product(casa_mediana, nights=3)
    
    print(f"\nResumen de {user1.name}:")
    print(f"  Productos comprados: {len(user1.purchase_history)}")
    print(f"  Presupuesto restante: ${user1.budget:,.0f}")
    
    print(f"\n--- Compras de María López ---")
    print(f"Presupuesto inicial: ${user2.budget:,.0f}")
    user2.purchase_product(vuelo2)
    user2.purchase_product(monoambiente, nights=3)
    
    print(f"\nResumen de {user2.name}:")
    print(f"  Productos comprados: {len(user2.purchase_history)}")
    print(f"  Presupuesto restante: ${user2.budget:,.0f}")
    
    print(f"\n--- Compras de Carlos Gómez ---")
    print(f"Presupuesto inicial: ${user3.budget:,.0f}")
    user3.purchase_product(hotel2, nights=3)  
    
    print_separator("3. INTENTO DE COMPRA SIN FONDOS")
    
    usuario_pobre = User("Ana Silva", 50000)
    print(f"Usuario: {usuario_pobre.name}")
    print(f"Presupuesto: ${usuario_pobre.budget:,.0f}\n")
    
    print("Intentando comprar hotel de 5 estrellas por 7 noches...")
    hotel_caro = Hotel("5th Avenue", "Luxury Hotel", 5)
    precio_hotel = hotel_caro.calculate_price(7)
    print(f"Precio del hotel: ${precio_hotel:,.0f}")
    usuario_pobre.purchase_product(hotel_caro, nights=7)
     
    print_separator("5. RANKING DE USUARIOS POR COMPRAS")
    
    usuarios = [user1, user2, user3, usuario_pobre]
    usuarios_ordenados = sorted(usuarios, key=lambda u: len(u.purchase_history), reverse=True)
    
    print("Ranking (mayor a menor cantidad de productos):\n")
    for i, user in enumerate(usuarios_ordenados, 1):
        print(f"  {i}. {user.name:<20} - {len(user.purchase_history)} producto(s) comprado(s)")
    
    print_separator("4. BONUS - PRODUCTOS QUE PUEDE COMPRAR")

    todos_los_productos = [
        vuelo1, vuelo2,
        hotel1, hotel2,
        monoambiente, casa_mediana, casa_grande,
        complejo
    ]

    user3.show_affordable_products_max_nights(todos_los_productos)
    
    print_separator("6. RESUMEN FINAL")
    
    total_usuarios = len(usuarios)
    total_compras = sum(len(u.purchase_history) for u in usuarios)
    presupuesto_total_gastado = sum(u.initial_budget - u.budget for u in usuarios)
    
    print(f"Total de usuarios: {total_usuarios}")
    print(f"Total de compras realizadas: {total_compras}")
    print(f"Presupuesto total gastado: ${presupuesto_total_gastado:,.0f}")
    
    print_separator()
    print("✓ Demo completada exitosamente")
    print_separator()


if __name__ == "__main__":
    main()