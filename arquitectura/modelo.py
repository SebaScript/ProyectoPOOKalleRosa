import json


class Usuario:
    def __init__(self, nombre: str, numero_id: str, contrasena: str, cargo: str):
        self.nombre: str = nombre
        self.numero_id: str = numero_id
        self.contrasena: str = contrasena
        self.cargo: str = cargo

    @staticmethod
    def iniciar_sesion(numero_id: str, contrasena: str):
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for linea in datos:
                if linea["numero_id"] == numero_id and linea["contrasena"] == contrasena:
                    print("Inicio de sesión exitoso")
                    return  # Si encuentra una coincidencia, termina la función aquí
            # Si llega hasta aquí, significa que no encontró ninguna coincidencia
            print("El usuario o contraseña no coinciden")

    def registrar_usuario(self, nombre: str, numero_id: str, contrasena: str, cargo: str):

        nuevo_usuario = {"nombre": "",
                         "numero_id": "",
                         "contrasena": "",
                         "cargo": ""}

        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            nuevo_usuario["nombre"] = self.nombre
            nuevo_usuario["numero_id"] = self.numero_id
            nuevo_usuario["contrasena"] = self.contrasena
            nuevo_usuario["cargo"] = self.cargo
            datos.append(nuevo_usuario)

        with open("usuarios.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=1)


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

    @staticmethod
    def calcular_precio(id_productos: list, cantidades: list):

        total: float = 0
        total_con_descuento: float = 0

        with open("inventario.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            for id_producto, cantidad in zip(id_productos, cantidades):
                for obj in datos:
                    productos = obj["productos"]
                    for producto in productos:
                        if 'id_producto' in producto and producto['id_producto'] == id_producto:
                            precio = obj["precio"]
                            subtotal = precio * cantidad
                            total += subtotal

        cantidad_total: int = sum(cantidades)
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

    @staticmethod
    def generar_factura(nombre_cliente, id_productos, cantidades, total_con_descuento):
        # Calculamos el subtotal
        subtotal = self.calcular_precio(id_producto, cantidad)
        # Creamos la factura
        factura = {
            "nombre_cliente": nombre_cliente,
            "id_producto": id_producto,
            "cantidad": cantidad,
            "subtotal": subtotal
        }
        # Guardamos la factura en un archivo .json
        with open(f'{nombre_cliente}_factura.json', 'w') as f:
            json.dump(factura, f)
        return factura

    @staticmethod
    def consultar_facturas(self, facturas):

        with open("facturas.json", "r", encoding= "utf-8") as archivo:
            datos = json.load(archivo)

        return datos

usuario = Usuario("", "", "", "")
x = Inventario

while True:
    dec = input("1 Registrar usuario, 2 Iniciar sesion 3 ingresar categoria, 4 Ingresar producto, "
                "5 Mostrar inventario, 6 modificar precio categoria, 7 Modificar cantidad producto, "
                "8 Calcular precio pedido, 9 buscar producto por ID, 10 ")
    if dec == "1":
        nombre = input("Nombre nuevo usuario: ")
        numero_id = input("Numero_id nuevo usuario: ")
        contrasena = input("Contrasena nuevo usuario: ")
        cargo = input("Cargo nuevo usuario: ")
        usuario = Usuario(nombre, numero_id, contrasena, cargo)
        usuario.registrar_usuario(nombre, numero_id, contrasena, cargo)
    elif dec == "2":
        numero_id = input("Numero_id usuario: ")
        contrasena = input("Contrasena usuario: ")
        usuario.iniciar_sesion(numero_id, contrasena)
    elif dec == "3":
        nombre = input("Nombre categoria: ")
        precio = float(input("precio categoria"))
        x.crear_categoria(nombre, precio)
    elif dec == "4":
        categoria = input("Categoria producto: ")
        id_prod = input("ID producto: ")
        cantidad = int(input("Cantidad producto: "))
        x.ingresar_producto(categoria, id_prod, cantidad)
    elif dec == "5":
        print(x.mostrar_inventario())

    elif dec == "6":
        categoria = input("Categoria a modificar: ")
        nuevo_precio = float(input("Nuevo_precio: "))
        x.modificar_categoria(categoria, nuevo_precio)
    elif dec == "7":
        categoria = input("Categoria del producto a modificar: ")
        id_prod = input("Id del producto a modificar")
        nueva_cantidad = int(input("Nueva cantidad de producto"))
        x.modificar_producto(categoria, id_prod, nueva_cantidad)
    elif dec == "8":
        id_productos = []
        cantidades = []
        while True:
            decision = input("¿Quiere ingresar un nuevo producto pa calcular precio? 1) Si, 2) No")
            if decision == "1":
                id_producto = input("Ingrese el id de producto")
                cantidad = int(input("Ingrese la cantidad"))
                id_productos.append(id_producto)
                cantidades.append(cantidad)
            if decision == "2":
                Factura.calcular_precio(id_productos, cantidades)
            print(id_productos)
            print(cantidades)
            print(Factura.calcular_precio(id_productos, cantidades))
    elif dec == "9":
        id_a_buscar = input("Ingrese el id a buscar")
        x.buscar_producto(id_a_buscar)


