import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import arquitectura.vista.util.generic as utl
from arquitectura.modelo import Inventario


class CrearCategoria:

    def crear_categoria(self, nombre_categoria: str, precio: float):
        nombre_categoria = self.nombre_categoria.get()
        precio = float(self.precio.get())
        categoria = Inventario()
        categoria.crear_categoria(nombre_categoria, precio)
        messagebox.showinfo(message="Categoría creada correctamente", title="Mensaje")

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Creación de Categoría')
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=None, height=None)
        utl.centrar_ventana(self.ventana, 800, 500)

        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="top", expand=tk.YES, fill=tk.BOTH)

        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side="top", fill=tk.X)
        title = tk.Label(frame_form_top, text="Creación de Categoría", font=('Times', 30), fg="#666a88", bg='#fcfcfc',
                         pady=50)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        frame_form_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_nombre_categoria = tk.Label(frame_form_fill, text="Nombre de Categoría", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                             anchor="w")
        etiqueta_nombre_categoria.pack(fill=tk.X, padx=20, pady=5)
        self.nombre_categoria = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.nombre_categoria.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_precio = tk.Label(frame_form_fill, text="Precio", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                   anchor="w")
        etiqueta_precio.pack(fill=tk.X, padx=20, pady=5)
        self.precio = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.precio.pack(fill=tk.X, padx=20, pady=10)

        crear = tk.Button(frame_form_fill, text="Crear Categoría", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0,
                          fg="#fff", command=lambda: self.crear_categoria(self.nombre_categoria.get(), float(self.precio.get())))
        crear.pack(fill=tk.X, padx=20, pady=20)

        self.ventana.mainloop()


if __name__ == "__main__":
    CrearCategoria()
