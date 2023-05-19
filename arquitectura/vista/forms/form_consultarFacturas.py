import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD

class ConsultarFacturas:
    facturas = [
        {
            "nombre_cliente": "Cliente 1",
            "id_producto": "A001",
            "cantidad": 10,
            "subtotal": 100.0
        },
        {
            "nombre_cliente": "Cliente 2",
            "id_producto": "A002",
            "cantidad": 5,
            "subtotal": 50.0
        }
    ]

    def consultar_facturas(self):
        return self.facturas

    def mostrar_resultado_consulta(self):
        facturas = self.consultar_facturas()
        resultado = ""
        for factura in facturas:
            resultado += f"{factura}\n"
        messagebox.showinfo(message=f"Facturas:\n{resultado}", title="Resultado de consulta")

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Consultar Facturas')
        self.ventana.geometry('400x200')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=None, height=None)

        consultar = tk.Button(self.ventana, text="Consultar Facturas", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0,
                              fg="#fff", command=self.mostrar_resultado_consulta)
        consultar.pack(fill=tk.X, padx=20, pady=20)

        self.ventana.mainloop()

if __name__ == "__main__":
    ConsultarFacturas()
