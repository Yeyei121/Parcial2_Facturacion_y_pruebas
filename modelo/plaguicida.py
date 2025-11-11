# modelo/plaguicida.py
from modelo.producto_control import ProductoControl

class Plaguicida(ProductoControl):
    def __init__(self, nombre, precio, registro_ICA, frecuencia_aplicacion, periodo_carencia):
        super().__init__(nombre, precio, registro_ICA, frecuencia_aplicacion)
        self.__periodo_carencia = periodo_carencia

    @property
    def periodo_carencia(self):
        return self.__periodo_carencia

    @periodo_carencia.setter
    def periodo_carencia(self, periodo_carencia):
        self.__periodo_carencia = periodo_carencia

    def __str__(self):
        return f"{super().__str__()} | Carencia: {self.__periodo_carencia} días"
