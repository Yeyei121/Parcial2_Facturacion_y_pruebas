from datetime import date
from modelo.factura import Factura
from modelo.producto_control import ProductoControl
from modelo.antibiotico import Antibiotico

factura = Factura(date(2025, 11, 1))
p1 = ProductoControl("Producto Control X", 50000, "ICA123", 30)
a1 = Antibiotico("Antibiótico A", 75000, 500, "Bovinos")
factura.agregar_producto_control(p1)
factura.agregar_antibiotico(a1)

print("Debug aquí")
