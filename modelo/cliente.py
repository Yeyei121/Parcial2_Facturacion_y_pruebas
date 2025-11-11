# modelo/cliente.py
from modelo.factura import Factura

class Cliente:
    def __init__(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__facturas = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, cedula):
        self.__cedula = cedula

    @property
    def facturas(self):
        return self.__facturas

    @facturas.setter
    def facturas(self, facturas):
        self.__facturas = facturas

    def agregar_factura(self, factura):
        self.__facturas.append(factura)

    def __str__(self):
        return f"Cliente(nombre='{self.__nombre}', cedula='{self.__cedula}', facturas={len(self.__facturas)})"
