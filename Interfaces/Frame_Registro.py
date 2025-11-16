from customtkinter import *


class frame_registro(CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=500, height=600)
        self.master = master
        self.configure(fg_color="#E4D7D7")
        self.place(x=400, y=60)

        self.titulo = CTkLabel(self, text="Formulario de Registro", font=("Arial", 20), text_color="#000000")
        self.titulo.place(x=150, y=20)

        self.label_nombre = CTkLabel(self, text="Nombre", font=("Arial", 14), text_color="#000000")
        self.label_nombre.place(x=80, y=70)

        self.nombre = CTkEntry(self, width=150,)
        self.nombre.place(x=80, y=100)

        self.label_apellido = CTkLabel(self, text="Apellido", font=("Arial", 14), text_color="#000000")
        self.label_apellido.place(x=260, y=70)

        self.apellido = CTkEntry(self, width=150,)
        self.apellido.place(x=260, y=100)

        self.label_cedula = CTkLabel(self, text="Cédula", font=("Arial", 14), text_color="#000000")
        self.label_cedula.place(x=80, y=140)

        self.cedula = CTkEntry(self, width=150,)
        self.cedula.place(x=80, y=170)

        self.fecha_nacimiento = CTkLabel(self, text="Fecha de Nacimiento", font=("Arial", 14), text_color="#000000")
        self.fecha_nacimiento.place(x=260, y=140)

        self.fecha_nacimiento = CTkEntry(self, width=150, placeholder_text="YYYY-MM-DD")
        self.fecha_nacimiento.place(x=260, y=170)

        self.label_correo = CTkLabel(self, text="Correo Electrónico", font=("Arial", 14), text_color="#000000")
        self.label_correo.place(x=80, y=210)

        self.correo = CTkEntry(self, width=150,)
        self.correo.place(x=80, y=240)

        self.nivel_autorizacion = CTkLabel(self, text="Nivel de Autorización", font=("Arial", 14), text_color="#000000")
        self.nivel_autorizacion.place(x=260, y=210)

        self.nivel_autorizacion_entry = CTkEntry(self, width=150,)
        self.nivel_autorizacion_entry.place(x=260, y=240)

        Registrarse = CTkButton(self, text="Registrarse")
        Registrarse.configure(fg_color="#625B66")
        Registrarse._hover_color = "#7A7282"
        Registrarse.place(x=180, y=470)

        Atras = CTkButton(self, text="Atrás", command=self.destroy)
        Atras.configure(fg_color="#625B66")
        Atras._hover_color = "#7A7282"
        Atras.place(x=180, y=520)