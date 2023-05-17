import tkinter as tk
import arquitectura.vista.util.generic as utl
from arquitectura.vista.forms.form_calcularPrecio import calcular_Precio
from arquitectura.vista.forms.form_crearCategoria import crear_categoria
from arquitectura.vista.forms.from_modificarCategoria import modificar_categoria
from arquitectura.vista.forms.from_modificarProducto import modificar_producto
from arquitectura.vista.forms.from_ingresarProducto import ingresar_producto
from arquitectura.vista.forms.from_generarFactura import generar_factura


class MasterPanel:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('KalleRosa')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=False, height=False)
        utl.centrar_ventana(self.ventana, 800, 500)

        # ...

        # Botones
        frame_botones = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_botones.pack(side="left", fill="y")

        botones = ["calcular Precio", "crear categoria", "modificar categoria", "modificar producto", "ingresar "
                                                                                                      "producto",
                   "generar factura", "Botón 7", "Botón 8", "Botón 9"]

        # Funciones personalizadas para los botones
        def funcion_boton_1():
            calcular_Precio()

        def funcion_boton_2():
            crear_categoria()

        def funcion_boton_3():
            modificar_categoria()

        def funcion_boton_4():
            modificar_producto()

        def funcion_boton_5():
            ingresar_producto()

        def funcion_boton_6():
            generar_factura()

        def funcion_boton_7():
            print("Se ha presionado el Botón 1")

        def funcion_boton_8():
            print("Se ha presionado el Botón 1")

        def funcion_boton_9():
            print("Se ha presionado el Botón 1")

        for boton_texto, funcion in zip(botones, [funcion_boton_1, funcion_boton_2, funcion_boton_3, funcion_boton_4,
                                                  funcion_boton_5, funcion_boton_6, funcion_boton_7, funcion_boton_8,
                                                  funcion_boton_9]):
            btn = tk.Button(frame_botones, text=boton_texto, font=('Times', 15, "bold"), bg='#3a7ff6', bd=0, fg="#fff",
                            command=funcion)
            btn.pack(fill=tk.X, padx=20, pady=10)

        self.ventana.mainloop()
