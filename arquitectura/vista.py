import tkinter as tk
from tkinter import messagebox
from modelo import UsuarioInicioSesion, Registro, Inventario


class Aplicacion:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x300')

        # Registro de usuario
        self.frame_registro = tk.Frame(root)
        self.frame_registro.pack()

        self.nombre_label = tk.Label(self.frame_registro, text='Nombre:')
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(self.frame_registro)
        self.nombre_entry.pack()

        self.numero_id_label = tk.Label(self.frame_registro, text='ID:')
        self.numero_id_label.pack()
        self.numero_id_entry = tk.Entry(self.frame_registro)
        self.numero_id_entry.pack()

        self.contrasena_label = tk.Label(self.frame_registro, text='Contraseña:')
        self.contrasena_label.pack()
        self.contrasena_entry = tk.Entry(self.frame_registro, show="*")
        self.contrasena_entry.pack()

        self.cargo_label = tk.Label(self.frame_registro, text='Cargo:')
        self.cargo_label.pack()
        self.cargo_entry = tk.Entry(self.frame_registro)
        self.cargo_entry.pack()

        self.boton_registro = tk.Button(self.frame_registro, text='Registrar', command=self.registrar_usuario)
        self.boton_registro.pack()

        # Inicio de sesion
        self.frame_inicio_sesion = tk.Frame(root)
        self.frame_inicio_sesion.pack()

        self.numero_id_inicio_label = tk.Label(self.frame_inicio_sesion, text='ID:')
        self.numero_id_inicio_label.pack()
        self.numero_id_inicio_entry = tk.Entry(self.frame_inicio_sesion)
        self.numero_id_inicio_entry.pack()

        self.contrasena_inicio_label = tk.Label(self.frame_inicio_sesion, text='Contraseña:')
        self.contrasena_inicio_label.pack()
        self.contrasena_inicio_entry = tk.Entry(self.frame_inicio_sesion, show="*")
        self.contrasena_inicio_entry.pack()

        self.boton_inicio = tk.Button(self.frame_inicio_sesion, text='Iniciar sesión', command=self.iniciar_sesion)
        self.boton_inicio.pack()

        self.frame_crear_categoria = tk.Frame(root)

        self.nombre_categoria_label = tk.Label(self.frame_crear_categoria, text='Nombre de la categoría:')
        self.nombre_categoria_label.pack()
        self.nombre_categoria_entry = tk.Entry(self.frame_crear_categoria)
        self.nombre_categoria_entry.pack()

        self.precio_label = tk.Label(self.frame_crear_categoria, text='Precio:')
        self.precio_label.pack()
        self.precio_entry = tk.Entry(self.frame_crear_categoria)
        self.precio_entry.pack()

        self.boton_crear_categoria = tk.Button(self.frame_crear_categoria, text='Crear categoría',
                                               command=self.crear_categoria)
        self.boton_crear_categoria.pack()

        self.frame_crear_categoria.pack_forget()

    def registrar_usuario(self):
        nombre = self.nombre_entry.get()
        numero_id = int(self.numero_id_entry.get())
        contrasena = self.contrasena_entry.get()
        cargo = self.cargo_entry.get()

        usuario = Registro(nombre, numero_id, contrasena, cargo)
        usuario.registrar_usuario()

        messagebox.showinfo('Registro', 'Usuario registrado exitosamente')

    def iniciar_sesion(self):
        numero_id = int(self.numero_id_inicio_entry.get())
        contrasena = self.contrasena_inicio_entry.get()

        usuario = UsuarioInicioSesion(numero_id, contrasena)
        if usuario.iniciar_sesion():
            messagebox.showinfo('Inicio de sesión', 'Inicio de sesión exitoso')
            self.frame_inicio_sesion.pack_forget()
            self.frame_crear_categoria.pack()
        else:
            messagebox.showerror('Inicio de sesión', 'ID o contraseña incorrecta')

    def crear_categoria(self):
        self.limpiar_ventana()
        nombre_categoria = self.nombre_categoria_entry.get()
        precio = float(self.precio_entry.get())
        Inventario.crear_categoria(nombre_categoria, precio)
        messagebox.showinfo('Crear categoría', 'Categoría creada exitosamente')

    def limpiar_ventana(self):
        for widget in root.winfo_children():
            widget.destroy()

root = tk.Tk()
app = Aplicacion(root)
root.mainloop()
