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

        self.entry = CTkEntry(self, width=150,)
        self.entry.place(x=80, y=100)

        self.label_apellido = CTkLabel(self, text="Apellido", font=("Arial", 14), text_color="#000000")
        self.label_apellido.place(x=260, y=70)

        self.entry2 = CTkEntry(self, width=150,)
        self.entry2.place(x=260, y=100)

        self.label_cedula = CTkLabel(self, text="Cédula", font=("Arial", 14), text_color="#000000")
        self.label_cedula.place(x=80, y=140)

        self.entry3 = CTkEntry(self, width=150,)
        self.entry3.place(x=80, y=170)

        self.fecha_nacimiento = CTkLabel(self, text="Fecha de Nacimiento", font=("Arial", 14), text_color="#000000")
        self.fecha_nacimiento.place(x=260, y=140)

        self.entry4 = CTkEntry(self, width=150, placeholder_text="YYYY-MM-DD")
        self.entry4.place(x=260, y=170)

        self.label_correo = CTkLabel(self, text="Correo Electrónico", font=("Arial", 14), text_color="#000000")
        self.label_correo.place(x=80, y=210)

        self.entry5 = CTkEntry(self, width=150,)
        self.entry5.place(x=80, y=240)

        self.nivel_autorizacion = CTkLabel(self, text="Nivel de Autorización", font=("Arial", 14), text_color="#000000")
        self.nivel_autorizacion.place(x=260, y=210)

        self.entry6 = CTkEntry(self, width=150,)
        self.entry6.place(x=260, y=240)

        Atras = CTkButton(self, text="Cerrar", command=self.destroy)
        Atras.configure(fg_color="#625B66")
        Atras._hover_color = "#7A7282"
        Atras.place(x=180, y=520)