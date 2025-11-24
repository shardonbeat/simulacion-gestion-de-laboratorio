from tkinter import Image
from customtkinter import *
from PIL import Image
import os

class frameLogin (CTkFrame):

	def __init__(self, master, main):
		super().__init__(master)
		self.main = main
		self.configure(
			fg_color = "#A79D8A",
			corner_radius = 0,
		)

	## Labels
			#@ Usuario

		self.labelFondo = CTkLabel(
			master = self,
			text = "",
			fg_color = "#2b2b39",
			corner_radius=15
		)
		self.labelFondo.place(
			relx=0.5, rely=0.5,
			relwidth=0.35, relheight=0.7,
			anchor=CENTER
		)

		self.labelUsuario = CTkLabel(
			master = self, text = "Laboratorio de investigación científica",
			text_color = "#ffffff",
			font = ("Times New Roman", 15, "bold"), corner_radius = 15,
			fg_color = "#8b8b9f",
			bg_color= "#2b2b39"
		)
		self.labelUsuario.place(
			relx=0.5, rely=0.2,
			relwidth=0.3, relheight=0.05,
			anchor=CENTER
		)

		self.Image_Usuario = CTkImage(
            light_image=Image.open(os.path.join(os.path.dirname(__file__), "Img", "Acceso.png")),
            dark_image=Image.open(os.path.join(os.path.dirname(__file__), "Img", "Acceso.png")),
            size=(128, 128)
        )

		self.labelUsuarioIcon = CTkLabel(
			master=self,
			image=self.Image_Usuario,
			text="",
			bg_color= "#2b2b39"
		)
		self.labelUsuarioIcon.place(
			relx=0.5, rely=0.35,
			anchor=CENTER
		)

			#@ Cédula

		self.input_user = CTkEntry(
			master=self,
			font=('Arial', 15), text_color='black',
			placeholder_text="Cédula", placeholder_text_color='black',
			justify='center',
			border_color='black', fg_color="#948D8D",
			bg_color="#2b2b39",
			corner_radius=10
		)
		self.input_user.place(relx=0.5, rely=0.52,
			relwidth=0.15, relheight=0.05, anchor=CENTER)

			#@ Contraseña

		self.input_password = CTkEntry(
			master=self,
			font=('Arial', 15), text_color='black',
			placeholder_text="Contraseña", placeholder_text_color='black',
			justify='center',
			border_color='black', fg_color="#948D8D",
			bg_color="#2b2b39",
			corner_radius=10,
			show='*'
		)
		self.input_password.place(relx=0.5, rely=0.60,
			relwidth=0.15, relheight=0.05, anchor=CENTER)
		
	## Botones

		self.login_button = CTkButton(
			master=self, text="Iniciar sesión",
            font=('Times New Roman', 15, 'bold'),
			hover_color="#898995",
			corner_radius=15,
            fg_color="#72737f",
			bg_color="#2b2b39",
            command=lambda:self.iniciar_sesion(
                self.input_user.get(), self.input_password.get()
            )
        )
		self.login_button.place (
			relx=0.43, rely=0.70,
			relwidth=0.12, relheight=0.05,
			anchor=CENTER
		)

		self.register_button = CTkButton(
			master=self, text="Registrarse",
            font=('Times New Roman', 15, 'bold'),
			hover_color="#898995",
			corner_radius=15,
            fg_color="#72737f",
			bg_color="#2b2b39",
            command=lambda:self.registrarse()
        )
		self.register_button.place (
			relx=0.57, rely=0.70,
			relwidth=0.12, relheight=0.05,
			anchor=CENTER
		)

	## Funciones

		#@ Función iniciar sesión
	def iniciar_sesion(self, cedula: str, password: str):
		validar = self.main.bdd.verificarLogin(cedula, password)
		if validar:
			data = self.main.bdd.obtenerUsuario(cedula)
			self.obtener_nivel_autorizacion(data)
			self.limpiar_inputs()
		else:
			print("Cédula o contraseña incorrecta.")

	def registrarse(self):
		self.main.frameLogin.place_forget()
		self.main.frameRegister.place(
			relx=0, rely=0,
			relwidth=1, relheight=1
		)
	
	def limpiar_inputs(self):
		self.input_user.delete(0, "end")
		self.input_password.delete(0, "end")

		'''
		Función para obtener el nivel de autorización del usuario
		y de acuerdo al nivel muestra el frame correspondiente.
		'''
	def obtener_nivel_autorizacion(self, data):
		nivel = data['nivel_autorizacion']
		
		self.main.frameLogin.place_forget()

		if nivel == 3:
			self.main.frameAdmin.place(
				relx=0, rely=0,
				relwidth=1, relheight=1
			)
		else:
			self.main.frameMain.place(
				relx=0, rely=0,
				relwidth=1, relheight=1
			)