from datetime import datetime
from customtkinter import *

class HacerRegistros(CTkFrame):
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
			text="Registros de Sustancias y Residuos",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 20, "bold"), corner_radius=15,
		)
		self.labelContenido.place(
			relx=0.5, rely=0.12,
			relwidth=0.6, relheight=0.2,
			anchor=CENTER
		)

		self.labelSustancia = CTkLabel(
			master=self,
			text="Sustancia utilizada:",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"), corner_radius=15
		)
		self.labelSustancia.place(
			relx=0.125, rely=0.2,
			relwidth=0.4, relheight=0.06,
		)

		self.SustanciaUtilizada = CTkEntry(
			master=self,
			fg_color="#5e5e72",
			bg_color="#2b2b39",
			font=("Times New Roman", 15),
			corner_radius=10
		)
		self.SustanciaUtilizada.place(
			relx=0.25, rely=0.25,
			relwidth=0.2, relheight=0.06,
		)

		self.labelresiduo = CTkLabel(
			master=self,
			text="Tipo de residuo:",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"), corner_radius=15
		)
		self.labelresiduo.place(
			relx=0.11, rely=0.35,
			relwidth=0.4, relheight=0.06,
		)

		self.Residuo = CTkEntry(
			master=self,
			fg_color="#5e5e72",
			bg_color="#2b2b39",
			font=("Times New Roman", 15),
			corner_radius=10
		)
		self.Residuo.place(
			relx=0.25, rely=0.4,
			relwidth=0.2, relheight=0.06
		)

		self.labelContenedor = CTkLabel(
			master=self,
			text="Contenedor usado:",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"), corner_radius=15
		)
		self.labelContenedor.place(
			relx=0.2, rely=0.5,
			relwidth=0.25, relheight=0.06
		)
		
		self.Contenedor = CTkEntry(
			master=self,
			fg_color="#5e5e72",
			bg_color="#2b2b39",
			font=("Times New Roman", 15),
			corner_radius=10
		)
		self.Contenedor.place(
			relx=0.25, rely=0.55,
			relwidth=0.2, relheight=0.06
		)

		self.labelFecha = CTkLabel(
			master=self,
			text="Fecha de almacenamiento:",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"), corner_radius=15
		)
		self.labelFecha.place(
			relx=0.47, rely=0.2,
			relwidth=0.25, relheight=0.06
		)
		
		self.FechaAlmacenamiento = CTkEntry(
			master=self,
			fg_color="#5e5e72",
			bg_color="#2b2b39",
			font=("Times New Roman", 15),
			corner_radius=10
		)
		self.FechaAlmacenamiento.place(
			relx=0.5, rely=0.25,
			relwidth=0.2, relheight=0.06
		)
		
		self.error_fecha = CTkLabel(
			master=self,
			text="Fecha invalida",
			text_color="#ff0000",
			font=("Times New Roman", 12, "bold"),
		)

		self.labelFechaRetiro = CTkLabel(
			master=self,
			text="Fecha de retiro:",
			text_color="#ffffff",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"), corner_radius=15
		)
		self.labelFechaRetiro.place(
			relx=0.45, rely=0.35,
			relwidth=0.23, relheight=0.06
		)
		
		self.FechaRetiro = CTkEntry(
			master=self,
			fg_color="#5e5e72",
			bg_color="#2b2b39",
			font=("Times New Roman", 15),
			corner_radius=10
		)
		self.FechaRetiro.place(
			relx=0.5, rely=0.4,
			relwidth=0.2, relheight=0.06
		)

		self.error_fecha_retiro = CTkLabel(
			master=self,
			text="Fecha invalida",
			text_color="#ff0000",
			font=("Times New Roman", 12, "bold"),
		)

		self.enviarButton = CTkButton(
			master=self, text="Enviar Solicitud",
			text_color="#ffffff",
			hover_color="#898995",
			fg_color="#5e5e72",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"),
			command=self.enviar_registro
		)
		self.enviarButton.place(
			relx=0.4, rely=0.85,
			relwidth=0.2, relheight=0.1,
		)

		self.mensaje_exito_label = CTkLabel(
			master=self,
			text="Registro enviado con éxito",
			text_color="#00ff00",
			font=("Times New Roman", 15, "bold"),
		)
		
	def enviar_registro(self):
		self.limpiar_errores()
		sustancia = self.SustanciaUtilizada.get()
		residuo = self.Residuo.get()
		contenedor = self.Contenedor.get()
		fecha_almacenamiento = self.FechaAlmacenamiento.get()
		fecha_retiro = self.FechaRetiro.get()
		id_usuario = self.main.bdd.obtener_id_usuario(self.main.usuario_actual['cedula'])
		
		acceso = True
		if not self.validar_fecha_almacenamiento():
			print("Fecha inválida.")
			acceso = False
		if not self.validar_fecha_retiro():
			print("Fecha inválida.")
			acceso = False
			
		if not acceso:
			return
		
		success = self.main.bdd.guardar_registro_sustancia_residuo(
			id_usuario, sustancia, residuo, contenedor, fecha_almacenamiento, fecha_retiro
		)

		if success and acceso:
			self.mensaje_exito()
			self.limpiar_campos()

	def validar_fecha_almacenamiento(self):
		try:
			fecha_text = self.FechaAlmacenamiento.get()
			fecha = datetime.strptime(fecha_text, "%Y-%m-%d").date()
		except Exception as e:
			print(e)
			self.error_fecha.place(
				relx=0.5, rely=0.31
			)
			return False

		if fecha <= datetime.now().date():
			return True
		else:
			self.error_fecha.place(
				relx=0.53, rely=0.31
			)
			return False

	def validar_fecha_retiro(self):
		try:
			fecha_text = self.FechaRetiro.get()
			fecha = datetime.strptime(fecha_text, "%Y-%m-%d").date()
			
			fecha_almacenamiento_text = self.FechaAlmacenamiento.get()
			fecha_almacenamiento = datetime.strptime(fecha_almacenamiento_text, "%Y-%m-%d").date()
		except Exception as e:
			print(e)
			return False
		
		if fecha >= fecha_almacenamiento:
			return True
		else:
			self.error_fecha_retiro.place(
				relx=0.53, rely=0.47
			)
			return False
		
	def mensaje_exito(self):
		self.mensaje_exito_label.place(
			relx=0.5, rely=0.8,
			anchor=CENTER
		)
	
	def limpiar_campos(self):
		self.SustanciaUtilizada.delete(0, 'end')
		self.Residuo.delete(0, 'end')
		self.Contenedor.delete(0, 'end')
		self.FechaAlmacenamiento.delete(0, 'end')
		self.FechaRetiro.delete(0, 'end')

	def limpiar_errores(self):
		self.error_fecha.place_forget()
		self.error_fecha_retiro.place_forget()