import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import arquitectura.vista.util.generic as utl
from arquitectura.vista.forms.form_master import MasterPanel


class generar_factura:

    def calcular_precio(self, id_productos: str, cantidades: str):
        # Realiza las acciones necesarias para calcular el precio (sin utilizar JSON)
        total_con_descuento = 0  # Aquí iría el cálculo real
        return total_con_descuento

    def generar_factura(self, nombre_cliente, id_productos, cantidades):
        total_con_descuento = self.calcular_precio(id_productos, cantidades)
        factura = {
            "nombre_cliente": nombre_cliente,
            "id_productos": id_productos,
            "cantidades": cantidades,
            "total_con_descuento": total_con_descuento
        }
        messagebox.showinfo(message=f"Factura generada:\n{factura}", title="Mensaje")

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Generar Factura')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=None, height=None)
        utl.centrar_ventana(self.ventana, 800, 500)

        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="top", expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Generar Factura", font=('Times', 30), fg="#666a88", bg='#fcfcfc',
                         pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_nombre_cliente = tk.Label(frame_form_fill, text="Nombre Cliente", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                           anchor="w")
        etiqueta_nombre_cliente.pack(fill=tk.X, padx=20, pady=5)
        self.nombre_cliente = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.nombre_cliente.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_id_productos = tk.Label(frame_form_fill, text="ID Productos (separados por comas)", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                         anchor="w")
        etiqueta_id_productos.pack(fill=tk.X, padx=20, pady=5)
        self.id_productos = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.id_productos.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_cantidades = tk.Label(frame_form_fill, text="Cantidades (separadas por comas)", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                       anchor="w")
        etiqueta_cantidades.pack(fill=tk.X, padx=20, pady=5)
        self.cantidades = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.cantidades.pack(fill=tk.X, padx=20, pady=10)

        generar = tk.Button(frame_form_fill, text="Generar Factura", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0,
                            fg="#fff", command=lambda: self.generar_factura(self.nombre_cliente.get(), self.id_productos.get(), self.cantidades.get()))
        generar.pack(fill=tk.X, padx=20, pady=20)

        self.ventana.mainloop()


if __name__ == "__main__":
    generar_factura()
