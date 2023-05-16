import json
from abc import ABC, abstractmethod


class Usuario(ABC):
    def __init__(self, nombre, numero_id, contrasena, cargo):
        self.nombre: str = nombre
        self.numero_id: str = numero_id
        self.contrasena: str = contrasena
        self.cargo: str = cargo

    @abstractmethod
    def iniciar_sesion(self, numero_id, contrasena):
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for linea in datos:
                if linea["numero_id"] == numero_id and linea["contrasena"] == contrasena:
                    print("Inicio de sesión exitoso")
                    return  # Si encuentra una coincidencia, termina la función aquí
            # Si llega hasta aquí, significa que no encontró ninguna coincidencia
            print("El usuario o contraseña no coinciden")

    @abstractmethod
    def mostrar_inventario(self, producto):
        pass


class Administrador(Usuario):
    def __init__(self, nombre, numero_id, contrasena):
        super().__init__(nombre, numero_id, contrasena, 'adminsitrador')

    def registrar_usuario(self, nombre, numero_id, contrasena, cargo):

        nuevo_usuario = {"nombre": "",
                         "numero_id": "",
                         "contrasena": "",
                         "cargo": ""}

        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            # Excepción
            for usuario in datos:
                if usuario["numero_id"] == numero_id:
                    raise Exception

            nuevo_usuario["nombre"] = nombre
            nuevo_usuario["numero_id"] = numero_id
            nuevo_usuario["contrasena"] = contrasena
            nuevo_usuario["cargo"] = cargo
            datos.append(nuevo_usuario)

        with open("usuarios.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo)

    def iniciar_sesion(self, numero_id, contrasena):
        super().iniciar_sesion(numero_id, contrasena)

    def mostrar_inventario(self, producto):
        super().mostrar_inventario(producto)

    def consultar_facturas(self, facturas):
        pass

    def calcular_precio(self, producto, cantidad):
        pass


class Vendedor(Usuario):

    def __init__(self, nombre, numero_id, contrasena):
        super().__init__(nombre, numero_id, contrasena, 'vendedor')

    def iniciar_sesion(self, numero_id, contrasena):
        super().iniciar_sesion(numero_id, contrasena)

    def mostrar_inventario(self, producto):
        super().mostrar_inventario(producto)

    def calcular_precio(self, producto, cantidad):
        pass

    def generar_factura(self, nombre_cliente, id_producto, cantidad, subtotal):
        pass


class EncargadoBodega(Usuario):

    def __init__(self, nombre, numero_id, contrasena):
        super().__init__(nombre, numero_id, contrasena, 'Encargadobodega')

    def iniciar_sesion(self, numero_id, contrasena):
        super().iniciar_sesion(numero_id, contrasena)

    def crear_categoria(self, nombre_categoria, precio):
        pass

    def ingresar_producto(self, categoria, id_producto, cantidad):
        pass

    def modificar_categoria(self, otro):
        pass

    def modificar_producto(self, otro):
        pass

    def mostrar_inventario(self, producto):
        super().mostrar_inventario(producto)


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


admin = Administrador("sebas", 23, "sebas")


def agregar_usuario():

    usuario = input("Ingrese el nombre del usuario: ")
    numero_id = input("Ingrese el id del usuario: ")
    contrasena = input("Ingrese la contrasena del usuario")
    cargo = input("Ingrese el cargo del usuario")
    admin.registrar_usuario(usuario, numero_id, contrasena, cargo)


def iniciar_sesion():
    numero_id = input("Ingrese el id")
    contrasena = input("Ingrese la contrasena")
    admin.iniciar_sesion(numero_id, contrasena)


while True:
    decision = input(" 1) Ingresar nuevo usuario. 2) Iniciar sesion. 3) Chao. ")
    if decision == "1":
        agregar_usuario()
    if decision == "2":
        iniciar_sesion()
    if decision == "3":
        break

archivo = open("usuarios.json")
print(archivo)
