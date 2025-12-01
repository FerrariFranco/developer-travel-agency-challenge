# Agencia de Viajes — Sistema OOP en Python

Sistema simple de Programación Orientada a Objetos para gestionar productos turísticos y compras de usuarios.

---

## Ejecución

Requisitos: Python 3.7+

    python main.py

o

    python3 main.py

---

## Estructura del Proyecto

product.py          # Producto base (abstracto)

flight.py           # Vuelos

accommodation.py    # Alojamiento base (abstracto)

hotel.py            # Hotel

house.py            # Casa/Departamento

complex.py          # Complejo de casas

package.py          # Paquete turístico

user.py             # Usuarios y compras



main.py


---

## Diseño y Responsabilidades

Product (abstracto)
- Define la interfaz común para todos los productos.
- Obliga a implementar `calculate_price()` en subclases.

Flight / Hotel / House / Complex
- Cada clase representa un producto concreto.
- Calculan su precio según sus propias reglas.
- `Accommodation` agrupa la lógica común para alojamientos.

Package
- Implementa composición de múltiples productos.
- Calcula el precio como suma de los productos incluidos.

User
- Gestiona presupuesto, historial de compras y validaciones.
- Controla si una compra puede realizarse según fondos.
