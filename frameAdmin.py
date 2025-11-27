from customtkinter import *
from PIL import Image

from AdministradorAuditarAcciones import AuditarAcciones
from AdministradorDefinirPoliticas import DefinirPoliticas
from AdministradorExportarInformes import ExportarInformes
from AdministradorGenerarReportes import GenerarReportes
from AdministradorMejoras import MejorasCierres
from Mostrar_ConfiguracionAdmin import MostrarConfiguracion

class frameAdmin (CTkFrame):
	def __init__(self, master, main):
		super().__init__(master)
		self.main = main
		self.main = main
		data = self.main.usuario_actual
		self.nombre = data['username']
		self.cedula = data['cedula']
		self.nivel_autorizacion = data['nivel_autorizacion']
		self.capacitación = data['id_capacitacion']
		self.id = self.main.bdd.obtener_id_usuario(data['cedula'])
		print(f"ID del usuario actual: {self.id}")
		self.configure(
			fg_color = "#A79D8A",
			corner_radius = 0
		)

		self.DefinirPoliticas = DefinirPoliticas(self.main.ventana, self.main)
		self.GenerarReportes = GenerarReportes(self.main.ventana, self.main)
		self.AuditarAcciones = AuditarAcciones(self.main.ventana, self.main)
		self.ExportarInformes = ExportarInformes(self.main.ventana, self.main)
		self.MejorasCierres = MejorasCierres(self.main.ventana, self.main)

		self.MostrarConfiguracion = MostrarConfiguracion(self.main.ventana, self.main)

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
            master = self, text = "Laboratorio Científico",
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
            relx=0.05, rely=0.40,
            relwidth=0.09, relheight=0.05
        )

		self.Informacion = CTkLabel(
            master = self, text = "Información del usuario",
            text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
            font = ("Times New Roman", 20, "bold")
        )
		self.Informacion.place(
            relx=0, rely=0.46,
            relwidth=0.2, relheight=0.05
        )

		self.nombre_label = CTkLabel(
			master = self, text = f"‣ Nombre: {self.nombre}",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold")
		)
		self.nombre_label.place(
			relx=0.015, rely=0.515,
			relwidth=0.1, relheight=0.04
		)

		self.cedula_label = CTkLabel(
			master = self, text = f"‣ Cédula: {self.cedula}",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),	
		)
		self.cedula_label.place(
			relx=0.020, rely=0.565,
			relwidth=0.1, relheight=0.04
		)

		self.nivel_autorizacion_label = CTkLabel(
			master = self, text = f"‣ Nivel de Autorización: {self.nivel_autorizacion}",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold")
		)
		self.nivel_autorizacion_label.place(
			relx=0.010, rely=0.60,
			relwidth=0.15, relheight=0.07
		)

		self.labelAdmin = CTkLabel(
			master=self, text="Administrador De Cumplimiento",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"),
		)
		self.labelAdmin.place(
			relx=0.015, rely=0.33,
			relwidth=0.17, relheight=0.05,
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
			text = "Sistema De Gestión Del Laboratorio",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 20, "bold"), corner_radius = 15,
		)
		self.labelContenido.place(
			relx=0.4, rely=0.15,
			relwidth=0.4, relheight=0.05
		)

		self.configurar= CTkButton(
			master = self, 
			text = "Configuración",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="left",
			command= lambda: self.configuracion(1)
		)
		self.configurar.place(
			relx=0.06, rely=0.8,
			relwidth=0.08, relheight=0.04
		)

		 ## Botones de funciones

		self.PoliticasImage = CTkImage(
			Image.open("Img/Politicas.png"),
			size = (64, 64)
		)
		self.Politicas = CTkButton(
			master = self, text = "Definir políticas",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.PoliticasImage,
			command=lambda: self.frame_manager(1)
		)
		self.Politicas.place(
			relx=0.33, rely=0.25,	
			relwidth=0.15, relheight=0.2
		)

		self.ReportesImage = CTkImage(
			Image.open("Img/GenerarReporte.png"),
			size = (64, 64)
		)

		self.Reportes = CTkButton(
			master = self, text = "Generar reportes",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.ReportesImage,
			command=lambda: self.frame_manager(2)
		)
		self.Reportes.place(
			relx=0.53, rely=0.25,
			relwidth=0.15, relheight=0.2
		)

		self.AccionesImage = CTkImage(
			Image.open("Img/AuditarAcciones.png"),
			size = (64, 64)
		)

		self.Acciones = CTkButton(
			master = self, text = "Auditar acciones",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.AccionesImage,
			command=lambda: self.frame_manager(3)
		)
		self.Acciones.place(
			relx=0.73, rely=0.25,
			relwidth=0.15, relheight=0.2
		)

		self.ExportarImage = CTkImage(
			Image.open("Img/ExportarInformes.png"),
			size = (64, 64)
		)
		self.Exportar_Informes = CTkButton(
			master = self, text = "Exportar informes",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.ExportarImage,
			command=lambda: self.frame_manager(4)
		)
		self.Exportar_Informes.place(
			relx=0.43, rely=0.5,
			relwidth=0.15, relheight=0.2
		)

		self.MejorasImage = CTkImage(
			Image.open("Img/Mejoras.png"),
			size = (64, 64)
		)
		self.Mejoras_Cierres = CTkButton(
			master = self, text = "Mejoras o cierres",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.MejorasImage,
			command=lambda: self.frame_manager(5)
		)
		self.Mejoras_Cierres.place(
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

	def removerfunciones(self):
		self.DefinirPoliticas.place_forget()
		self.GenerarReportes.place_forget()
		self.AuditarAcciones.place_forget()
		self.ExportarInformes.place_forget()
		self.MejorasCierres.place_forget()

	def	frame_manager(self, frame):
		self.removerfunciones()

		if frame == 1:
			self.DefinirPoliticas.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
		elif frame == 2:
			self.GenerarReportes.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
		elif frame == 3:
			self.AuditarAcciones.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
		elif frame == 4:
			self.ExportarInformes.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
		elif frame == 5:
			self.MejorasCierres.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
	
	def configuracion(self, valor):
		self.removerfunciones()
		
		if valor == 1:
			self.MostrarConfiguracion.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)

	def volver_main(self):
		self.removerfunciones()
		self.main.frameAdmin.place_forget()
		go = frameAdmin(self.main.ventana, self.main)
		self.main.frameAdmin = go
		self.main.frameAdmin.place(
			relx=0, rely=0,
			relwidth=1, relheight=1
		)
		
	def cerrar(self):
		self.removerfunciones()
		self.main.mostrar_login()
