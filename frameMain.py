from customtkinter import *
from PIL import Image

class frameMain (CTkFrame):
	def __init__(self, master, main):
		super().__init__(master)
		self.main = main
		self.configure(
			fg_color = "#A79D8A",
			corner_radius = 0,
		)

		## Labels
		self.labelWelcome = CTkLabel(
			master = self, text="",
			font = ("Arial", 15, "bold"),
			fg_color = "#2b2b39"
		)
		self.labelWelcome.place(
			relx=0, rely=0,
			relwidth=0.2, relheight=2,
		)

		self.image = CTkImage(
			Image.open("Img/Laboratorio.ico"),
			size = (128, 128)
		)

		self.logoImage = CTkLabel(
			master = self,text="",
			fg_color = "#2b2b39",
			image = self.image
			
		)
		self.logoImage.place(
			relx=0, rely=0.01,
			relwidth=0.2, relheight=0.3,
		)

		self.logotitulo = CTkLabel(
            master = self, text = "Laboratorio científico",
            text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
            font = ("Times New Roman", 15, "bold")
        )
		self.logotitulo.place(
            relx=0, rely=0.27,
            relwidth=0.2, relheight=0.05,
        )

		self.Niveles = CTkLabel(
            master = self, text = "Niveles de acceso",
            text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
            font = ("Times New Roman", 20, "bold")
        )
		self.Niveles.place(
            relx=0, rely=0.35,
            relwidth=0.2, relheight=0.05,
        )

		self.Nivel_1 = CTkButton(
			master = self, text = "‣  Nivel 1",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold")
		)
		self.Nivel_1.place(
			relx=0.02, rely=0.41,
			relwidth=0.1, relheight=0.04,
		)

		self.Nivel_2 = CTkButton(
			master = self, text = "‣  Nivel 2",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold")
		)
		self.Nivel_2.place(
			relx=0.02, rely=0.45,
			relwidth=0.1, relheight=0.04,
		)

		self.Nivel_3 = CTkButton(
			master = self, text = "‣  Nivel 3",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold")
		)
		self.Nivel_3.place(
			relx=0.02, rely=0.49,
			relwidth=0.1, relheight=0.04,
		)

		self.cerrar_sesion = CTkButton(
			master = self, text = "Cerrar sesión",
			hover_color="#540c0c",
			text_color = "#c51818",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			command=self.cerrar
		)
		self.cerrar_sesion.place(
			relx=0.06, rely=0.9,
			relwidth=0.08, relheight=0.04
		)

	def cerrar(self):
		self.main.frameMain.place_forget()
		self.main.frameLogin.place(
            relx=0, rely=0,
            relwidth=1, relheight=1
        )




