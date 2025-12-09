from constants import PRICE_HOUSE_TWO_TO_FOUR_ROOMS
import pytest
from models.flight import Flight
from models.hotel import Hotel
from models.house import House
from models.complex import Complex
from models.package import Package
from models.user import User


class TestFlight:
    """Pruebas para la clase Flight"""

    def test_flight_creation_round_trip(self):
        """Verifica la creación de un vuelo de ida y vuelta"""
        flight = Flight("2025-01-15", "2025-01-20", "Aerolíneas Argentinas", 120000)
        assert flight.departure_date == "2025-01-15"
        assert flight.return_date == "2025-01-20"
        assert flight.airline == "Aerolíneas Argentinas"
        assert flight.price == 120000

    def test_flight_creation_one_way(self):
        """Verifica la creación de un vuelo solo de ida"""
        flight = Flight("2025-02-10", None, "LATAM", 80000)
        assert flight.return_date is None
        assert flight.calculate_price() == 80000

    def test_flight_price_calculation(self):
        """Verifica el cálculo del precio del vuelo"""
        flight = Flight("2025-01-15", "2025-01-20", "Aerolíneas Argentinas", 120000)
        assert flight.calculate_price() == 120000


class TestHotel:
    """Pruebas para la clase Hotel"""

    def test_hotel_creation(self):
        """Verifica la creación de un hotel"""
        hotel = Hotel("Av. Corrientes 1234", "Hotel Plaza", 4)
        assert hotel.address == "Av. Corrientes 1234"
        assert hotel.name == "Hotel Plaza"
        assert hotel.stars == 4

    def test_hotel_price_calculation_4_stars(self):
        """Verifica el cálculo del precio para un hotel de 4 estrellas"""
        hotel = Hotel("Av. Corrientes 1234", "Hotel Plaza", 4)
        assert hotel.calculate_price(3) == 120000


class TestHouse:
    """Pruebas para la clase House"""

    def test_house_creation_studio(self):
        """Verifica la creación de un monoambiente"""
        house = House("Av. Santa Fe 890", 1)
        assert house.address == "Av. Santa Fe 890"
        assert house.rooms == 1

    def test_house_creation_multiple_rooms(self):
        """Verifica la creación de casas con múltiples habitaciones"""
        house = House("Calle Rivadavia 456", 3)
        assert house.rooms == 3
        assert house.calculate_price(1) == PRICE_HOUSE_TWO_TO_FOUR_ROOMS

    def test_house_price_increases_with_rooms(self):
        """Verifica que el precio aumente con más habitaciones"""
        small = House("Address 1", 1)
        medium = House("Address 2", 3)
        large = House("Address 3", 5)

        assert small.calculate_price(2) < medium.calculate_price(2)
        assert medium.calculate_price(2) < large.calculate_price(2)


class TestComplex:
    """Pruebas para la clase Complex"""

    def test_complex_creation(self):
        """Verifica la creación de un complejo"""
        complex_obj = Complex("Barrio Privado Las Palmas", [
            House("Unit 1", 2),
            House("Unit 2", 3),
            House("Unit 3", 2)
        ])
        assert complex_obj.address == "Barrio Privado Las Palmas"
        assert len(complex_obj.houses) == 3

    def test_complex_price_one_unit(self):
        """Verifica el precio de alquilar una sola unidad"""
        complex_obj = Complex("Test Complex", [
            House("Unit 1", 2),
            House("Unit 2", 3)
        ])
        price = complex_obj.calculate_price(5, 2)
        assert price > 0
        assert price == 240000

    def test_complex_price_multiple_units(self):
        """Verifica el precio de alquilar múltiples unidades"""
        complex_obj = Complex("Test Complex", [
            House("Unit 1", 2),
            House("Unit 2", 3),
            House("Unit 3", 2)
        ])
        price_one = complex_obj.calculate_price(5, 1)
        price_three = complex_obj.calculate_price(5, 3)
        assert price_three > price_one

    def test_complex_max_discount(self):
        """Verifica la aplicación del descuento máximo"""
        complex_obj = Complex("Test Complex", [
            House("Unit 1", 2),
            House("Unit 2", 2),
            House("Unit 3", 2),
            House("Unit 4", 2),
            House("Unit 5", 2),
            House("Unit 6", 2)
        ])
        price = complex_obj.calculate_price(1, 6)
        assert price == 90000


class TestPackage:
    """Pruebas para la clase Package"""

    def test_package_creation(self):
        """Verifica la creación de un paquete"""
        package = Package("Vacaciones en Buenos Aires", "Paquete todo incluido")
        assert package.name == "Vacaciones en Buenos Aires"
        assert package.description == "Paquete todo incluido"

    def test_package_add_products(self):
        """Verifica agregar productos al paquete"""
        package = Package("Test Package", "Description")
        flight = Flight("2025-01-15", "2025-01-20", "Test Airline", 100000)
        hotel = Hotel("Test Address", "Test Hotel", 4)

        package.add_product(flight)
        package.add_product(hotel)

        assert len(package.products) == 2

    def test_package_price_calculation(self):
        """Verifica el cálculo del precio del paquete"""
        package = Package("Test Package", "Description")
        flight = Flight("2025-01-15", "2025-01-20", "Test Airline", 100000)
        hotel = Hotel("Test Address", "Test Hotel", 4)

        package.add_product(flight)
        package.add_product(hotel)

        total_price = package.calculate_price(nights=5)
        assert total_price > 0
        assert total_price == 300000


class TestUser:
    """Pruebas para la clase User"""

    def test_user_creation(self):
        """Verifica la creación de un usuario"""
        user = User("Juan Pérez", 500000)
        assert user.name == "Juan Pérez"
        assert user.budget == 500000
        assert user.initial_budget == 500000

    def test_user_purchase_successful(self):
        """Verifica una compra exitosa"""
        user = User("Test User", 500000)
        flight = Flight("2025-01-15", "2025-01-20", "Test Airline", 100000)

        user.purchase_product(flight)

        assert len(user.purchase_history) == 1
        assert user.budget < user.initial_budget
        assert user.budget == 400000

    def test_user_purchase_insufficient_funds(self):
        """Verifica el escenario de fondos insuficientes"""
        user = User("Poor User", 50000)
        expensive_hotel = Hotel("5th Avenue", "Luxury Hotel", 5)
        user.purchase_product(expensive_hotel, nights=7)

        assert user.budget == user.initial_budget
        assert len(user.purchase_history) == 0

    def test_user_multiple_purchases(self):
        """Verifica múltiples compras"""
        user = User("Rich User", 1000000)

        flight = Flight("2025-01-15", "2025-01-20", "Test Airline", 100000)
        hotel = Hotel("Test Address", "Test Hotel", 4)
        house = House("Test House", 2)

        user.purchase_product(flight)
        user.purchase_product(hotel, nights=3)
        user.purchase_product(house, nights=2)

        assert len(user.purchase_history) == 3
        assert user.budget < 1000000

    def test_user_show_affordable_products(self):
        """Verifica la lista de productos accesibles según el presupuesto"""
        user = User("Test User", 200000)

        products = [
            Flight("2025-01-15", "2025-01-20", "Test Airline", 100000),
            Hotel("Test Address", "Test Hotel", 5),
            House("Test House", 2)
        ]

        user.show_affordable_products_max_nights(products)


class TestUserRanking:
    """Pruebas para el ranking de usuarios"""

    def test_user_ranking_by_purchases(self):
        """Verifica el orden de usuarios según cantidad de compras"""
        user1 = User("User 1", 500000)
        user2 = User("User 2", 500000)
        user3 = User("User 3", 500000)

        for _ in range(3):
            user1.purchase_product(Flight("2025-01-15", None, "Test", 50000))

        user2.purchase_product(Flight("2025-01-15", None, "Test", 50000))

        users = [user1, user2, user3]
        sorted_users = sorted(users, key=lambda u: len(u.purchase_history), reverse=True)

        assert sorted_users[0].name == "User 1"
        assert sorted_users[1].name == "User 2"
        assert sorted_users[2].name == "User 3"
