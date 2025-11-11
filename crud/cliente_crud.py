from modelo.cliente import Cliente

clientes = []  # Lista para almacenar clientes

def crear_cliente(nombre, cedula):
    cliente = Cliente(nombre, cedula)
    clientes.append(cliente)
    return cliente

def leer_clientes():
    return clientes

def buscar_cliente(cedula):
    for cliente in clientes:
        if cliente.cedula == cedula:
            return cliente
    return None

def eliminar_cliente(cedula):
    global clientes
    clientes = [c for c in clientes if c.cedula != cedula]
    return True
