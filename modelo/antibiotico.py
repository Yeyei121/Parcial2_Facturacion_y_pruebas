# modelo/antibiotico.py
class Antibiotico:
    def __init__(self, nombre, precio, dosis, tipo_animal):
        self.__nombre = nombre
        self.__precio = precio
        self.__dosis = dosis
        self.__tipo_animal = tipo_animal

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
    def dosis(self):
        return self.__dosis

    @dosis.setter
    def dosis(self, dosis):
        self.__dosis = dosis

    @property
    def tipo_animal(self):
        return self.__tipo_animal

    @tipo_animal.setter
    def tipo_animal(self, tipo_animal):
        self.__tipo_animal = tipo_animal

    def __str__(self):
        return f"{self.__nombre} - ${self.__precio:.2f} | Dosis: {self.__dosis}kg | Animal: {self.__tipo_animal}"
