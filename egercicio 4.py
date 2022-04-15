"""hace un programa para ingresar el radio de un
circulo y se reporte su area y la longitud
de la circuferencia

área = π * r²
longitud = 2 * π * r

"""

r = float(input("radio: "))

area = 3.14 * r**2
longitud = 2 * 3.14 * r

print(f"El area del circulo es {area:.2f} y la logitud es {longitud:.2f}")
