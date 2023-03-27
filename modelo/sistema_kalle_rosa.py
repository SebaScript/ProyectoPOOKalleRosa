class Usuario:
    def __init__(self, nombre, contrasena, numero_id, cargo):
        self.nombre = nombre
        self.contrasena = contrasena
        self.numero_id = numero_id
        self.cargo = cargo

    def tipo_de_usuario(self):
        return self.cargo


class AdministradorUsuarios:
    def __init__(self):
        self.usuarios = []

    def registro(self):
        nombre = input("Ingrese su nombre: ")
        contrasena = input("Ingrese su contraseña: ")
        numero_id = input("Ingrese su número de identificación: ")
        cargo = input("Ingrese tipo de usuario (1: Administrador, 2: Vendedor, 3: Encargado de inventario)")

        usuario = Usuario(nombre, contrasena, numero_id, cargo)
        self.usuarios.append(usuario)
        print("Usuario registrado con éxito")

    def iniciar_sesion(self):
        numero_id = input("Ingrese su número de identificación: ")
        contrasena = input("Ingrese su contraseña: ")

        for usuario in self.usuarios:
            if usuario.numero_id == numero_id and usuario.contrasena == contrasena:
                print("Inicio de sesión exitoso")
                return
        print("Número de identificación o contraseña incorrectos")


administrador_usuarios = AdministradorUsuarios()
print("¡Bienvenido al sistema!")

while True:
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

    seleccion = input("Ingrese su opción: ")

    if seleccion == "1":
        administrador_usuarios.registro()
    elif seleccion == "2":
        administrador_usuarios.iniciar_sesion()
    elif seleccion == "3":
        break
    else:
        print("Opción inválida")
