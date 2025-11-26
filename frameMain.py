from customtkinter import *
from PIL import Image

from frameSolicitudAcceso import solicitudAcceso
from frameSolicitudSustancias import solicitudSustancia

class frameMain (CTkFrame):
	def __init__(self, master, main):
		super().__init__(master)
		self.main = main
		data = self.main.bdd.obtener_usuario()
		self.configure(
			fg_color = "#A79D8A",
			corner_radius = 0
		)

		self.frameSolicitudAcceso = solicitudAcceso(self.main.ventana, self.main)
		self.frameSolicitudSustancia = solicitudSustancia(self.main.ventana, self.main)

		## Labels
		self.labelWelcome = CTkLabel(
			master = self, text="",
			font = ("Arial", 15, "bold"),
			fg_color = "#2b2b39"
		)
		self.labelWelcome.place(
			relx=0, rely=0,
			relwidth=0.2, relheight=2
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
			relwidth=0.2, relheight=0.3
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
            relwidth=0.2, relheight=0.05
        )

		self.Inicio = CTkButton(
            master = self, text = "Inicio",
            text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			hover_color="#898995",
            font = ("Times New Roman", 20, "bold"),
			command= self.volver_main
        )
		self.Inicio.place(
            relx=0.05, rely=0.33,
            relwidth=0.09, relheight=0.05
        )

		self.Niveles = CTkLabel(
            master = self, text = "Niveles de acceso",
            text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
            font = ("Times New Roman", 20, "bold")
        )
		self.Niveles.place(
            relx=0, rely=0.4,
            relwidth=0.2, relheight=0.05
        )

		self.Nivel_1 = CTkButton(
			master = self, text = "‣  Nivel 1",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			command= self.laboratorioNivel1
		)
		self.Nivel_1.place(
			relx=0.02, rely=0.46,
			relwidth=0.1, relheight=0.04
		)

		self.Nivel_2 = CTkButton(
			master = self, text = "‣  Nivel 2",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),	
			command= self.laboratorioNivel2 if data in ["2", "3"] else self.AccesoDenegado
		)
		self.Nivel_2.place(
			relx=0.02, rely=0.50,
			relwidth=0.1, relheight=0.04
		)

		self.Nivel_3 = CTkButton(
			master = self, text = "‣  Nivel 3",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			command= self.laboratorioNivel3 if data == "3" else self.AccesoDenegado
		)
		self.Nivel_3.place(
			relx=0.02, rely=0.54,
			relwidth=0.1, relheight=0.04
		)

		self.labelFondo = CTkLabel(
			master = self,
			text = "",
			fg_color = "#2b2b39",
			bg_color= "#A79D8A",
			corner_radius=15
		)
		self.labelFondo.place(
			relx=0.25, rely=0.12,
			relwidth=0.7, relheight=0.75
		)

		self.labelContenido = CTkLabel(
			master = self,
			text = "¡ Bienvenido al laboratorio !",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 20, "bold"), corner_radius = 15,
		)
		self.labelContenido.place(
			relx=0.49, rely=0.15,
			relwidth=0.22, relheight=0.05
		)

		self.AccesoImage = CTkImage(
			Image.open("Img/Acceso-nivel.png"),
			size = (64, 64)
		)
		self.AccesoNivel = CTkButton(
			master = self, text = "Solicitar acceso",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.AccesoImage,
			command = lambda: self.frameSolicitudAcceso.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
		)
		self.AccesoNivel.place(
			relx=0.33, rely=0.25,	
			relwidth=0.15, relheight=0.2
		)

		self.SustanciasImage = CTkImage(
			Image.open("Img/sustancias-quimicas.png"),
			size = (64, 64)
		)

		self.Sustancias = CTkButton(
			master = self, text = "Solicitar sustancias",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.SustanciasImage,
			command= lambda: self.frameSolicitudSustancia.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
		)
		self.Sustancias.place(
			relx=0.53, rely=0.25,
			relwidth=0.15, relheight=0.2
		)

		self.RegistrosImage = CTkImage(
			Image.open("Img/Registros.png"),
			size = (64, 64)
		)

		self.Registros = CTkButton(
			master = self, text = "Hacer registros",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.RegistrosImage
		)
		self.Registros.place(
			relx=0.73, rely=0.25,
			relwidth=0.15, relheight=0.2
		)

		self.reportesImage = CTkImage(
			Image.open("Img/Reportes.png"),
			size = (64, 64)
		)

		self.Reportes = CTkButton(
			master = self, text = "Reportar incidencias",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.reportesImage
		)
		self.Reportes.place(
			relx=0.43, rely=0.5,
			relwidth=0.15, relheight=0.2
		)

		self.HistorialImage = CTkImage(
			Image.open("Img/Historial.png"),
			size = (64, 64)
		)

		self.Historial = CTkButton(
			master = self, text = "Ver historial",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.HistorialImage
		)
		self.Historial.place(
			relx=0.63, rely=0.5,
			relwidth=0.15, relheight=0.2
		)

		self.cerrar_sesion = CTkButton(
			master = self, text = "Cerrar sesión",
			hover_color="#540c0c",
			text_color = "#c51818",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			command= self.cerrar
		)
		self.cerrar_sesion.place(
			relx=0.06, rely=0.9,
			relwidth=0.08, relheight=0.04
		)
	
	def laboratorioNivel1(self):
		self.AccesoNivel.destroy()
		self.Acceso.destroy() if hasattr(self, 'Acceso') else None
		self.Sustancias.destroy()
		self.Registros.destroy()
		self.Reportes.destroy()
		self.Historial.destroy()
		self.cerrar_sesion.destroy()

		self.labelContenido.configure(
		text = "¡ Acceso al laboratorio nivel 1 otorgado !"
		)
		self.labelContenido.place(
			relx=0.43, rely=0.15,
			relwidth=0.3, relheight=0.05
		)

		self.back_image = CTkImage(
            Image.open("Img/Back_image.png"),
            size=(30, 30)
        )

	def laboratorioNivel2(self):
		self.AccesoNivel.destroy()
		self.Acceso.destroy()
		self.Sustancias.destroy()
		self.Registros.destroy()
		self.Reportes.destroy()
		self.Historial.destroy()
		self.cerrar_sesion.destroy()

		self.labelContenido.configure(
			text = "¡ Acceso al laboratorio nivel 2 otorgado !"
		)
		self.labelContenido.place(
			relx=0.43, rely=0.15,
			relwidth=0.3, relheight=0.05
		)

		self.back_image = CTkImage(
            Image.open("Img/Back_image.png"),
            size=(30, 30)
        )
	
	def laboratorioNivel3(self):
		self.AccesoNivel.destroy()
		self.Acceso.destroy()
		self.Sustancias.destroy()
		self.Registros.destroy()
		self.Reportes.destroy()
		self.Historial.destroy()
		self.cerrar_sesion.destroy()

		self.labelContenido.configure(
			text = "¡ Acceso al laboratorio nivel 3 otorgado !"
		)
		self.labelContenido.place(
			relx=0.43, rely=0.15,
			relwidth=0.3, relheight=0.05
		)

	def AccesoDenegado(self):

		# Si ya existe un mensaje anterior, lo eliminamos primero
		if hasattr(self, 'Acceso') and self.Acceso is not None:
			try:
				self.Acceso.destroy()
			except Exception:
				pass

		self.Acceso = CTkLabel(
			master=self,
			text="Acceso denegado",
			text_color="#ff0000",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold")
		)
		self.Acceso.place(
			relx=0.03, rely=0.6,
			relwidth=0.15, relheight=0.04
		)

		# Programar que el mensaje se elimine automáticamente después de 1 segundo (1000 ms)
		try:
			self.after(1000, lambda: self.Acceso.destroy() if hasattr(self, 'Acceso') else None)
		except Exception:
			# En caso de que after no esté disponible, ignoramos silenciosamente
			pass

	def removerfunciones(self):
		self.frameSolicitudAcceso.place_forget()
		self.frameSolicitudAcceso.place_forget()
	
	def volver_main(self):
		self.removerfunciones()
		self.main.frameMain.place_forget()
		go = frameMain(self.main.ventana, self.main)
		self.main.frameMain = go
		self.main.frameMain.place(
			relx=0, rely=0,
			relwidth=1, relheight=1
		)
		

	def cerrar(self):
		self.removerfunciones()
		self.main.frameMain.place_forget()
		self.main.frameLogin.place(
            relx=0, rely=0,
            relwidth=1, relheight=1
        )
