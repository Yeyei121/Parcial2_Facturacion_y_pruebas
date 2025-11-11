# modelo/producto_control.py
class ProductoControl:
    def __init__(self, nombre, precio, registro_ICA, frecuencia_aplicacion):
        self.__nombre = nombre
        self.__precio = precio
        self.__registro_ICA = registro_ICA
        self.__frecuencia_aplicacion = frecuencia_aplicacion

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def registro_ICA(self):
        return self.__registro_ICA

    @registro_ICA.setter
    def registro_ICA(self, registro_ICA):
        self.__registro_ICA = registro_ICA

    @property
    def frecuencia_aplicacion(self):
        return self.__frecuencia_aplicacion

    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, frecuencia_aplicacion):
        self.__frecuencia_aplicacion = frecuencia_aplicacion

    def __str__(self):
        return f"{self.__nombre} - ${self.__precio:.2f} | ICA: {self.__registro_ICA} | Frecuencia: {self.__frecuencia_aplicacion} días"
