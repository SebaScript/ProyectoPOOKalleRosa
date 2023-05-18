import json


class Registro:
    def __init__(self, nombre: str, numero_id: int, contrasena: str):
        self.nombre: str = nombre
        self.numero_id: int = numero_id
        self.contrasena: str = contrasena

    def registrar_usuario(self):

        nuevo_usuario = {"nombre": "",
                         "numero_id": "",
                         "contrasena": "",
                         "cargo": ""}

        with open("vista/usuarios.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            for usuario in datos:
                if usuario["numero_id"] == self.numero_id:
                    raise ValueError

            nuevo_usuario["nombre"] = self.nombre
            nuevo_usuario["numero_id"] = self.numero_id
            nuevo_usuario["contrasena"] = self.contrasena
            datos.append(nuevo_usuario)

        with open("vista/usuarios.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=1)


class UsuarioInicioSesion:

    def __init__(self, numero_id: int, contrasena: str):
        self.numero_id: int = numero_id
        self.contrasena: str = contrasena

    def iniciar_sesion(self):
        with open("vista/usuarios.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for linea in datos:
                if linea["numero_id"] == self.numero_id and linea["contrasena"] == self.contrasena:
                    print("Inicio de sesión exitoso")
                    self.nombre = linea["nombre"]
                    return True
            return False


class Inventario:

    @staticmethod
    def buscar_producto(id_producto):
        with open('inventario.json') as file:
            data = json.load(file)

            for obj in data:
                if 'productos' in obj:
                    productos = obj['productos']
                    for producto in productos:
                        if 'id_producto' in producto and producto['id_producto'] == id_producto:
                            return True

        return False

    @staticmethod
    def mostrar_inventario():

        with open("inventario.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            return datos

    @staticmethod
    def crear_categoria(nombre_categoria: str, precio: float):
        nueva_categoria = {"nombre_categoria": nombre_categoria, "productos": [], "precio": precio}

        with open("inventario.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            nueva_categoria["nombre_categoria"] = nombre_categoria
            nueva_categoria["precio"] = precio
            datos.append(nueva_categoria)

        with open("inventario.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=1)

    @staticmethod
    def ingresar_producto(categoria: str, id_producto: str, cantidad: int):
        nuevo_producto = {"id_producto": "", "cantidad": 0}

        with open("inventario.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            nuevo_producto["id_producto"] = id_producto
            nuevo_producto["cantidad"] = cantidad

            for linea in datos:
                if linea["nombre_categoria"] == categoria:
                    linea["productos"].append(nuevo_producto)

        with open("inventario.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=1)

    @staticmethod
    def modificar_categoria(categoria: str, nuevo_precio: float):

        with open("inventario.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            for linea in datos:
                if linea["nombre_categoria"] == categoria:
                    linea["precio"] = nuevo_precio

        with open("inventario.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=1)

    @staticmethod
    def modificar_producto(categoria, id_producto: str, nueva_cantidad: int):

        with open("inventario.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            for dicc in datos:
                if dicc["nombre_categoria"] == categoria:
                    for i in dicc["productos"]:
                        if i["id_producto"] == id_producto:
                            i["cantidad"] = nueva_cantidad

        with open("inventario.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=1)


class Factura:

    def __init__(self, nombre_cliente: str, id_productos: list, cantidades: list):
        self.nombre_cliente: str = nombre_cliente
        self.id_productos: list = id_productos
        self.cantidades: list = cantidades

    def calcular_precio(self):

        total: float = 0
        total_con_descuento: float = 0

        with open("inventario.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            for id_producto, cantidad in zip(self.id_productos, self.cantidades):
                for obj in datos:
                    productos = obj["productos"]
                    for producto in productos:
                        if 'id_producto' in producto and producto['id_producto'] == id_producto:
                            precio = obj["precio"]
                            subtotal = precio * cantidad
                            total += subtotal

        cantidad_total: int = sum(self.cantidades)
        if cantidad_total < 6:
            total_con_descuento = total
        elif 6 <= cantidad_total < 12:
            total_con_descuento = (total * 90) / 100
        elif 12 <= cantidad_total < 120:
            total_con_descuento = (total * 85) / 100
        elif cantidad_total >= 120:
            total_con_descuento = (total * 80) / 100
        else:
            return False
        return total_con_descuento

    def generar_factura(self, nombre_vendedor):

        precio = self.calcular_precio()

        factura = {
            "nombre_cliente": "",
            "nombre_vendedor": "",
            "id_productos": "",
            "cantidades": "",
            "precio": ""
        }

        with open("facturas.json", 'r', encoding="utf-8") as archivo:
            datos = json.load(archivo)

            factura["nombre_cliente"] = self.nombre_cliente
            factura["nombre_vendedor"] = nombre_vendedor
            factura["id_productos"] = self.id_productos
            factura["cantidades"] = self.cantidades
            factura["precio"] = precio

            datos.append(factura)

        with open("facturas.json", 'w') as f:
            json.dump(datos, f, indent=1)
        return factura

    @staticmethod
    def consultar_facturas():

        with open("facturas.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            return datos
