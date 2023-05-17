import tkinter as tk
from tkinter.font import BOLD
import arquitectura.vista.util.generic as utl
from arquitectura.vista.forms.form_registro import RegistroVentana
from arquitectura.vista.forms.form_inicio_sesion import App


def registrarse():
    RegistroVentana()


class InicioVentana:

    def iniciar_sesion(self):
        self.ventana_inicio.destroy()
        App()

    def __init__(self):
        self.ventana_inicio = tk.Tk()
        self.ventana_inicio.title('Inicio')
        self.ventana_inicio.geometry('800x500')
        self.ventana_inicio.config(bg='#fcfcfc')
        self.ventana_inicio.resizable(width=False, height=False)
        utl.centrar_ventana(self.ventana_inicio, 800, 500)

        # Logo
        logo = utl.leer_imagen("./imagenes/logo.png", (200, 200))
        frame_logo = tk.Frame(self.ventana_inicio, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frame_logo.pack(side="top", expand=tk.YES, fill=tk.BOTH)
        label_logo = tk.Label(frame_logo, image=logo, bg='#3a7ff6')
        label_logo.place(x=0, y=0, relwidth=1, relheight=1)

        # Mensaje de bienvenida
        frame_mensaje = tk.Frame(self.ventana_inicio, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_mensaje.pack(side="top", expand=tk.YES, fill=tk.BOTH)
        label_bienvenida = tk.Label(frame_mensaje, text="Bienvenido", font=('Times', 24, BOLD), fg="#666a88",
                                    bg='#fcfcfc', pady=20)
        label_bienvenida.pack(expand=tk.YES, fill=tk.BOTH)

        # Botones de Iniciar sesión y Registrarse
        frame_botones = tk.Frame(self.ventana_inicio, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_botones.pack(side="top", expand=tk.YES, fill=tk.BOTH)

        btn_iniciar_sesion = tk.Button(frame_botones, text="Iniciar sesión", font=('Times', 15, BOLD), bg='#3a7ff6',
                                       bd=0,
                                       fg="#fff", command=self.iniciar_sesion)
        btn_iniciar_sesion.pack(fill=tk.X, padx=20, pady=10)

        btn_registrarse = tk.Button(frame_botones, text="Registrarse", font=('Times', 15, BOLD), bg='#3a7ff6', bd=0,
                                    fg="#fff", command=registrarse)
        btn_registrarse.pack(fill=tk.X, padx=20, pady=10)

        self.ventana_inicio.mainloop()
