# modelo/factura.py
from datetime import date
from modelo.producto_control import ProductoControl
from modelo.antibiotico import Antibiotico


class Factura:
    def __init__(self, fecha):
        self.__fecha = fecha
        self.__productos_control = []  # Lista para productos de control
        self.__antibioticos = []  # Lista para antibióticos
        self.__valor_total = 0.0

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def productos_control(self):
        return self.__productos_control

    @productos_control.setter
    def productos_control(self, productos_control):
        self.__productos_control = productos_control

    @property
    def antibioticos(self):
        return self.__antibioticos

    @antibioticos.setter
    def antibioticos(self, antibioticos):
        self.__antibioticos = antibioticos

    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor_total):
        self.__valor_total = valor_total

    def agregar_producto_control(self, producto):
        self.__productos_control.append(producto)
        self.__valor_total += producto.precio

    def agregar_antibiotico(self, antibiotico):
        self.__antibioticos.append(antibiotico)
        self.__valor_total += antibiotico.precio

    def mostrar_productos(self):
        return self.__productos_control + self.__antibioticos

    def calcular_total(self):
        return self.__valor_total

    def __str__(self):
        total_productos = len(self.__productos_control) + len(self.__antibioticos)
        return f"Factura del {self.__fecha} - Total: ${self.__valor_total:.2f} - {total_productos} productos"
