import unittest
from modelo.cliente import Cliente
from modelo.factura import Factura
from datetime import date

class TestFacturacion(unittest.TestCase):
    def test_creacion_cliente(self):
        cliente_obj = Cliente("Pedro Gómez", "111222333")
        self.assertEqual(cliente_obj.nombre, "Pedro Gómez")
        self.assertEqual(cliente_obj.cedula, "111222333")
        self.assertEqual(len(cliente_obj.facturas), 0)

    def test_agregar_factura_a_cliente(self):
        cliente_obj = Cliente("Pedro Gómez", "111222333")
        factura_obj = Factura(date.today())
        cliente_obj.agregar_factura(factura_obj)
        self.assertEqual(len(cliente_obj.facturas), 1)
        self.assertEqual(cliente_obj.facturas[0], factura_obj)

    def test_obtener_facturas_vacias(self):
        cliente_obj = Cliente("Pedro Gómez", "111222333")
        self.assertEqual(cliente_obj.facturas, [])

    def test_agregar_varias_facturas(self):
        cliente_obj = Cliente("Pedro Gómez", "111222333")
        factura1 = Factura(date.today())
        factura2 = Factura(date.today())
        cliente_obj.agregar_factura(factura1)
        cliente_obj.agregar_factura(factura2)
        self.assertEqual(len(cliente_obj.facturas), 2)
        self.assertIn(factura1, cliente_obj.facturas)
        self.assertIn(factura2, cliente_obj.facturas)

unittest.main(argv=[''], exit=False)
