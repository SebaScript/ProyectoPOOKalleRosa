import tkinter as tk
import arquitectura.vista.util.generic as utl
from arquitectura.vista.forms.form_calcularPrecio import CalcularPrecio
from arquitectura.vista.forms.form_crearCategoria import CrearCategoria
from arquitectura.vista.forms.from_modificarCategoria import ModificarCategoria
from arquitectura.vista.forms.from_modificarProducto import ModificarProducto
from arquitectura.vista.forms.from_ingresarProducto import IngresarProducto
from arquitectura.vista.forms.from_generarFactura import GenerarFactura
from arquitectura.vista.forms.form_mostrar_Inventario import MostrarInventario
from arquitectura.vista.forms.form_consultarFacturas import ConsultarFacturas
from arquitectura.vista.forms.form_buscarProducto import BuscarProducto


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

        botones = ["Crear categoria", "Modificar precio categoria", "Ingresar producto", "Modificar cantidad producto", "Calular Precio",
                   "generar factura", "mostrar inventario", "consultar facturas", "buscar producto"]

        # Funciones personalizadas para los botones
        def funcion_boton_1():
            CrearCategoria()

        def funcion_boton_2():
            ModificarCategoria()

        def funcion_boton_3():
            IngresarProducto()

        def funcion_boton_4():
            ModificarProducto()

        def funcion_boton_5():
            CalcularPrecio()

        def funcion_boton_6():
            GenerarFactura()

        def funcion_boton_7():
            MostrarInventario()

        def funcion_boton_8():
            ConsultarFacturas()

        def funcion_boton_9():
            BuscarProducto()

        for boton_texto, funcion in zip(botones, [funcion_boton_1, funcion_boton_2, funcion_boton_3, funcion_boton_4,
                                                  funcion_boton_5, funcion_boton_6, funcion_boton_7, funcion_boton_8,
                                                  funcion_boton_9]):
            btn = tk.Button(frame_botones, text=boton_texto, font=('Times', 15, "bold"), bg='#3a7ff6', bd=0, fg="#fff",
                            command=funcion)
            btn.pack(fill=tk.X, padx=20, pady=10)

        self.ventana.mainloop()
