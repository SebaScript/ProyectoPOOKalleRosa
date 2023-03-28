class Usuario:
    def __init__(self, nombre, contrasena, numero_id, cargo):
        self.nombre: str = nombre
        self.contrasena: str = contrasena
        self.numero_id: int = numero_id
        self.cargo: str = cargo

    def tipo_de_usuario(self):
        return self.cargo


class Registro:
    def __init__(self):
        self.usuarios: list = []
        self.id_ingresados: list = []

    def registro(self):
        nombre = input("Ingrese su nombre: ")
        contrasena = input("Ingrese su contraseña: ")
        numero_id = input("Ingrese su número de identificación: ")

        for usuario in self.usuarios:
            if usuario.numero_id == numero_id:
                print("El número de identificación ya existe, Intente de nuevo")
                return

        cargo = input("Ingrese tipo de usuario (1: Administrador, 2: Vendedor 3: Encargado de inventario): ")

        usuario = Usuario(nombre, contrasena, numero_id, cargo)
        self.usuarios.append(usuario)
        print("Usuario registrado con éxito")

    def iniciar_sesion(self):
        numero_id = input("Ingrese su número de identificación: ")
        contrasena = input("Ingrese su contraseña: ")

        for usuario in self.usuarios:
            if usuario.numero_id == numero_id and usuario.contrasena == contrasena:
                print(f"Bienvenido {usuario.nombre}")

            if usuario.cargo == "3":

                while True:
                    print("1. Crear categoria")
                    print("2. Salir")

                    seleccion = input("Ingrese su opción: ")

                    if seleccion == "1":
                        categoria.crear_categoria()
                    elif seleccion == "2":
                        break
                    else:
                        print("Opción inválida")
                return
            return
        print("Número de identificación o contraseña incorrectos")


class Categoria:
    def __init__(self, ):
        self.nombre_categoria: str
        self.precio_categoria: float
        self.lista_categorias = []

    def crear_categoria(self):
        self.nombre_categoria = input("Ingrese el nombre de la categoria a crear: ")
        self.precio_categoria = input("Ingrese el precio de la categoria a crear: ")

        diccionario_categoria = {self.nombre_categoria: self.precio_categoria}
        self.lista_categorias.append(diccionario_categoria)
        print("La categoria ha sido creada correctamente")
        print(self.lista_categorias)


registro = Registro()
categoria = Categoria()
print("¡Bienvenido al sistema!")

while True:
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

    seleccion = input("Ingrese su opción: ")

    if seleccion == "1":
        registro.registro()
    elif seleccion == "2":
        registro.iniciar_sesion()
    elif seleccion == "3":
        break
    else:
        print("Opción inválida")
