from customtkinter import *
from PIL import Image

from CoordinadorBloquearUsuario import BloquearUsuario
from CoordinadorEmitirAlertas import EmitirAlertas
from CoordinadorGestionarInventario import GestionarInventario
from CoordinadorRegistrarCapacitaciones import RegistrarCapacitaciones
from CoordinadorSolicitudesAcceso import SolicitudesAcceso
from CoordinadorSolicitudesSustancias import SolicitudesSustancias


class FrameCoordinador(CTkFrame):
	def __init__(self, master, main):
		super().__init__(master)
		self.main = main
		data = self.main.usuario_actual
		self.nombre = data['username']
		self.cedula = data['cedula']
		self.nivel_autorizacion = data['nivel_autorizacion']
		self.capacitación = data['capacitacion']
		self.id = self.main.bdd.obtener_id_usuario(data['cedula'])
		print(f"ID del usuario actual: {self.id}")
		self.configure(
			fg_color="#A79D8A",
			corner_radius=0,
		)

		self.ventana_actual = self.main.FrameCoordinador
		self.CoordinadorSolicitudesAcceso = None
		self.CoordinadorSolicitudesSustancias = None
		self.CoordinadorRegistrarCapacitaciones = None
		self.CoordinadorGestionarInventario = None
		self.CoordinadorEmitirAlertas = None
		self.CoordinadorBloquearUsuario = None

		# Labels
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
			size=(128, 128),
		)

		self.logoImage = CTkLabel(
			master=self, text="",
			fg_color="#2b2b39",
			image=self.image,
		)
		self.logoImage.place(
			relx=0, rely=0.01,
			relwidth=0.2, relheight=0.3,
		)

		self.logotitulo = CTkLabel(
			master=self, text="Laboratorio Científico",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"),
		)
		self.logotitulo.place(
			relx=0, rely=0.27,
			relwidth=0.2, relheight=0.05,
		)

		self.labelCoordinador = CTkLabel(
			master=self, text="Coordinador De Seguridad",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"),
		)
		self.labelCoordinador.place(
			relx=0.02, rely=0.33,
			relwidth=0.16, relheight=0.05,
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
			text = " Sistema de Gestión Del Laboratorio",
			text_color = "#ffffff",
			fg_color= "#2b2b39",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 20, "bold"), corner_radius = 15
		)
		self.labelContenido.place(
			relx=0.4, rely=0.15,
			relwidth=0.4, relheight=0.05
		)

		self.AccesoImage = CTkImage(
			Image.open("Img/Acceso-nivel.png"),
			size = (64, 64)
		)
		self.AccesoNivel = CTkButton(
			master = self, text = "Solicitudes de acceso",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.AccesoImage,
			command=lambda: self.frame_manager(1)
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
			master = self, text = "Solicitudes de sustancias",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.SustanciasImage,
			command=lambda: self.frame_manager(2)
		)
		self.Sustancias.place(
			relx=0.53, rely=0.25,
			relwidth=0.15, relheight=0.2
		)

		self.CapacitacionesImage = CTkImage(
			Image.open("Img/Capacitaciones.png"),
			size = (64, 64)
		)

		self.Capacitaciones = CTkButton(
			master = self, text = "Registrar capacitaciones",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.CapacitacionesImage,
			command=lambda: self.frame_manager(3)
		)
		self.Capacitaciones.place(
			relx=0.73, rely=0.25,
			relwidth=0.15, relheight=0.2
		)

		self.InventarioSustanciasImage = CTkImage(
			Image.open("Img/sustancias-peligrosas.png"),
			size = (64, 64)
		)

		self.InventarioSustancias = CTkButton(
			master = self, text = "Gestionar inventario",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.InventarioSustanciasImage,
			command=lambda: self.frame_manager(4)
		)
		self.InventarioSustancias.place(
			relx=0.33, rely=0.5,
			relwidth=0.15, relheight=0.2
		)

		self.AlertasImage = CTkImage(
			Image.open("Img/Alertas.png"),
			size = (64, 64)
		)

		self.Alertas = CTkButton(
			master = self, text = "Emitir alertas",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.AlertasImage,
			command=lambda: self.frame_manager(5)
		)
		self.Alertas.place(
			relx=0.53, rely=0.5,
			relwidth=0.15, relheight=0.2
		)

		self.BloquearUsuariosImage = CTkImage(
			Image.open("Img/bloquear-usuario.png"),
			size = (64, 64)
		)

		self.BloquearUsuarios = CTkButton(
			master = self, text = "Bloquear usuarios",
			text_color = "#ffffff",
			hover_color="#898995",
			fg_color= "#5e5e72",
			bg_color= "#2b2b39",
			font = ("Times New Roman", 15, "bold"),
			compound="top",
			image=self.BloquearUsuariosImage,
			command=lambda: self.frame_manager(6)
		)
		self.BloquearUsuarios.place(
			relx=0.73, rely=0.5,
			relwidth=0.15, relheight=0.2
		)

		self.Inicio = CTkButton(
			master=self, text="Inicio",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			hover_color="#898995",
			font=("Times New Roman", 20, "bold"),
			command=self.volver_main
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
			relx=0.009, rely=0.515,
			relwidth=0.15, relheight=0.04
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

		self.cerrar_sesion = CTkButton(
			master=self, text="Cerrar sesión",
			hover_color="#540c0c",
			text_color="#c51818",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"),
			command=self.cerrar
		)
		self.cerrar_sesion.place(
			relx=0.06, rely=0.9,
			relwidth=0.08, relheight=0.04
		)
	
	def frame_manager(self, frame):
		self.cerrar_ventanas()

		if frame == 1:
			self.CoordinadorSolicitudesAcceso = SolicitudesAcceso(self.main.ventana, self.main)
			self.CoordinadorSolicitudesAcceso.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
			self.ventana_actual = self.CoordinadorSolicitudesAcceso
		elif frame == 2:
			self.CoordinadorSolicitudesSustancias = SolicitudesSustancias(self.main.ventana, self.main)
			self.CoordinadorSolicitudesSustancias.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
			self.ventana_actual = self.CoordinadorSolicitudesSustancias
		elif frame == 3:
			self.CoordinadorRegistrarCapacitaciones = RegistrarCapacitaciones(self.main.ventana, self.main)
			self.CoordinadorRegistrarCapacitaciones.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
			self.ventana_actual = self.CoordinadorRegistrarCapacitaciones
		elif frame == 4:
			self.CoordinadorGestionarInventario = GestionarInventario(self.main.ventana, self.main)
			self.CoordinadorGestionarInventario.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
			self.ventana_actual = self.CoordinadorGestionarInventario
		elif frame == 5:
			self.CoordinadorEmitirAlertas = EmitirAlertas(self.main.ventana, self.main)
			self.CoordinadorEmitirAlertas.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
			self.ventana_actual = self.CoordinadorEmitirAlertas
		elif frame == 6:
			self.CoordinadorBloquearUsuario = BloquearUsuario(self.main.ventana, self.main)
			self.CoordinadorBloquearUsuario.place(
				relx=0.25, rely=0.12,
				relwidth=0.7, relheight=0.75
			)
			self.ventana_actual = self.CoordinadorBloquearUsuario

	def volver_main(self):
		self.cerrar_ventanas()
		self.main.FrameCoordinador.place_forget()
		go = FrameCoordinador(self.main.ventana, self.main)
		self.main.FrameCoordinador = go
		self.main.FrameCoordinador.place(
			relx=0, rely=0,
			relwidth=1, relheight=1
		)

	def cerrar_ventanas(self):
		ventanas = [
            self.CoordinadorSolicitudesAcceso, 
            self.CoordinadorSolicitudesSustancias,
            self.CoordinadorRegistrarCapacitaciones, 
            self.CoordinadorGestionarInventario,
			self.CoordinadorEmitirAlertas,
			self.CoordinadorBloquearUsuario
        ]

		for ventana in ventanas:
			if ventana is not None:
				ventana.place_forget()
				
		self.ventana_actual = None

	def cerrar(self):
		self.ventana_actual.place_forget()
		self.main.mostrar_login()