from customtkinter import *
from tkinter import ttk
from tkinter import CENTER, W

class BloquearUsuario(CTkFrame):
    def __init__(self, master, main):
        super().__init__(master)
        self.main = main
        self.configure(
            fg_color="#2b2b39",
            corner_radius=0,
        )

        self.labelFondo = CTkLabel(
			master=self,
			text="",
			fg_color="#2b2b39",
			bg_color="#A79D8A",
			corner_radius=15
		)
        self.labelFondo.place(
			relx=0, rely=0,
			relwidth=1, relheight=1
		)

        self.labelContenido = CTkLabel(
			master=self,
			text="Bloqueo De Usuarios",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 20, "bold"), corner_radius=15,
		)
        self.labelContenido.place(
			relx=0.5, rely=0.12,
			relwidth=0.4, relheight=0.2,
			anchor=CENTER
		)
        self.texto_exito = CTkLabel(
            master=self,
            text="",
            text_color="#00FF00",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=15
        )
        self.texto_exito.place(relx=0.5, rely=0.94, anchor=CENTER)

        self.texto_error = CTkLabel(
            master=self,
            text="",
            text_color="#FF0000",
            fg_color="#2b2b39",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=15
        )
        self.texto_error.place(relx=0.5, rely=0.94, anchor=CENTER)

        self.boton_bloquear = CTkButton(
            master=self,
            text="Bloquear/Desbloquear Usuario",
            fg_color="#5e5e72",
            bg_color="#2b2b39",
            font=("Times New Roman", 15, "bold"),
            corner_radius=10,
            command=self.toggle_bloqueo_seleccion
        )
        self.boton_bloquear.place(
            relx=0.5, rely=0.88,
            anchor=CENTER
        )

        # Crear la tabla al inicio
        self.cargar_usuarios()

    def _cargar_usuarios(self):
        for i in self.tablaUsuarios.get_children():
            self.tablaUsuarios.delete(i)
        rows = self.main.bdd.obtener_usuarios_detalles()
        for r in rows:
            self.tablaUsuarios.insert('', 'end', values=(
                r.get('id_usuario'),
                r.get('username'),
                r.get('cedula'),
                r.get('nacimiento'),
                r.get('mail'),
                r.get('role'),
                r.get('nivel_autorizacion'),
                r.get('capacitacion')
            ))

    def toggle_bloqueo_seleccion(self):
        sel = self.tablaUsuarios.focus()
        if not sel:
            self.texto_error.configure(text="Seleccione un usuario para bloquear/desbloquear")
            self.texto_error.place(relx=0.5, rely=0.94, anchor=CENTER)
            return
        vals = self.tablaUsuarios.item(sel).get('values')
        if not vals:
            self.texto_error.configure(text="Fila seleccionada inválida")
            self.texto_error.place(relx=0.5, rely=0.94, anchor=CENTER)
            return
        try:
            id_usuario = int(vals[0])
        except Exception:
            self.texto_error.configure(text="ID de usuario inválido")
            self.texto_error.place(relx=0.5, rely=0.94, anchor=CENTER)
            return

        ok = self.main.bdd.toggle_bloqueo_usuario(id_usuario)
        if ok:
            self.texto_exito.configure(text="Operación aplicada con éxito")
            self.texto_exito.place(relx=0.5, rely=0.94, anchor=CENTER)
            self.texto_error.configure(text="")
            self._cargar_usuarios()
        else:
            self.texto_error.configure(text="No se pudo modificar el estado del usuario")
            self.texto_error.place(relx=0.5, rely=0.94, anchor=CENTER)
        # Recargar la vista de usuarios (la tabla ya existe o será creada)
        try:
            self._cargar_usuarios()
        except Exception:
            # Si la tabla aún no existe, crearla ahora
            self.cargar_usuarios()

    def cargar_usuarios(self):
        # destruir tabla previa si existe
        try:
            if hasattr(self, 'tablaUsuarios'):
                self.tablaUsuarios.destroy()
        except Exception:
            pass

        # Treeview de usuarios
        columnas = ("ID", "Usuario", "Cédula", "Nacimiento", "Mail", "Rol", "Nivel", "Capacitacion")
        self.tablaUsuarios = ttk.Treeview(master=self, columns=columnas, show='headings')
        for col in columnas:
            self.tablaUsuarios.heading(col, text=col)

        self.tablaUsuarios.column("ID", width=50, anchor=CENTER)
        self.tablaUsuarios.column("Usuario", width=150, anchor=W)
        self.tablaUsuarios.column("Cédula", width=120, anchor=W)
        self.tablaUsuarios.column("Nacimiento", width=120, anchor=W)
        self.tablaUsuarios.column("Mail", width=180, anchor=W)
        self.tablaUsuarios.column("Rol", width=120, anchor=CENTER)
        self.tablaUsuarios.column("Nivel", width=80, anchor=CENTER)
        self.tablaUsuarios.column("Capacitacion", width=150, anchor=W)

        self.tablaUsuarios.place(relx=0.5, rely=0.4, relwidth=0.9, relheight=0.45, anchor=CENTER)

        # asegurar que la tabla tenga datos
        self._cargar_usuarios()