# modelo/fertilizante.py
from modelo.producto_control import ProductoControl
from datetime import date

class Fertilizante(ProductoControl):
    def __init__(self, nombre, precio, registro_ICA, frecuencia_aplicacion, fecha_ultima_aplicacion):
        super().__init__(nombre, precio, registro_ICA, frecuencia_aplicacion)
        self.__fecha_ultima_aplicacion = fecha_ultima_aplicacion

    @property
    def fecha_ultima_aplicacion(self):
        return self.__fecha_ultima_aplicacion

    @fecha_ultima_aplicacion.setter
    def fecha_ultima_aplicacion(self, fecha_ultima_aplicacion):
        self.__fecha_ultima_aplicacion = fecha_ultima_aplicacion

    def __str__(self):
        return f"{super().__str__()} | Última aplicación: {self.__fecha_ultima_aplicacion}"
