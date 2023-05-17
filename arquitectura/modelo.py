import json


class Usuario:
    def __init__(self, nombre: str, numero_id: str, contrasena: str, cargo: str):
        self.nombre: str = nombre
        self.numero_id: str = numero_id
        self.contrasena: str = contrasena
        self.cargo: str = cargo

    def iniciar_sesion(self, numero_id, contrasena):
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            for linea in datos:
                if linea["numero_id"] == numero_id and linea["contrasena"] == contrasena:
                    print("Inicio de sesión exitoso")
                    return  # Si encuentra una coincidencia, termina la función aquí
            # Si llega hasta aquí, significa que no encontró ninguna coincidencia
            print("El usuario o contraseña no coinciden")

    def registrar_usuario(self, nombre, numero_id, contrasena, cargo):

        nuevo_usuario = {"nombre": "",
                         "numero_id": "",
                         "contrasena": "",
                         "cargo": ""}

        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            nuevo_usuario["nombre"] = nombre
            nuevo_usuario["numero_id"] = numero_id
            nuevo_usuario["contrasena"] = contrasena
            nuevo_usuario["cargo"] = cargo
            datos.append(nuevo_usuario)

        with open("usuarios.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=1)

    def consultar_facturas(self, facturas):
        pass

    def mostrar_inventario(self, producto):
        pass

    def calcular_precio(self, id_producto, cantidad):
        producto = self.inventario.get(id_producto)
        # Calculamos el precio
        precio = producto.precio * cantidad
        return precio

    def generar_factura(self, nombre_cliente, id_producto, cantidad):
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

    def crear_categoria(self, nombre_categoria, precio):
        nueva_categoria = {"nombre_categoria": nombre_categoria, "productos": [], "precio": precio}

        with open("inventario.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)

            nueva_categoria["nombre_categoria"] = nombre_categoria
            nueva_categoria["precio"] = precio
            datos.append(nueva_categoria)

        with open("inventario.json", "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=1)

    def ingresar_producto(self, categoria: str, id_producto: str, cantidad: int):
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

    def modificar_categoria(self, otro):
        pass

    def modificar_producto(self, otro):
        pass


class Factura:

    def __init__(self, id_producto, cantidad):
        self.id_producto: int = id_producto
        self.cantidad: int = cantidad


class Inventario:
    pass


bodego = Usuario("sebas", "12", "123", "bodega")

while True:
    dec = input("1 ingresar categoria, 2 Ingresar producto")
    if dec == "1":
        nombre = input("Nombre categoria: ")
        precio = input("precio categoria")
        bodego.crear_categoria(nombre, precio)
    elif dec == "2":
        categoria = input("Categoria producto: ")
        id_prod = input("ID producto: ")
        cantidad = int(input("Cantidad producto: "))
        bodego.ingresar_producto(categoria, id_prod, cantidad)


