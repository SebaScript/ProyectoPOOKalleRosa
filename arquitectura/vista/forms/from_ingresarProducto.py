import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import arquitectura.vista.util.generic as utl
from arquitectura.modelo import Inventario


class IngresarProducto:

    def ingresar_producto(self, categoria: str, id_producto: int, cantidad: int):
        categoria = self.categoria.get()
        id_producto = int(self.id_producto.get())
        cantidad = int(self.cantidad.get())
        Inventario.ingresar_producto(categoria, id_producto, cantidad)
        messagebox.showinfo(message="Producto agregado correctamente", title="Mensaje")

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Ingreso de Producto')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=None, height=None)
        utl.centrar_ventana(self.ventana, 800, 500)

        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="top", expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Ingreso de Producto", font=('Times', 30), fg="#666a88", bg='#fcfcfc',
                         pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_categoria = tk.Label(frame_form_fill, text="Categoría", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                      anchor="w")
        etiqueta_categoria.pack(fill=tk.X, padx=20, pady=5)
        self.categoria = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.categoria.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_id_producto = tk.Label(frame_form_fill, text="ID Producto", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                        anchor="w")
        etiqueta_id_producto.pack(fill=tk.X, padx=20, pady=5)
        self.id_producto = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.id_producto.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_cantidad = tk.Label(frame_form_fill, text="Cantidad", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                     anchor="w")
        etiqueta_cantidad.pack(fill=tk.X, padx=20, pady=5)
        self.cantidad = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.cantidad.pack(fill=tk.X, padx=20, pady=10)

        ingresar = tk.Button(frame_form_fill, text="Ingresar Producto", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0,
                             fg="#fff", command=lambda: self.ingresar_producto(self.categoria.get(), self.id_producto.get(), int(self.cantidad.get())))
        ingresar.pack(fill=tk.X, padx=20, pady=20)

        self.ventana.mainloop()
