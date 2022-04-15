"""
Una tienda ofrese un descuento del 15% sobre el total
y un cliente desea saber cuando deberá pagar finalmnete
por su compra
"""

precio = float(input("Ingrese su precio: "))
descuento = precio * 0.15
precio_final = precio - descuento
print(f"el prescio a pagar es ${precio_final:.2f}")