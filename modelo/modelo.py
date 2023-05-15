import json
from abc import ABC


class Usuario(ABC):
    def __init__(self, nombre, numero_id, contrasena, cargo):
        self.nombre: str = nombre
        self.numero_id: int = numero_id
        self.contrasena: str = contrasena
        self.cargo: str = cargo


class Administrador(Usuario):

    def __init__(self, nombre, numero_id, contrasena):
        super().__init__(nombre, numero_id, contrasena, 'adminsitrador')


class Vendedor(Usuario):

    def __init__(self, nombre, numero_id, contrasena):
        super().__init__(nombre, numero_id, contrasena, 'vendedor')


class EncargadoBodega(Usuario):

    def __init__(self, nombre, numero_id, contrasena):
        super().__init__(nombre, numero_id, contrasena, 'Encargadobodega')


class Factura:

    def __init__(self, id_producto, cantidad):
        self.id_producto: int = id_producto
        self.cantidad: int = cantidad


class Categoria:

    def __init__(self, nombre_categoria, precio_base):
        self.nombre_categoria: str = nombre_categoria
        self.precio_base: float = precio_base


class Producto:

    def __init__(self, id_producto, cantidad, categoria):
        pass


facturas = []


def crear_factura():
    cantidad = float(input("Ingrese la cantidad de producto"))
    id_producto = None
    factura = Factura()
