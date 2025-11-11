from modelo.factura import Factura
from datetime import date

facturas = []  # Lista para almacenar facturas

def crear_factura(fecha):
    factura = Factura(fecha)
    facturas.append(factura)
    return factura

def leer_facturas():
    return facturas

def buscar_factura(fecha):
    for factura in facturas:
        if factura.fecha == fecha:
            return factura
    return None

def eliminar_factura(factura):
    global facturas
    facturas = [f for f in facturas if f != factura]
    return True

def agregar_producto_control(factura, producto_control):
    factura.agregar_producto_control(producto_control)
    return True

def agregar_antibiotico(factura, antibiotico):
    factura.agregar_antibiotico(antibiotico)
    return True
