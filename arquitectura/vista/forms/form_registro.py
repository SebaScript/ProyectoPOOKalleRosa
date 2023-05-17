import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import arquitectura.vista.util.generic as utl


class RegistroVentana:

    def guardar_registro(self):
        nombre = self.nombre.get()
        numero_id = self.numero_id.get()
        contrasena = self.contrasena.get()

    def __init__(self):
        self.ventana_registro = tk.Toplevel()
        self.ventana_registro.title('Registro')
        self.ventana_registro.geometry('600x500')
        self.ventana_registro.config(bg='#fcfcfc')
        utl.centrar_ventana(self.ventana_registro, 600, 500)

        frame_form_registro = tk.Frame(self.ventana_registro, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_registro.pack(expand=tk.YES, fill=tk.BOTH)

        etiqueta_nombre = tk.Label(frame_form_registro, text="Nombre", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                   anchor="w")
        etiqueta_nombre.pack(fill=tk.X, padx=20, pady=10)
        self.nombre = ttk.Entry(frame_form_registro, font=('Times', 14))
        self.nombre.pack(fill=tk.X, padx=20, pady=5)

        etiqueta_id = tk.Label(frame_form_registro, text="Número de ID", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                               anchor="w")
        etiqueta_id.pack(fill=tk.X, padx=20, pady=10)
        self.numero_id = ttk.Entry(frame_form_registro, font=('Times', 14))
        self.numero_id.pack(fill=tk.X, padx=20, pady=5)

        etiqueta_contrasena = tk.Label(frame_form_registro, text="Contraseña", font=('Times', 14), fg="#666a88",
                                       bg='#fcfcfc',
                                       anchor="w")
        etiqueta_contrasena.pack(fill=tk.X, padx=20, pady=10)
        self.contrasena = ttk.Entry(frame_form_registro, font=('Times', 14))
        self.contrasena.pack(fill=tk.X, padx=20, pady=5)
        self.contrasena.config(show="*")

        etiqueta_cargo = tk.Label(frame_form_registro, text="Cargo", font=('Times', 14), fg="#666a88", bg='#fcfcfc',
                                  anchor="w")
        etiqueta_cargo.pack(fill=tk.X, padx=20, pady=10)
        self.opciones_cargo = ttk.Combobox(frame_form_registro, font=('Times', 14), state="readonly")
        self.opciones_cargo['values'] = ('Administrador', 'Vendedor', 'Encargado de bodega')
        self.opciones_cargo.current(0)
        self.opciones_cargo.pack(fill=tk.X, padx=20, pady=5)

        registro = tk.Button(frame_form_registro, text="Registrar", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0,
                             fg="#fff", command=self.guardar_registro)
        registro.pack(fill=tk.X, padx=20, pady=20)

        registro.bind("<Return>", (lambda event: self.guardar_registro()))

        self.ventana_registro.mainloop()
