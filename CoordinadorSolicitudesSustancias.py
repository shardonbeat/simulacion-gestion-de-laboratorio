from customtkinter import *
from tkinter import ttk

class SolicitudesSustancias(CTkFrame):
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
			text="Solicitudes de Sustancias",
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
		
		self.boton_cambiar_estado = CTkButton(
			master=self,
			text="Cambiar Estado",
			fg_color="#5e5e72",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"),
			corner_radius=10,
			command=lambda: self.actualizar_estado_solicitud()
		)
		self.boton_cambiar_estado.place(
			relx=0.5, rely=0.85,
			anchor=CENTER,
		)

		self.texto_exito = CTkLabel(
			master=self,
			text="Estado actualizado con éxito",
			text_color="#00FF00",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"),
			corner_radius=15
		)

		self.texto_error = CTkLabel(
			master=self,
			text="",
			text_color="#FF0000",
			fg_color="#2b2b39",
			bg_color="#2b2b39",
			font=("Times New Roman", 15, "bold"),
			corner_radius=15
		)
		
		columnas = ("ID", "Usuario", "Sustancia", "Nivel de Riesgo", "Cantidad", "Descripción",  "Fecha Solicitud", "Capacitacion", "Estado", "Accion")

		self.tablaSolicitudes_sustancia = ttk.Treeview(
			master=self,
			columns=columnas,
			show="headings"
		)
		self.tablaSolicitudes_sustancia.heading("ID", text="ID")
		self.tablaSolicitudes_sustancia.column("ID", width=50)
		self.tablaSolicitudes_sustancia.heading("Usuario", text="Usuario")
		self.tablaSolicitudes_sustancia.column("Usuario", width=100)
		self.tablaSolicitudes_sustancia.heading("Sustancia", text="Sustancia")
		self.tablaSolicitudes_sustancia.column("Sustancia", width=100)
		self.tablaSolicitudes_sustancia.heading("Nivel de Riesgo", text="Nivel de Riesgo")
		self.tablaSolicitudes_sustancia.column("Nivel de Riesgo", width=75)
		self.tablaSolicitudes_sustancia.heading("Cantidad", text="Cantidad")
		self.tablaSolicitudes_sustancia.column("Cantidad", width=50)
		self.tablaSolicitudes_sustancia.heading("Descripción", text="Descripción")
		self.tablaSolicitudes_sustancia.column("Descripción", width=200)
		self.tablaSolicitudes_sustancia.heading("Fecha Solicitud", text="Fecha Solicitud")
		self.tablaSolicitudes_sustancia.column("Fecha Solicitud", width=100)
		self.tablaSolicitudes_sustancia.heading("Capacitacion", text="Capacitacion")
		self.tablaSolicitudes_sustancia.column("Capacitacion", width=100)
		self.tablaSolicitudes_sustancia.heading("Estado", text="Estado")
		self.tablaSolicitudes_sustancia.column("Estado", width=75)
		self.tablaSolicitudes_sustancia.place(
			relx=0.5, rely=0.55,
			relwidth=1, relheight=0.6,
			anchor=CENTER
		)
		self.cargar_solicitudes()

	def cargar_solicitudes(self):
		self.tablaSolicitudes_sustancia.destroy()
		columnas = ("ID", "Usuario", "Sustancia", "Nivel de Riesgo", "Cantidad", "Descripción", 
			  		"Fecha Solicitud", "Capacitacion", "Estado")
		self.tablaSolicitudes_sustancia = ttk.Treeview(
			master=self,
			columns=columnas,
			show="headings"
		)
		self.tablaSolicitudes_sustancia.heading("ID", text="ID")
		self.tablaSolicitudes_sustancia.heading("Usuario", text="Usuario")
		self.tablaSolicitudes_sustancia.heading("Sustancia", text="Sustancia")
		self.tablaSolicitudes_sustancia.heading("Nivel de Riesgo", text="Nivel de Riesgo")
		self.tablaSolicitudes_sustancia.heading("Cantidad", text="Cantidad")
		self.tablaSolicitudes_sustancia.heading("Descripción", text="Descripción")
		self.tablaSolicitudes_sustancia.heading("Fecha Solicitud", text="Fecha Solicitud")
		self.tablaSolicitudes_sustancia.heading("Capacitacion", text="Capacitacion")
		self.tablaSolicitudes_sustancia.heading("Estado", text="Estado")
		self.tablaSolicitudes_sustancia.place(relx=0.5, rely=0.4, relwidth=0.8, relheight=0.5, anchor="center")
		
		solicitudes = self.main.bdd.obtener_solicitudes_sustancias()
		print(solicitudes)
		try:
			for solicitud in solicitudes:
				self.tablaSolicitudes_sustancia.insert(
				"", "end",
				values=(solicitud['id_solicitud_s'], solicitud['id_usuario'], solicitud['nombre_sustancia'],
				solicitud['nivel_riesgo'], solicitud['cantidad_solicitada'], solicitud['motivo'],
				solicitud['fecha_solicitud'], solicitud['capacitacion'], solicitud['estado'])
			)
		except Exception:
			try:
				for solicitud in solicitudes:
					self.tablaSolicitudes_sustancia.insert(
					"", "end",
					values=(solicitud[0], solicitud[1], solicitud[2], solicitud[3], solicitud[4],
					solicitud[5], solicitud[6], solicitud[7], solicitud[8])
				)
			except Exception as e:
				self.texto_error.configure(
					text=f"Error al cargar solicitudes: {e}"
				)
				self.texto_error.place(
					relx=0.5, rely=0.75,
					anchor=CENTER
				)
		
	def actualizar_estado_solicitud(self):
		solicitud = self.tablaSolicitudes_sustancia.focus()
		datos_solicitud = self.tablaSolicitudes_sustancia.item(solicitud)

		if not datos_solicitud['values']:
			print("No se ha seleccionado ninguna solicitud.")
			return
		
		id_solicitud = datos_solicitud['values'][0]
		estado_actual = datos_solicitud['values'][8]

		nuevo_estado = "Aprobada" if estado_actual == "Pendiente" else "Pendiente"
		self.main.bdd.actualizar_estado_solicitud(id_solicitud, nuevo_estado)
		self.cargar_solicitudes()
		self.texto_exito.place(
			relx=0.5, rely=0.75,
			anchor=CENTER
		)