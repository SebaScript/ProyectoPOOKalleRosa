import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD

class buscar_producto:

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

    def buscar_producto(self, id_producto: str):
        for obj in self.inventario:
            if 'productos' in obj:
                productos = obj['productos']
                for producto in productos:
                    if 'id_producto' in producto and producto['id_producto'] == id_producto:
                        return True
        return False

    def mostrar_resultado_busqueda(self, id_producto: str):
        resultado = self.buscar_producto(id_producto)
        if resultado:
            messagebox.showinfo(message=f"El producto con ID '{id_producto}' fue encontrado en el inventario.",
                                title="Resultado de búsqueda")
        else:
            messagebox.showinfo(message=f"El producto con ID '{id_producto}' no se encuentra en el inventario.",
                                title="Resultado de búsqueda")

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Buscar Producto')
        self.ventana.geometry('400x200')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=None, height=None)

        etiqueta_id_producto = tk.Label(self.ventana, text="ID Producto", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                         anchor="w")
        etiqueta_id_producto.pack(fill=tk.X, padx=20, pady=5)
        self.id_producto = ttk.Entry(self.ventana, font=('Times', 14))
        self.id_producto.pack(fill=tk.X, padx=20, pady=10)

        buscar = tk.Button(self.ventana, text="Buscar Producto", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0,
                            fg="#fff", command=lambda: self.mostrar_resultado_busqueda(self.id_producto.get()))
        buscar.pack(fill=tk.X, padx=20, pady=20)

        self.ventana.mainloop()


if __name__ == "__main__":
    buscar_producto()
