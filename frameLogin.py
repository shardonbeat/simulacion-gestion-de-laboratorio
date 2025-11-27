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

		self.input_cedula = CTkEntry(
			master=self,
			font=('Arial', 15, "bold"), text_color='black',
			placeholder_text="Cédula", placeholder_text_color='black',
			justify='center',
			border_color='black', fg_color="#BCB4B4",
			bg_color="#2b2b39",
			corner_radius=10
		)
		self.input_cedula.place(relx=0.5, rely=0.52,
			relwidth=0.15, relheight=0.05, anchor=CENTER)

			#@ Contraseña

		self.input_password = CTkEntry(
			master=self,
			font=('Arial', 15, "bold"), text_color='black',
			placeholder_text="Contraseña", placeholder_text_color='black',
			justify='center',
			border_color='black', fg_color="#BCB4B4",
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
                self.input_cedula.get(), self.input_password.get()
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

		self.error_label = CTkLabel(
			master=self,
			text="Cédula o contraseña incorrecta",
			text_color="red",
			font=("Times New Roman", 15, "bold"),
			bg_color="#2b2b39"
		)

	## Funciones

		#@ Función iniciar sesión
	def iniciar_sesion(self, cedula, password):
		cedula = self.input_cedula.get()
		password = self.input_password.get()

		validar = self.main.bdd.verificarLogin(cedula, password)
		if validar:
			data = self.main.bdd.obtenerUsuario(cedula)
			if data:
				if data.get('role') == 'Bloqueado':
					self.error_label.configure(text='Error: Usuario Bloqueado')
					self.error_label.place(relx=0.5, rely=0.77, anchor=CENTER)
					return
				self.main.usuario_actual = data
				self.obtener_nivel_autorizacion(data)
				self.limpiar_inputs()
		else:
			self.error_label.place(
				relx=0.5, rely=0.77,
				anchor=CENTER
			)

	def registrarse(self):
		self.main.frameLogin.place_forget()
		go = frameLogin(self.main.ventana, self.main)
		self.main.frameLogin = go
		self.main.mostrar_register()
		self.limpiar_inputs()
	
	def limpiar_inputs(self):
		self.input_cedula.delete(0, "end")
		self.input_password.delete(0, "end")

		'''
		Función para obtener el nivel de autorización del usuario
		y de acuerdo al nivel muestra el frame correspondiente.
		'''
	def obtener_nivel_autorizacion(self, data):
		nivel = data['role']
		
		self.main.frameLogin.place_forget()

		if nivel == "Administrador de Cumplimiento":
			self.main.mostrar_admin()
		elif nivel == "Coordinador de Seguridad":
			self.main.mostrar_coordinador()
		else:
			self.main.mostrar_main()