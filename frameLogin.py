from customtkinter import *

class frameLogin (CTkFrame):

	def __init__(self, master, main):
		super().__init__(master)
		self.main = main
		self.configure(
			fg_color = "#ebebeb",
			corner_radius = 0,
		)

		## Labels
			#@ Usuario
		self.labelUsuario = CTkLabel(
			master = self, text = "Cédula:",
			text_color = "#ffffff",
			font = ("Arial", 15, "bold"), corner_radius = 15,
			fg_color = "#474aff"
		)
		self.labelUsuario.place(
			relx=0.5, rely=0.2,
			relwidth=0.25, relheight=0.1,
			anchor=CENTER
		)

		self.input_user = CTkEntry(
			master=self,
			font=('Arial', 25), text_color='black',
			placeholder_text="Cédula", placeholder_text_color='black',
			justify='center',
			border_color='black', fg_color='white', border_width=5
		)
		self.input_user.place(relx=0.5, rely=0.35,
			relwidth=0.3, relheight=0.1, anchor=CENTER)

			#@ Contraseña
		self.labelPassword = CTkLabel(
			master = self, text = "Contraseña:",	
			text_color = "#ffffff",
			font = ("Arial", 15, "bold"), corner_radius = 15,
			fg_color = "#474aff"
		)
		self.labelPassword.place(
			relx=0.5, rely=0.5,
			relwidth=0.3, relheight=0.1,
			anchor=CENTER
		)

		self.input_password = CTkEntry(
			master=self,
			font=('Arial', 25), text_color='black',
			placeholder_text="Contraseña", placeholder_text_color='black',
			justify='center',
			border_color='black', fg_color='white', border_width=5,
			show='*'
		)
		self.input_password.place(relx=0.5, rely=0.65,
			relwidth=0.3, relheight=0.1, anchor=CENTER)
		
		## Botones

		self.login_button = CTkButton(
			master=self, text="Iniciar sesión",
            font=('Times New Roman', 15, 'bold'),
            width=100, height=100, corner_radius=15,
            fg_color="#474aff",
            command=lambda:self.iniciar_sesion(
                self.input_user.get(), self.input_password.get()
            )
        )
		self.login_button.place (
			relx=0.40, rely=0.77,
			relwidth=0.20, relheight=0.1,
			anchor=CENTER
		)

		self.register_button = CTkButton(
			master=self, text="Registrarse",
            font=('Times New Roman', 15, 'bold'),
            width=100, height=100, corner_radius=15,
            fg_color="#474aff",
            command=lambda:self.registrarse()
        )
		self.register_button.place (
			relx=0.60, rely=0.77,
			relwidth=0.20, relheight=0.1,
			anchor=CENTER
		)

	## Funciones

		#@ Función iniciar sesión
	def iniciar_sesion(self, cedula: str, password: str):
		validar = self.main.bdd.verificarLogin(cedula, password)
		if validar:
			data = self.main.bdd.obtenerUsuario(cedula)
			self.obtener_nivel_autorizacion(data)
		else:
			print("Cédula o contraseña incorrecta.")

	def registrarse(self):
		self.main.frameLogin.place_forget()
		self.main.frameRegister.place(
			relx=0, rely=0,
			relwidth=1, relheight=1
		)

	

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