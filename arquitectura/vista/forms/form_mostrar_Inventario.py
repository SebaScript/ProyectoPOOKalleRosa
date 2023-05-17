import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD

class mostrar_inventario:
#prueba no es el inventario real
    inventario = [
        {
            "nombre_categoria": "Categoria 1",
            "productos": [
                {"id_producto": "A001", "cantidad": 10},
                {"id_producto": "A002", "cantidad": 5}
            ]
        },
        {
            "nombre_categoria": "Categoria 2",
            "productos": [
                {"id_producto": "B001", "cantidad": 7},
                {"id_producto": "B002", "cantidad": 8}
            ]
        }
    ]

    def mostrar_inventario(self):
        return self.inventario

    def mostrar_inventario_en_pantalla(self):
        inventario_str = ''
        for categoria in self.mostrar_inventario():
            inventario_str += f"Categoria: {categoria['nombre_categoria']}\n"
            for producto in categoria['productos']:
                inventario_str += f"  - ID: {producto['id_producto']} - Cantidad: {producto['cantidad']}\n"
            inventario_str += "\n"

        messagebox.showinfo(message=f"Inventario:\n\n{inventario_str}", title="Inventario")

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Mostrar Inventario')
        self.ventana.geometry('400x200')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=None, height=None)

        mostrar = tk.Button(self.ventana, text="Mostrar Inventario", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0,
                            fg="#fff", command=self.mostrar_inventario_en_pantalla)
        mostrar.pack(fill=tk.X, padx=20, pady=20)

        self.ventana.mainloop()

if __name__ == "__main__":
    mostrar_inventario()
