from modelo import *

x = Inventario

while True:
    dec = input("1 Registrar usuario, 2 Iniciar sesion 3 ingresar categoria, 4 Ingresar producto, "
                "5 Mostrar inventario, 6 modificar precio categoria, 7 Modificar cantidad producto, "
                "8 Calcular precio pedido, 9 buscar producto por ID, 10 Generar factura 11 Mostrar facturas")
    if dec == "1":
        nombre = input("Nombre nuevo usuario: ")
        numero_id = int(input("Numero_id nuevo usuario: "))
        contrasena = input("Contrasena nuevo usuario: ")
        cargo = input("Cargo nuevo usuario: ")
        usuario = Registro(nombre, numero_id, contrasena)
        usuario.registrar_usuario()
    elif dec == "2":
        numero_id = int(input("Numero_id usuario: "))
        contrasena = input("Contrasena usuario: ")
        usuario_inicio_sesion = UsuarioInicioSesion(numero_id, contrasena)
        usuario_inicio_sesion.iniciar_sesion()
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
        id_productos_calcular = []
        cantidades_calcular = []
        while True:
            decision = input("¿Quiere ingresar un nuevo producto para calcular precio? 1) Si, 2) No ")
            if decision == "1":
                id_producto = input("Ingrese el id de producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                id_productos_calcular.append(id_producto)
                cantidades_calcular.append(cantidad)
            elif decision == "2":
                factura = Factura("", id_productos_calcular, cantidades_calcular)
                print(id_productos_calcular)
                print(cantidades_calcular)
                print(factura.calcular_precio())
                break
    elif dec == "9":
        id_a_buscar = input("Ingrese el id a buscar")
        x.buscar_producto(id_a_buscar)
    elif dec == "10":
        id_productos_factura = []
        cantidades_factura = []
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        nombre_vendedor = input("Ingrese el nombre del vendedor. ")
        while True:
            decision = input("¿Quiere ingresar un nuevo producto para la factura? 1) Si, 2) No")
            if decision == "1":
                id_producto = input("Ingrese el id de producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                id_productos_factura.append(id_producto)
                cantidades_factura.append(cantidad)
            elif decision == "2":
                factura = Factura(nombre_cliente, id_productos_factura, cantidades_factura)
                print(factura.generar_factura(nombre_vendedor))
                break
    elif dec == "11":
        print(Factura.consultar_facturas())
